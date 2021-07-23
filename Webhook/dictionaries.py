
def abbrevations(x):
    dict = {
        "Affidavit of Intent": "1528",
        "College Transcript": "UCT",
        "Degree Certificate": "UCT",
        "Duolingo Scores": "UDET",
        "Financial Support Statement": "FASS",
        "GED Scores": "UGED",
        "GRE Scores": "UGRE",
        "High School Transcript": "UHS",
        "IELTS Scores": "UELT",
        "Letter of Recommendation": "LTR",
        "MAT Scores": "UMAT",
        "Military Discharge Form": "D214",
        "Military Leave & Earnings": "LES",
        "Naturalization Certificate": "NCRT",
        "Other": "OTHR",
        "Passport": "PASS",
        "Personal Statement": "PERS",
        "PTE Scores": "UPET",
        "Residency Alien Card": "RACD",
        "Resume": "RSME",
        "SAT or ACT Scores": "TSTS",
        "Statement of Purpose": "STMT",
        "Secondary School Transcript": "SCTR",
        "TOEFL Scores": "UTFL",
        "TSI Scores": "UTSI"
    }
    return dict[x]

def departments(x):
    dict = { 
        0 : "Admission", 
        1 : "Financial Aid", 
        2 : "Military and Veteran Resource Center",
        3 : "Registrar", 
        4 : "International Student & Scholar Services", 
        5 : "Other", 
        6 : "All"
    }
    return dict[x]

def text(x):
    dict = {
        "app_text": "Applicant ID (K0012345)",
        "des_text": "Describe the document(s) you are loading.",
        "up_text": "Upload your file(s)",
        "dept_text": "Submit your document(s) to the following department:",
        "mail_text": "Email",
        "name_text": "Name"
    }
    return dict[x]

def table_vertical(x):
    dict = {
        0 : "-1-",
        1 : "-2-",
        2 : "-3-",
        3 : "-4-",
        4 : "-5-",
        5 : "-6-",
    }
    return dict[x]

def table_horizontal(x):
    dict = {
        0 : "Entries",
        1 : "Date",
        2 : "Time",
        3 : "Last",
    }
    return dict[x]