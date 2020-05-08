from PyQt5.QtWidgets import QMessageBox

from key import KeyGetter


def get_key():
    """Get the Key using KeyGetter

    Notify user if key file is not found
    :return A KeyGetter if successful, None if failed
    """

    key = None
    while key is None:
        try:
            key = KeyGetter()
            return key

        except OSError:
            msg = QMessageBox(QMessageBox.Information,
                              '请插入USB Key',
                              '未找到USB Key, 请插入USB Key后点击确定重试')
            msg.addButton(QMessageBox.Ok).setText('确定')
            msg.addButton(QMessageBox.Abort).setText('退出')

            r = msg.exec()
            if r == QMessageBox.Abort:
                return None

        except ValueError:
            msg = QMessageBox(QMessageBox.Warning,
                              '错误',
                              '插入了错误的USB Key, 请插入正确的USB Key后点击确定重试')
            msg.addButton(QMessageBox.Ok).setText('确定')
            msg.addButton(QMessageBox.Abort).setText('退出')

            r = msg.exec()
            if r == QMessageBox.Abort:
                return None
