
def abbrevations(x):
    dict = {
        "Affidavit of Intent": "1528",
        "Certificate of Eligibility/Award Letter": "VETA-COE",
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
        "Military Discharge Form": "VETA-DD214",
        "Military Leave & Earnings": "LES",
        "Military Transcript": "VETA-TRNSCRPT-MLTRY",
        "Naturalization Certificate": "NCRT",
        "Other": "OTHR",
        "Passport": "PASS",
        "Personal Statement": "PERS",
        "Proof of Dependency/Vital Records": "VETA-VITAL_RECORDS",
        "PTE Scores": "UPET",
        "Residency Alien Card": "RACD",
        "Resume": "RSME",
        "SAT or ACT Scores": "TSTS",
        "Statement of Purpose": "STMT",
        "Secondary School Transcript": "SCTR",
        "TX Hazelwood Act Continued Enrollment Form": "VETA-CONT_ENROLMNT",
        "TX Hazelwood Act Exemption App": "VETA-HZLWED-EXEMPT",
        "TOEFL Scores": "UTFL",
        "TSI Scores": "UTSI",
        "VA Disability Rating Sheet": "VETA-LTR_DISAB-RATING"
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

def exists(x):
    dict = {
        0: "_a",
        1: "_b",
        2: "_c",
        3: "_d",
        4: "_e",
        5: "_f",
        6: "_g",
        7: "_h",
        8: "_i",
        9: "_j",
        10: "_k",
        11: "_l",
        12: "_m",
        13: "_n",
        14: "_o",
        15: "_p",
        16: "_q",
        17: "_r",
        18: "_s",
        19: "_t",
        20: "_u",
        21: "_v",
        22: "_w",
        23: "_x",
        24: "_y",
        25: "_z"
    }
    return dict[x]
