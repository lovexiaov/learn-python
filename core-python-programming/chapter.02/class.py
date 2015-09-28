__author__ = 'weixy6'

class FooClass(object):
    '''this is a demo class'''
    version = 0.1 # static variable, all method can access

    def __init__(self, age, name='lovexiaov'):
        'constructor'
        self.name = name
        print 'create a class instance for', name

    def showName(self):
        'instance attribute and class name'
        print 'attribute:', self.name
        print 'class name:', self.__class__.__name__

# create a instance, need args to match __init__ method
foo = FooClass(25)
foo.showName()


