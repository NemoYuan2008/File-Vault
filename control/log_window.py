from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox

from UI.log_window import Ui_log_window
from algorithm.file_op import open_log, clear_log


class LogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_log_window()
        self.ui.setupUi(self)
        self.ui.textBrowser.setText(open_log())
        self.ui.btn_clear.clicked.connect(clear_log)
        self.ui.btn_export.clicked.connect(self.__export_log)

    def __export_log(self):
        file_name = QFileDialog.getSaveFileName(self, '选择保存路径', filter='*.log')[0]
        if file_name:
            try:
                with open(file_name, 'w') as f:
                    f.write(open_log())
                QMessageBox.information(self, '导出成功', '日志已成功导出到%s' % file_name)
            except OSError:
                QMessageBox.warning(self, '导出失败', '日志导出失败, 请换一个路径再试')
