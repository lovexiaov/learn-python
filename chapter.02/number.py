# --coding: utf-8 --
__author__ = 'lovexiaov'

# int
inum1 = 89
inum2 = 0x89
inum3 = 0X89
inum4 = -89

print type(inum1)
print type(inum2)
print type(inum3)
print type(inum4)

# long
lnum1 = 89L
lnum2 = -89l
lnum3 = 0XABCL

print type(lnum1)
print type(lnum2)
print type(lnum3)

# float
fnum1 = 0.89
fnum2 = 8.9E-10
fnum3 = -89.
fnum4 = 8.9e10

print type(fnum1)
print type(fnum2)
print type(fnum3)
print type(fnum4)

# bool
bool1 = True
bool2 = False

print type(bool1)
print type(bool2)

# if participate in operation, True is 1, False is 0
print 89 + bool1
print 89 + bool2

# complex
cnum1 = 89 + 1.5j
cnum2 = -89 - 1.5J

print cnum1
print cnum2





