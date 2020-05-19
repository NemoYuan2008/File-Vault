from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from algorithm.key import KeyBase


def encrypt_data(data: bytes, rsa_key: KeyBase):
    """Encrypt data

    :param data: data to be encrypted
    :param rsa_key: a KeyBase class to provide public key
    :return: encrypted data with encrypted key

    len(key_enc) == 256, len(nonce) == 16, len(tag) == 16
    """

    # encrypt the data
    key = get_random_bytes(32)  # AES-256
    cipher_aes = AES.new(key, AES.MODE_EAX)
    nonce = cipher_aes.nonce
    data_enc, tag = cipher_aes.encrypt_and_digest(data)

    # encrypt the AES key
    cipher_rsa = PKCS1_OAEP.new(rsa_key.public_key)
    key_enc = cipher_rsa.encrypt(key)

    return key_enc + nonce + tag + data_enc


def decrypt_data(data: bytes, rsa_key: KeyBase):
    """Decrypt data

    :param data: data to be decrypted
    :param rsa_key: a KeyBase class to provide private key
    :return: decrypted data
    """

    # unpack data
    key_enc = data[:256]
    nonce = data[256:272]
    tag = data[272:288]
    data_enc = data[288:]

    # decrypt the key
    cipher_rsa = PKCS1_OAEP.new(rsa_key.private_key)
    key = cipher_rsa.decrypt(key_enc)

    # decrypt the data
    cipher_aes = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(data_enc, tag)

    return data


# tests
if __name__ == '__main__':
    from algorithm.key import KeyGenerator

    k = KeyGenerator(b'123')
    t = get_random_bytes(100)
    t_enc = encrypt_data(t, k)
    t_dec = decrypt_data(t_enc, k)
    assert t == t_dec
