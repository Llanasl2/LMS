######################################################
#    Login Screen
######################################################

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from adminScreen import Ui_Administrator
from studentScreen import Ui_Student
from professorMenu import Ui_professorMenu
from studentMenu import Ui_studentMenu

class Ui_loginScreen(object):
    #Function to open Admin window
    def openAdminWindow(self):
        print("Opened")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Administrator()
        self.ui.setupUi(self.window)
        self.window.show()
        loginScreen.setVisible(False)

    #Function to open student window
    def openStudentWindow(self, usernameValue):
        print("Opened")
        Ui_Student.usernameValue = usernameValue
        self.window = QtWidgets.QMainWindow()
        #self.ui = Ui_Student()
        self.ui = Ui_studentMenu()
        self.ui.setupUi(self.window)
        self.window.show()
        loginScreen.setVisible(False)

    #Function to open Professor Menu
    def openProfessorWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_professorMenu()
        self.ui.setupUi(self.window)
        self.window.show()
        loginScreen.setVisible(False)
    #Function to exit the application
    def quitApp(self):
        print("quit")
        import os
        os._exit(0)

    #function for the button login
    def loginUser(self):
        print(self.usernameText.text())
        conn = sqlite3.connect('lms-system.db')
        c = conn.cursor()
        usernameValue =  (self.usernameText.text(),)
        c.execute('SELECT password,type FROM users WHERE user=?', usernameValue)
        queryValue = c.fetchone()
        conn.commit()
        conn.close()
        if (self.studentCheck.isChecked() == True) and (self.professorCheck.isChecked() == False):
            userType = 'student'
        if (self.professorCheck.isChecked() == True) and (self.studentCheck.isChecked() == False):
            userType = 'professor'
        if (self.professorCheck.isChecked() == True) and (self.studentCheck.isChecked() == True):
            userType = 'admin'
        if (self.professorCheck.isChecked() == False) and (self.studentCheck.isChecked() == False):
            userType = 'admin'
        if (queryValue[0] == self.passwordText.text()) and (queryValue[1] == userType):
            #Function if the login pass
            print("Access granted")

            if (userType == 'admin'):
                self.openAdminWindow()
            elif(userType == 'student'):
                self.openStudentWindow(usernameValue)
            elif (userType == 'professor'):
                self.openProfessorWindow()

        else:
            #Function if the login fail
            print("Access denied")

    #Function for user signup
    def signupUser(self):
        try:
            conn = sqlite3.connect('lms-system.db')
            c = conn.cursor()

            usernameValue = self.usernameText.text()
            passwordValue = self.passwordText.text()
            if (self.studentCheck.isChecked() == True) and (self.professorCheck.isChecked() == False):
                userType = 'student'
            if (self.professorCheck.isChecked() == True) and (self.studentCheck.isChecked() == False):
                userType = 'professor'
            if (self.professorCheck.isChecked() == True) and (self.studentCheck.isChecked() == True):
                userType = 'admin'
            if (self.professorCheck.isChecked() == False) and (self.studentCheck.isChecked() == False):
                userType = 'admin'

            c.execute("INSERT INTO users (user, password, type) values (?, ?, ?)", (usernameValue, passwordValue, userType))
            conn.commit()
            conn.close()

        except:
            print('Error')


    def setupUi(self, loginScreen):
        loginScreen.setObjectName("loginScreen")
        loginScreen.resize(329, 359)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginScreen.sizePolicy().hasHeightForWidth())
        loginScreen.setSizePolicy(sizePolicy)
        loginScreen.setMinimumSize(QtCore.QSize(329, 359))
        loginScreen.setMaximumSize(QtCore.QSize(329, 359))
        self.centralwidget = QtWidgets.QWidget(loginScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 281, 311))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.usernameLabel = QtWidgets.QLabel(self.groupBox)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout_4.addWidget(self.usernameLabel)
        self.usernameText = QtWidgets.QLineEdit(self.groupBox)
        self.usernameText.setObjectName("usernameText")
        self.verticalLayout_4.addWidget(self.usernameText)
        self.passwordLabel = QtWidgets.QLabel(self.groupBox)
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout_4.addWidget(self.passwordLabel)
        self.passwordText = QtWidgets.QLineEdit(self.groupBox)
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordText.setObjectName("passwordText")
        self.verticalLayout_4.addWidget(self.passwordText)
        self.usertypeArea = QtWidgets.QFrame(self.groupBox)
        self.usertypeArea.setFrameShape(QtWidgets.QFrame.HLine)
        self.usertypeArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.usertypeArea.setObjectName("usertypeArea")
        self.verticalLayout_4.addWidget(self.usertypeArea)
        self.studentCheck = QtWidgets.QCheckBox(self.groupBox)
        self.studentCheck.setChecked(True)
        self.studentCheck.setObjectName("studentCheck")
        self.verticalLayout_4.addWidget(self.studentCheck)
        self.professorCheck = QtWidgets.QCheckBox(self.groupBox)
        self.professorCheck.setObjectName("professorCheck")
        self.verticalLayout_4.addWidget(self.professorCheck)
        self.buttonsArea = QtWidgets.QFrame(self.groupBox)
        self.buttonsArea.setFrameShape(QtWidgets.QFrame.HLine)
        self.buttonsArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.buttonsArea.setObjectName("buttonsArea")
        self.verticalLayout_4.addWidget(self.buttonsArea)
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_4.addWidget(self.loginButton)
        self.siginupButton = QtWidgets.QPushButton(self.groupBox)
        self.siginupButton.setObjectName("siginupButton")
        self.verticalLayout_4.addWidget(self.siginupButton)
        self.quitButton = QtWidgets.QPushButton(self.groupBox)
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout_4.addWidget(self.quitButton)
        self.loginButton.raise_()
        self.siginupButton.raise_()
        self.quitButton.raise_()
        self.usernameText.raise_()
        self.passwordLabel.raise_()
        self.passwordText.raise_()
        self.studentCheck.raise_()
        self.professorCheck.raise_()
        self.buttonsArea.raise_()
        self.usertypeArea.raise_()
        self.usernameLabel.raise_()
        loginScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(loginScreen)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        loginScreen.setStatusBar(self.statusbar)

        self.retranslateUi(loginScreen)
        self.usernameText.returnPressed.connect(self.passwordText.setFocus)
        self.passwordText.returnPressed.connect(self.loginButton.setFocus)

        #Buttons Actions
        self.quitButton.clicked.connect(self.quitApp)
        self.siginupButton.clicked.connect(self.signupUser)
        self.loginButton.clicked.connect(self.loginUser)

        QtCore.QMetaObject.connectSlotsByName(loginScreen)

        print(self.studentCheck.isChecked())
        print(self.professorCheck.isChecked())

    def retranslateUi(self, loginScreen):
        _translate = QtCore.QCoreApplication.translate
        loginScreen.setWindowTitle(_translate("loginScreen", "LMS"))
        self.groupBox.setTitle(_translate("loginScreen", "Singin"))
        self.usernameLabel.setText(_translate("loginScreen", "Username:"))
        self.usernameText.setPlaceholderText(_translate("loginScreen", "Username"))
        self.passwordLabel.setText(_translate("loginScreen", "Password:"))
        self.passwordText.setPlaceholderText(_translate("loginScreen", "Password"))
        self.studentCheck.setText(_translate("loginScreen", "Student"))
        self.professorCheck.setText(_translate("loginScreen", "Professor"))
        self.loginButton.setText(_translate("loginScreen", "Login"))
        self.siginupButton.setText(_translate("loginScreen", "Signup"))
        self.quitButton.setText(_translate("loginScreen", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginScreen = QtWidgets.QMainWindow()
    ui = Ui_loginScreen()
    ui.setupUi(loginScreen)
    loginScreen.show()
    sys.exit(app.exec_())
