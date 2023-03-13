import os


def get_account():
    if os.path.exists('upload.txt'):
        with open('upload.txt') as file:
            f_read = file.read()
            if f_read == '':
                print('Файл пустой.')
                return None

            f = f_read.split('\n')
            result = f[0]

        _str = ''
        for i in f[1:]:
            _str += i + '\n'
        _str = _str[:-1]

        with open('upload.txt', 'w') as file:
            file.write(_str)

        return result
    else:
        print('Файл не найден.')
        return None


def get_account2():
    if os.path.exists('upload2.txt'):
        with open('upload2.txt') as file:
            f_read = file.read()
            if f_read == '':
                print('Файл пустой.')
                return None

            f = f_read.split('\n')
            result = f[0]

        _str = ''
        for i in f[1:]:
            _str += i + '\n'
        _str = _str[:-1]

        with open('upload2.txt', 'w') as file:
            file.write(_str)

        return result
    else:
        print('Файл не найден.')
        return None
