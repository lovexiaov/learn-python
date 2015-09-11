"""
    mapping is a disorder type
"""

__author__ = 'weixy6'

def dividingLine():
    print '-' * 20


dict1 = {}
dict2 = {'name': 'zhangsan', 'age': 28}
# use factory method to create dict(after python 2.2)
fdict = dict((['x', 1], ['y', 2]))
# use BIF to create dict which contains the same value, default value is None
ddict = {}.fromkeys(('x', 'y'), -1)
ddict2 = {}.fromkeys(('x', 'y'))

print dict1, dict2, fdict, ddict, ddict2

for key in dict2.keys():
# after python 2.2, you can do it this way
# for key in dict2:
    print dict2.get(key), # dict2[key]
print

# add element
dict1[1] = 'hello'
dict1[2] = 'world'
dict1[3] = '!'
print dict1

dividingLine()

# update element
dict1[2] = 'python'
print dict1

dividingLine()

# delete element or dict
del dict1[1]
dict1.pop(2)
print dict1
dict1.clear()
print dict1
del dict1

dividingLine()

# factory function dict()
print dict(zip(('x', 'y'),(1, 2)))
print dict([['x', 'y'], [1, 2]])
print dict([('xy'[i-1], i) for i in range(1, 3)])

dividingLine()




