import dbm

from PyQt5.QtWidgets import QDialog, QMessageBox

from UI.verify_password import Ui_DialogEnterPasswd
from UI.set_password import Ui_DialogSetPasswd

from control.main_window import MainWindow
from control.save_key import SaveKeyDialog

from password import Authentication, register_password
from file_op import delete_all_enc_files


def initialize():
    with dbm.open('./sys_file/db', 'c') as db:
        ret = db.get(b'has_init', b'False')

        if b'public_key' in db:
            return True
        else:
            db[b'wrong_count'] = b'0'
            return False


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        if initialize():
            self.authenticator = Authentication()

            self.ui_verify_password = Ui_DialogEnterPasswd()
            self.ui_verify_password.setupUi(self)
            self.ui_verify_password.btn_ok.clicked.connect(self.__verify_password)

        else:
            self.ui_set_password = Ui_DialogSetPasswd()
            self.ui_set_password.setupUi(self)
            self.ui_set_password.btn_ok.clicked.connect(self.__set_password)

    def __verify_password(self):
        password = self.ui_verify_password.le_password.text()

        try:
            if self.authenticator.check(password):
                QMessageBox.information(self, '密码正确', '密码正确')

                # Enter the main window
                self.main_win = MainWindow()
                self.main_win.show()
                self.close()

            else:
                QMessageBox.warning(self, '密码错误',
                                    '密码错误, 还有%d次机会, 否则所有已加密文件将被删除' %
                                    (10 - self.authenticator.wrong_count))
                self.ui_verify_password.le_password.clear()

        except ValueError:
            delete_all_enc_files()
            QMessageBox.critical(self, '密码错误', '连续10次密码错误, 所有已加密文件将被删除')
            self.close()

    def __set_password(self):
        password1 = self.ui_set_password.le_passwd.text()
        password2 = self.ui_set_password.le_confirm.text()
        if password1 == password2:
            register_password(password1)
            self.close()
            self.save_key_dialog = SaveKeyDialog()
            self.save_key_dialog.exec()
            # TODO: Enter main window
        else:
            QMessageBox.warning(self, '输入不正确', '两次密码输入不一致, 请重新输入')
            self.ui_set_password.le_passwd.clear()
            self.ui_set_password.le_confirm.clear()
