class course:
    def __init__(self, courseID, courseName, facultyID):
        self.__courseID = courseID
        self.__courseName = courseName
        self.__facultyID = facultyID

    #Functions to get the variables.

    def get_courseID(self):
        return self.__courseID
    def get_courseName(self):
        return self.__courseName
    def get_facultyID(self):
        return self.__facultyID

    #Functions to Set the variables.

    def set_courseID(self, courseID):
        self.__courseID = courseID
    def set_courseName(self, courseName):
        self.__courseName = courseName
    def set_facultyID(self, facultyID):
        self.__facultyID = facultyID
