
#grades( a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], a[16])
class grades:
    def __init__(self, user, c1c, c1e1, c1e2, c1f, c2c, c2e1, c2e2, c2f, c3c, c3e1, c3e2, c3f, c4c, c4e1, c4e2, c4f):
        #student name
        self.student = user
        #create each grade as an object that can be calculated as desired.
        #class1
        self.class1credits = grade(c1c)
        self.class1exam1 = grade(c1e1)
        self.class1exam2 = grade(c1e2)
        self.class1final = grade(c1f)
        #class2
        self.class2credits = grade(c2c)
        self.class2exam1 = grade(c2e1)
        self.class2exam2 = grade(c2e2)
        self.class2final = grade(c2f)
        #class3
        self.class3credits = grade(c3c)
        self.class3exam1 = grade(c3e1)
        self.class3exam2 = grade(c3e2)
        self.class3final = grade(c3f)
        #class4
        self.class4credits = grade(c4c)
        self.class4exam1 = grade(c4e1)
        self.class4exam2 = grade(c4e2)
        self.class4final = grade(c4f)

    def GPA(self):
        credits = int(self.class1credits.value()) + int(self.class2credits.value()) + int(self.class3credits.value()) + int(self.class4credits.value())
        class1 = int(self.class1exam1.letterGrade()[1]) + int(self.class1exam2.letterGrade()[1]) + int(self.class1final.letterGrade()[1])
        class2 = int(self.class2exam1.letterGrade()[1]) + int(self.class2exam2.letterGrade()[1]) + int(self.class2final.letterGrade()[1])
        class3 = int(self.class3exam1.letterGrade()[1]) + int(self.class3exam2.letterGrade()[1]) + int(self.class3final.letterGrade()[1])
        class4 = int(self.class4exam1.letterGrade()[1]) + int(self.class4exam2.letterGrade()[1]) + int(self.class4final.letterGrade()[1])
        return str((class1 + class2 + class3 + class4)/(credits))
#class to generate the letter Grade.
#this class should be used inside another class that takes the grades from the database.
class grade:
    def __init__(self, grade):
        self.grade = grade

    def  letterGrade(self):
        if (int(self.grade) < 60): return ('F', 0)
        if (int(self.grade) >= 60) and (int(self.grade) < 70): return ('D', 1)
        if (int(self.grade) >= 70) and (int(self.grade) < 80): return ('C', 2)
        if (int(self.grade) >= 80) and (int(self.grade) < 90): return ('B', 3)
        if (int(self.grade) >= 90): return ('A', 4)

    #function to return the value of the variable grade as string
    def value(self):
        return str(self.grade)

class examsTest:
    def __init__(self, classNum, exam, questionNum, question, answerA, answerB, answerC, answerD):
        self.classNum = classNum
        self.exam = exam
        self.questionNum = questionNum
        self.question = question
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD
