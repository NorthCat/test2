# -*- coding: UTF-8 -*-

import ConfigParser


class ConfigFileParser:
    def __init__(self, path='config.ini'):
        self.config = ConfigParser.ConfigParser()
        self.config.read(path)


    def host(self):
        return self.config.get('NETWORK', 'host')


    def port(self):
        return self.config.get('NETWORK', 'port')


    def login(self):
        return self.config.get('AUTH', 'login')


    def password(self):
        return self.config.get('AUTH', 'password')



if __name__ == '__main__':
    parser = ConfigFileParser()
    print parser.host()
    print parser.port()
    print parser.login()
    print parser.password()
