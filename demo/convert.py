import re

__author__ = 'weixy6'

while True:
    filename = raw_input('please input source file name:')
    if filename.strip():
        break
    else:
        print 'file name can not be null'
try:
    newName = filename.split('.')[0]+'.csv'
    data = file(filename, 'r')
    ndata = file(newName, 'w')
    ndata.write('device_ID,time,current_data,upload_data\n')
    for eachLine in data:
        if eachLine.strip():
            if eachLine.startswith('[device_ID]') or eachLine.startswith('[device_type]'):
                continue
            pattern = re.compile(r' \d+\.\d+')
            matcher = pattern.search(eachLine)
            newLine = re.sub(pattern, ',' + matcher.group().strip(), eachLine, 1)
            matcher = pattern.search(newLine)
            newLine = re.sub(pattern, ',' + matcher.group().strip(), newLine, 1)
            ndata.write(newLine.replace(' ', ',', 1))
    ndata.close()

    print """data convert success!!!
    new file name is '%s'""" % newName
except IOError:
    print 'file open failed'
