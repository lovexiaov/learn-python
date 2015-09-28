from random import randint

__author__ = 'weixy6'


def simpleGen():
    yield 1
    yield 2


def randGen(aList):
    while len(aList) > 0:
        index = randint(0, len(aList)-1)
        yield aList.pop(index)


def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1


if __name__ == '__main__':
    gen = simpleGen()
    print simpleGen().next()
    # print gen.next()
    # print gen.next()
    # print gen.next()

    for item in randGen(['jane', 'joe', 'lily', 'lucy']):
        print item

    count = counter(5)
    print count.next()
    print count.next()
    count.send(9)
    print count.next()
    print count.next()
    count.close()
    # count.next()  # StopIteration
