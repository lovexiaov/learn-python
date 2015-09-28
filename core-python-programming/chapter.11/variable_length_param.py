__author__ = 'weixy6'


def tupleArgs(arg1, arg2='Arg2', *theRest):
    """
    Non_keyword params
    :param arg1:
    :param arg2:
    :param theRest:
    :return:
    """
    print 'first arg is: ', arg1
    print 'second arg is: ', arg2
    for t in theRest:
        print 'another arg: ', t
    print '-' * 20


if __name__ == '__main__':
    tupleArgs('arg1')
    tupleArgs('arg1', 'arg2')
    tupleArgs('arg1', 'arg2', 'arg3', 'arg4')
