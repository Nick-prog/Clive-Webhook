
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
            "Certificate of Eligibility/Award Letter": "OTHR",
            "College Transcript": "UCT",
            "Degree Certificate": "UDC",
            "Duolingo Scores": "UDET",
            "Financial Support Statement": "FASS",
            "GED Scores": "UGED",
            "GRE Scores": "UGRE",
            "High School Transcript": "UHS",
            "IELTS Scores": "UELT",
            "Letter of Recommendation": "LTR",
            "MAT Scores": "UMAT",
            "Military Discharge Form": "OTHR",
            "Military Leave & Earnings": "LES",
            "Military Transcript": "UCT",
            "Naturalization Certificate": "NCRT",
            "Other": "OTHR",
            "Passport": "PASS",
            "Personal Statement": "PERS",
            "Proof of Dependency/Vital Records": "OTHR",
            "PTE Scores": "PTEU",
            "Resident Alien Card": "RACD",
            "Residency Verification Form": "RSEF",
            "Resume": "RSME",
            "SAT or ACT Scores": "TSTS",
            "Statement of Purpose": "STMT",
            "Secondary School Transcript": "SCTR",
            "TX Hazelwood Act Continued Enrollment Form": "OTHR",
            "TX Hazelwood Act Exemption App": "OTHR",
            "TOEFL Scores": "UTFL",
            "TSI Scores": "TSIA",
            "VA Disability Rating Sheet": "OTHR"
        }

        self.description = _dict[description]