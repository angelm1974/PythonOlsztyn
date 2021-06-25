from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikacja z inputem")
        #self.setFixedSize(QSize(600, 450))
        self.label = QLabel("Mój kot")
        font = self.label.font()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(
            Qt.Alignment.AlignJustify | Qt.Alignment.AlignVCenter)
        self.label.setPixmap(QPixmap('./obrazy/kot.jpeg'))
        self.label.setScaledContents(True)
        self.setCentralWidget(self.label)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
