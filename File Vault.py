#! /usr/bin/env python3

import logging
import os

from control.main import Main
from algorithm.paths import working_dir, log_path, enc_path

if __name__ == '__main__':
    if not os.path.exists(working_dir):
        os.mkdir(working_dir)

    if not os.path.exists(enc_path):
        os.mkdir(enc_path)

    logging.basicConfig(filename=log_path,
                        level=logging.INFO,
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S %p')
    m = Main()
