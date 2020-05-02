import os
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from UI.enter_passwd import Ui_DialogEnterPasswd
from UI.set_passwd import Ui_DialogSetPasswd
from password import *


class Main(object):
    def __init__(self):
        app = QApplication(sys.argv)
        self.dialog = QDialog()

        if os.path.exists('./sys_file/db'):
            self.verify_password_dialog = Ui_DialogEnterPasswd()
            self.verify_password_dialog.setupUi(self.dialog)
            self.verify_password_dialog.btn_ok.clicked.connect(self.__verify_password)
        else:
            self.authenticator = Authentication()

            self.set_password_dialog = Ui_DialogSetPasswd()
            self.set_password_dialog.setupUi(self.dialog)
            self.set_password_dialog.btn_ok.clicked.connect(self.__set_password)

        self.dialog.show()
        sys.exit(app.exec_())

    def __verify_password(self):
        password = self.verify_password_dialog.le_password.text()
        # TODO: add exception handler
        self.authenticator.check(password)

    def __set_password(self):
        password1 = self.set_password_dialog.le_passwd.text()
        password2 = self.set_password_dialog.le_confirm.text()
        print(password1, password2)
        if password1 == password2:
            register_password(password1)
            # TODO: Enter main window
        else:
            QMessageBox.warning(self.dialog, '输入不正确', '两次密码输入不一致, 请重新输入')
            self.set_password_dialog.le_passwd.clear()
            self.set_password_dialog.le_confirm.clear()


if __name__ == '__main__':
    m = Main()
