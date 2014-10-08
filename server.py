# -*- coding: UTF-8 -*-

import rpyc
from rpyc.utils.authenticators import AuthenticationError

import ConfigFileParser
import MySQLWrapper

def client_authenticator(sock):
    channel = rpyc.Channel(rpyc.SocketStream(sock))
    data = channel.recv()

    data = rpyc.core.brine.load(data)

    login       = data[0]
    password    = data[1]

    config_parser       = ConfigFileParser.ConfigFileParser()
    expected_login      = config_parser.login()
    expected_password   = config_parser.password()

    if login != expected_login or password != expected_password:
        channel.send('AUTH_ERROR')
        raise rpyc.utils.authenticators.AuthenticationError('Invalid password from client.')

    channel.send('AUTH_SUCCESS')
    return sock, None



class RPCService(rpyc.Service):

    mysql = MySQLWrapper.MySQLWrapper()


    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass


    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass


    def exposed_get_answer(self):
        raise ValueError('QWERTY')
        return "Hello, world!!!!","QWERTY"


    def exposed_get(self, key): # this is an exposed method
        #print key
        return self.mysql.select(key)


    def exposed_put(self, key, val): # this is an exposed method
        return self.mysql.insert(key,val)


    def exposed_update(self, key, val): # this is an exposed method
        return self.mysql.update(key,val)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    config_parser = ConfigFileParser.ConfigFileParser()
    port = int( config_parser.port() )
    t = ThreadedServer(RPCService, port = port, authenticator = client_authenticator)

    t.start()
