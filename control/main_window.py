from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QToolButton, QApplication, QFileDialog, QMessageBox, QListWidget

from UI.main_window import Ui_MainWindow
from control.get_key import get_key
from control.log_window import LogWindow
from file_op import encrypt_file, decrypt_file, get_encrypted_file_names, clear_log
from ico.res_path import icon_path


class MyToolButton(QToolButton):
    """Tool button with specific style"""

    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPointSize(15)

        self.setFont(font)
        self.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.app = QApplication.instance()

        self.__key = get_key()

        if self.__key is None:
            self.app.quit()
        else:
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.__setup_ui()

    def __setup_ui(self):
        """Setup UI which isn't setup by self.ui"""

        self.ui.actionEncrypt_file.triggered.connect(self.__encrypt_file)
        self.ui.actionDecrypt_file.triggered.connect(self.__decrypt_file)
        self.ui.actionClose.triggered.connect(self.app.quit)
        self.ui.actionOpen_the_log.triggered.connect(self.__open_log)
        self.ui.actionClear_the_log.triggered.connect(self.__clear_log)

        self.btn_encrypt = MyToolButton()
        self.btn_encrypt.setIcon(QIcon(icon_path['lock']))
        self.btn_encrypt.setText('加密文件')
        self.btn_encrypt.clicked.connect(self.__encrypt_file)

        self.btn_decrypt = MyToolButton()
        self.btn_decrypt.setIcon(QIcon(icon_path['unlock']))
        self.btn_decrypt.setText('解密文件')
        self.btn_decrypt.clicked.connect(self.__decrypt_file)

        self.btn_open_log = MyToolButton()
        self.btn_open_log.setIcon(QIcon(icon_path['log']))
        self.btn_open_log.setText('查看日志')
        self.btn_open_log.clicked.connect(self.__open_log)

        self.btn_about = MyToolButton()
        self.btn_about.setIcon(QIcon(icon_path['about']))
        self.btn_about.setText('关于')
        self.btn_about.clicked.connect(self.__about)

        self.btn_exit = MyToolButton()
        self.btn_exit.setIcon(QIcon(icon_path['exit']))
        self.btn_exit.setText('退出')
        self.btn_exit.clicked.connect(self.app.quit)

        self.ui.toolBar.addWidget(self.btn_encrypt)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.btn_decrypt)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.btn_open_log)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.btn_about)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.btn_exit)

        self.ui.listWidget.setSelectionMode(QListWidget.ExtendedSelection)
        self.__refresh_list()

        self.setCentralWidget(self.ui.centralwidget)

    def __refresh_list(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(get_encrypted_file_names())

    def __encrypt_file(self):
        """Slot for actionEncrypt_file.triggered and btn_encrypt.clicked"""

        paths = QFileDialog.getOpenFileNames(self, caption='请选择要加密的文件')[0]
        if paths:
            r = QMessageBox.question(self, '确定加密文件',
                                     '<p>所选文件将被加密并保存至保险柜中</p>'
                                     '<p>原文件将被删除, 确定?</p>',
                                     defaultButton=QMessageBox.Yes)
            if r == QMessageBox.Yes:
                for path in paths:
                    try:
                        encrypt_file(path, self.__key)
                    except FileExistsError:
                        QMessageBox.warning(self, '加密错误',
                                            '<p>加密文件</p>'
                                            '<p>%s</p>'
                                            '<p>时发生错误, 因为保险柜中已经有和它同名的文件</p> '
                                            '<p>请将原文件重命名后再试</p>' % path)
                    except OSError:
                        QMessageBox.warning(self, '加密错误',
                                            '<p>加密文件</p>'
                                            '<p>%s</p>'
                                            '<p>时发生错误, 因为无法打开这个文件</p> ' % path)
                self.__refresh_list()

    def __decrypt_file(self):
        """Slot for actionDecrypt_file.triggered and btn_decrypt.clicked"""

        file_names = self.ui.listWidget.selectedItems()
        if not file_names:
            QMessageBox.warning(self, '错误',
                                '<p>没有选择文件</p>'
                                '<p>请选择要解密的文件</p>')
        else:
            QMessageBox.information(self, '提示', '请选择解密后的文件要保存在哪个文件夹')
            dec_path = QFileDialog.getExistingDirectory(self, caption='选择保存路径')
            if dec_path:
                r = QMessageBox.question(self, '确定解密文件',
                                         '<p>所选文件将被解密并保存至所选文件夹中</p>'
                                         '<p>原加密文件将被删除, 确定?</p>',
                                         defaultButton=QMessageBox.Yes)
                if r == QMessageBox.Yes:
                    success = True
                    for file_name in file_names:
                        s = file_name.text()
                        try:
                            decrypt_file(file_name.text() + '.enc', self.__key, dec_path)
                        except FileExistsError:
                            success = False
                            QMessageBox.warning(self, '解密错误',
                                                '<p>解密文件</p>'
                                                '<p>%s</p>'
                                                '<p>时发生错误, 因为所选路径中已经有和它同名的文件</p> '
                                                '<p>请将同名文件移动至别处后再试</p>' % file_name)
                        except ValueError:
                            success = False
                            QMessageBox.warning(self, '解密错误',
                                                '<p>解密文件</p>'
                                                '<p>%s</p>'
                                                '<p>时发生错误, 因为该文件验证失败, 可能已损坏</p> '
                                                '<p>损坏的文件已被删除</p>' % file_name)

                    self.__refresh_list()
                    if success:
                        QMessageBox.information(self, '完成', '文件已解密完成')

    def __clear_log(self):
        """Slot for actionClear_the_log.triggered"""

        clear_log()
        QMessageBox.information(self, '日志已清除', '日志已清除')

    def __open_log(self):
        """Slot for actionOpen_the_log.triggered and btn_open_log.clicked"""

        self.log_window = LogWindow()
        self.log_window.show()

    def __about(self):
        """Slot for btn_about.clicked"""

        QMessageBox.about(self,
                          '关于文件保险柜',
                          '<p>作者: 袁博实</p>'
                          '<p>学号: U201714853</p>'
                          '<p>使用PyQt5开发</p>'
                          '<p>电子商务与电子政务安全  期末作业</p>')
