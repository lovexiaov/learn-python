# --coding: utf-8--
"""
    this module aimed to learn how to use file related function
"""
__author__ = 'lovexiaov'

f = file('test.tmp', 'r')

for eachLine in f:
    print eachLine,
print f.tell()
f.seek(-59, 1)
print f.readline(),
print f.name
f.close()

