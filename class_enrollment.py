class course:
    def __init__(self, enrollmentID, studentID, courseID):
        self.__enrollmentID = enrollmentID
        self.__studentID = studentID
        self.__courseID = courseID

    #Functions to get the variables.

    def get_enrollmentID(self):
        return self.__enrollmentID
    def get_studentID(self):
        return self.__studentID
    def get_courseID(self):
        return self.__courseID

    #Functions to Set the variables.

    def set_enrollmentID(self, enrollmentID):
        self.__enrollmentID = enrollmentID
    def set_studentID(self, studentID):
        self.__studentID = studentID
    def set_courseID(self, courseID):
        self.__courseID = courseID

    #Include Aditional functions.
