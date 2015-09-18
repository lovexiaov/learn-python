__author__ = 'weixy6'


class Person(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __del__(self):
        print "Persion's __del__()"

    def updatePhone(self, phone):
        self.phone = phone


p1 = Person('jane', '777-262-555')
print p1.name
print p1.phone
p1.updatePhone('444-444-444')
print p1.phone

print '-' * 20


class Joe(Person):
    def __init__(self, name, phone, email, address):
        Person.__init__(self, name, phone)
        self.email = email
        self.address = address


joe = Joe('joe', '442-256-734', 'joe@gmail.com', 'sanfransisco')
print joe.name
print joe.phone
print joe.email
print joe.address

print joe is Joe
print joe is Person
print isinstance(joe, Joe)
print isinstance(joe, Person)

print '-' * 20


class Jane(Person):
    def __init__(self):
        print 'initialized'

    def __del__(self):
        Person.__del__(self)
        print 'deleted'


jane = Jane()
jane2 = jane
jane3 = jane

print id(jane), id(jane2), id(jane3)
del jane
del jane2
del jane3  # delete the last object will invoke __del__()

print dir(joe)
print joe.__dict__
# print joe.__mro__  # AttributeError: 'Joe' object has no attribute '__mro__'

print '-' * 20


class Test(object):
    def __init__(self):
        pass

    @staticmethod
    def foo():
        pass

    @classmethod
    def bar(cls):
        print cls.__name__
