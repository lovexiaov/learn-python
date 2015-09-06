# --coding: utf-8 --
__author__ = 'lovexiaov'

nameList = ['zhangsan', 'lisi', 'wangwu', 'maliu']
for name in nameList:
    print "the current name is: %s" % name

print '-' * 20
# add a comma on the end of print sentence, it will not wrap a new line
for name in nameList:
    print name,
print

print '=' * 20

# range() function
for eachNum in range(0, 3, 1): # range(0, 3, 1) equal with range(3)
    print eachNum,
print

print '=' * 20

# enumberate() function
foo = 'abc'

for x in range(len(foo)):
    print x, foo[x]

print '=' * 20

for i, ch in enumerate(foo):
    print i, ch




