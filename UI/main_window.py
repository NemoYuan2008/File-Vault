# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 741, 521))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Songti SC")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuLogging = QtWidgets.QMenu(self.menubar)
        self.menuLogging.setObjectName("menuLogging")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEncrypt_file = QtWidgets.QAction(MainWindow)
        self.actionEncrypt_file.setObjectName("actionEncrypt_file")
        self.actionDecrypt_file = QtWidgets.QAction(MainWindow)
        self.actionDecrypt_file.setObjectName("actionDecrypt_file")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen_the_log = QtWidgets.QAction(MainWindow)
        self.actionOpen_the_log.setObjectName("actionOpen_the_log")
        self.actionClear_the_log = QtWidgets.QAction(MainWindow)
        self.actionClear_the_log.setObjectName("actionClear_the_log")
        self.menu.addAction(self.actionEncrypt_file)
        self.menu.addAction(self.actionDecrypt_file)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menuLogging.addAction(self.actionOpen_the_log)
        self.menuLogging.addAction(self.actionClear_the_log)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuLogging.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件保险柜"))
        self.label.setText(_translate("MainWindow", "文件保险柜中的文件"))
        self.label_2.setText(_translate("MainWindow", "选择文件来解密"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menuLogging.setTitle(_translate("MainWindow", "Logging"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionEncrypt_file.setText(_translate("MainWindow", "Encrypt file"))
        self.actionDecrypt_file.setText(_translate("MainWindow", "Decrypt file"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionOpen_the_log.setText(_translate("MainWindow", "Open the log"))
        self.actionClear_the_log.setText(_translate("MainWindow", "Clear the log"))
