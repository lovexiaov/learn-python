"""
    sequence contains list, string, tuple.
    all sequence can use '+' to mosaic two or more together.
    all sequence can use '*' to copy itself N times.
    all sequence can use slice operator ([],[:],[::]).
    if mosaic normal string with unicode string, system will convert normal string to unicode string first.
    use '%' format string output.
    use 'u/U' before a string will convert a string to a unicode string.
    use 'r/R' before a string, the content will show us directly.
    use BIF cmp() can compare two sequence.
    string is a unchangeable type.
    tuple is a unchangeable type too.
    multi object, separate with comma, but no explicit symbol definition, its default type is tuple.
    because unchangeable feature, tuple can be used to store dict's keys
"""

import string
from string import Template

__author__ = 'weixy6'

t = (1, 2, 3, 4, 5)
l = [6, 7, 8, 9, 0]
s = '13579'
print 9 in t, 6 in l, '7' in s

print t + t
print l + l
print s + s
print s[:2] + s[3:]
# print t + l  # TypeError: can only concatenate tuple (not "list") to tuple

print t * 3

print t[2]
print t[1:2]
print t[0:4:2]
print t[::2]

s = 'abcdef'
for i in [None] + range(-1, -len(s), -1):
    print s[:i],
print

# build in functions
print list(t)
print tuple(s)
print str(l)
print unicode(t)

print enumerate(s).next()
print len(t)
print max(l)
print min(t)
print reversed(s).next()
print sorted(s, reverse=True)
# print sum(s)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print sum(l)

print '-' * 20

# string mosaic
s1 = 'love' + ' ' + 'python'
s2 = ''.join(('love', u' ', 'python'))
s3 = '%s %s' % ('love', 'python')
s4 = 'love' ' ' 'python'
print s1
print s2
print s3
print s4

print ('%s%s' % (s1[:3], s1[7])).upper()

print '-' * 20

print '%f' % 1234.567890
print '%.2f' % 1234.567890
print '%x' % 108
print '%#x' % 108
print '%o' % 108
print '%#o' % 108
print '%E' % 108
print '%.2E' % 108
print '%.2f%%' % 1234.567890
print '%+d' % 4
print 'MM/DD/YY = %02d/%02d/%02d' % (2, 15, 19)
print 'There are %(howmany)d %(lang)s Quotation Symbols.' % {'lang': 'Python', 'howmany': 3}

# use Template to format string easily
s = Template('There are ${howmany} ${lang} Quotation Symbols.')

print s.substitute(lang='Python', howmany=3)
# print s.substitute(lang='Python')  # KeyError: 'howmany'
print s.safe_substitute(lang='Python')

print '-' * 20

print '\n'  # it will output
print r'\n'

print ur'Hello World!'

print '-' * 20

# use cmp() len() max() min() enumerate() zip
str1 = 'abc'
str2 = 'asd'
li1 = ['a', 'b', 'c']
li2 = [1, 2, 3]

print cmp(str1, str2)
print cmp(li1, li2)
print len(str1)
print max(str2)
print min(li2)

print '-' * 20

foobar = 'foobar'
for i, t in enumerate(foobar):
    print i, t

print '-' * 20

s, t = '123', 'abcd'
print zip(s, t)  # [('1', 'a'), ('2', 'b'), ('3', 'c')]

print '-' * 20

question = 'what is your favorite color?'
print question.title()
print question.center(40)
print question.upper()
print len(question)
print len(question.center(40))
print question.endswith('color?')
print question.find('or', 22)  # start from index 22
print question.index('or', 22)

str = 'abc'
print id(str)
str += 'asd'
print id(str)

# str[2] = 'C'  # TypeError: 'str' object does not support item assignment

print ord('a')  # ordinal

print '-' * 20
# list
list1 = [i * 2 for i in [8, -2, 5]]
list2 = [i for i in range(8) if i % 2 == 0]
print list1
print list2

list1.extend(enumerate(list2))
print list1

# default type is tuple
s = 1, 2, 3, 'a'
print type(s)

print 4, 2 < 3, 5  # (4, True, 5)
print (4, 2) < (3, 5)  # False

# tuple with only one element
print type((1))  # int
print type((1,))  # tuple
