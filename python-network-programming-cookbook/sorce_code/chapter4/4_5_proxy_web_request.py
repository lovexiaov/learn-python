#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import urllib

URL = 'https://www.github.com'
PROXY_ADDRESS = "165.24.10.8:8080" # By Googling free proxy server


if __name__ == '__main__':
    resp = urllib.urlopen(URL, proxies = {"http" : PROXY_ADDRESS})
    print "Proxy server returns response headers: %s " %resp.headers

