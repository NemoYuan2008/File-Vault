import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

from control.login import LoginDialog
from ico.res_path import icon_path


class Main(object):
    def __init__(self):
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(icon_path['app']))

        self.login_dialog = LoginDialog()
        self.login_dialog.show()

        sys.exit(app.exec_())
