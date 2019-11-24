


from PyQt5 import QtCore, QtGui, QtWidgets
from classes import *

import sqlite3
conn = sqlite3.connect('lms-system.db')
c = conn.cursor()

#c.execute('''CREATE TABLE exam (classNum, exam, questionNum, question, answerA, answerB, answerC, answerD)''')

#c.execute('''CREATE TABLE users (user PRIMARY KEY, password, type)''')
#c.execute("INSERT INTO users VALUES ('rafael','1234','student')")

#c.execute("DROP TABLE studentGrades")

#c.execute('''CREATE TABLE studentGrades (user PRIMARY KEY, c1c, c1e1, c1e2, c1f, c2c, c2e1, c2e2, c2f, c3c, c3e1, c3e2, c3f, c4c, c4e1, c4e2, c4f)''')
#                                                                                            0                     1        2        3       4     5        6         7       8     9      10      11   12    13     14      15      16


#c.execute("INSERT INTO studentGrades VALUES ('rafael', '3', '80', '90', '85', '3', '50', '70', '80',  '3', '100', '100', '85', '3', '90', '90', '100' )")

#c.execute("INSERT INTO studentGrades VALUES ('diana', '3', '80', '90', '85', '3', '50', '70', '80',  '3', '100', '100', '85', '3', '90', '90', '100' )")
#c.execute("INSERT INTO studentGrades VALUES ('luis', '3', '80', '90', '85', '3', '50', '70', '80',  '3', '100', '100', '85', '3', '90', '90', '100' )")
#c.execute("INSERT INTO studentGrades VALUES ('eva', '3', '80', '90', '85', '3', '50', '70', '80',  '3', '100', '100', '85', '3', '90', '90', '100' )")

c.execute("SELECT * FROM studentGrades")
#c.execute("INSERT INTO users VALUES ('admin','admin','admin')")

#a = c.fetchone()
#b = c.fetchall()
conn.commit()
conn.close()


#classNum, exam, questionNum, question, answerA, answerB, answerC, answerD)
