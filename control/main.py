import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

from control.logindialog import LoginDialog


class Main(object):
    def __init__(self):
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon('ico/app.png'))

        app.setObjectName('123')

        self.login_dialog = LoginDialog()
        self.login_dialog.show()

        sys.exit(app.exec_())
