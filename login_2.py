# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 503)
        MainWindow.setMinimumSize(QtCore.QSize(799, 503))
        MainWindow.setMaximumSize(QtCore.QSize(799, 503))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../stock/img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background:url(img/loginbg.jpg);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userid = QtWidgets.QLineEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(200, 140, 431, 51))
        self.userid.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 16pt \"Comic Sans MS\";")
        self.userid.setObjectName("userid")
        self.pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd.setGeometry(QtCore.QRect(200, 230, 431, 51))
        self.pwd.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 16pt \"Comic Sans MS\";")
        self.pwd.setText("")
        self.pwd.setObjectName("pwd")
        self.logbutton = QtWidgets.QPushButton(self.centralwidget)
        self.logbutton.setGeometry(QtCore.QRect(360, 360, 121, 41))
        self.logbutton.setStyleSheet("\n"
"QWidget#logbutton{\n"
"border-radius:10px;\n"
"background:rgb(90, 181, 70);\n"
"color:black;\n"
"font-size:24px;\n"
"font-variant:small-caps;\n"
"}\n"
"QWidget#logbutton:hover{\n"
"border-radius:10px;\n"
"background:rgba(139, 190, 99,0.8);\n"
"color:black;\n"
"font-size:24px;\n"
"font-variant:small-caps;\n"
"}")
        self.logbutton.setObjectName("logbutton")
        self.err = QtWidgets.QLabel(self.centralwidget)
        self.err.setGeometry(QtCore.QRect(210, 310, 411, 21))
        self.err.setStyleSheet("color:red;\n"
"font-variant:small-caps;\n"
"font-size:22px;")
        self.err.setText("")
        self.err.setObjectName("err")
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(610, 430, 121, 41))
        self.exitbutton.setStyleSheet("QWidget#exitbutton{\n"
"background: rgb(255, 46, 67);\n"
"border-radius:15px;\n"
"font-size:24px;\n"
"font-variant:small-caps;\n"
"}\n"
"QWidget#exitbutton:hover{\n"
"background: rgb(255, 87, 98);\n"
"border-radius:15px;\n"
"font-size:24px;\n"
"font-variant:small-caps;\n"
"}")
        self.exitbutton.setObjectName("exitbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 30, 111, 61))
        self.label.setStyleSheet("font: 75 25pt \"Comic Sans MS\" ;\n"
"color:rgb(24,85,116);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "USER LOGIN"))
        self.logbutton.setText(_translate("MainWindow", "login"))
        self.exitbutton.setText(_translate("MainWindow", "exit"))
        self.label.setText(_translate("MainWindow", "login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
