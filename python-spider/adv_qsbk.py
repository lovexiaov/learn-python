# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import thread
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = 'http://qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read()  # .decode('utf-8')
            return pageCode
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print u'connect failed, error msg:', e.reason
                return None

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)

        if not pageCode:
            print 'loading page failed...'
            return None
        pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?content">(.*?)' +
                             '<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            haveImg = re.search('img', item[3])
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR, '\n', item[1])
                replaceQuot = re.compile('&quot;')
                text = re.sub(replaceQuot, '"', text)
                pageStories.append([item[0].strip(), text.strip(), item[2].strip(), item[4].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            x = time.localtime(int(story[2]))
            localTime = time.strftime('%Y-%m-%d %H:%M:%S', x)
            print u'第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s' % (page, story[0], localTime, story[3], story[1])

    def start(self):
        print u'reading... press ENTER to browser, and Q to quit'
        self.enable = True
        self.loadPage()
        currentPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                currentPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, currentPage)


if __name__ == '__main__':
    spider = QSBK()
    spider.start()
