# --coding: utf-8 --
"""
this program should run in the command line, like this:
python argv.py sdfa aer 'ooo ooo'                                                                                             master  ✭
you entered 4 arguments
they were:  ['argv.py', 'sdfa', 'aer', 'ooo ooo']
"""
import sys
__author__ = 'lovexiaov'

print 'you entered', len(sys.argv), 'arguments'
print 'they were: ', str(sys.argv)
