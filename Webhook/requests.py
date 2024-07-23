import Webhook
import json
import wget
import os.path
import os
import ssl
from datetime import datetime

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

        pd = Webhook.Pipedream(self.doc_type)
        metadata = pd.get_events()
        ids = json.loads(metadata)
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
    
    def parse_metadata(self) -> None:
        """Method that gets the documents sent through the designated Pipedream target and passes them to the download_doc method.
        """

        pd = Webhook.Pipedream(self.doc_type)
        data = pd.get_data()
        object = json.loads(data)
        metadata = object["data"]

        if len(metadata) == 0:
            return
        
        path = f"{self.path}/{self.get_date(1)}/{self.get_date(2)}"
        
        field_values = []
        
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
                        _dict[value] = str(item["event"]["body"]["formSubmission"]["fieldValues"][value]).strip("[']")
                    field_values.append(_dict)

        for idx, item in enumerate(field_values):
            full_path = os.path.abspath(os.path.join(path, f"{item['Applicant ID (K0012345)']}_{item['Name']}"))
                
            if not os.path.exists(full_path):
                os.makedirs(full_path)

            if item['Upload your file(s)'] == '':
                item['Upload your file(s)'] = item['Fee Waiver Supportive Document']
            
            if item['Name'] == '':
                item['Name'] = f"{item['First Name']} {item['Last Name']}"

            if item['Describe the document(s) you are loading.'] == '':
                item['Describe the document(s) you are loading.'] = "App Fee Waiver"

            self.download_uploaded_files(item['Upload your file(s)'], 
                                        item['Applicant ID (K0012345)'], 
                                        item['Describe the document(s) you are loading.'], 
                                        full_path)
            
            self.create_info_file(full_path, 
                                  item['Applicant ID (K0012345)'],
                                  item['Name'],
                                  item['Email'], 
                                  item['Submit your document(s) to the following department:'],)
            
            pd.store_data(idx)
            self.metadata.append(field_values)

        pd.delete_data()

    def download_uploaded_files(self, upload: str, applicant_id: str, description: str, full_path: str) -> None:

        ssl._create_default_https_context = ssl._create_unverified_context
        doc = wget.download(upload, full_path)
        doc_components = os.path.splitext(doc)

        total = 1
        d = Webhook.Definitions(description)
        file = os.path.abspath(os.path.join((full_path), f'{applicant_id}_{d.description}{total}{doc_components[1]}'))

        while os.path.exists(file):
            total += 1
            file = os.path.abspath(os.path.join((full_path), f'{applicant_id}_{d.description}{total}{doc_components[1]}'))

        os.rename(doc, file)

    def create_info_file(self, full_path: str, applicant_id: str, name: str, email: str, department: str) -> None:

        with open(f"{full_path}" + "/" + f"{applicant_id}" + "_" + "info.txt", "w") as file:
            file.write("Name: " + name + "\n" 
                       + "Email: " + email + "\n"
                        + "Applicant: " + applicant_id + "\n" 
                        + "Department: " + department)
            file.close()