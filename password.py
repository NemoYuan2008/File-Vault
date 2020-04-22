import dbm

from Crypto.Hash import SHA3_256


def register_password(password):
    if isinstance(password, str):
        password = password.encode('utf-8')
    password = SHA3_256.new(password).digest()

    with dbm.open('./sys_file/db', 'c') as db:
        db[b'password'] = password


class Authentication(object):
    def __init__(self):
        # TODO: read __wrong_count from dbm
        self.__wrong_count = 0
        with dbm.open('./sys_file/db', 'c') as db:
            self.__correct_password = db[b'password']

    def check(self, input_password):
        if isinstance(input_password, str):
            input_password = input_password.encode('utf-8')
        input_password = SHA3_256.new(input_password).digest()

        if input_password == self.__correct_password:
            s.__wrong_count = 0
            return True
        else:
            self.__wrong_count += 1
            if self.__wrong_count == 10:
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
