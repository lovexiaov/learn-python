# -*- coding: utf-8 -*-

import xml.dom.minidom as dom_parser
import json

result = file('wtf.csv', 'w')
dom = dom_parser.parse('result.xml')
# 文档节点
root = dom.documentElement
print root.nodeName
# 根节点
root = dom.firstChild
print root.nodeName
print '-' * 20
# 第一子节点
for child in root.childNodes:
    # 第二子节点
    for data in child.childNodes:
        if data.nodeName == 'responseData':
            # 子节点中的数据
            json_data = data.firstChild.data
            # 将子节点数据转化为dict对象
            dd = json.loads(json_data)
            # if dd.has_key('gadget_key'):
            if 'gadget_key' in dd:
                result.write(dd['gadget_key'] + ',')

        if data.nodeName == 'queryString':
            json_data = data.firstChild.data
            dd = json.loads(json_data)
            if dd.has_key('gadget_mac'):
                result.write(dd['gadget_mac'] + '\n')
