import Webhook, json, wget, os, os.path
from datetime import datetime

app_text = "Applicant ID (K0012345)"
des_text = "Describe the document(s) you are loading."
up_text = "Upload your file(s)"
dept_text = "Submit your document(s) to the following department:"
mail_text = "Email"
name_text = "Name"

def total():
    Data = Webhook.id()
    dict = json.loads(Data)
    total = dict["page_info"]["total_count"]
    return total

def download(dept, loc):
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list)!= 0):
        for x in range (len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues")
            for y in fieldValues:
                items = fieldValues.get(y)
                department = str(fieldValues.get(dept_text)).strip("[']")
                applicant = str(fieldValues.get(app_text)).strip("[']")
                description = str(fieldValues.get(des_text)).strip("[']")
                name = str(fieldValues.get(name_text)).strip("[']")
                mail= str(fieldValues.get(mail_text)).strip("[']")

                if (y == up_text and dept == "All"):
                    url = str(items).strip("[']")
                    path = f"{loc}"
                    doc = wget.download(url, path)
                    old_file = os.path.join(path, doc)
                    new_file = os.path.join(path, applicant + "_" + f"{x}" +".pdf")
                    os.rename(old_file, new_file)

                    file_name = f"{path}" + "/" + f"{applicant}" + "_" + "info.txt"
                    file_info = open(file_name, "w")
                    file_info.write("Name: " + name + "\n"
                    + "Email: " + mail + "\n"
                    + "Applicant: " + applicant + "\n"
                    + "Description: " + description + "\n"
                    + "Department: " + department)
                    file_info.close()

                elif(y == up_text and department == f"{dept}"):
                    url = str(items).strip("[']")
                    path = f"{loc}"
                    doc = wget.download(url, path)
                    old_file = os.path.join(path, doc)
                    new_file = os.path.join(path, applicant + "_" + f"{x}" + ".pdf")
                    os.rename(old_file, new_file)

                    file_name = f"{path}" + "/" + f"{applicant}" + "_" + "info.txt"
                    file_info = open(file_name, "w")
                    file_info.write("Name: " + name + "\n"
                    + "Email: " + mail + "\n"
                    + "Applicant: " + applicant + "\n"
                    + "Description: " + description + "\n"
                    + "Department: " + department)
                    file_info.close()

def entries(dept):
    total = 0
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list)!= 0):
        for x in range(len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues")
            for y in fieldValues:
                department = str(fieldValues.get(dept_text)).strip("[']")
                if(y == dept_text and department == f"{dept}"):
                    total += 1

    return total


def date(dept):
    date = {0: "None"}
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list) != 0):
        for x in range(len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues")
            for y in fieldValues:
                department = str(fieldValues.get(dept_text)).strip("[']")
                if(y == dept_text and department == f"{dept}"):
                    result = list[x].get("event").get("body").get("formSubmission").get("context").get("time")
                    date[x] = result[:-14]
    
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
                department = str(fieldValues.get(dept_text)).strip("[']")
                if(y == dept_text and department == f"{dept}"):
                    result = list[x].get("event").get("body").get("formSubmission").get("context").get("time")
                    current[x] = result[11:-8]
    
    return current[0]

def last():
    today = datetime.now()
    today_format = today.strftime("%d/%m/%Y")
    return today_format