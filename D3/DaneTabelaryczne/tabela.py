import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class TabelaModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index):

        return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWndow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabela = QtWidgets.QTableView()

        dane = [[2, 3, 4], [3, 4, 5], [1, 1, 1], [3, 2, 6], [7, 4, 3], ]

        self.model = TabelaModel(dane)
        self.tabela.setModel(self.model)
        self.setCentralWidget(self.tabela)


app = QtWidgets.QApplication(sys.argv)
window = MainWndow()
window.show()
app.exec()
