import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from datetime import datetime


class TabelaModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:

            value = self._data[index.row()][index.column()]

            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                return "%.2f" % value

            if isinstance(value, str):
                return '"%s"' % value

            return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWndow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabela = QtWidgets.QTableView()

        dane = [[2, 3, 4], [3, 4, 5.2324], [
            1, 1, 'hello'], [3, 2, 6], [7, 4, datetime(2020, 6, 24)], ]

        self.model = TabelaModel(dane)
        self.tabela.setModel(self.model)
        self.setCentralWidget(self.tabela)


app = QtWidgets.QApplication(sys.argv)
window = MainWndow()
window.show()
app.exec()
