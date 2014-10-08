# -*- coding: UTF-8 -*-

import rpyc

import CommandLineParser
import ConfigFileParser


class RPCClient:

    def __init__(self, host, port, login, password):

        channel = rpyc.Channel(rpyc.SocketStream.connect(host, port))
        secure = rpyc.core.brine.dump( (login,password) )

        channel.send( secure )

        response = channel.recv()

        if response == 'AUTH_ERROR':
            raise ValueError('Invalid login or password for daemon')

        self.conn = rpyc.utils.factory.connect_channel(channel)


    def foo(self):
        print self.conn.root.get_answer()


    def get(self, key):
        return self.conn.root.get(key)


    def put(self, key, val):
        return self.conn.root.put(key, val)


    def update(self, key, val):
        return self.conn.root.update(key, val)


    
if __name__ == '__main__':
    try:
        config_parser    = ConfigFileParser.ConfigFileParser()

        host = config_parser.host()
        port = int( config_parser.port() )
        login = config_parser.login()
        password = config_parser.password()

        client = RPCClient( host, port, login, password )


        clp  = CommandLineParser.CommandLineParser()

        if clp.get_method() == 'get':
            key = clp.get_args()
            res =  client.get(key)[0]
            if res:
                print 'ID: %s, KEY: %s, DATA: %s' % (res[0],res[1],res[2])
            else:
                print 'Nothing select'

        elif clp.get_method() == 'put':
            key, val = clp.put_args()
            client.put(key, val)
            print "Success insert"

        elif clp.get_method() == 'upd':
            key, val = clp.upd_args()
            rowcount = client.update(key, val)
            print 'Updated rows: %d' % rowcount

        else:
            print 'Error method!: ', clp.get_method()

    except Exception as e:
        print e

