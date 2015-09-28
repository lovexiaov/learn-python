#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 6
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import argparse
import os
import urllib

ERROR_STRING = '<error>'

def find_lat_long(city):
        """ Find geographic coordinates """
        # Encode query string into Google maps URL
        url = 'http://maps.google.com/?q=' + urllib.quote(city) + '&output=js'
        print 'Query: %s' % (url)
    
        # Get XML location from Google maps
        xml = urllib.urlopen(url).read()
    
        if ERROR_STRING in xml:
            print '\nGoogle cannot interpret the city.'
            return
        else:
            # Strip lat/long coordinates from XML
            lat,lng = 0.0,0.0
            center = xml[xml.find('{center')+10:xml.find('}',xml.find('{center'))]
            center = center.replace('lat:','').replace('lng:','')
            lat,lng = center.split(',')
            print "Latitude/Longitude: %s/%s\n" %(lat, lng)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='City Geocode Search')
    parser.add_argument('--city', action="store", dest="city", required=True)
    given_args = parser.parse_args() 
    
    print "Finding geographic coordinates of %s" %given_args.city
    find_lat_long(given_args.city)



