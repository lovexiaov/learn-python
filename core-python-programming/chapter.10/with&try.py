# --coding: utf-8 --

__author__ = 'lovexiaov'


with file('test.tmp', 'r') as f:
    for eachLine in f:
        print eachLine,


try:
    f = file('test2.tmp', 'r')
    for eachLine in f:
        print eachLine,
    f.close()
except IOError:
    print 'open file error'