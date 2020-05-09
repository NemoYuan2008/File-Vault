#! /usr/bin/env python3

import logging
import os

from control.main import Main
from paths import working_dir, log_path

if __name__ == '__main__':
    if not os.path.exists(working_dir):
        os.mkdir(working_dir)

    logging.basicConfig(filename=log_path,
                        level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    m = Main()
