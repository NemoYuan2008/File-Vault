"""
Manipulate USB IO
This file is likely to be discarded
"""

import platform
import os

from psutil import disk_partitions


def usb_path_0():
    """Get a list of mobile devices

    :return a list of device names (str)

    NOTE: this function hasn't been tested on Windows and Linux
    Use usb_path instead
    """
    sys_name = platform.system()

    if sys_name == 'Windows':
        ret = []
        for part in disk_partitions():
            if 'removable' in part.opts:
                ret.append(part.device)
        return ret
    elif sys_name == 'Linux':
        return os.listdir('/media')
    elif sys_name == 'Darwin':
        return os.listdir('/Volumes')
    else:
        raise ValueError('OS not supported')


def usb_path():
    """Get a list of all mounted devices

    :return: a tuple (device, mount_point)
    """
    for part in disk_partitions():
        yield (part.device, part.mountpoint)


# tests
if __name__ == '__main__':
    print(list(usb_path()))
