
def abbrevations(x): #Dictionary for the different options in "Describe the document(s) you are loading."
    dict = {
        "Affidavit of Intent": "1528",
        "All/Multiple" : "All",
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
        "PTE Scores": "PTEU",
        "Resident Alien Card": "RACD",
        "Residency Verification Form": "RSVF",
        "Resume": "RSME",
        "SAT or ACT Scores": "TSTS",
        "Statement of Purpose": "STMT",
        "Secondary School Transcript": "SCTR",
        "Transcripts": "UCT",
        "TX Hazelwood Act Continued Enrollment Form": "VETA-CONT_ENROLMNT",
        "TX Hazelwood Act Exemption App": "VETA-HZLWED-EXEMPT",
        "TOEFL Scores": "UTFL",
        "TSI Scores": "TSIA",
        "VA Disability Rating Sheet": "VETA-LTR_DISAB-RATING"
    }
    return dict[x]

def departments(x): #Dictionary for the different option in "Submit your document(s) to the following department:"
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

def text(x): #Dictionary to shorten the categories present on the Upload Documents Clive form
    dict = {
        "mail_text": "Email",
        "name_text": "Name",
        "app_text": "Applicant ID (K0012345)",
        "des_text": "Describe the document(s) you are loading.",
        #"up_text": "No file chosen",
        "up_text": "Upload your file(s)",
        "dept_text": "Submit your document(s) to the following department:",
    }
    return dict[x]

def text2(x): #Dictionary to shorten the categories present on the Fee Waiver Request Clive form
    dict = {
        "first_text": "First Name",
        "last_text": "Last Name",
        "phone_text": "Phone Number",
        "mail_text": "Email",
        "up_text": "Fee Waiver Supportive Document",
        "app_text": "Applicant ID (K0012345)"
    }
    return dict[x]

def exists(x): #Dictionary for any potential repeat files sent by students
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