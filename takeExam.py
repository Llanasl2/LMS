
from PyQt5 import QtCore, QtGui, QtWidgets
from classes import *
import sqlite3
import win32api
import sys

class Ui_includeExam(object):

    def nextQuestion(self):
        print(self.questBox.currentIndex())
        self.nextButton.setEnabled(True)
        self.previousButton.setEnabled(True)
        if self.questBox.currentIndex() == 4:
            self.nextButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)
        self.questBox.setCurrentIndex(self.questBox.currentIndex() + 1)
        self.readQuestion()

    def previousQuestion(self):
        print(self.questBox.currentIndex())
        self.nextButton.setEnabled(True)
        self.previousButton.setEnabled(True)
        if self.questBox.currentIndex() == 2:
            self.previousButton.setEnabled(False)
        else:
            self.previousButton.setEnabled(True)
        self.questBox.setCurrentIndex(self.questBox.currentIndex() - 1)
        self.readQuestion()


    def readQuestion(self):
        #This function reads the selected question from the database and fill up the corresponding fields.
        classNum = self.courseDropbox.currentText()
        exam = self.examDropbox.currentText()
        questionNum = self.questBox.currentText()

        if ( (classNum=="") or (exam=="") or (questionNum=="") ):
            return win32api.MessageBox(0, 'Please select a class, exam, or title.', 'Missing Information')

        #set the question number according to the question selected.
        if questionNum == "Question1": qnum = 0
        if questionNum == "Question2": qnum = 1
        if questionNum == "Question3": qnum = 2
        if questionNum == "Question4": qnum = 3
        if questionNum == "Question5": qnum = 4

        try:
            conn = sqlite3.connect('lms-system.db')
            c = conn.cursor()
            c.execute("SELECT * FROM exams WHERE classNum=? AND exam=?", (classNum,exam))
            a = c.fetchall()
            conn.commit()
            conn.close()
            print(a)
            #print(a[0],"-", a[1],"-", a[2],"-", a[3],"-", a[4],"-", a[5],"-", a[6],"-", a[7],"-", "Test")
            examquestion = []
            for i in range(len(a)):
                examquestion.append(examsTest(str(a[i][0]), str(a[i][1]), str(a[i][2]), str(a[i][3]), str(a[i][4]), str(a[i][5]), str(a[i][6]), str(a[i][7]), str(a[i][8])))
            print(examquestion)
            self.questionTextbox.setText(str(examquestion[qnum].question))
            self.answerA.setText(str(examquestion[qnum].answerA))
            self.answerB.setText(str(examquestion[qnum].answerB))
            self.answerC.setText(str(examquestion[qnum].answerC))
            self.answerD.setText(str(examquestion[qnum].answerD))
            print("done reading")
        except:
            #print(sys.exc_info())
            return win32api.MessageBox(0, 'This Question do not exist.', 'Question do not Exist')

    def setupUi(self, includeExam):
        includeExam.setObjectName("includeExam")
        includeExam.resize(288, 346)
        includeExam.setMinimumSize(QtCore.QSize(262, 346))
        includeExam.setMaximumSize(QtCore.QSize(1000, 1000))
        self.examDropbox = QtWidgets.QComboBox(includeExam)
        self.examDropbox.setGeometry(QtCore.QRect(150, 30, 121, 22))
        self.examDropbox.setObjectName("examDropbox")
        examDropbox = ["","Exam1", "Exam2", "Final"]
        self.examDropbox.addItems(examDropbox)
        self.courseDropbox = QtWidgets.QComboBox(includeExam)
        self.courseDropbox.setGeometry(QtCore.QRect(20, 30, 121, 22))
        self.courseDropbox.setObjectName("courseDropbox")
        courseItems = ["","Class1", "Class2", "Class3", "Class4"]
        self.courseDropbox.addItems(courseItems)
        self.classLabel = QtWidgets.QLabel(includeExam)
        self.classLabel.setGeometry(QtCore.QRect(20, 10, 47, 14))
        self.classLabel.setObjectName("classLabel")
        self.examLabel = QtWidgets.QLabel(includeExam)
        self.examLabel.setGeometry(QtCore.QRect(150, 10, 47, 14))
        self.examLabel.setObjectName("examLabel")
        self.questionTextbox = QtWidgets.QTextEdit(includeExam)
        self.questionTextbox.setEnabled(False)
        self.questionTextbox.setGeometry(QtCore.QRect(20, 90, 251, 51))
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
        self.answerA.setEnabled(False)
        self.answerA.setGeometry(QtCore.QRect(40, 160, 201, 21))
        self.answerA.setObjectName("answerA")
        self.answerB = QtWidgets.QLineEdit(includeExam)
        self.answerB.setEnabled(False)
        self.answerB.setGeometry(QtCore.QRect(40, 190, 201, 21))
        self.answerB.setObjectName("answerB")
        self.answerC = QtWidgets.QLineEdit(includeExam)
        self.answerC.setEnabled(False)
        self.answerC.setGeometry(QtCore.QRect(40, 220, 201, 21))
        self.answerC.setObjectName("answerC")
        self.answerD = QtWidgets.QLineEdit(includeExam)
        self.answerD.setEnabled(False)
        self.answerD.setGeometry(QtCore.QRect(40, 250, 201, 21))
        self.answerD.setObjectName("answerD")
        self.questBox = QtWidgets.QComboBox(includeExam)
        self.questBox.setGeometry(QtCore.QRect(90, 60, 181, 22))
        self.questBox.setObjectName("questBox")
        quest = ["","Question1","Question2","Question3","Question4","Question5"]
        self.questBox.addItems(quest)
        self.quitButton = QtWidgets.QPushButton(includeExam)
        self.quitButton.setGeometry(QtCore.QRect(190, 310, 80, 22))
        self.quitButton.setObjectName("quitButton")
        self.previousButton = QtWidgets.QPushButton(includeExam)
        self.previousButton.setGeometry(QtCore.QRect(10, 280, 80, 22))
        self.previousButton.setObjectName("previousButton")
        self.openButton = QtWidgets.QPushButton(includeExam)
        self.openButton.setGeometry(QtCore.QRect(100, 280, 80, 22))
        self.openButton.setObjectName("openButton")
        self.nextButton = QtWidgets.QPushButton(includeExam)
        self.nextButton.setGeometry(QtCore.QRect(190, 280, 80, 22))
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setEnabled(True)
        self.radioA = QtWidgets.QRadioButton(includeExam)
        self.radioA.setGeometry(QtCore.QRect(250, 160, 99, 22))
        self.radioA.setText("")
        self.radioA.setObjectName("radioA")
        self.buttonGroup = QtWidgets.QButtonGroup(includeExam)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioA)
        self.radioB = QtWidgets.QRadioButton(includeExam)
        self.radioB.setGeometry(QtCore.QRect(250, 190, 99, 22))
        self.radioB.setText("")
        self.radioB.setObjectName("radioB")
        self.buttonGroup.addButton(self.radioB)
        self.radioC = QtWidgets.QRadioButton(includeExam)
        self.radioC.setGeometry(QtCore.QRect(250, 220, 99, 22))
        self.radioC.setText("")
        self.radioC.setObjectName("radioC")
        self.buttonGroup.addButton(self.radioC)
        self.radioD = QtWidgets.QRadioButton(includeExam)
        self.radioD.setGeometry(QtCore.QRect(250, 250, 99, 22))
        self.radioD.setText("")
        self.radioD.setObjectName("radioD")
        self.buttonGroup.addButton(self.radioD)

        self.retranslateUi(includeExam)
        self.previousButton.clicked.connect(self.previousQuestion)
        self.openButton.clicked.connect(self.readQuestion)
        self.nextButton.clicked.connect(self.nextQuestion)
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
        self.previousButton.setText(_translate("includeExam", "Previous"))
        self.openButton.setText(_translate("includeExam", "Open"))
        self.nextButton.setText(_translate("includeExam", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    includeExam = QtWidgets.QWidget()
    ui = Ui_includeExam()
    ui.setupUi(includeExam)
    includeExam.show()
    sys.exit(app.exec_())
