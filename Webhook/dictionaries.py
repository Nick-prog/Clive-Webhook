
class Definitions:

    def __init__(self, description: str):
        """Dictionary method for the different options in "Describe the document(s) you are loading."

        :param input: chosen file type option
        :type input: str
        :return: correlated markdown text
        :rtype: str
        """

        _dict = {
            "App Fee Waiver": "AFWR",
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
            "Letter of recommendation": "LTR",
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

        self.description = _dict[description]