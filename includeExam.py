
from PyQt5 import QtCore, QtGui, QtWidgets
from classes import *
import sqlite3
import win32api
import sys


class Ui_includeExam(object):

    def addQuestion(self):
        conn = sqlite3.connect('lms-system.db')
        c = conn.cursor()

        classNum = self.courseDropbox.currentText()
        exam = self.examDropbox.currentText()
        questionNum = self.questBox.currentText()
        question = self.questionTextbox.toPlainText()
        answerA = self.answerA.text()
        answerB = self.answerB.text()
        answerC = self.answerC.text()
        answerD = self.answerD.text()
        correctAnswer = self.correctanswerTextbox.text()

        print(classNum, exam, questionNum, question, answerA, answerB, answerC, answerD, correctAnswer)

        if ( (classNum=="") or (exam=="") or (questionNum=="") ):
            win32api.MessageBox(0, 'Please select a class, exam, or title.', 'Missing Information')
        else:
            try:
                c.execute("INSERT INTO exams (classNum, exam, questionNum, question, answerA, answerB, answerC, answerD, correctAnswer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (classNum, exam, questionNum, question, answerA, answerB, answerC, answerD, correctAnswer))

            except:
                return win32api.MessageBox(0, 'This Question already exists. Choose update to change', 'Question Exists')

        conn.commit()
        conn.close()

    def readQuestion(self):
        #This function reads the selected question from the database and fill up the corresponding fields.
        classNum = self.courseDropbox.currentText()
        exam = self.examDropbox.currentText()
        questionNum = self.questBox.currentText()

        if ( (classNum=="") or (exam=="") or (questionNum=="") ):
            return win32api.MessageBox(0, 'Please select a class, exam, or title.', 'Missing Information')

        try:
            conn = sqlite3.connect('lms-system.db')
            c = conn.cursor()
            c.execute("SELECT * FROM exams WHERE classNum=? AND exam=? AND questionNum=?", (classNum,exam,questionNum))
            a = c.fetchone()
            conn.commit()
            conn.close()
            print(a)
            #print(a[0],"-", a[1],"-", a[2],"-", a[3],"-", a[4],"-", a[5],"-", a[6],"-", a[7],"-", "Test")
            examquestion = examsTest(str(a[0]), str(a[1]), str(a[2]), str(a[3]), str(a[4]), str(a[5]), str(a[6]), str(a[7]), str(a[8]))
            print(examquestion)
            self.questionTextbox.setText(str(examquestion.question))
            self.answerA.setText(str(examquestion.answerA))
            self.answerB.setText(str(examquestion.answerB))
            self.answerC.setText(str(examquestion.answerC))
            self.answerD.setText(str(examquestion.answerD))
            self.correctanswerTextbox.setText(str(examquestion.correctAnswer))
            print("done reading")
        except:
            #print(sys.exc_info())
            return win32api.MessageBox(0, 'This Question do not exist.', 'Question do not Exist')


    def updateQuestion(self):

        classNum = self.courseDropbox.currentText()
        exam = self.examDropbox.currentText()
        questionNum = self.questBox.currentText()
        question = self.questionTextbox.toPlainText()
        answerA = self.answerA.text()
        answerB = self.answerB.text()
        answerC = self.answerC.text()
        answerD = self.answerD.text()
        correctAnswer = self.correctanswerTextbox.text()

        print(classNum, exam, questionNum, question, answerA, answerB, answerC, answerD, correctAnswer, "-update")

        if (question=="" or answerA=="" or answerb=="" or answerC=="" or answerD==""):
            return win32api.MessageBox(0, 'Please type a complete question', 'Missing Information')

        print(classNum, exam, questionNum, question, answerA, answerB, answerC, answerD, correctAnswer, "-updateAf")

        try:
            Print("trying")
            conn = sqlite3.connect('lms-system.db')
            c = conn.cursor()
            c.execute("UPDATE exams SET question=?, answerA=?, answerB=?, answerC=?, answerD=?, correctAnswer=? WHERE classNum=? AND exam=? AND questionNum=?", (question, answerA, answerB, answerC, answerD, correctAnswer, classNum, exam, questionNum))
            conn.commit()
            conn.close()
            print("Done Saving")
        except:
            print(sys.exc_info())
            return win32api.MessageBox(0, 'We could not save it!', 'Question do not Exist')



    def newQuestion(self):
        self.questBox.setCurrentIndex(0)
        self.questionTextbox.setText("")
        self.answerA.setText("")
        self.answerB.setText("")
        self.answerC.setText("")
        self.answerD.setText("")
        self.correctanswerTextbox.setText("")

    def setupUi(self, includeExam):
        includeExam.setObjectName("includeExam")
        includeExam.resize(262, 346)
        includeExam.setMinimumSize(QtCore.QSize(262, 346))
        includeExam.setMaximumSize(QtCore.QSize(262, 346))
        self.examDropbox = QtWidgets.QComboBox(includeExam)
        self.examDropbox.setGeometry(QtCore.QRect(140, 30, 101, 22))
        self.examDropbox.setObjectName("examDropbox")
        examDropbox = ["","Exam1", "Exam2", "Final"]
        self.examDropbox.addItems(examDropbox)
        self.courseDropbox = QtWidgets.QComboBox(includeExam)
        self.courseDropbox.setGeometry(QtCore.QRect(20, 30, 111, 22))
        self.courseDropbox.setObjectName("courseDropbox")
        courseItems = ["","Class1", "Class2", "Class3", "Class4"]
        self.courseDropbox.addItems(courseItems)
        self.classLabel = QtWidgets.QLabel(includeExam)
        self.classLabel.setGeometry(QtCore.QRect(20, 10, 47, 14))
        self.classLabel.setObjectName("classLabel")
        self.examLabel = QtWidgets.QLabel(includeExam)
        self.examLabel.setGeometry(QtCore.QRect(140, 10, 47, 14))
        self.examLabel.setObjectName("examLabel")
        self.questionTextbox = QtWidgets.QTextEdit(includeExam)
        self.questionTextbox.setGeometry(QtCore.QRect(20, 90, 221, 51))
        self.questionTextbox.setObjectName("questionTextbox")
        self.questionLabel = QtWidgets.QLabel(includeExam)
        self.questionLabel.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.questionLabel.setObjectName("questionLabel")
        self.aLabel = QtWidgets.QLabel(includeExam)
        self.aLabel.setGeometry(QtCore.QRect(20, 160, 47, 14))
        self.aLabel.setObjectName("aLabel")
        self.bLabel = QtWidgets.QLabel(includeExam)
        self.bLabel.setGeometry(QtCore.QRect(20, 190, 47, 14))
        self.bLabel.setObjectName("bLabel")
        self.cLabel = QtWidgets.QLabel(includeExam)
        self.cLabel.setGeometry(QtCore.QRect(20, 220, 47, 14))
        self.cLabel.setObjectName("cLabel")
        self.dLabel = QtWidgets.QLabel(includeExam)
        self.dLabel.setGeometry(QtCore.QRect(20, 250, 47, 14))
        self.dLabel.setObjectName("dLabel")
        self.answerA = QtWidgets.QLineEdit(includeExam)
        self.answerA.setGeometry(QtCore.QRect(40, 160, 201, 21))
        self.answerA.setObjectName("answerA")
        self.answerB = QtWidgets.QLineEdit(includeExam)
        self.answerB.setGeometry(QtCore.QRect(40, 190, 201, 21))
        self.answerB.setObjectName("answerB")
        self.answerC = QtWidgets.QLineEdit(includeExam)
        self.answerC.setGeometry(QtCore.QRect(40, 220, 201, 21))
        self.answerC.setObjectName("answerC")
        self.answerD = QtWidgets.QLineEdit(includeExam)
        self.answerD.setGeometry(QtCore.QRect(40, 250, 201, 21))
        self.answerD.setObjectName("answerD")
        self.questBox = QtWidgets.QComboBox(includeExam)
        self.questBox.setGeometry(QtCore.QRect(90, 60, 151, 22))
        self.questBox.setObjectName("questBox")
        quest = ["","Question1","Question2","Question3","Question4","Question5"]
        self.questBox.addItems(quest)
        self.quitButton = QtWidgets.QPushButton(includeExam)
        self.quitButton.setGeometry(QtCore.QRect(170, 310, 80, 22))
        self.quitButton.setObjectName("quitButton")
        self.addButton = QtWidgets.QPushButton(includeExam)
        self.addButton.setGeometry(QtCore.QRect(10, 280, 80, 22))
        self.addButton.setObjectName("addButton")
        self.updateButton = QtWidgets.QPushButton(includeExam)
        self.updateButton.setGeometry(QtCore.QRect(90, 280, 80, 22))
        self.updateButton.setObjectName("updateButton")
        self.saveButton = QtWidgets.QPushButton(includeExam)
        self.saveButton.setGeometry(QtCore.QRect(170, 280, 80, 22))
        self.saveButton.setObjectName("saveButton")
        self.correctanswerTextbox = QtWidgets.QLineEdit(includeExam)
        self.correctanswerTextbox.setGeometry(QtCore.QRect(100, 310, 60, 22))
        self.correctanswerTextbox.setObjectName("correctanswerTextbox")
        self.correctanswerTextbox.setPlaceholderText("Answer")
        self.correctanswerTextbox.setMaxLength(1)
        self.newButton = QtWidgets.QPushButton(includeExam)
        self.newButton.setGeometry(QtCore.QRect(10, 310, 80, 22))
        self.newButton.setObjectName("newButton")

        self.retranslateUi(includeExam)
        self.addButton.clicked.connect(self.addQuestion)
        self.updateButton.clicked.connect(self.readQuestion)
        self.saveButton.clicked.connect(self.updateQuestion)
        self.newButton.clicked.connect(self.newQuestion)
        self.quitButton.clicked.connect(includeExam.close)
        QtCore.QMetaObject.connectSlotsByName(includeExam)

    def retranslateUi(self, includeExam):
        _translate = QtCore.QCoreApplication.translate
        includeExam.setWindowTitle(_translate("includeExam", "Form"))
        self.classLabel.setText(_translate("includeExam", "Class:"))
        self.examLabel.setText(_translate("includeExam", "Exam:"))
        self.questionLabel.setText(_translate("includeExam", "Question:"))
        self.aLabel.setText(_translate("includeExam", "A)"))
        self.bLabel.setText(_translate("includeExam", "B)"))
        self.cLabel.setText(_translate("includeExam", "C)"))
        self.dLabel.setText(_translate("includeExam", "D)"))
        self.quitButton.setText(_translate("includeExam", "Quit"))
        self.addButton.setText(_translate("includeExam", "Add"))
        self.updateButton.setText(_translate("includeExam", "Update"))
        self.saveButton.setText(_translate("includeExam", "Save"))
        self.newButton.setText(_translate("includeExam", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    includeExam = QtWidgets.QWidget()
    ui = Ui_includeExam()
    ui.setupUi(includeExam)
    includeExam.show()
    sys.exit(app.exec_())
