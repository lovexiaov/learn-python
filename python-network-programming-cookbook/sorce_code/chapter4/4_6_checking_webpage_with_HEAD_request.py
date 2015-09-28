#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import argparse
import httplib
import urlparse
import re
import urllib

DEFAULT_URL = 'http://www.python.org'
HTTP_GOOD_CODES =  [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]

def get_server_status_code(url):
    """
    Download just the header of a URL and
    return the server's status code.
    """
    host, path = urlparse.urlparse(url)[1:3] 
    try:
        conn = httplib.HTTPConnection(host)
        conn.request('HEAD', path)
        return conn.getresponse().status
    except StandardError:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example HEAD Request')
    parser.add_argument('--url', action="store", dest="url", default=DEFAULT_URL)
    given_args = parser.parse_args() 
    url = given_args.url
    if get_server_status_code(url) in HTTP_GOOD_CODES:
        print "Server: %s status is OK: " %url
    else:
        print "Server: %s status is NOT OK!" %url


'''
python 4_6_checking_webpage_with_HEAD_request.py 
Server: http://www.python.org status is OK!


$ python 4_6_checking_webpage_with_HEAD_request.py --url=http://www.pytho.org
Server: http://www.pytho.org status is NOT OK!
'''
