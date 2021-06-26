from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt

from okno_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.przelicz)
        self.la
        self.show()

    def przelicz(self):
        self.label_2.setText(self.lineEdit.text().upper())
        


app = QApplication([])
w = MainWindow()
app.exec()
