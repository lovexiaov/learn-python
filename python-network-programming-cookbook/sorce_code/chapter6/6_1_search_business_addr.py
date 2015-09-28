#!/usr/bin/env python

# Python Network Programming Cookbook -- Chapter - 6
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

from pygeocoder import Geocoder

def search_business(business_name):

    results = Geocoder.geocode(business_name)
    
    for result in results:
        print result

if __name__ == '__main__':
    business_name =  "Argos Ltd, London" 
    print "Searching %s" %business_name
    search_business(business_name)  
