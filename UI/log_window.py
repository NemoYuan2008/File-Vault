# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_log_window(object):
    def setupUi(self, log_window):
        log_window.setObjectName("log_window")
        log_window.resize(599, 454)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(log_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(log_window)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_close = QtWidgets.QPushButton(log_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setDefault(True)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.btn_export = QtWidgets.QPushButton(log_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy)
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout.addWidget(self.btn_export)
        self.btn_clear = QtWidgets.QPushButton(log_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout.addWidget(self.btn_clear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(log_window)
        self.btn_close.clicked.connect(log_window.close)
        self.btn_clear.clicked.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(log_window)

    def retranslateUi(self, log_window):
        _translate = QtCore.QCoreApplication.translate
        log_window.setWindowTitle(_translate("log_window", "logs"))
        self.btn_close.setText(_translate("log_window", "关闭"))
        self.btn_export.setText(_translate("log_window", "导出..."))
        self.btn_clear.setText(_translate("log_window", "清除"))
