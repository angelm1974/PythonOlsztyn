# Form implementation generated from reading ui file 'interfejs.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 290, 441, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnKasuj = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnKasuj.setObjectName("btnKasuj")
        self.gridLayout.addWidget(self.btnKasuj, 1, 0, 1, 1)
        self.btnKoniecZadania = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnKoniecZadania.setObjectName("btnKoniecZadania")
        self.gridLayout.addWidget(self.btnKoniecZadania, 1, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 50, 441, 229))
        self.listView.setObjectName("listView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 390, 441, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.btnDodaj = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnDodaj.setObjectName("btnDodaj")
        self.verticalLayout.addWidget(self.btnDodaj)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnKasuj.setText(_translate("MainWindow", "Kasuj"))
        self.btnKoniecZadania.setText(_translate("MainWindow", "Zako??czone"))
        self.btnDodaj.setText(_translate("MainWindow", "Dodaj zadanie"))
