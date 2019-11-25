# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_studentMenu(object):
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
        self.studentexamsButton.clicked.connect(studentMenu.close)
        self.studentgradesButton.clicked.connect(studentMenu.close)
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
