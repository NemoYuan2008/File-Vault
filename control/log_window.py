from PyQt5.QtWidgets import QWidget

from UI.log_window import Ui_log_window
from file_op import open_log, clear_log


class LogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_log_window()
        self.ui.setupUi(self)
        self.ui.textBrowser.setText(open_log())
        self.ui.btn_clear.clicked.connect(clear_log)
