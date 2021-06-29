import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView




class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.dane = QSqlDatabase("QSQLITE")
        self.dane.setDatabaseName("baza\chinook.db")
        self.dane.open()

        self.table = QTableView()
        self.model = QSqlTableModel(db=self.dane)

        self.table.setModel(self.model)

        self.model.setTable("tracks")
        self.model.select()

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = Okno()
window.show()
app.exec()
