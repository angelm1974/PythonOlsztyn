import sys

from PyQt6.QtSql import QSqlDatabase, QSqlRelation, QSqlTableModel, QSqlRelationalTableModel, QSqlRelationalDelegate, QSqlQuery

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

from interfejs import Ui_MainWindow


class Okno(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dane = QSqlDatabase("QSQLITE")
        self.dane.setDatabaseName("baza\chinook.db")
        self.dane.open()

        self.filtruj_po = 'Name'
        self.model = QSqlRelationalTableModel(db=self.dane)

        self.tableView.setModel(self.model)

        # self.model.setTable("invoices")
        query = QSqlQuery(
            'SELECT  Count(InvoiceDate) as "Data fakturowania" FROM invoices where InvoiceDate >"2013-11-01"', db=self.dane)
        self.model.setQuery(query)

        self.btnArtysci.pressed.connect(self.pokaz_artystow)
        self.btnPlyty.pressed.connect(self.pokaz_plyty)
        self.btnUtwory.pressed.connect(self.pokaz_utwory)
        self.search.textChanged.connect(self.aktualizuj_filtr)

    def pokaz_artystow(self):
        self.model.setTable("artists")
        self.model.setSort(1, Qt.SortOrder.AscendingOrder)
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "Identyfikator")
        self.model.setHeaderData(1, Qt.Orientation.Horizontal, "Nazwa")
        self.filtruj_po = 'Name'

        self.model.select()

    def pokaz_plyty(self):
        self.model.setTable("albums")
        idx = self.model.fieldIndex("Title")
        self.model.setSort(idx, Qt.SortOrder.DescendingOrder)
        self.filtruj_po = 'Title'
        self.model.select()

    def pokaz_utwory(self):
        self.model.setTable("tracks")

        self.model.setRelation(2, QSqlRelation("albums", "AlbumId", "Title"))

        delegate = QSqlRelationalDelegate(self.tableView)
        self.tableView.setItemDelegate(delegate)

        kolumny_do_usuniecia = ['TrackId',
                                'MediaTypeId', 'GenreId', 'Bytes']
        for cdu in kolumny_do_usuniecia:
            idx = self.model.fieldIndex(cdu)
            self.model.removeColumns(idx, 1)
            self.filtruj_po = 'Composer'

        tytuly_kolumn = {
            "Name": "Tytuł",
            "AlbumId": "Nazwa Albumu",
            "MediaTypeId": "Id Media",
            "GenreId": "Id typ",
            "Composer": "Autor"
        }
        for n, t in tytuly_kolumn.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Orientation.Horizontal, t)

        #self.model.removeColumns(0, 1)

        self.model.select()

    def aktualizuj_filtr(self, s):

        filtr_str = f'{self.filtruj_po} LIKE "%{s}%"'
        self.model.setFilter(filtr_str)


app = QtWidgets.QApplication(sys.argv)
glowne_okno = Okno()
glowne_okno.show()
app.exec()
