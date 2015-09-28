__author__ = 'weixy6'

# define a function
def fun1(arg1, arg2):
    "this is a test function"
    # function suite
    print "print args:", arg1, arg2

# invoke a function
fun1('hello', 'world')

print '-' * 20

# default arguments
def fun2(debug=True):
    'determine if in debug mode with default argument'
    if debug:
        print 'in debug mod'
    print 'done'
# fun2()
fun2(False)



