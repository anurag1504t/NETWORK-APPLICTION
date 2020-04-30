# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerConnect.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Server_Connection(object):
    def setupUi(self, Server_Connection):
        Server_Connection.setObjectName("Server_Connection")
        Server_Connection.resize(797, 303)
        self.label = QtWidgets.QLabel(Server_Connection)
        self.label.setGeometry(QtCore.QRect(190, 20, 451, 61))
        self.label.setStyleSheet("font: 75 25pt \"Comic Sans MS\" ;\n"
"color:rgb(24,85,116);")
        self.label.setObjectName("label")
        self.server_ip = QtWidgets.QLineEdit(Server_Connection)
        self.server_ip.setGeometry(QtCore.QRect(200, 120, 431, 51))
        self.server_ip.setStyleSheet("background: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"font: 16pt \"Comic Sans MS\";")
        self.server_ip.setObjectName("server_ip")
        self.connect_button = QtWidgets.QPushButton(Server_Connection)
        self.connect_button.setGeometry(QtCore.QRect(360, 200, 131, 41))
        self.connect_button.setStyleSheet("\n"
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
        self.connect_button.setObjectName("connect_button")

        self.retranslateUi(Server_Connection)
        QtCore.QMetaObject.connectSlotsByName(Server_Connection)

    def retranslateUi(self, Server_Connection):
        _translate = QtCore.QCoreApplication.translate
        Server_Connection.setWindowTitle(_translate("Server_Connection", "Dialog"))
        self.label.setText(_translate("Server_Connection", "Connect to the Server"))
        self.connect_button.setText(_translate("Server_Connection", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Server_Connection = QtWidgets.QDialog()
    ui = Ui_Server_Connection()
    ui.setupUi(Server_Connection)
    Server_Connection.show()
    sys.exit(app.exec_())
