import os
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from UI.enter_passwd import Ui_DialogEnterPasswd
from UI.set_passwd import Ui_DialogSetPasswd


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()

    if os.path.exists('./sys_file/db'):
        password_dialog = Ui_DialogEnterPasswd()
        password_dialog.setupUi(dialog)
    else:
        password_dialog = Ui_DialogSetPasswd()
        password_dialog.setupUi(dialog)

    dialog.show()
    sys.exit(app.exec_())
