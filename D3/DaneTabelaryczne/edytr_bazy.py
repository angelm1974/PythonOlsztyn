import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

from PyQt6.QtWidgets import(
    QApplication, QComboBox, QDataWidgetMapper, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow, QPushButton, QSpinBox, QTableView, QVBoxLayout, QWidget
)

dane = QSqlDatabase("QSQLITE")
dane.setDatabaseName("baza\chinook.db")
dane.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        form = QFormLayout()
        self.track_id = QSpinBox()
        self.track_id.setDisabled(True)
        self.name = QLineEdit()
        self.album = QComboBox()
        self.media_type = QComboBox()
        self.genre = QComboBox()
        self.composer = QLineEdit()

        self.miliseconds = QSpinBox()
        self.miliseconds.setRange(0, 2147282287)
        self.miliseconds.setSingleStep(1)

        self.bytes = QSpinBox()
        self.bytes.setRange(0, 2147282287)
        self.bytes.setSingleStep(1)

        self.unit_price = QDoubleSpinBox()
        self.unit_price.setRange(0, 999)
        self.unit_price.setSingleStep(0.01)
        self.unit_price.setSuffix("pln")
        
       
        form.addRow(QLabel("Utwór ID"), self.track_id)
        form.addRow(QLabel("Nazwa utworu"), self.name)
        form.addRow(QLabel("Kompozytor"), self.composer)
        form.addRow(QLabel("Milisekundy"), self.miliseconds)
        form.addRow(QLabel("Bytes"), self.bytes)
        form.addRow(QLabel("Cena"), self.unit_price)

        self.model = QSqlTableModel(db=dane)

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)

        self.mapper.addMapping(self.track_id, 0)
        self.mapper.addMapping(self.name, 1)
        self.mapper.addMapping(self.composer, 5)
        self.mapper.addMapping(self.miliseconds, 6)
        self.mapper.addMapping(self.bytes, 7)
        self.mapper.addMapping(self.unit_price, 8)

        self.model.setTable("tracks")
        self.model.select()

        self.mapper.toFirst()

        self.setMinimumSize(QSize(600, 300))

        #przyciski
        kontrolki=QHBoxLayout()
        poprzedni=QPushButton("< Poprzedni")
        poprzedni.clicked.connect(self.mapper.toPrevious)
        
        nastepny=QPushButton("Następny >")
        nastepny.clicked.connect(self.mapper.toNext)
        
        zapisz=QPushButton("Zapisz")
        zapisz.clicked.connect(self.mapper.submit)
        
        kontrolki.addWidget(poprzedni)
        kontrolki.addWidget(nastepny)
        kontrolki.addWidget(zapisz)
        
        layout=QVBoxLayout()
        
        layout.addLayout(form)
        layout.addLayout(kontrolki)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
