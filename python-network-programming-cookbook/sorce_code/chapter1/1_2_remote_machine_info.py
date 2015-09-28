#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 1
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.


import socket

def get_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print "IP address of %s: %s" %(remote_host, socket.gethostbyname(remote_host))
    except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)
    
if __name__ == '__main__':
    get_remote_machine_info()
