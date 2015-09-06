# --encoding: utf-8--
__author__ = 'weixy6'

# mode: 'r'=read, 'w'=write, 'a'=add, '+'=read&write, 'b'=binary, default is 'r'
# file1 = open('file.tmp', mode='r')
file1 = file('file2.tmp', mode='r') #open() is equal with file()
try:
    for eachLine in file1:
        print eachLine,
    file1.close()
except IOError, e:
    print 'file open error:', e

