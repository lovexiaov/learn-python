# -*- coding: utf-8 -*-
"""
Opener:
我们需要用一个Opener(urllib2.OpenerDirector的实例)来打开url,urlopen是一个特殊的实例。

Cookielib：此模块的主要作用是提供可存储cookie的对象。

"""

import urllib2
import cookielib


def getCookies():
    # 声明一个CookieJar对象实例用来保存cookie
    cookie = cookielib.CookieJar()
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value
        print '-' * 20


def saveCookies():
    # 设置保存cookie的文件名
    filename = 'cookie.tmp'
    # 声明一个MozillaCookieJar对象实例来保存cookie, 之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    # ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    # getCookies()
    saveCookies()
