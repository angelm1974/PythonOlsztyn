import sys
import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class TabelaModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]


class MainWndow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabela = QtWidgets.QTableView()

        dane = np.genfromtxt('dane.csv',delimiter=';')

        self.model = TabelaModel(dane)
        self.tabela.setModel(self.model)
        self.setCentralWidget(self.tabela)
        self.setGeometry(600, 100, 400, 200)


app = QtWidgets.QApplication(sys.argv)
window = MainWndow()
window.show()
app.exec()
 