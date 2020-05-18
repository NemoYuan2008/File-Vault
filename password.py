import dbm.dumb
import logging

from Crypto.Hash import SHA3_256
from Crypto.Random import get_random_bytes

from paths import db_path


def calc_hash(password, salt):
    """Calculate and return hash of password with the provided salt

    result = SHA3(SHA3(password) + salt)
    """

    password_hash = SHA3_256.new(password).digest()
    hash_obj = SHA3_256.new(password_hash)
    hash_obj.update(salt)
    return hash_obj.digest()


def register_password(password):
    """Register a new password and write its hash value to db

    Note: this function is only called for initialization
    """
    if isinstance(password, str):
        password = password.encode('utf-8')

    salt = get_random_bytes(32)
    password_hash = calc_hash(password, salt)

    with dbm.dumb.open(db_path, 'c') as db:
        db[b'has_init'] = b'True'
        db[b'password'] = password_hash
        db[b'wrong_count'] = b'0'
        db[b'salt'] = salt

    logging.info('New password is registered')


class Authentication(object):
    def __init__(self):
        """Read correct_password_hash and wrong_count from db"""
        with dbm.dumb.open(db_path, 'c') as db:
            self.__correct_password_hash = db.get(b'password', None)
            self.__salt = db.get(b'salt', None)
            self.__wrong_count = int(db.get(b'wrong_count', b'0'))

    def __del__(self):
        """Save wrong_count to db"""
        with dbm.dumb.open(db_path, 'c') as db:
            db[b'wrong_count'] = str(self.__wrong_count).encode('utf-8')

    def check(self, input_password):
        """Check if input_password is correct

        :param input_password: the password to check
        :return: True if correct, False otherwise

        :raise ValueError: if failed password attempt times reaches 10
        """
        if isinstance(input_password, str):
            input_password = input_password.encode('utf-8')
        input_password_hash = calc_hash(input_password, self.__salt)

        if input_password_hash == self.__correct_password_hash:
            self.__wrong_count = 0
            logging.info('Login succeed')
            return True
        else:
            logging.warning('Incorrect password')
            self.__wrong_count += 1
            if self.__wrong_count >= 10:
                logging.error('10 failed password attempts')
                raise ValueError('10 failed password attempts')
            return False

    @property
    def wrong_count(self):
        return self.__wrong_count


# tests
if __name__ == '__main__':
    register_password('123123')
    s = Authentication()
    assert s.check('123123')
    for i in range(10):
        print(i, s.check('1'))
