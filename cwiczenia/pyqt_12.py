from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication([])
window = uic.loadUi("ui\main1.ui")
window.show()
app.exec()
