# -*- coding: UTF-8 -*-

import sys

class CommandLineParser:

    def __init__(self):
        self.method = sys.argv[1]


    def get_method(self):
        return self.method


    #Возвращает ключ по которому будет проводится селект в БД
    def get_args(self):
        assert self.method == 'get', ''

        get_params = sys.argv[2].rpartition(':')
        return get_params[2]

    #параметр key: содержит значение поля 'keys' создаваемой строки, параметр val: содержит значение поля 'data' создаваемой строки
    def put_args(self):
        assert self.method == 'put', ''

        put_key = sys.argv[2].rpartition(':')[2]
        put_val = sys.argv[3].rpartition(':')[2]

        return put_key, put_val

    # параметр upd указывает на обновление строки со значением поля 'keys' равным test1, параметр val:
    # содержит значение поля 'data' которое будет установлено в результате обновления.
    def upd_args(self):
        assert self.method == 'upd', ''

        upd_key = sys.argv[2].rpartition(':')[2]
        upd_val = sys.argv[3].rpartition(':')[2]

        return upd_key, upd_val


if __name__ == '__main__':
    clp = CommandLineParser()
    print clp.get_method()

    if clp.get_method() == 'get':
        print clp.get_args()
    elif clp.get_method() == 'put':
        print clp.put_args()
    elif clp.get_method() == 'upd':
        print clp.upd_args()
    else:
        print 'Error method!: ', clp.get_method()
