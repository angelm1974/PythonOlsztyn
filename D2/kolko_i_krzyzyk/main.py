from typing import Text
from testy import Kolko_Krzyzyk
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt

from interfejs import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_start.clicked.connect(self.uruchom_gre)

        self.bt_1.clicked.connect(self.bt1_click)
        self.bt_2.clicked.connect(self.bt2_click)
        self.bt_3.clicked.connect(self.bt3_click)
        self.bt_4.clicked.connect(self.bt4_click)
        self.bt_5.clicked.connect(self.bt5_click)
        self.bt_6.clicked.connect(self.bt6_click)
        self.bt_7.clicked.connect(self.bt7_click)
        self.bt_8.clicked.connect(self.bt8_click)
        self.bt_9.clicked.connect(self.bt9_click)
        self.buttonBox.accepted.connect(self.podaj_dane_gracza)
        self.gra = Kolko_Krzyzyk()
        self.show()

    def podaj_dane_gracza(self):
        self.gra.czlowiek.imie = str(self.lineEdit.text())
        self.lblImie.setText(self.gra.czlowiek.imie)
        self.lblImie_2.setText(self.gra.komputer.imie)
        self.lbl_runda.setText("0")
        self.widget.hide()

    def uruchom_gre(self):
        self.gra.run()

    def graj(self):
        self.gra.ruch()
        # print(p)

    def bt1_click(self):
        self.gra.wybor_z_interfejsu = 0
        self.graj()
        self.bt_1.setIcon(self.icon)

    def bt2_click(self):
        self.gra.wybor_z_interfejsu = 1
        self.graj()
        self.bt_2.setIcon(self.icon)

    def bt3_click(self):
        self.gra.wybor_z_interfejsu = 2
        self.graj()
        self.bt_3.setIcon(self.icon)

    def bt4_click(self):
        self.gra.wybor_z_interfejsu = 3
        self.graj()
        self.bt_4.setIcon(self.icon)

    def bt5_click(self):
        self.gra.wybor_z_interfejsu = 4
        self.graj()
        self.bt_5.setIcon(self.icon)

    def bt6_click(self):
        self.gra.wybor_z_interfejsu = 5
        self.graj()
        self.bt_6.setIcon(self.icon)

    def bt7_click(self):
        self.gra.wybor_z_interfejsu = 6
        self.graj()
        self.bt_7.setIcon(self.icon)

    def bt8_click(self):
        self.gra.wybor_z_interfejsu = 7
        self.graj()
        self.bt_8.setIcon(self.icon)

    def bt9_click(self):
        self.gra.wybor_z_interfejsu = 8
        self.graj()
        self.bt_9.setIcon(self.icon)


app = QApplication([])
w = MainWindow()
app.exec()
