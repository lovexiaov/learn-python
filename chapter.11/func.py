__author__ = 'weixy6'


def foo():
    return 'abc', ['x', 'y'], True  # ('abc', ['x', 'y'], True)

# bellow three ways is equivalent
x, y, z = foo()
aTuple = foo()
(a, b, c) = foo()

def net_conn(host, port):
    pass
# two way of calling function
net_conn('lovexiaov.io', 8080)
net_conn(port=8080, host='lovexiaov.io')
