__author__ = 'weixy6'

CODEC = 'utf-8'
FILE = 'unicode.tmp'

output_str = u'Hello World!\n'
output_byte = output_str.encode(CODEC)

f = file(FILE, 'w')
f.write(output_byte)
f.close()

print '-' * 20

f = file(FILE, 'r')
input_byte = f.read()
f.close()

input_str = input_byte.decode(CODEC)
print input_str
