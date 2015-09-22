from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from htmllib import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO

__author__ = 'weixy6'


class Retriever(object):  # download web pages
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, defaultname='index.htm'):
        parsedurl = urlparse(url, 'http:', 0)
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        if find(ext[1], '#'):
            path = path[:find(path, '#')]
            pass

        if ext[1] == '' or ext[1] == '.com' or ext[1] == '.net':
            if path[-1] == '/':
                path += defaultname
            else:
                path += '/' + defaultname
        localdir = dirname(path)  # local directory
        if sep != '/':
            localdir = replace(localdir, '/', sep)
        if not isdir(localdir):
            if exists(localdir):
                unlink(localdir)
            makedirs(localdir)
        return path

    def download(self):  # download web page
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' % self.url)
        return retval

    def parseAndGetLinks(self):  # parse HTML, save links
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist


class Crawler(object):  # manage entire crawling process
    count = 0  # static downloaded page counter

    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getpage(self, url):
        retriever = Retriever(url)
        retval = retriever.download()
        if retval and retval[0] == '*':  # error situation, do not parse
            print retval, '... skipping parse'
            return
        Crawler.count += 1
        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', retval[0]
        self.seen.append(url)

        links = retriever.parseAndGetLinks()  # get and process links
        for eachLink in links:
            if eachLink[:4] != 'http' and find(eachLink, '://') == -1:
                eachLink = urljoin(url, eachLink)
            print '* ', eachLink

            if find(lower(eachLink), 'mailto:') != -1:
                print '... new, added to Q'
                continue

            if eachLink not in self.seen:
                if find(eachLink, self.dom) == -1:
                    print '... discarded, not in domain'
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print '... now, added to Q'
                    else:
                        print '... discarded, already in Q'
            else:
                print '... discarded, already processed'

    def go(self):  # process links in queue
        while self.q:
            url = self.q.pop()
            self.getpage(url)


def main():
    if len(argv) > 1:
        url = argv[1]

    else:
        try:
            url = raw_input('Enter starting URL:')
        except (KeyboardInterrupt, EOFError):
            url = ''
        if not url:
            return
        robot = Crawler(url)
        robot.go()


if __name__ == '__main__':
    main()
