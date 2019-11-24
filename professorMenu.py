# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'professorMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_professorMenu(object):
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
        self.profexamsButton.clicked.connect(professorMenu.close)
        self.profgradesButton.clicked.connect(professorMenu.close)
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
