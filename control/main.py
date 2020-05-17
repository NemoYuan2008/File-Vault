import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon

from control.login import LoginDialog
from ico.res_path import icon_path


class Main(object):
    def __init__(self):
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(icon_path['app']))

        QMessageBox.warning(None,
                            '测试版警告',
                            '<h2>请备份文件!!!</h2>'
                            '<p>本文件保险柜目前仍在测试阶段</p>'
                            '<p>为避免数据丢失, 请在加密文件前备份原文件!</p>')

        self.login_dialog = LoginDialog()
        self.login_dialog.show()

        sys.exit(app.exec_())
