import abc
import dbm.dumb
import logging
from os import chmod
from stat import S_IRUSR

from Crypto.PublicKey import RSA

from paths import db_path


class KeyBase(abc.ABC):
    def __init__(self):
        with dbm.dumb.open(db_path, 'r') as db:
            self._path = db[b'private_key_path'].decode('utf-8')
            self._pass_phrase = db[b'password']

    @property
    @abc.abstractmethod
    def private_key(self):
        pass

    @property
    @abc.abstractmethod
    def public_key(self):
        pass


class KeyGenerator(KeyBase):
    def __init__(self):
        super().__init__()
        self.__private_key = RSA.generate(2048)
        self.__public_key = self.__private_key.publickey()
        self.__write_public_key()
        self.__write_private_key()

    def __write_public_key(self):
        """Write public key to database"""
        with dbm.dumb.open(db_path, 'c') as db:
            db[b'public_key'] = self.__public_key.export_key()
        logging.info('Public key is generated and written to database')

    def __write_private_key(self):
        """Write private key to self.__path"""
        private_key_enc = self.__private_key.export_key(passphrase=self._pass_phrase, pkcs=8,
                                                        protection="scryptAndAES128-CBC")
        with open(self._path, 'wb') as f:
            f.write(private_key_enc)
        chmod(self._path, S_IRUSR)

        logging.info('Private key is generated and written to %s', self._path)

    @property
    def private_key(self):
        return self.__private_key

    @property
    def public_key(self):
        return self.__public_key


class KeyGetter(KeyBase):
    def __init__(self):
        super().__init__()
        self.__public_key = self.__get_public_key()
        self.__private_key = self.__get_private_key()

    def __get_public_key(self):
        """Read and return the public key"""
        with dbm.dumb.open(db_path, 'c') as db:
            public_key = db[b'public_key']
        logging.info('Public key is read from database')
        return RSA.import_key(public_key)

    def __get_private_key(self):
        """Read and return the private key"""
        with open(self._path) as f:
            private_key_enc = f.read()
        # TODO: add handler to deal with incorrect password
        logging.info('Private key is read from %s', self._path)
        return RSA.import_key(private_key_enc, passphrase=self._pass_phrase)

    @property
    def private_key(self):
        return self.__private_key

    @property
    def public_key(self):
        return self.__public_key


# test
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    with dbm.dumb.open(db_path, 'w') as d:
        d[b'private_key_path'] = b'./private_key.bin'
    s = KeyGenerator('123123')
    h = KeyGetter('123123')
    assert s.public_key == h.public_key
    assert s.private_key == h.private_key
