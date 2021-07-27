import Webhook
import json
import wget
import os.path
from datetime import datetime

current_id = {}

def total():
    Data = Webhook.id()
    dict = json.loads(Data)
    total = dict["page_info"]["total_count"]
    return total

def download(dept, loc):
    index = 0
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list)!= 0):
        for x in range (len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues")
            for y in fieldValues:
                items = fieldValues.get(y)
                department = str(fieldValues.get(Webhook.text("dept_text"))).strip("[']")
                applicant = str(fieldValues.get(Webhook.text("app_text"))).strip("[']")
                description = str(fieldValues.get(Webhook.text("des_text"))).strip("[']")
                name = str(fieldValues.get(Webhook.text("name_text"))).strip("[']")
                mail= str(fieldValues.get(Webhook.text("mail_text"))).strip("[']")

                if (y == Webhook.text("up_text") and department == f"{dept}"):
                    id = Webhook.id()
                    dict = json.loads(id)
                    current_id[index] = dict["data"][x]["id"]
                    index += 1
                    temp = str(items).strip("[']")
                    url = str(temp).replace("\\", "/")
                    path = f"{loc}" + "/" + applicant.replace(" ", "")
                    if(url != ""):
                        Webhook.download_method(path, url, applicant, description, name, mail, department, index)

                elif (y == Webhook.text("up_text") and dept == "All"):
                    id = Webhook.id()
                    dict = json.loads(id)
                    current_id[index] = dict["data"][x]["id"]
                    index += 1
                    url = str(items).strip("[']")
                    path = f"{loc}"
                    if(url != ""):
                        Webhook.download_method(path, url, applicant, description, name, mail, department, index)

def entries(dept):
    total = 0
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list)!= 0):
        for x in range(len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues")
            for y in fieldValues:
                department = str(fieldValues.get(Webhook.text("dept_text"))).strip("[']")
                if(y == Webhook.text("dept_text") and department == Webhook.departments(dept)):
                    total += 1

    return str(total)


def date(dept):
    date = {0: "None"}
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list) != 0):
        for x in range(len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues")
            for y in fieldValues:
                department = str(fieldValues.get(Webhook.text("dept_text"))).strip("[']")
                if(y == Webhook.text("dept_text") and department == Webhook.departments(dept)):
                    result = list[x].get("event").get("body").get("formSubmission").get("context").get("time")
                    date[0] = result[:-14]

    return date[0]

def current(dept):
    current = {0: "None"}
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list) != 0):
        for x in range(len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues")
            for y in fieldValues:
                department = str(fieldValues.get(Webhook.text("dept_text"))).strip("[']")
                if(y == Webhook.text("dept_text") and department == Webhook.departments(dept)):
                    result = list[x].get("event").get("body").get("formSubmission").get("context").get("time")
                    current[0] = result[11:-8]

    return current[0]

def last():
    today = datetime.now()
    today_format = today.strftime("%m/%d/%Y")
    return today_format

def month_year():
    today = datetime.now()
    today_format = today.strftime("%B %Y")
    return today_format

def now():
    today = datetime.now()
    today_format = today.strftime("%m.%d.%Y")
    return today_format

def download_method(path, url, applicant, description, name, mail, department, index):

    if not os.path.exists(path):
        os.makedirs(path)
        doc = wget.download(url, path)
        old_file = os.path.join(path, doc)
        ext = os.path.splitext(doc)
        new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + ext[1])
        os.rename(old_file, new_file)

        file_name = f"{path}" + "/" + f"{applicant}" + "_" + "info.txt"
        file_info = open(file_name, "w")
        file_info.write("Name: " + name + "\n"
        + "Email: " + mail + "\n"
        + "Applicant: " + applicant + "\n"
        + "Department: " + department)
        file_info.close()

    else:
        doc = wget.download(url, path)
        old_file = os.path.join(path, doc)
        ext = os.path.splitext(doc)
        new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index) + ext[1])
        os.rename(old_file, new_file)

        file_name = f"{path}" + "/" + f"{applicant}" + "_" + "info.txt"
        file_info = open(file_name, "w")
        file_info.write("Name: " + name + "\n"
        + "Email: " + mail + "\n"
        + "Applicant: " + applicant + "\n"
        + "Department: " + department)
        file_info.close()
