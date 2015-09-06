# --coding: utf-8 --
"""makeTextFile.py -- create text file"""

__author__ = 'lovexiaov'

import os
ls = os.linesep
# get filename
fname = ''
while True:
    fname = raw_input('input file name:')
    if os.path.exists(fname):
        print 'ERROR: %s is already exists' % fname
    else:
        break

# get file content(text) line
all = []
print '\nEntenr lines("." by itself to quit)\n'

# loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

# write line to file with proper line-ending
fobj = file(fname, 'w')
fobj.writelines(('%s%s' % (x, ls) for x in all))
fobj.close()
print 'DONE!'


