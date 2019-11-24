
from PyQt5 import QtCore, QtGui, QtWidgets
from includeExam import Ui_includeExam
from ProfessorScreen import Ui_Professor

class Ui_professorMenu(object):
    def openExams(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_includeExam()
        self.ui.setupUi(self.window)
        self.window.show()
        #I do not know why but this function call breaks the login screen
        #professorMenu.hide()

    def openGrades(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Professor()
        self.ui.setupUi(self.window)
        self.window.show()
        #This one also breaks the login screen
        #professorMenu.hide()

    def setupUi(self, professorMenu):
        professorMenu.setObjectName("professorMenu")
        professorMenu.resize(137, 128)
        self.profexamsButton = QtWidgets.QPushButton(professorMenu)
        self.profexamsButton.setGeometry(QtCore.QRect(20, 40, 101, 25))
        self.profexamsButton.setObjectName("profexamsButton")
        self.profgradesButton = QtWidgets.QPushButton(professorMenu)
        self.profgradesButton.setGeometry(QtCore.QRect(20, 80, 101, 25))
        self.profgradesButton.setObjectName("profgradesButton")
        self.professprmenuLabel = QtWidgets.QLabel(professorMenu)
        self.professprmenuLabel.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.professprmenuLabel.setObjectName("professprmenuLabel")

        self.retranslateUi(professorMenu)
        self.profexamsButton.clicked.connect(self.openExams)
        self.profgradesButton.clicked.connect(self.openGrades)
        QtCore.QMetaObject.connectSlotsByName(professorMenu)

    def retranslateUi(self, professorMenu):
        _translate = QtCore.QCoreApplication.translate
        professorMenu.setWindowTitle(_translate("professorMenu", "Professor Menu"))
        self.profexamsButton.setText(_translate("professorMenu", "Exams"))
        self.profgradesButton.setText(_translate("professorMenu", "Grades"))
        self.professprmenuLabel.setText(_translate("professorMenu", "Professor Menu:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    professorMenu = QtWidgets.QWidget()
    ui = Ui_professorMenu()
    ui.setupUi(professorMenu)
    professorMenu.show()
    sys.exit(app.exec_())
