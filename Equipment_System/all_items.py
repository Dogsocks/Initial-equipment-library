# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_items.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_all_itemsMainWindow(object):
    def setupUi(self, Ui_all_itemsMainWindow):
        Ui_all_itemsMainWindow.setObjectName("Ui_all_itemsMainWindow")
        Ui_all_itemsMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Ui_all_itemsMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.available_items_label = QtWidgets.QLabel(self.centralwidget)
        self.available_items_label.setObjectName("available_items_label")
        self.verticalLayout.addWidget(self.available_items_label)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkinbutton = QtWidgets.QPushButton(self.centralwidget)
        self.checkinbutton.setEnabled(True)
        self.checkinbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.checkinbutton.setObjectName("checkinbutton")
        self.gridLayout_2.addWidget(self.checkinbutton, 0, 0, 1, 1)
        self.allitemsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.allitemsbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.allitemsbutton.setObjectName("allitemsbutton")
        self.gridLayout_2.addWidget(self.allitemsbutton, 0, 2, 1, 1)
        self.checkoutbutton = QtWidgets.QPushButton(self.centralwidget)
        self.checkoutbutton.setMinimumSize(QtCore.QSize(0, 75))
        self.checkoutbutton.setObjectName("checkoutbutton")
        self.gridLayout_2.addWidget(self.checkoutbutton, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 75))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        Ui_all_itemsMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_all_itemsMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Ui_all_itemsMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_all_itemsMainWindow)
        self.statusbar.setObjectName("statusbar")
        Ui_all_itemsMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_all_itemsMainWindow)
        QtCore.QMetaObject.connectSlotsByName(Ui_all_itemsMainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.available_items_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">All Items</span></p></body></html>"))
        self.checkinbutton.setText(_translate("MainWindow", "Check-in an item"))
        self.allitemsbutton.setText(_translate("MainWindow", "Available Items"))
        self.checkoutbutton.setText(_translate("MainWindow", "Check-out an item"))
        self.pushButton.setText(_translate("MainWindow", "Log Out"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_all_itemsMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())