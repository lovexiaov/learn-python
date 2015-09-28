"""
    check is the id legal or not
"""
import string
__author__ = 'weixy6'

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Id Checker v1.0'
print 'Testees must be at least 2 chars long'
inp = raw_input('input word to test: >')
if len(inp) > 1:
    if inp[0] not in alphas:
        print 'invalid: first symbol must be alphabetic'
    else:
        for otherChar in inp[1:]:
            if otherChar not in alphas+nums:
                print 'invalid: remaining symbol must be alphanumberic'
                break
        else:
            print 'okay as identifier!'
else:
    print 'Error: your input length must > 2'


