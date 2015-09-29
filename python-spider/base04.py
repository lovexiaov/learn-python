# -*- coding: utf-8 -*-
"""
设置网络请求的Headers
在Headers中设置‘Referer’属性可以应对“反盗链”机制

另外Headers的一些属性，下面的需要特别注意一下：
User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
application/json ： 在 JSON RPC 调用时使用
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
"""
import urllib2
import urllib


def login_zhihu():
    try:
        url = 'http://www.zhihu.com/#signin'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {'username': 'cantywei@qq.com', 'password': 'xxxxx'}
        headers = {'User-Agent': user_agent, 'Referer': 'http://www.zhihu.com/',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        print response.read()
    except urllib2.HTTPError, e:
        print 'you have an error:', e


# 开启DebugLog
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')



if __name__ == '__main__':
    login_zhihu()
