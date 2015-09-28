# --encoding: utf-8 --

# 1. normal arithmetic operator: +, -, *, /, %
addition = 3 + 5
subtraction = 3 - 5
multiplication = 3 * 5
# four home five
division = 3 / 5

remainder = 3 % 5

print '3 + 5 = ', addition
print '3 - 5 = ', subtraction
print '3 * 5 = ', multiplication
print '3 / 5 = ', division
print '3 % 5 = ', remainder

# 2. special arithmetic operator: //, **
# "//" will abandon the number after dot
sDivision = '14 // 3 = %d' % (14 // 3)
# "**" involution multiplication
sMultiplication = '3 ** 2 = %d' % (3 ** 2)

print sDivision
print sMultiplication

# comparison operator: >, >=, <, <= == != <>
print '3 > 5: ', 3 > 5
print '3 >= 5: ', 3 >= 5
print '3 < 5: ', 3 < 5
print '3 <= 5: ', 3 <= 5
print '3 == 5: ', 3 == 5
print '3 != 5: ', 3 != 5
# '<>' is deprecated, equal with '!='
print '3 <> 5: ', 3 <> 5
# especial
print '3 < 4 < 5: ', 3 < 4 < 5

# logical operator: and or not
logical1 = 'True and False is: %s' % (True and False)
logical2 = 'True or False is: %s' % (True or False)
logical3 = 'not False is: %s' % (not False)

print logical1
print logical2
print logical3


