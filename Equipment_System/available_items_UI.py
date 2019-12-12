# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'available_items.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logoutbutton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutbutton.setObjectName("logoutbutton")
        self.gridLayout.addWidget(self.logoutbutton, 3, 3, 1, 1)
        self.available_items_label = QtWidgets.QLabel(self.centralwidget)
        self.available_items_label.setObjectName("available_items_label")
        self.gridLayout.addWidget(self.available_items_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkinbutton = QtWidgets.QPushButton(self.centralwidget)
        self.checkinbutton.setEnabled(True)
        self.checkinbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.checkinbutton.setObjectName("checkinbutton")
        self.verticalLayout.addWidget(self.checkinbutton)
        self.checkoutbutton = QtWidgets.QPushButton(self.centralwidget)
        self.checkoutbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.checkoutbutton.setObjectName("checkoutbutton")
        self.verticalLayout.addWidget(self.checkoutbutton)
        self.allitemsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.allitemsbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.allitemsbutton.setObjectName("allitemsbutton")
        self.verticalLayout.addWidget(self.allitemsbutton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 3, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.logoutbutton.setText(_translate("MainWindow", "Log Out"))
        self.available_items_label.setText(_translate("MainWindow",
                                                      "<html><head/><body><p><span style=\" font-size:12pt;\">Available Items</span></p></body></html>"))
        self.checkinbutton.setText(_translate("MainWindow", "Check-in an item"))
        self.checkoutbutton.setText(_translate("MainWindow", "Check-out an item"))
        self.allitemsbutton.setText(_translate("MainWindow", "All Items"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
