# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import bs4
import re


def printLine():
    print '-' * 20


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
# print soup.prettify()
print soup.title
print soup.head
print soup.a
print soup.p

print type(soup.a)

printLine()

print soup.name
print soup.head.name
print soup.p.attrs
print soup.p['class']
soup.p['class'] = 'newClass'
print soup.p
print soup.p.string

printLine()

print soup.a
if type(soup.a.string) != bs4.element.Comment:
    print soup.a.string
print type(soup.a.string)

printLine()

print soup.head.contents
print soup.head.contents[0]

for child in soup.body.children:
    print child

printLine()

for child in soup.descendants:
    print child

printLine()

for string in soup.strings:
    print (repr(string))

printLine()

for string in soup.stripped_strings:  # 去除空行
    print (repr(string))

printLine()

p = soup.p
print p.parent.name

content = soup.head.title.string
print content.parent.name

printLine()

for parent in content.parents:
    print parent.name

printLine()

print soup.p.next_sibling
print soup.p.prev_sibling
print soup.p.next_sibling.next_sibling

printLine()

for sibling in soup.a.next_siblings:
    print repr(sibling)

printLine()

print soup.head.next_element
for element in soup.a.next_elements:
    print repr(element)

printLine()
print soup.find_all('b')[0]

print soup.find_all('a')

printLine()

for tag in soup.find_all(re.compile('^b')):
    print tag.name

printLine()

print soup.find_all(['a', 'b'])
printLine()
for tag in soup.find_all(True):
    print tag.name

printLine()


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


print soup.find_all(has_class_but_no_id)

printLine()
print soup.find_all(id='link2')
print soup.find_all(href=re.compile('elsie'))
print soup.find_all(href=re.compile('elsie'), id='link1')
print soup.find_all('a', class_='sister')

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
print data_soup.find_all(attrs={'data-foo': 'value'})

printLine()

print soup.find_all(text='Elsie')
print soup.find_all(text=['Tillie', 'Elsie', 'Lacie'])
print soup.find_all(text=re.compile('Dormouse'))

printLine()

print soup.find_all('a', limit=2)

printLine()

print soup.html.find_all('title')
print soup.html.find_all('title', recursive=False)

printLine()

# 通过标签查找
print soup.select('title')
# 通过类名查找
print soup.select('.sister')
# 通过id查找
print soup.select('#link1')
# 组合查找
print soup.select('p #link1')
# 通过子标签查找('>'前后必须有空格)
print soup.select('head > title')
# 属性查找
print soup.select('a[class="sister"]')
print soup.select('p a[href="http://example.com/elsie"]')
