#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 3
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.
#IPv6  test in Unix  commandline: $cat /proc/net/if_inet6


import socket
import argparse
import netifaces as ni


def inspect_ipv6_support():
    """ Find the ipv6 address"""
    print "IPV6 support built into Python: %s" %socket.has_ipv6
    ipv6_addr = {}
    for interface in ni.interfaces():
        all_addresses = ni.ifaddresses(interface)
        print "Interface %s:" %interface
        for family,addrs in all_addresses.iteritems():
            fam_name = ni.address_families[family]
            print '  Address family: %s' % fam_name
            for addr in addrs:
                if fam_name == 'AF_INET6':
                    ipv6_addr[interface] = addr['addr']
                print     '    Address  : %s' % addr['addr']
                nmask = addr.get('netmask', None)
                if nmask:
                    print '    Netmask  : %s' % nmask
                bcast = addr.get('broadcast', None)
                if bcast:
                    print '    Broadcast: %s' % bcast
    if ipv6_addr:
        print "Found IPv6 address: %s" %ipv6_addr
    else:
        print "No IPv6 interface found!"  

    # 

if __name__ == '__main__':
    inspect_ipv6_support()