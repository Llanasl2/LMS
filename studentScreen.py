from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from classes import *

class Ui_Student(object):

    def populateFields(self):
        conn = sqlite3.connect('lms-system.db')
        c = conn.cursor()
        usernameValue =  Ui_Student.usernameValue
        print(usernameValue)
        print("hello")
        c.execute('SELECT * FROM studentGrades WHERE user=?', usernameValue)
        a = c.fetchone()
        print(a)
        conn.commit()
        conn.close()

        studentUser = grades(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15], a[16] )
        #Class 1 data for student
        self.exam1class1Text.setText(str(studentUser.class1exam1.value()))
        self.exam2class2Text.setText(str(studentUser.class1exam2.value()))
        self.finalclass1Text.setText(str(studentUser.class1final.value()))

        #Class 2 data for student
        self.exam1class2Text.setText(str(studentUser.class2exam1.value()))
        self.exam2class2Text_2.setText(str(studentUser.class2exam2.value()))
        self.finalclass2Text.setText(str(studentUser.class2final.value()))

        #Class 3 data for student
        self.exam1class3Text.setText(str(studentUser.class3exam1.value()))
        self.exam2class3Text.setText(str(studentUser.class3exam2.value()))
        self.finalclass3Text.setText(str(studentUser.class3final.value()))

        #Class 4 data for student
        self.exam1class4Text.setText(str(studentUser.class4exam1.value()))
        self.exam2class4Text.setText(str(studentUser.class4exam2.value()))
        self.finalclass4Text.setText(str(studentUser.class4final.value()))

        #GPA
        GPA = "%.2f" % float(studentUser.GPA())
        self.gpaText.setText(GPA)

    def setupUi(self, Student):
        Student.setObjectName("Student")
        Student.resize(622, 710)
        self.centralwidget = QtWidgets.QWidget(Student)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 201, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exam1class1Label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.exam1class1Label.setObjectName("exam1class1Label")
        self.horizontalLayout.addWidget(self.exam1class1Label)
        self.exam1class1Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.exam1class1Text.setEnabled(False)
        self.exam1class1Text.setObjectName("exam1class1Text")
        self.horizontalLayout.addWidget(self.exam1class1Text)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 140, 201, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exam2class1Label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.exam2class1Label.setObjectName("exam2class1Label")
        self.horizontalLayout_2.addWidget(self.exam2class1Label)
        self.exam2class2Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.exam2class2Text.setEnabled(False)
        self.exam2class2Text.setObjectName("exam2class2Text")
        self.horizontalLayout_2.addWidget(self.exam2class2Text)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 200, 201, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.finalclass1Label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.finalclass1Label.setObjectName("finalclass1Label")
        self.horizontalLayout_3.addWidget(self.finalclass1Label)
        self.finalclass1Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.finalclass1Text.setEnabled(False)
        self.finalclass1Text.setObjectName("finalclass1Text")
        self.horizontalLayout_3.addWidget(self.finalclass1Text)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(310, 80, 201, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.exam1class2Label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.exam1class2Label.setObjectName("exam1class2Label")
        self.horizontalLayout_4.addWidget(self.exam1class2Label)
        self.exam1class2Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.exam1class2Text.setEnabled(False)
        self.exam1class2Text.setObjectName("exam1class2Text")
        self.horizontalLayout_4.addWidget(self.exam1class2Text)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(310, 140, 201, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.exam2class2Label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.exam2class2Label.setObjectName("exam2class2Label")
        self.horizontalLayout_5.addWidget(self.exam2class2Label)
        self.exam2class2Text_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.exam2class2Text_2.setEnabled(False)
        self.exam2class2Text_2.setObjectName("exam2class2Text_2")
        self.horizontalLayout_5.addWidget(self.exam2class2Text_2)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(310, 200, 201, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.finalclass2Label = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.finalclass2Label.setObjectName("finalclass2Label")
        self.horizontalLayout_6.addWidget(self.finalclass2Label)
        self.finalclass2Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.finalclass2Text.setEnabled(False)
        self.finalclass2Text.setObjectName("finalclass2Text")
        self.horizontalLayout_6.addWidget(self.finalclass2Text)
        self.class1Label = QtWidgets.QLabel(self.centralwidget)
        self.class1Label.setGeometry(QtCore.QRect(100, 60, 47, 14))
        self.class1Label.setObjectName("class1Label")
        self.class2Label = QtWidgets.QLabel(self.centralwidget)
        self.class2Label.setGeometry(QtCore.QRect(390, 60, 47, 14))
        self.class2Label.setObjectName("class2Label")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(30, 340, 201, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.exam1class3Label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.exam1class3Label.setObjectName("exam1class3Label")
        self.horizontalLayout_7.addWidget(self.exam1class3Label)
        self.exam1class3Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.exam1class3Text.setEnabled(False)
        self.exam1class3Text.setObjectName("exam1class3Text")
        self.horizontalLayout_7.addWidget(self.exam1class3Text)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(30, 400, 201, 51))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.exam2class3Label = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.exam2class3Label.setObjectName("exam2class3Label")
        self.horizontalLayout_8.addWidget(self.exam2class3Label)
        self.exam2class3Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.exam2class3Text.setEnabled(False)
        self.exam2class3Text.setObjectName("exam2class3Text")
        self.horizontalLayout_8.addWidget(self.exam2class3Text)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(30, 460, 201, 51))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.finalclass3Label = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.finalclass3Label.setObjectName("finalclass3Label")
        self.horizontalLayout_9.addWidget(self.finalclass3Label)
        self.finalclass3Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.finalclass3Text.setEnabled(False)
        self.finalclass3Text.setObjectName("finalclass3Text")
        self.horizontalLayout_9.addWidget(self.finalclass3Text)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(310, 340, 201, 51))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.exam1class4Label = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.exam1class4Label.setObjectName("exam1class4Label")
        self.horizontalLayout_10.addWidget(self.exam1class4Label)
        self.exam1class4Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.exam1class4Text.setEnabled(False)
        self.exam1class4Text.setObjectName("exam1class4Text")
        self.horizontalLayout_10.addWidget(self.exam1class4Text)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(310, 400, 201, 51))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.exam2class4Label = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.exam2class4Label.setObjectName("exam2class4Label")
        self.horizontalLayout_11.addWidget(self.exam2class4Label)
        self.exam2class4Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_11)
        self.exam2class4Text.setEnabled(False)
        self.exam2class4Text.setObjectName("exam2class4Text")
        self.horizontalLayout_11.addWidget(self.exam2class4Text)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(310, 460, 201, 51))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.finalclass4Label = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.finalclass4Label.setObjectName("finalclass4Label")
        self.horizontalLayout_12.addWidget(self.finalclass4Label)
        self.finalclass4Text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_12)
        self.finalclass4Text.setEnabled(False)
        self.finalclass4Text.setReadOnly(False)
        self.finalclass4Text.setObjectName("finalclass4Text")
        self.horizontalLayout_12.addWidget(self.finalclass4Text)
        self.class3Label = QtWidgets.QLabel(self.centralwidget)
        self.class3Label.setGeometry(QtCore.QRect(100, 320, 47, 14))
        self.class3Label.setObjectName("class3Label")
        self.class4Label = QtWidgets.QLabel(self.centralwidget)
        self.class4Label.setGeometry(QtCore.QRect(390, 320, 47, 14))
        self.class4Label.setObjectName("class4Label")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(250, 580, 75, 23))
        self.quitButton.setObjectName("quitButton")
        self.gpaLabel = QtWidgets.QLabel(self.centralwidget)
        self.gpaLabel.setGeometry(QtCore.QRect(310, 530, 47, 14))
        self.gpaLabel.setObjectName("gpaLabel")
        self.gpaText = QtWidgets.QLineEdit(self.centralwidget)
        self.gpaText.setEnabled(False)
        self.gpaText.setGeometry(QtCore.QRect(340, 530, 113, 20))
        self.gpaText.setObjectName("gpaText")
        Student.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Student)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 22))
        self.menubar.setObjectName("menubar")
        Student.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Student)
        self.statusbar.setObjectName("statusbar")
        Student.setStatusBar(self.statusbar)


        #Populate all the fields when loaded
        self.populateFields()
        #Quit button
        self.quitButton.clicked.connect(Student.close)


        self.retranslateUi(Student)
        QtCore.QMetaObject.connectSlotsByName(Student)

    def retranslateUi(self, Student):
        _translate = QtCore.QCoreApplication.translate
        Student.setWindowTitle(_translate("Student", "MainWindow"))
        self.exam1class1Label.setText(_translate("Student", "Exam 1:"))
        self.exam2class1Label.setText(_translate("Student", "Exam 2:"))
        self.finalclass1Label.setText(_translate("Student", "Final:"))
        self.exam1class2Label.setText(_translate("Student", "Exam 1:"))
        self.exam2class2Label.setText(_translate("Student", "Exam 2:"))
        self.finalclass2Label.setText(_translate("Student", "Final:"))
        self.class1Label.setText(_translate("Student", "Class 1"))
        self.class2Label.setText(_translate("Student", "Class 2"))
        self.exam1class3Label.setText(_translate("Student", "Exam 1:"))
        self.exam2class3Label.setText(_translate("Student", "Exam 2:"))
        self.finalclass3Label.setText(_translate("Student", "Final:"))
        self.exam1class4Label.setText(_translate("Student", "Exam 1:"))
        self.exam2class4Label.setText(_translate("Student", "Exam 2:"))
        self.finalclass4Label.setText(_translate("Student", "Final:"))
        self.class3Label.setText(_translate("Student", "Class 3"))
        self.class4Label.setText(_translate("Student", "Class 4"))
        self.quitButton.setText(_translate("Student", "Quit"))
        self.gpaLabel.setText(_translate("Student", "GPA:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Student = QtWidgets.QMainWindow()
    ui = Ui_Student()
    ui.setupUi(Student)
    Student.show()
    sys.exit(app.exec_())
