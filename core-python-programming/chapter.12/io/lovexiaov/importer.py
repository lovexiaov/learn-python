from importee import foo
# from .importee import foo  # if import this way, this module can not be run directly
import importee

__author__ = 'weixy6'


def foo():
    print 'foo() in importer'


foo()
importee.foo()
