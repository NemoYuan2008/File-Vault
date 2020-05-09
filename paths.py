"""Paths to save all files"""

import os


working_dir = os.path.join(os.path.expanduser('~'), '.FileVault')
log_path = os.path.join(working_dir, 'log.log')
enc_path = os.path.join(working_dir, 'encrypted_files')
db_path = os.path.join(working_dir, 'db')
