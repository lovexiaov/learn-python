# -*- coding: utf-8 -*-
import hashlib



start_id = 10000000001
number = 2000

csvfile = file('data.csv', 'w')


for i in range(number):
    md5 = hashlib.md5()
    md5.update(str(start_id))
    csvfile.write(str(start_id)+","+md5.hexdigest()+'\n')
    start_id += 1
    print i,":", md5.hexdigest()

