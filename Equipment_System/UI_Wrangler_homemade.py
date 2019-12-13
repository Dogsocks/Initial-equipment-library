from available_items_UI import Ui_MainWindow
from all_items import Ui_all_itemsMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

"""

def openWindow(self):
    self.window = QtWidgets.QMainWindow()
    self.ui = Ui_all_itemsMainWindow
    self.ui.setupUI(self.window)
    self.window.show()"""

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())