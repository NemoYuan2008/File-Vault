import os
import dbm
import logging
from operator import itemgetter

from encrypt import encrypt_data, decrypt_data
from key import KeyBase

# get the paths
with dbm.open('./sys_file/db', 'c') as db:
    enc_path = db.get(b'enc_path', b'./encrypted_file').decode('utf-8')
    dec_path = db.get(b'dec_path', b'./decrypted_file').decode('utf-8')


def encrypt_file(file_path: str, rsa_key: KeyBase):
    """Encrypt the given file

    The encrypted file is saved to directory enc_path with its name appended '.enc'
    The original file is deleted

    :param file_path: path to the file to be encrypted
    :param rsa_key: a KeyBase class to provide public key

    :raise FileNotFoundError: if file is not found
    :raise FileExistsError: if file with the same name exists in enc_path

    TODO: deal with directories
    """

    with open(file_path, 'rb') as f:
        data = f.read()
    data = encrypt_data(data, rsa_key)

    # append file name with '.enc'
    out_path = os.path.join(enc_path, os.path.split(file_path)[1]) + '.enc'
    if os.path.exists(out_path):
        raise FileExistsError('Corrupted file name')

    with open(out_path, 'wb') as f:
        f.write(data)

    os.remove(file_path)

    logging.info('File %s is encrypted and deleted, encrypted file is written to %s', file_path, out_path)


def decrypt_file(file_name: str, rsa_key: KeyBase, dec_path: str = dec_path):
    """Decrypt the given file

    The decrypted file is saved to directory dec_path with its original name (without '.enc')
    The encrypted file is deleted

    :param dec_path: a directory to output decrypted files
    :param file_name: file to be decrypted, just a file name, not a path
    :param rsa_key: a KeyBase class to provide private key

    :raise FileExistsError: if file with the same name exists in dec_path
    """

    file_path = os.path.join(enc_path, file_name)
    with open(file_path, 'rb') as f:
        data = f.read()
    data = decrypt_data(data, rsa_key)

    # path + file name without '.enc'
    out_path = os.path.join(dec_path, os.path.splitext(file_name)[0])
    if os.path.exists(out_path):
        logging.error('File %s already exists in the encrypted files directory', file_name)
        raise FileExistsError('Corrupted file name')

    with open(out_path, 'wb') as f:
        f.write(data)

    os.remove(file_path)

    logging.info('Encrypted file %s is decrypted and deleted, decrypted file is written to %s', file_name, out_path)


def delete_all_enc_files():
    """Remove all encrypted files

    This function is ONLY used when failed password attempt times reaches 10

    CAUTION: this function is DANGEROUS!!!!
    ALL ENCRYPTED FILES WILL BE DELETED!!!!
    """
    for root, dirs, files in os.walk(enc_path, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            os.remove(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
            os.rmdir(os.path.join(root, name))
    os.remove('./sys_file/db')
    logging.warning('Deleting all Encrypted files and the database!')


def get_encrypted_file_names():
    """Get a list of all encrypted file names"""

    return list(map(itemgetter(0), map(os.path.splitext, os.listdir(enc_path))))


def open_log():
    """Open and return the contents of the log"""

    with open('./sys_file/log.log', 'r') as f:
        return f.read()


def clear_log():
    """Clear the contents of the log"""

    with open('./sys_file/log.log', 'w') as f:
        pass


# tests
if __name__ == '__main__':
    from key import KeyGenerator, KeyGetter

    logging.basicConfig(level=logging.DEBUG)

    delete_all_enc_files()
    # now enc_path should be empty
    assert len(list(os.walk(enc_path, topdown=False))) == 1

    with open('./original_file/test.txt', 'w') as f:
        f.write('test test test test test ')

    with open('./original_file/test.txt', 'rb') as f:
        ori_data = f.read()

    k = KeyGetter(b'123123')
    encrypt_file('./original_file/test.txt', k)
    decrypt_file('test.txt.enc', k)

    with open('./decrypted_file/test.txt', 'rb') as f:
        dec_data = f.read()

    assert ori_data == dec_data
    assert not os.path.exists('./original_file/test.txt')
    assert not os.path.exists('./encrypted_file/test.txt.enc')

    os.remove('./decrypted_file/test.txt')
