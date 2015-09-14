__author__ = 'weixy6'
#===std type===
# Number(Integer, Boolean, Long Integer, Floating point real number, complex number)
# String
# List
# Tuple
# Dictionary

#===other type===
# Type
print type(26)
print type(type(26))
# None #Object Null, similar with void in C language
if None:
    print 'None is true'
else:
    print 'None is false'
print type(None)

print '------' * 5

# reduce query times than directly "import types"
from types import IntType, LongType, FloatType, BooleanType, ComplexType


def displayNumberType(num):
    print num, 'is',
    # if type(num) is IntType:
    #     print 'an Integer'
    # elif type(num) is LongType:
    #     print 'a Long'
    # elif type(num) == FloatType:
    #     print 'a Float'
    # elif type(num) == BooleanType:
    #     print 'a Boolean'
    # elif type(num) == ComplexType:
    #     print 'a complex'

    # can use a tuple as variable
    if isinstance(num,(int, long, float, bool, complex)):
        print 'a', type(num).__name__
    else:
        print 'not a number at all!!!'

displayNumberType(1)
displayNumberType(2L)
displayNumberType(True)
displayNumberType(1.5+1.5j)
displayNumberType('xxx')
displayNumberType(0.5)

# compare object value VS compare object id
# type(1) == type(2) # value compare
# type(1) is types.IntType # id compare


