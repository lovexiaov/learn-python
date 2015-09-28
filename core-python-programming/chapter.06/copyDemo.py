"""
    Shallow copy, unchangeable type(string, tuple) will be explict copied, and create a new object.
    Deep copy, copy.deepcopy()
"""
__author__ = 'weixy6'

# shallow copy
person = ['name', ['saving', 100.00]]
husband = person[:]
wife = list(person)
print [id(x) for x in husband]
print [id(x) for x in wife]

print '--------after change name----'
husband[0] = 'joe'
wife[0] = 'jane'
print [id(x) for x in husband]
print [id(x) for x in wife]

print husband, wife  # husband's name unaffected by wife

print '--------after change money----'

husband[1][1] = 50.00
wife[1][1] = 150.00
print [id(x) for x in husband]
print [id(x) for x in wife]

print husband, wife  # list is a changeable type, change one's list will affect others

print '-----deep copy-----'

#deep copy
import copy
person = ['name', ['saving', 100.00]]
husband = person
wife = copy.deepcopy(person)

husband[0] = 'joe'
wife[0] = 'jane'

print husband, wife

husband[1][1] = 50.00
wife[1][1] = 150.00

print husband, wife

