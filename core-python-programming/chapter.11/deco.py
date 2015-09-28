from time import ctime, sleep

__author__ = 'weixy6'


def tsfunc(func):
    def wrappedfunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()

    return wrappedfunc


@tsfunc
def foo():
    pass


foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
