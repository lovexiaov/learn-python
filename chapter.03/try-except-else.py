# --coding: utf-8 --
"""demo for try-except-else grammar"""
__author__ = 'lovexiaov'

try:
    pyFile = file('makeTextFile.py', 'r')

except IOError, e:
    print 'there is an error:', e
else:
    for eachLine in pyFile:
        print eachLine,
    pyFile.close()







