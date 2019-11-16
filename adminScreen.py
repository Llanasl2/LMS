from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from classes import *

class Ui_Administrator(object):

    #Function to poppulate all fields in the screen.
    def populateFields(self):
        conn = sqlite3.connect('lms-system.db')
        c = conn.cursor()
        usernameValue =  (self.dropboxStudents.currentText(),)
        print(usernameValue)
        c.execute('SELECT * FROM studentGrades WHERE user=?', usernameValue)
        a = c.fetchone()
        conn.commit()
        conn.close()

        students = grades( a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], a[16])

        self.class1exam1Text.setText(students.class1exam1)
        self.class1exam2Text.setText(students.class1exam2)
        self.class1finalText.setText(students.class1final)

        self.class2exam1Text.setText(students.class2exam1)
        self.class2exam2Text.setText(students.class2exam2)
        self.class2finalText.setText(students.class2final)

        self.class3exam1Text.setText(students.class3exam1)
        self.class3exam2Text.setText(students.class3exam2)
        self.class3finalText.setText(students.class3final)

        self.class4exam1Text.setText(students.class4exam1)
        self.class4exam2Text.setText(students.class4exam2)
        self.class4finalText.setText(students.class4final)

    #function go get all users for the dropbox
    def allstudents(self):
        conn = sqlite3.connect('lms-system.db')
        c = conn.cursor()
        c.execute("SELECT * FROM studentGrades")
        a = c.fetchall()
        studentslist = list()
        for i in a:
            studentslist.append(i[0])
        conn.commit()
        conn.close()
        return studentslist

    def searchStudent(self):
        print(str(self.searchBox.text()))
        conn = sqlite3.connect('lms-system.db')
        c = conn.cursor()
        c.execute("SELECT * FROM studentGrades")
        a = c.fetchall()
        studentslist = list()
        for i in a:
            if (i[0] == self.searchBox.Text()):
                studentslist.append(i[0])
        conn.commit()
        conn.close()
        return studentslist


    def setupUi(self, Administrator):
        Administrator.setObjectName("Administrator")
        Administrator.resize(551, 491)
        Administrator.setMinimumSize(QtCore.QSize(551, 491))
        Administrator.setMaximumSize(QtCore.QSize(551, 491))
        self.centralwidget = QtWidgets.QWidget(Administrator)
        self.centralwidget.setObjectName("centralwidget")
        self.dropboxStudents = QtWidgets.QComboBox(self.centralwidget)
        self.dropboxStudents.setGeometry(QtCore.QRect(30, 10, 229, 22))
        self.dropboxStudents.setObjectName("dropboxStudents")

        #items in dropbox
        items = self.allstudents()
        self.dropboxStudents.addItems(items)

        self.gpaLabel = QtWidgets.QLabel(self.centralwidget)
        self.gpaLabel.setGeometry(QtCore.QRect(360, 390, 47, 14))
        self.gpaLabel.setObjectName("gpaLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 60, 231, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.class2exam1Label = QtWidgets.QLabel(self.layoutWidget)
        self.class2exam1Label.setObjectName("class2exam1Label")
        self.horizontalLayout_4.addWidget(self.class2exam1Label)
        self.class2exam1Text = QtWidgets.QLineEdit(self.layoutWidget)
        self.class2exam1Text.setObjectName("class2exam1Text")
        self.horizontalLayout_4.addWidget(self.class2exam1Text)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.class2exam2Label = QtWidgets.QLabel(self.layoutWidget)
        self.class2exam2Label.setObjectName("class2exam2Label")
        self.horizontalLayout_5.addWidget(self.class2exam2Label)
        self.class2exam2Text = QtWidgets.QLineEdit(self.layoutWidget)
        self.class2exam2Text.setObjectName("class2exam2Text")
        self.horizontalLayout_5.addWidget(self.class2exam2Text)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.class2finalLabel = QtWidgets.QLabel(self.layoutWidget)
        self.class2finalLabel.setObjectName("class2finalLabel")
        self.horizontalLayout_6.addWidget(self.class2finalLabel)
        self.class2finalText = QtWidgets.QLineEdit(self.layoutWidget)
        self.class2finalText.setObjectName("class2finalText")
        self.horizontalLayout_6.addWidget(self.class2finalText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 230, 231, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.class3exam1Label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.class3exam1Label_2.setObjectName("class3exam1Label_2")
        self.horizontalLayout_7.addWidget(self.class3exam1Label_2)
        self.class3exam1Text = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.class3exam1Text.setObjectName("class3exam1Text")
        self.horizontalLayout_7.addWidget(self.class3exam1Text)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.class3exam2Label = QtWidgets.QLabel(self.layoutWidget_2)
        self.class3exam2Label.setObjectName("class3exam2Label")
        self.horizontalLayout_8.addWidget(self.class3exam2Label)
        self.class3exam2Text = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.class3exam2Text.setObjectName("class3exam2Text")
        self.horizontalLayout_8.addWidget(self.class3exam2Text)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.class3finalLabel = QtWidgets.QLabel(self.layoutWidget_2)
        self.class3finalLabel.setObjectName("class3finalLabel")
        self.horizontalLayout_9.addWidget(self.class3finalLabel)
        self.class3finalText = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.class3finalText.setObjectName("class3finalText")
        self.horizontalLayout_9.addWidget(self.class3finalText)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(280, 230, 231, 151))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.class4exam1Label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.class4exam1Label_2.setObjectName("class4exam1Label_2")
        self.horizontalLayout_10.addWidget(self.class4exam1Label_2)
        self.class4exam1Text = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.class4exam1Text.setObjectName("class4exam1Text")
        self.horizontalLayout_10.addWidget(self.class4exam1Text)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.class4exam2Label = QtWidgets.QLabel(self.layoutWidget_3)
        self.class4exam2Label.setObjectName("class4exam2Label")
        self.horizontalLayout_11.addWidget(self.class4exam2Label)
        self.class4exam2Text = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.class4exam2Text.setObjectName("class4exam2Text")
        self.horizontalLayout_11.addWidget(self.class4exam2Text)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.class4finalLabel = QtWidgets.QLabel(self.layoutWidget_3)
        self.class4finalLabel.setObjectName("class4finalLabel")
        self.horizontalLayout_12.addWidget(self.class4finalLabel)
        self.class4finalText = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.class4finalText.setObjectName("class4finalText")
        self.horizontalLayout_12.addWidget(self.class4finalText)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.gpaText = QtWidgets.QLineEdit(self.centralwidget)
        self.gpaText.setEnabled(False)
        self.gpaText.setGeometry(QtCore.QRect(390, 390, 113, 21))
        self.gpaText.setObjectName("gpaText")
        self.class1Label = QtWidgets.QLabel(self.centralwidget)
        self.class1Label.setGeometry(QtCore.QRect(120, 40, 47, 14))
        self.class1Label.setObjectName("class1Label")
        self.class3exam1Label = QtWidgets.QLabel(self.centralwidget)
        self.class3exam1Label.setGeometry(QtCore.QRect(120, 220, 47, 14))
        self.class3exam1Label.setObjectName("class3exam1Label")
        self.class2Label = QtWidgets.QLabel(self.centralwidget)
        self.class2Label.setGeometry(QtCore.QRect(380, 40, 47, 14))
        self.class2Label.setObjectName("class2Label")
        self.class4exam1Label = QtWidgets.QLabel(self.centralwidget)
        self.class4exam1Label.setGeometry(QtCore.QRect(370, 220, 47, 14))
        self.class4exam1Label.setObjectName("class4exam1Label")
        self.savegradesButton = QtWidgets.QPushButton(self.centralwidget)
        self.savegradesButton.setGeometry(QtCore.QRect(140, 420, 80, 22))
        self.savegradesButton.setObjectName("savegradesButton")
        self.okgradesButton = QtWidgets.QPushButton(self.centralwidget)
        self.okgradesButton.setGeometry(QtCore.QRect(230, 420, 80, 22))
        self.okgradesButton.setObjectName("okgradesButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(320, 420, 80, 22))
        self.quitButton.setObjectName("quitButton")
        self.searchBox = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBox.setGeometry(QtCore.QRect(330, 10, 113, 21))
        self.searchBox.setObjectName("searchBox")
        self.searchboxLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchboxLabel.setGeometry(QtCore.QRect(280, 10, 47, 14))
        self.searchboxLabel.setObjectName("searchboxLabel")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 60, 231, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.class1exam1Label = QtWidgets.QLabel(self.layoutWidget1)
        self.class1exam1Label.setObjectName("class1exam1Label")
        self.horizontalLayout.addWidget(self.class1exam1Label)
        self.class1exam1Text = QtWidgets.QLineEdit(self.layoutWidget1)
        self.class1exam1Text.setObjectName("class1exam1Text")
        self.horizontalLayout.addWidget(self.class1exam1Text)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.class1exam2Label = QtWidgets.QLabel(self.layoutWidget1)
        self.class1exam2Label.setObjectName("class1exam2Label")
        self.horizontalLayout_2.addWidget(self.class1exam2Label)
        self.class1exam2Text = QtWidgets.QLineEdit(self.layoutWidget1)
        self.class1exam2Text.setObjectName("class1exam2Text")
        self.horizontalLayout_2.addWidget(self.class1exam2Text)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.class1finalLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.class1finalLabel.setObjectName("class1finalLabel")
        self.horizontalLayout_3.addWidget(self.class1finalLabel)
        self.class1finalText = QtWidgets.QLineEdit(self.layoutWidget1)
        self.class1finalText.setObjectName("class1finalText")
        self.horizontalLayout_3.addWidget(self.class1finalText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(450, 10, 51, 22))
        self.searchButton.setObjectName("searchButton")
        Administrator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Administrator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 21))
        self.menubar.setObjectName("menubar")
        Administrator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Administrator)
        self.statusbar.setObjectName("statusbar")
        Administrator.setStatusBar(self.statusbar)

        #Populate all the fields when loaded
        self.populateFields()

        self.retranslateUi(Administrator)
        self.dropboxStudents.currentTextChanged.connect(self.populateFields)
        self.savegradesButton.clicked.connect(Administrator.close)
        self.okgradesButton.clicked.connect(Administrator.close)
        self.quitButton.clicked.connect(Administrator.close)
        self.searchButton.clicked.connect(self.searchStudent)
        QtCore.QMetaObject.connectSlotsByName(Administrator)



    def retranslateUi(self, Administrator):
        _translate = QtCore.QCoreApplication.translate
        Administrator.setWindowTitle(_translate("Administrator", "MainWindow"))
        self.gpaLabel.setText(_translate("Administrator", "GPA"))
        self.class2exam1Label.setText(_translate("Administrator", "Exam 1:"))
        self.class2exam2Label.setText(_translate("Administrator", "Exam 2:"))
        self.class2finalLabel.setText(_translate("Administrator", "Final:"))
        self.class3exam1Label_2.setText(_translate("Administrator", "Exam 1:"))
        self.class3exam2Label.setText(_translate("Administrator", "Exam 2:"))
        self.class3finalLabel.setText(_translate("Administrator", "Final:"))
        self.class4exam1Label_2.setText(_translate("Administrator", "Exam 1:"))
        self.class4exam2Label.setText(_translate("Administrator", "Exam 2:"))
        self.class4finalLabel.setText(_translate("Administrator", "Final:"))
        self.class1Label.setText(_translate("Administrator", "Class 1:"))
        self.class3exam1Label.setText(_translate("Administrator", "Class 3:"))
        self.class2Label.setText(_translate("Administrator", "Class 2:"))
        self.class4exam1Label.setText(_translate("Administrator", "Class 4:"))
        self.savegradesButton.setText(_translate("Administrator", "Save"))
        self.okgradesButton.setText(_translate("Administrator", "Ok"))
        self.quitButton.setText(_translate("Administrator", "Quit"))
        self.searchboxLabel.setText(_translate("Administrator", "Search:"))
        self.class1exam1Label.setText(_translate("Administrator", "Exam 1:"))
        self.class1exam2Label.setText(_translate("Administrator", "Exam 2:"))
        self.class1finalLabel.setText(_translate("Administrator", "Final:"))
        self.searchButton.setText(_translate("Administrator", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Administrator = QtWidgets.QMainWindow()
    ui = Ui_Administrator()
    ui.setupUi(Administrator)
    Administrator.show()
    sys.exit(app.exec_())
