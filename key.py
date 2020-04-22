import abc
import dbm

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP


class KeyBase(abc.ABC):
    def __init__(self, password):
        if isinstance(password, str):
            password = password.encode('utf-8')
        self._password = password

    @property
    @abc.abstractmethod
    def symmetric_key(self):
        pass


class KeyGenerator(KeyBase):
    def __init__(self, password, path='./pri.bin'):
        super().__init__(password)
        self.__path = path
        self.__private_key = RSA.generate(2048)
        self.__public_key = self.__private_key.publickey()
        self.__symmetric_key = get_random_bytes(32)  # AES-256
        self.__encrypt_symmetric_key()
        self.__write_private_key_to_file()
        self.__write_symmetric_key_to_file()

    def __encrypt_symmetric_key(self):
        cipher_rsa = PKCS1_OAEP.new(self.__public_key)
        self.__symmetric_key_enc = cipher_rsa.encrypt(self.__symmetric_key)

    def __write_private_key_to_file(self):
        private_key_enc = self.__private_key.export_key(passphrase=self._password, pkcs=8,
                                                        protection="scryptAndAES128-CBC")
        with open(self.__path, 'wb') as f:
            f.write(private_key_enc)

    def __write_symmetric_key_to_file(self):
        with dbm.open('./sys_file/db', 'c') as db:
            db[b'symmetric_key'] = self.__symmetric_key_enc

    @property
    def symmetric_key(self):
        return self.__symmetric_key


class KeyGetter(KeyBase):
    def __init__(self, password, path='./pri.bin'):
        super().__init__(password)
        with open(path) as f:
            private_key_enc = f.read()
            # TODO: add handler to deal with incorrect password
            self.__private_key = RSA.import_key(private_key_enc, passphrase=self._password)
        self.__get_symmetric_key_from_file()

    def __get_symmetric_key_from_file(self):
        """
        get the encrypted symmetric key from file then decrypt it
        """
        with dbm.open('./sys_file/db', 'r') as db:
            self.__symmetric_key = db[b'symmetric_key']
        cipher_rsa = PKCS1_OAEP.new(self.__private_key)
        self.__symmetric_key = cipher_rsa.decrypt(self.__symmetric_key)

    @property
    def symmetric_key(self):
        return self.__symmetric_key


if __name__ == '__main__':
    s = KeyGenerator('123123')
    h = KeyGetter('12323')
    print(s.symmetric_key, h.symmetric_key)
    assert s.symmetric_key == h.symmetric_key
