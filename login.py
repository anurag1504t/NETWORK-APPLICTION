from PyQt5 import uic,QtWidgets,QtCore
app=QtWidgets.QApplication([])
loginui=uic.loadUi("ui/login.ui")

def login():
    loginui.userid.setText("")
    loginui.userid.setPlaceholderText("User id")
    loginui.pwd.setPlaceholderText("Password")
    loginui.userid.setAlignment(QtCore.Qt.AlignCenter)
    loginui.pwd.setAlignment(QtCore.Qt.AlignCenter)
    loginui.pwd.setText("")
    loginui.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
    err = loginui.err
    err.hide()
    loginui.show()

login()
app.exec()