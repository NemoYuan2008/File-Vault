import sys
import dbm

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from UI.enter_passwd import Ui_DialogEnterPasswd
from UI.set_passwd import Ui_DialogSetPasswd
from password import Authentication, register_password
from file_op import delete_all_enc_files


def initialize():
    with dbm.open('./sys_file/db', 'c') as db:
        ret = db.get(b'has_init', b'False')

        if ret == b'True':
            return True
        else:
            db[b'wrong_count'] = b'0'
            return False


class Login(object):
    def __init__(self):
        app = QApplication(sys.argv)
        self.dialog = QDialog()

        if initialize():
            self.authenticator = Authentication()

            self.verify_password_dialog = Ui_DialogEnterPasswd()
            self.verify_password_dialog.setupUi(self.dialog)
            self.verify_password_dialog.btn_ok.clicked.connect(self.__verify_password)
        else:
            self.set_password_dialog = Ui_DialogSetPasswd()
            self.set_password_dialog.setupUi(self.dialog)
            self.set_password_dialog.btn_ok.clicked.connect(self.__set_password)

        self.dialog.show()
        sys.exit(app.exec_())

    def __verify_password(self):
        password = self.verify_password_dialog.le_password.text()
        try:
            if self.authenticator.check(password):
                # TODO: Enter main window
                pass
            else:
                QMessageBox.warning(self.dialog, '密码错误',
                                    '密码错误, 还有%d次机会, 否则所有已加密文件将被删除' %
                                    (10 - self.authenticator.wrong_count))
        except ValueError:
            delete_all_enc_files()
            QMessageBox.critical(self.dialog, '密码错误', '连续10次密码错误, 所有已加密文件将被删除')
            self.dialog.close()

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
