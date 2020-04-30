from PyQt5 import uic,QtWidgets,QtCore
app=QtWidgets.QApplication([])
connect_server_ui=uic.loadUi("ui/ServerConnect.ui")

def ServerConnect():
    connect_server_ui.server_ip.setText("")
    connect_server_ui.server_ip.setPlaceholderText("SERVER IP")
    connect_server_ui.server_ip.setAlignment(QtCore.Qt.AlignCenter)
    connect_server_ui.show()

ServerConnect()
app.exec()