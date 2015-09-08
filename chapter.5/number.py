from __future__ import division
from decimal import Decimal
import random

__author__ = 'weixy6'

anInt = 3
del anInt
# print anInt  # NameError: name 'anInt' is not defined

# complex
c = 1.5 + 1.5j
print c.real
print c.imag
print c.conjugate()

print 5

# in the future there will be two way of division
print 1 / 2  # real division
print 1 // 2  # floor division

print '---------' * 5

# Conversion factory function
print int(4.6)
print long(4)
print float(4)
print complex(4.6)
print bool(1)

print '---------' * 5

# function method
print abs(-1), abs(1)
print coerce(1, 2), coerce(1, 2L), coerce(1.3, 134L)

# divmod() return a tuple contains result and remainder
print divmod(5, 2), divmod(10, 2.5)

# round() realize four homes five function
print round(3), round(3.499999), round(3.4999, 1)

# pow() is seem as '**'
print pow(2, 5), pow(2, 5, 3)

print '---------' * 5

# Hex Conversion
print hex(255), oct(255)

print '---------' * 5

# ascii conversion
print ord('a'), ord('A')
print chr(97), chr(65)
print unichr(97)

print '---------' * 5

t = (1,)
print t

print '---------' * 5


class C: pass


c = C()
print bool(c)


class CC:
    def __nonzero__(self):
        return False


cc = CC()
print bool(cc)

print '---------' * 5

dec = Decimal(.1)
print dec
print dec + Decimal('1.0')

print '---------' * 5

print range(1, 5, 1)




