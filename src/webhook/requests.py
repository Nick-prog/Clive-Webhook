import json
import wget
import os.path
import os
import ssl
import sys
import pymsgbox
from datetime import datetime
# docx2pdf requires macOS native components and can abort the process on unsupported
# systems during module import. Import lazily inside download_uploaded_files() so
# the rest of the program can run even if conversion isn't available.
from time import sleep
from tqdm import tqdm
from typing import Any

from src.webhook.logger import logger
from src.tools.dictionaries import Definitions


def convert(src: str, dst: str) -> bool:
    """Convert a .docx file to PDF using docx2pdf if available and enabled.

    Returns True on success, False if conversion was skipped or failed.
    This wrapper exists so tests can patch Webhook.requests.convert safely.
    """
    if os.getenv('CLIVE_ENABLE_DOCX2PDF', '0') != '1':
        logger.info("docx->pdf conversion is disabled (set CLIVE_ENABLE_DOCX2PDF=1 to enable)")
        return False
    try:
        from docx2pdf import convert as _convert
    except Exception as e:
        logger.warning("docx2pdf import failed; skipping conversion: %s", e)
        return False
    try:
        _convert(src, dst)
        logger.info("convert: converted %s -> %s", src, dst)
        return True
    except Exception:
        logger.exception("convert: error converting %s to PDF", src)
        return False


class Request:

    def __init__(self, doc_type: int, path: str):
        """Class created to host methods for file manipulation. Identifies student information,
        downloads given file, and stores it based on unique 

        :param doc_type: _description_
        :type doc_type: int
        """

        self.doc_type = doc_type
        self.path = path
        self.metadata = []

    def get_total(self) -> int:
        """Method to gets the total amount of entries in the given Pipedream target

        :return: number of entries found
        :rtype: int
        """

        from src.webhook.pipedream import Pipedream
        pd = Pipedream(self.doc_type)
        metadata = pd.get_events()
        ids: dict[str, Any] = json.loads(str(metadata))
        return ids["page_info"]["total_count"]
    
    def get_date(self, select: int) -> str:
        """Method to get the current date and formats it based on selected value

        :param select: format selector
        :type select: int
        :raises ValueError: one of the two formatters wasn't selected
        :return: formatted date string
        :rtype: str
        """

        date = datetime.now()

        if select == 1:
            return date.strftime("%B %Y")
        elif select == 2:
            return date.strftime("%m.%d.%Y")
        else:
            return date.strftime("%B %Y")
    
    def parse_metadata(self) -> int:
        """Method that gets the documents sent through the designated Pipedream target and passes them to the download_doc method.
        """

        from src.webhook.pipedream import Pipedream
        pd = Pipedream(self.doc_type)
        data = pd.get_data()
        object: dict[str, Any] = json.loads(str(data))
        metadata = object["data"]

        if len(metadata) == 0:
            logger.info("parse_metadata: no metadata found for doc_type=%s", self.doc_type)
            return 0
        
        path = f"{self.path}/{self.get_date(1)}/{self.get_date(2)}"

        field_values = []

        logger.info("parse_metadata: starting parse for doc_type=%s; events=%d", self.doc_type, len(metadata))

        for item in metadata:
            if item["event"]["method"] == "POST" and item["event"]["body"] != "":
                _dict = {'Name': '',
                         'First Name': '',
                         'Last Name': '',
                         'Applicant ID (K0012345)': '',
                         'Describe the document(s) you are loading.': '',
                         'Submit your document(s) to the following department:': '',
                         'Upload your file(s)': '',
                         'Fee Waiver Supportive Document': '',
                         'Phone Number': '',
                         'Email': ''
                         }
                for value in item["event"]["body"]["formSubmission"]["fieldValues"]:
                    _dict[value] = str(item["event"]["body"]["formSubmission"]["fieldValues"][value]).strip("[']").replace("'", "").replace('"', '')
                field_values.append(_dict)

        for idx, item in tqdm(enumerate(field_values)):
            try:
                full_path = os.path.abspath(os.path.join(path, f"{item['Applicant ID (K0012345)']}_{item['Name']}"))
                logger.info("Processing applicant %s name=%s -> %s", item['Applicant ID (K0012345)'], item['Name'], full_path)

                if not os.path.exists(full_path):
                    os.makedirs(full_path)
            except BaseException as b:
                logger.exception("Invalid directory path for %s: %s", full_path, b)
                pymsgbox.alert(f"{full_path} is not a possible directory. \n{sys.exc_info()[0]}\n{sys.exc_info()[1]}", "Warning!")

            if item['Upload your file(s)'] == '':
                item['Upload your file(s)'] = item['Fee Waiver Supportive Document']

            if item['Name'] == '':
                item['Name'] = f"{item['First Name']} {item['Last Name']}"

            if item['Describe the document(s) you are loading.'] == '':
                item['Describe the document(s) you are loading.'] = "App Fee Waiver"

            try:
                self.download_uploaded_files(item['Upload your file(s)'],
                                             item['Applicant ID (K0012345)'],
                                             item['Describe the document(s) you are loading.'],
                                             full_path, idx)
            except BaseException as b:
                logger.exception("Download failed for applicant %s url=%s", item['Applicant ID (K0012345)'], item['Upload your file(s)'])
                pymsgbox.alert(f"Download went wrong, please review {item['Upload your file(s)']} \n{sys.exc_info()[0]}\n{sys.exc_info()[1]}", "Warning!")

            self.create_info_file(full_path,
                                  item['Applicant ID (K0012345)'],
                                  item['Name'],
                                  item['Email'],
                                  item['Submit your document(s) to the following department:'],)

            pd.store_data(idx)
            sleep(1)

        # Save processed field values (one list per parse run)
        self.metadata = field_values

        pd.delete_data()

        # Return how many entries this parse handled so the caller can accurately total
        logger.info("parse_metadata: completed for doc_type=%s processed=%d", self.doc_type, len(field_values))
        return len(field_values)

    def download_uploaded_files(self, upload: str, applicant_id: str, description: str, full_path: str, idx: int) -> None:
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            logger.info("download_uploaded_files: downloading url=%s for applicant=%s", upload, applicant_id)
            doc = wget.download(upload, full_path)
            doc_components = os.path.splitext(doc)

            total = 1
            d = Definitions(description)
            file = os.path.abspath(os.path.join((full_path), f'{applicant_id}_{d.description}{total}{doc_components[1]}'))

            while os.path.exists(file):
                total += 1
                file = os.path.abspath(os.path.join((full_path), f'{applicant_id}_{d.description}{total}{doc_components[1]}'))

            os.rename(doc, file)
            logger.info("download_uploaded_files: saved file=%s", file)
            if doc_components[1] == '.docx':
                pdf_file = os.path.abspath(os.path.join((full_path), f'{applicant_id}_{d.description}{total}.pdf'))
                # Use the module-level convert() wrapper which performs a lazy import
                # and respects the CLIVE_ENABLE_DOCX2PDF environment guard. Tests patch
                # Webhook.requests.convert, so keep conversion logic centralized here.
                try:
                    converted = convert(file, pdf_file)
                    if converted:
                        logger.info("download_uploaded_files: conversion succeeded for %s", file)
                    else:
                        logger.info("download_uploaded_files: conversion not performed for %s", file)
                except Exception:
                    logger.exception("download_uploaded_files: unexpected error while converting %s", file)
        except BaseException as B:
            logger.exception("download_uploaded_file() error at %s: <%s, %s, %s>", idx, applicant_id, description, upload)
            pymsgbox.alert(f"download_uploaded_file() error at {idx}: <{applicant_id}, {description}, {upload}>. \n{sys.exc_info()}", "Warning!")

    def create_info_file(self, full_path: str, applicant_id: str, name: str, email: str, department: str) -> None:

        info_path = os.path.join(full_path, f"{applicant_id}_info.txt")
        with open(info_path, "w") as file:
            file.write("Name: " + name + "\n"
                       + "Email: " + email + "\n"
                       + "Applicant: " + applicant_id + "\n"
                       + "Department: " + department)
        logger.info("create_info_file: wrote %s", info_path)

    def count_files_created(self) -> int:
        """Counts files created under the directories referenced by the last parse run in self.metadata.

        This is a separate file-level counting method that does not modify download_uploaded_files().
        It inspects each applicant directory created during the last parse and sums up the files present.
        """
        if not self.metadata:
            logger.debug("count_files_created: no metadata available to count files")
            return 0

        base_path = os.path.join(self.path, self.get_date(1), self.get_date(2))
        total_files = 0
        for item in self.metadata:
            applicant_dir = os.path.abspath(os.path.join(base_path, f"{item['Applicant ID (K0012345)']}_{item['Name']}"))
            if os.path.isdir(applicant_dir):
                try:
                    files = [f for f in os.listdir(applicant_dir) if os.path.isfile(os.path.join(applicant_dir, f))]
                    # exclude info file entries
                    files = [f for f in files if not f.endswith('_info.txt')]
                    total_files += len(files)
                except Exception:
                    logger.exception("count_files_created: unable to list files in %s", applicant_dir)
        logger.info("count_files_created: total_files=%d", total_files)
        return total_files