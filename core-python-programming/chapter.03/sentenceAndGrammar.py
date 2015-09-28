__author__ = 'weixy6'

# use '\' to split a sentence to multi lines
name = 'zhangsan'
if name == 'zhangsan' or \
                name == 'lisi':
    print name
# you also can use the bracket to do this
if (name == 'zhangsan' or
            name == 'lisi'):
    print name

# use semicolon to let multi sentence in one line
print 'line1'
print 'line2'

# mul-tuple assignment
(x, y, z) = (1, 2, 'a string')
print x, y, z

print '-' * 20
# exchange tow values
x, y = y, x
print x, y
