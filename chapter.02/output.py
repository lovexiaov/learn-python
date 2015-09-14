# -- encoding: utf-8 --
import sys
__author__ = 'lovexiaov'

# 1. Print only string
print "Hello world!"
print 'Hello world!'

name = "lovexiaov"
print 'your name is: ', name

# 2. Print string with params
print "%d, hello world, %s" % (222, "lovexiaov")

# 3. Redirect output with ">>"
print >> sys.stderr, 'Fatal error: invalid input!'

# 4. Redirect output to file with ">>"
logfile = open("logfile.tmp", "w")
print >> logfile, 'Fatal error: invalid input!'
logfile.close()


