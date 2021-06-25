from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikacja z inputem")
        self.label=QLabel()
        self.label2=QLabel("Mój tekst")
        self.input=QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        layout=QVBoxLayout()
        layout.addWidget(self.label2)
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        
        kontener=QWidget()
        kontener.setLayout(layout)
        self.setCentralWidget(kontener)
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec()