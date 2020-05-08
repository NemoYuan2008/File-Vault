#! /usr/bin/env python3

import logging

from control.main import Main


if __name__ == '__main__':
    logging.basicConfig(filename='./sys_file/log.log',
                        level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    m = Main()
