# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class QSBK:
    def __init__(self):
        self.page_index = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.joke_pages = []
        self.enable = False

    def get_page(self, page_index):
        """
        get page source code
        :param page_index: the page index
        :return: page content, or None, if there is something wrong
        """
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(page_index)
            print 'url:', url
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            page_content = response.read()  # .decode('utf-8')
            return page_content
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print u'connect failed, error msg:', e.reason
                return None

    def get_jokes(self, page_index):
        """
        get jokes in the page content
        :param page_index:
        :return: a list of jokes in appointed page, or None, if there is something wrong
        """
        page_content = self.get_page(page_index)

        if not page_content:
            print 'loading page failed...'
            return None
        pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?content">(.*?)' +
                             '<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, page_content)
        stories = []
        for item in items:
            haveImg = re.search('img', item[3])
            if not haveImg:
                replace_br = re.compile('<br/>')
                # text = re.sub(replace_br, '\n', item[1])
                text = replace_br.sub('\n', item[1])
                replace_quot = re.compile('&quot;')
                text = re.sub(replace_quot, '"', text)
                stories.append([item[0].strip(), text.strip(), item[2].strip(), item[4].strip()])
        return stories

    def load_pages(self):
        """
        load next page when current page in ending
        :return:
        """
        print '============loading pages...'
        if self.enable:
            if len(self.joke_pages) < 2:
                jokes = self.get_jokes(self.page_index)
                if jokes:
                    self.joke_pages.append(jokes)
                    self.page_index += 1

    def get_one_joke(self, jokes, page):
        """
        get a joke from joke list, and print it
        :param jokes:
        :param page:
        :return:
        """
        for joke in jokes:
            command = raw_input()
            # self.load_pages()
            if command == 'Q':
                self.enable = False
                return
            x = time.localtime(int(joke[2]))
            format_time = time.strftime('%Y-%m-%d %H:%M:%S', x)
            print '第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s' % (page, joke[0], format_time, joke[3], joke[1])

    def start(self):
        print u'press ENTER for reading, and Q for quit'
        self.enable = True
        # self.load_pages()
        current_page = 0
        while self.enable:
            if len(self.joke_pages) > 0:
                jokes = self.joke_pages[0]
                current_page += 1
                del self.joke_pages[0]
                self.get_one_joke(jokes, current_page)
            else:
                self.load_pages()


if __name__ == '__main__':
    spider = QSBK()
    spider.start()
