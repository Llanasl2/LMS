# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'includeExam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_includeExam(object):
    def setupUi(self, includeExam):
        includeExam.setObjectName("includeExam")
        includeExam.resize(262, 346)
        includeExam.setMinimumSize(QtCore.QSize(262, 346))
        includeExam.setMaximumSize(QtCore.QSize(262, 346))
        self.examDropbox = QtWidgets.QComboBox(includeExam)
        self.examDropbox.setGeometry(QtCore.QRect(140, 30, 101, 22))
        self.examDropbox.setObjectName("examDropbox")
        self.courseDropbox = QtWidgets.QComboBox(includeExam)
        self.courseDropbox.setGeometry(QtCore.QRect(20, 30, 111, 22))
        self.courseDropbox.setObjectName("courseDropbox")
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
        self.comboBox = QtWidgets.QComboBox(includeExam)
        self.comboBox.setGeometry(QtCore.QRect(70, 60, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.quitButton = QtWidgets.QPushButton(includeExam)
        self.quitButton.setGeometry(QtCore.QRect(170, 310, 80, 22))
        self.quitButton.setObjectName("quitButton")
        self.addButton = QtWidgets.QPushButton(includeExam)
        self.addButton.setGeometry(QtCore.QRect(10, 280, 80, 22))
        self.addButton.setObjectName("addButton")
        self.updateButton = QtWidgets.QPushButton(includeExam)
        self.updateButton.setGeometry(QtCore.QRect(90, 280, 80, 22))
        self.updateButton.setObjectName("updateButton")
        self.removeButton = QtWidgets.QPushButton(includeExam)
        self.removeButton.setGeometry(QtCore.QRect(170, 280, 80, 22))
        self.removeButton.setObjectName("removeButton")
        self.newButton = QtWidgets.QPushButton(includeExam)
        self.newButton.setGeometry(QtCore.QRect(10, 310, 80, 22))
        self.newButton.setObjectName("newButton")

        self.retranslateUi(includeExam)
        self.addButton.clicked.connect(self.addButton.close)
        self.updateButton.clicked.connect(self.updateButton.close)
        self.removeButton.clicked.connect(self.removeButton.close)
        self.newButton.clicked.connect(self.newButton.close)
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
        self.removeButton.setText(_translate("includeExam", "Remove"))
        self.newButton.setText(_translate("includeExam", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    includeExam = QtWidgets.QWidget()
    ui = Ui_includeExam()
    ui.setupUi(includeExam)
    includeExam.show()
    sys.exit(app.exec_())
