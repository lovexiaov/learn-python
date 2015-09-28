"""
    set and frozenset
"""
__author__ = 'weixy6'


def dividingline():
    print '-' * 20


s = set('cheeseshop')
f = frozenset('bookshop')
u = frozenset(s)
print s
print f
print type(s)
print type(f)

dividingline()

print len(s) == len(f)
print s == f
print s == u
print set('posh') == set('shop')

dividingline()

print s & f  # set type
print s | f
print s - f
print s ^ f
# print s + s  # unsupported operator

dividingline()

print f & s  # frozenset type
print f | s

dividingline()

for i in s:
    print i,
print

dividingline()

v = s | f
print s < v
dividingline()

# update set
s |= set('abcd')
s.update('wxy')
print s

s &= set('shop')
print s

dividingline()
# BIF
print s.issubset(f)
print s.issuperset(f)
print s.union(f)
print s.intersection(f)
print s.difference(f)
print s.symmetric_difference(f)
print s.copy()

