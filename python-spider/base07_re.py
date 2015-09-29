# -*- coding: utf-8 -*-
"""
在正则表达式中表示一个'\'，要用'\\\\'来表示，前两个和后两个分别被转义为一个'\',最后这转化为正则中的'\'
1) re.match(pattern, string[, flags])
2) re.search(pattern, string[, flags])
3) re.split(pattern, string[, maxsplit])
4) re.findall(pattern, string[, flags])
5) re.finditer(pattern, string[, flags])
6) re.sub(pattern, repl, string[, count])

"""
import re


def testMatch():
    pattern = re.compile(r'hello')

    result1 = re.match(pattern, 'hello')
    result2 = re.search(pattern, 'thelloo lovexiaov!')
    result3 = re.match(pattern, 'helo lovexiaov!')
    result4 = re.match(pattern, 'hello lovexiaov')

    if result1:
        print '匹配的字符串', result1.string
        print '正则表达式对象', result1.re
        print '文本中正则表达式结束搜索的索引', result1.pos
        print '文本中正则表达式结束搜索的索引', result1.endpos
        print '最后一个被捕获的分组在文本中的索引', result1.lastindex
        print '最后一个被捕获的分组的别名', result1.lastgroup
        print '-' * 20
    else:
        print 'result1 匹配失败'

    if result2:
        print result2.group()
    else:
        print 'result2 匹配失败'

    if result3:
        print result3.group()
    else:
        print 'result3 匹配失败'

    if result4:
        print result4.group()
    else:
        print 'result4 匹配失败'


def testSub():
    pattern = re.compile(r'(\w+) (\w+)')
    text = 'i say, hello world!'
    print re.sub(pattern, r'\2 \1', text)
    print re.sub(pattern, r'hello', text)
    # below tow lines is the same
    print re.match(pattern,text).group()
    print pattern.match(text).group()

    def func(m):
        return m.group(1).title() + ' ' + m.group(2).title()

    print re.sub(pattern, func, text)


if __name__ == '__main__':
    # testMatch()
    testSub()
