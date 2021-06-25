from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja aplikacja")
        self.button_is_checked = True
        self.button = QPushButton("Kliknij")
        self.button.setCheckable(True)
        self.button.setFixedSize(200, 100)
        self.button.clicked.connect(self.button_klikniety)
        self.button.clicked.connect(self.button_przelacz)
        self.setCentralWidget(self.button)
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(600, 450))

    def button_klikniety(self):
        print("Kliknięto przycisk")

    def button_przelacz(self, checked):
        self.button_is_checked = checked
        self.button.setText(str(checked))
        print('Zaznaczony przycisk?', checked)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
