import sys
from PyQt6 import QtWidgets,QtGui
import pyqtgraph as pg

from pyqtgraph import PlotWidget, plot

 
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.grafika = pg.PlotWidget()
        
        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.grafika)
        widget=QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)           

        godziny = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperatura = [30, 32, 34, 36, 38, 36, 33, 31, 28, 26]

        self.grafika.plotItem.plot(godziny, temperatura)


app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()
