from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Encrypt(object):
    def __init__(self, key):
        self.__key = key

    def encrypt_data(self, data: bytes):
        cipher = AES.new(self.__key, AES.MODE_EAX)
        nonce = cipher.nonce
        cipher_text, tag = cipher.encrypt_and_digest(data)
        return nonce + tag + cipher_text

    def decrypt_data(self, data: bytes):
        cipher = AES.new(self.__key, AES.MODE_EAX)


class Decrypt(object):
    def __init__(self, key):
        self.__key = key
        self.__cipher = AES.new(key, AES.MODE_CBC)

    def decrypt_data(self, data: bytes):
        cipher = AES.new(key, AES.MODE_CBC)
        data = self.__cipher.decrypt(data)
        return unpad(data, AES.block_size)


if __name__ == '__main__':
    from Crypto.Random import get_random_bytes
