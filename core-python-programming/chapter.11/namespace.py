__author__ = 'weixy6'


def foo():
    """balabala..."""
    pass


def bar():
    pass


bar.__doc__ = 'Oops, forgot write document for bar()'
bar.version = 0.1

if __name__ == '__main__':
    help(bar)
    print bar.version
    print foo.__doc__
