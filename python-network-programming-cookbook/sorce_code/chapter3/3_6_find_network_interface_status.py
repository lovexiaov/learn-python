#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 3
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import argparse
import socket
import struct
import fcntl
import nmap


SAMPLE_PORTS = '21-23'


def get_interface_status(ifname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = socket.inet_ntoa(fcntl.ioctl(
        sock.fileno(),
        0x8915, #SIOCGIFADDR, C socket library sockios.h
        struct.pack('256s', ifname[:15])
    )[20:24])
    nm = nmap.PortScanner()         
    nm.scan(ip_address, SAMPLE_PORTS)      
    return nm[ip_address].state()          

    
if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python networking utils')
    parser.add_argument('--ifname', action="store", dest="ifname", required=True)
    given_args = parser.parse_args() 
    ifname = given_args.ifname    
    print "Interface [%s] is: %s" %(ifname, get_interface_status(ifname))       

