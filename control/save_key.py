import dbm

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from UI.save_key import Ui_save_key
from control.main_window import MainWindow
from key import KeyGenerator


class ThreadGenerateKey(QThread):
    """A thread to generate key

    emits signal_success if key is generated successfully
    emits signal_failure if error happens
    """

    signal_success = pyqtSignal()
    signal_failure = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        try:
            generator = KeyGenerator()
            self.signal_success.emit()
        except OSError:
            self.signal_failure.emit()


class SaveKeyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_save_key()
        self.ui.setupUi(self)

        self.ui.btn_ok.setDefault(True)

        self.ui.btn_ok.clicked.connect(self.__generate_key)
        self.ui.btn_browse.clicked.connect(self.__browse_file)

    def __browse_file(self):
        """Slot for btn_browse.clicked"""

        path = QFileDialog.getSaveFileName(self, filter='*.pem')[0]
        self.ui.le_path.setText(path)

    def __generate_key(self):
        """Slot for btn_browse.clicked"""

        self.msg = QMessageBox(parent=self, text='正在生成密钥, 请稍候', icon=QMessageBox.Information)
        self.msg.show()
        self.msg.button(QMessageBox.Ok).hide()

        path = self.ui.le_path.text()
        with dbm.open('./sys_file/db', 'c') as db:
            db['private_key_path'] = path.encode('utf-8')

        self.thread_generate_key = ThreadGenerateKey()
        self.thread_generate_key.signal_success.connect(self.__on_success)
        self.thread_generate_key.signal_failure.connect(self.__on_failure)
        self.thread_generate_key.start()

    def __on_success(self):
        """Slot for signal_success"""

        self.msg.close()
        QMessageBox.information(self, '成功', '密钥生成完成, 请妥善保存')

        self.main_win = MainWindow()
        self.main_win.show()
        self.close()

    def __on_failure(self):
        """Slot for signal_failure"""
        self.msg.close()
        QMessageBox.warning(self, '错误', '无法保存文件, 换一个路径再试')
        self.ui.le_path.clear()
