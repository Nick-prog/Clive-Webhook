import Webhook
import json
import wget
import os.path
from datetime import datetime

current_id = {} #Stores the ids of the entries pulled during any instances

def total():
    Data = Webhook.id()
    dict = json.loads(Data)
    total = dict["page_info"]["total_count"]
    return total #Returns the total amount of entries available

def download(dept, loc):
    index = 0
    Data = Webhook.get()
    dict = json.loads(Data)
    list = dict["data"]

    if(len(list)!= 0):
        for x in range (len(list)):
            fieldValues = list[x].get("event").get("body").get("formSubmission").get("fieldValues") #Cycle through all 6 of the field values we acquire
            for y in fieldValues:
                items = fieldValues.get(y) #Grabs the context present in each field value
                department = str(fieldValues.get(Webhook.text("dept_text"))).strip("[']")
                applicant = str(fieldValues.get(Webhook.text("app_text"))).strip("[']")
                description = str(fieldValues.get(Webhook.text("des_text"))).strip("[']")
                name = str(fieldValues.get(Webhook.text("name_text"))).strip("[']")
                mail= str(fieldValues.get(Webhook.text("mail_text"))).strip("[']")

                if (y == Webhook.text("up_text") and department == f"{dept}"): #Method for pulling only files uploaded to a specfic department
                    id = Webhook.id()
                    dict = json.loads(id)
                    current_id[index] = dict["data"][x]["id"]
                    index += 1
                    temp = str(items).strip("[']")
                    url = str(temp).replace("\\", "/")
                    path = f"{loc}" + "/" + applicant.replace(" ", "")
                    if(url != ""):
                        Webhook.download_method(path, url, applicant, description, name, mail, department)

                elif (y == Webhook.text("up_text") and dept == "All"): #Method for pulling files from all departments
                    id = Webhook.id()
                    dict = json.loads(id)
                    current_id[index] = dict["data"][x]["id"]
                    index += 1
                    temp = str(items).strip("[']")
                    url = str(temp).replace("\\", "/")
                    path = f"{loc}"
                    if(url != ""):
                        Webhook.download_method(path, url, applicant, description, name, mail, department)

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

    return str(total) #Returns the current amount of entries for the real time table


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

    return date[0] #Returns the current date value for the real time table

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

    return current[0] #Returns the current time value for the real time table

def last():
    today = datetime.now()
    today_format = today.strftime("%m/%d/%Y")
    return today_format #Returns the last time the program has updated its real time values

def month_year():
    today = datetime.now()
    today_format = today.strftime("%B %Y")
    return today_format #Returns the current month and year

def now():
    today = datetime.now()
    today_format = today.strftime("%m.%d.%Y")
    return today_format #Returns the current month/date/year

def download_method(path, url, applicant, description, name, mail, department):

    filename = path + "/" + os.path.basename(url) #Acquire the filename

    if not os.path.exists(path): #Does a folder currently exist for this student?
        os.makedirs(path) #If not, create one...
        option = os.path.exists(filename)
        download_sent_file(url, path, applicant, description, option) #Downloads the user's sent file
        download_info_file(path, applicant, name, mail, department) #Creates a txt file based on the user's information
    else: #Else store the file in the student's folder
        option = os.path.exists(filename)
        download_sent_file(url, path, applicant, description, option)
        download_info_file(path, applicant, name, mail, department)
       
def download_sent_file(url, path, applicant, description, option):
    index = 0
    if(option == False): #File doesn't exist yet
        doc = wget.download(url, path)
        old_file = os.path.join(path, doc)
        ext = os.path.splitext(doc)
        new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + ext[1])
        while(os.path.exists(new_file) == True):
            new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index) + ext[1])
            index += 1
        os.rename(old_file, new_file)
    elif(option == True): #File does exist
        doc = wget.download(url, path)
        old_file = os.path.join(path, doc)
        ext = os.path.splitext(doc)
        new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index) + ext[1])
        while (os.path.exists(new_file) == True):
            index+=1
            new_file = os.path.join(path, applicant + "_" + Webhook.abbrevations(description) + Webhook.exists(index) + ext[1])
        os.rename(old_file, new_file)

def download_info_file(path, applicant, name, mail, department):
    file_name = f"{path}" + "/" + f"{applicant}" + "_" + "info.txt"
    file_info = open(file_name, "w")
    file_info.write("Name: " + name + "\n"
    + "Email: " + mail + "\n"
    + "Applicant: " + applicant + "\n"
    + "Department: " + department)
    file_info.close()
