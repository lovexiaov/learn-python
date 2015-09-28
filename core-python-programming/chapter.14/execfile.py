__author__ = 'weixy6'

execfile('hello.py')
# below code is equal with above
f = file('hello.py', 'r')
exec f
f.close()
