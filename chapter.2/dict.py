# --coding: utf-8 --
__author__ = 'lovexiaov'

aDict = {'name': 'lovexiaov'}
aDict['name'] = 'zhangsan'
aDict['gentle'] = 'male'

print aDict
print aDict.keys()

for key in aDict:
    print key, ':', aDict[key]

