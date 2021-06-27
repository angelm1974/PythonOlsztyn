from os.path import expanduser
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
home_directory = expanduser("~")

home_directory = expanduser("~")
app = QApplication([])
model = QDirModel()
view = QTreeView()
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()
app.exec()