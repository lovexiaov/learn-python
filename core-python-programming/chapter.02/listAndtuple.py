# --coding: utf-8 --
__author__ = 'lovexiaov'

# list, value can be modified, length can be changed
aList = [1, 2, 3, 4]
aList[0] = 7
aList.insert(2, 5)
aList.append(6)

print aList
print aList[2]
print aList[-1]
print aList[:2]
print aList[2:]
print aList[2:2]

print '-' * 20

# tuple, value can *not* be modified, length can *not* be changed
aTuple = ('A', 'B', 'C', 'D', 1, 3)

# aTuple[1] = 'E' # TypeError: 'tuple' object does not support item assignment

print aTuple
print aTuple[2]
print aTuple[-1]
print aTuple[:2]
print aTuple[2:]
print aTuple[2:2]

