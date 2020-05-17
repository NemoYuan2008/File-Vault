"""Provide paths for png icons

Needed by pyinstaller
"""


import os
import sys


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


icon_path = {
    'app': resource_path('app.png'),
    'exit': resource_path('exit.png'),
    'lock': resource_path('lock.png'),
    'unlock': resource_path('unlock.png'),
    'log': resource_path('log.png'),
    'about': resource_path('about.png')
}
