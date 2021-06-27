import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

from interfejs import Ui_MainWindow


ikona = QtGui.QImage('bd.png')
kolor = QtGui.QColor('green')


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return kolor

    def rowCount(self, index):
        return len(self.todos)

# CRUD
#Create - ok
#Read - ok
# Update
#Delete - ok


class Okno(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        todos = [(False, 'Kup bułki'), (True, 'Jakaś wartość')]
        self.model = TodoModel(todos)
        self.listView.setModel(self.model)
        self.btnDodaj.pressed.connect(self.add)
        self.btnKoniecZadania.pressed.connect(self.update)
        self.btnKasuj.pressed.connect(self.delete)

    def add(self):
        text = self.lineEdit.text()
        text = text.strip()

        if text:
            # dodawnie tekstu do modelu
            self.model.todos.append((False, text))

            # powiadomienie interfejsu ze dane się zmieniły
            self.model.layoutChanged.emit()
            # czyszczenie pola tekstowe
            self.lineEdit.clear()

    def delete(self):
        indexy = self.listView.selectedIndexes()

        if indexy:
            # wybór pierwszego zaznaczonego wiersza listy
            index = indexy[0]

            # kasowanie elementu listy o zadanym indexie
            del self.model.todos[index.row()]

            # powiadomienie interfejsu ze dane się zmieniły
            self.model.layoutChanged.emit()

            # czyszczenie zaznaczenia na liscie
            self.listView.clearSelection()

    def update(self):
        indexy = self.listView.selectedIndexes()

        if indexy:
            # wybór pierwszego zaznaczonego wiersza listy
            index = indexy[0]
            row = index.row()

            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)

            self.model.dataChanged.emit(index, index)

            # czyszczenie zaznaczenia na liscie
            self.listView.clearSelection()


app = QtWidgets.QApplication(sys.argv)
glowne_okno = Okno()
glowne_okno.show()
app.exec()
