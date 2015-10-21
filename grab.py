#-*- coding: utf-8 -*-
import os
import sys
import urllib2
import urllib
import re
import test
from urllib import unquote


def grab_pic(href,path):
    content = urllib2.urlopen(href).read()
    #content = content.decode("utf-8")
    m = re.search(u'\["(.*)\]',content)
    if m:
        link = m.group(0)
    m = re.search(u'\'(.*)\'.split',content)
    if m:
        matchlist = m.group(1).split(',')[-1][1:]
        matchlist = matchlist.split('|')
    link = link.replace("\\",'')
    link = link[1:-1]
    link = link.split(',')
    base = len(matchlist)
    #print matchlist.encode("utf-8")


    count = base
    Dic = {}
    while count > 0:
        count -=  1
        ch = test.e(count,base)
        Dic[ch] = matchlist[count]
    print Dic
    sys.stdout.flush()
    abs_add = 'http://images.dmzj.com/'
    address = []
    for wd in link:
        address.append(abs_add + test.convert(wd[1:-1],Dic))
    countf = 1
    for add in address:
        print 'downloading page ',countf,'from',unquote(add)
        sys.stdout.flush()
        while True:
            try:
                urllib.urlretrieve(add,path+'%d.jpg'%(countf))
                break
            except:
                print 'retry'
        countf += 1










'''
<a href="http://images.dmzj.com/b/%E8%9D%99%E8%9D%A0%E4%BE%A0-8354/%E7%AC%AC0%E5%8D%B7/0001.jpg">右键另存此图片</a>
'''

def grab(title,href):
    print 'grabbing',title.encode('utf-8'),'from',href
    sys.stdout.flush()
    if os.path.exists(title.encode("utf-8")) is False:
        os.mkdir(title.encode("utf-8"))
    path = title.encode("utf-8") +'/'
    grab_pic(href,path)




if __name__ =='__main__':
    fp = open('grablist.txt')
    while True:
        line = fp.readline()
        if not line: break
        m = re.search(u'title=\"(.*?)\"',line)
        if m:
            title = m.group(1)
        else :continue
        m = re.search(u'href=\"(.*?)\"',line)
        if m:
            href = m.group(1)
        grab(title.decode('utf-8'),'http://manhua.dmzj.com/' + href)


