class grades:
    def __init__(self, gradeID, studentID, courseID,courseGrade):
        self.__gradeID = gradeID
        self.__courseName = courseName
        self.__courseID = courseID
        self.__courseGrade = courseGrade

    #Functions to get the variables.

    def get_gradeID(self):
        return self.__gradeID
    def get_studentID(self):
        return self.__studentID
    def get_courseID(self):
        return self.__courseID
    def get_courseGrade(self):
        return self.__courseGrade

    #Functions to Set the variables.

    def set_gradeID(self, gradeID):
        self.__gradeID = gradeID
    def set_studentID(self, studentID):
        self.__studentID = studentID
    def set_courseID(self, courseID):
        self.__courseID = courseID
    def set_courseGrade(self, courseGrade):
        self.__courseGrade = courseGrade

    #Include Additional functions
