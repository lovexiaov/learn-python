# --coding: utf-8 --
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

__author__ = 'lovexiaov'

HOST = ''
PORT = 34568
ADDRESS = (HOST, PORT)


class MyRequestHeader(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))


tcpServer = TCP(ADDRESS, MyRequestHeader)

print 'waiting for connection...'
tcpServer.serve_forever()
