__author__ = 'weixy6'

def getNumbers():
    "get 5 numbers and return by list"
    counter = 0
    nums = list()
    while counter < 5:
        hint = 'please input the %d number:' % (counter+1)
        num = raw_input(hint)
        nums.append(int(num))
        counter += 1
    return nums

choice = raw_input('''please have a choice input:
 (1) get a sum of 5 numbers
 (2) get the mean value of 5 numbers
 (x) exit this program\n''')
if choice=='1':
    result = 0
    nums = getNumbers()
    for num in nums:
        result = result + num
    print 'the result is: %d' % result

elif choice=='2':
    result = 1
    nums = getNumbers()
    for num in nums:
        result = result * num
    print 'the result is: %d' % result

elif choice=='x' or choice=='X':
    exit('this program is exited')

