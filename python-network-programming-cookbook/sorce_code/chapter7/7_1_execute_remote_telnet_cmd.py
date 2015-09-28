#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 7
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import getpass
import sys
import telnetlib

HOST = "localhost"

def run_telnet_session():
    user = raw_input("Enter your remote account: ")
    password = getpass.getpass()
    
    session = telnetlib.Telnet(HOST)
    
    session.read_until("login: ")
    session.write(user + "\n")
    if password:
        session.read_until("Password: ")
        session.write(password + "\n")
    
    session.write("ls\n")
    session.write("exit\n")
    
    print session.read_all()

if __name__ == '__main__':
    run_telnet_session()

