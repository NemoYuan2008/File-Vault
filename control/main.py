import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

from control.login import LoginDialog


class Main(object):
    def __init__(self):
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon('ico/app.png'))

        self.login_dialog = LoginDialog()
        self.login_dialog.show()

        sys.exit(app.exec_())
