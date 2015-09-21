# --coding: utf-8 --
from socket import *
from time import ctime

__author__ = 'lovexiaov'

HOST = ''
PORT = \
    23456
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpServerSocket = socket(AF_INET, SOCK_DGRAM)
udpServerSocket.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpServerSocket.recvfrom(BUFSIZE)
    udpServerSocket.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from and returned to:', addr

udpServerSocket.close()
