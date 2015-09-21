# --coding: utf-8 --
from socket import *

__author__ = 'lovexiaov'

HOST = ''
PORT = 34568
BUFFERSIZE = 1024

ADDRESS = (HOST, PORT)

while True:
    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    tcpClientSocket.connect(ADDRESS)
    data = raw_input('>')
    if not data:
        break
    tcpClientSocket.send('%s\r\n' % data)
    data = tcpClientSocket.recv(BUFFERSIZE)

    if not data:
        break
    print data.strip()
    tcpClientSocket.close()
