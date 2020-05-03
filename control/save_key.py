import dbm

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from UI.save_key import Ui_save_key
from control.main_window import MainWindow
from key import KeyGenerator


class SaveKeyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_save_key()
        self.ui.setupUi(self)
        self.ui.btn_ok.setDefault(True)
        self.ui.btn_ok.clicked.connect(self.__generate_key)
        self.ui.btn_browse.clicked.connect(self.__browse_file)

    def __browse_file(self):
        path = QFileDialog.getSaveFileName(self)[0]
        self.ui.le_path.setText(path)

    def __generate_key(self):
        path = self.ui.le_path.text()
        with dbm.open('./sys_file/db', 'c') as db:
            db['private_key_path'] = path.encode('utf-8')

        try:
            self.generator = KeyGenerator()
            self.main_win = MainWindow()
            self.main_win.show()
            self.close()
        except OSError:
            QMessageBox.warning(self, '保存错误', '无法保存文件, 换一个路径再试')
            self.ui.le_path.clear()
