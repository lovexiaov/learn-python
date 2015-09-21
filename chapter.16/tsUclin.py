# --coding: utf-8 --
from socket import *

__author__ = 'lovexiaov'

HOST = 'localhost'
PORT = 23456
BUFSIZE = 1024

ADDRESS = (HOST, PORT)

udpClientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('>')

    if not data:
        break
    udpClientSocket.sendto(data, ADDRESS)
    data, address = udpClientSocket.recvfrom(BUFSIZE)
    if not data:
        break
    print data

udpClientSocket.close()
