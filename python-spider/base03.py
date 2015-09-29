# -*-coding: utf-8 -*-
"""
urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            cafile=None, capath=None, cadefault=False, context=None)
前三个参数分别代表了：网页地址，访问url需要传入的数据，连接超时时间。
返回一个response对象，通过该对象的read方法打印获取到的内容。

urlopen方法还可以传入一个Request对象，和上面的效果上样
"""
import urllib2
import urllib

__author__ = 'weixy6'

# way 1
response1 = urllib2.urlopen('http://www.baidu.com')

# way 2(recommend)
request2 = urllib2.Request('http://www.baidu.com')
response2 = urllib2.urlopen(request2)

# login csdn(use post)
values = {'username': 'wxynetwork', 'password': 'xxxxx'}
data = urllib.urlencode(values)
# %3A(:) %2F(/)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request3 = urllib2.Request(url, data)
response3 = urllib2.urlopen(request3)

# login csdn(use get)
url2 = 'https://passport.csdn.net/account/login'
geturl = url2 + '?' + data
request4 = urllib2.Request(geturl)
response4 = urllib2.urlopen(request4)

if __name__ == '__main__':
    # print response1.read()
    # print response2.read()
    # print response3.read()
    print response4.read()
