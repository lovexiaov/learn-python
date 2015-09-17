__author__ = 'weixy6'


def foo():
    def bar():  # embedded function
        print 'bar() called'

    print 'foo() called'
    bar()


if __name__ == '__main__':
    foo()
    # bar()  # NameError: name 'bar' is not defined