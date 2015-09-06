# --coding: utf-8 --
__author__ = 'lovexiaov'

sName = raw_input("please input your age:")
name = int(sName)
if 0 < name < 18:
    print "you are a teenager."
elif name < 40:
    print "you are a man."
else:
    print "you are a old fool."


