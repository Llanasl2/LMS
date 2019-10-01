class faculty:
    def __init__(self, facultyID, fName, lName, userName, password, jobTitle):
        self.__facultyID = facultyID
        self.__fName = fName
        self.__lName = lName
        self.__userName = userName
        self.__password = password
        self.__jobTitle = jobTitle

    #Functions to get the variables.

    def get_falcultyID(self):
        return self.__facultyID
    def get_fName(self):
        return self.__fName
    def get_lName(self):
        return self.__lName
    def get_userName(self):
        return self.__userName
    def get_password(self):
        return self.__password
    def get_jobTitle(self):
        return self.__jobTitle

    #Functions to Set the variables.

    def set_facultyID(self, facultyID):
        self.__facultyID = facultyID
    def set_fName(self, fName ):
        self.__fName = fName
    def set_lName(self, lName ):
        self.__lName = lName
    def set_userName(self, userName):
        self.__userName = userName
    def set_password(self, password):
        self.__password = password
    def set_GPA(self, jobTitle):
        self.__jobTitle = jobTitle
