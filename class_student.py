class student:
    def __init__(self, studentID, fName, lName, userName, password, GPA):
        self.__studentID = studentID
        self.__fName = fName
        self.__lName = lName
        self.__userName = userName
        self.__password = password
        self.__GPA = GPA

    #Functions to get the variables.

    def get_studentID(self):
        return self.__studentID
    def get_fName(self):
        return self.__fName
    def get_lName(self):
        return self.__lName
    def get_userName(self):
        return self.__userName
    def get_password(self):
        return self.__password
    def get_GPA(self):
        return self.__GPA

    #Functions to Set the variables.

    def set_studentID(self, studentID):
        self.__studentID = studentID
    def set_fName(self, fName ):
        self.__fName = fName
    def set_lName(self, lName ):
        self.__lName = lName
    def set_userName(self, userName):
        self.__userName = userName
    def set_password(self, password):
        self.__password = password
    def set_GPA(self, GPA):
        self.__GPA = GPA
