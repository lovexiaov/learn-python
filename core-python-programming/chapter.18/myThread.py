import threading
from time import ctime

__author__ = 'weixy6'


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.result

    def run(self):
        print 'starting', self.name, 'at:', ctime()
        # apply(self.func, self.args)
        self.result = self.func(*self.args)
        print self.name, 'finished at:', ctime()
