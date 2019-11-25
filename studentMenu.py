######################################################
#    Student Menu Screen
######################################################


from PyQt5 import QtCore, QtGui, QtWidgets
from studentScreen import Ui_Student
from takeExam import Ui_includeExam

class Ui_studentMenu(object):

    def openExams(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_includeExam()
        self.ui.setupUi(self.window)
        self.window.show()
        #I do not know why but this function call breaks the login screen
        #professorMenu.hide()

    def openGrades(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Student()
        self.ui.setupUi(self.window)
        self.window.show()
        #This one also breaks the login screen
        #professorMenu.hide()

    def setupUi(self, studentMenu):
        studentMenu.setObjectName("studentMenu")
        studentMenu.resize(137, 128)
        self.studentexamsButton = QtWidgets.QPushButton(studentMenu)
        self.studentexamsButton.setGeometry(QtCore.QRect(20, 40, 101, 25))
        self.studentexamsButton.setObjectName("studentexamsButton")
        self.studentgradesButton = QtWidgets.QPushButton(studentMenu)
        self.studentgradesButton.setGeometry(QtCore.QRect(20, 80, 101, 25))
        self.studentgradesButton.setObjectName("studentgradesButton")
        self.professprmenuLabel = QtWidgets.QLabel(studentMenu)
        self.professprmenuLabel.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.professprmenuLabel.setObjectName("professprmenuLabel")

        self.retranslateUi(studentMenu)
        self.studentexamsButton.clicked.connect(self.openExams)
        self.studentgradesButton.clicked.connect(self.openGrades)
        QtCore.QMetaObject.connectSlotsByName(studentMenu)

    def retranslateUi(self, studentMenu):
        _translate = QtCore.QCoreApplication.translate
        studentMenu.setWindowTitle(_translate("studentMenu", "Professor Menu"))
        self.studentexamsButton.setText(_translate("studentMenu", "Exams"))
        self.studentgradesButton.setText(_translate("studentMenu", "Grades"))
        self.professprmenuLabel.setText(_translate("studentMenu", "Student Menu:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    studentMenu = QtWidgets.QWidget()
    ui = Ui_studentMenu()
    ui.setupUi(studentMenu)
    studentMenu.show()
    sys.exit(app.exec_())
