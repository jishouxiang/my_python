# -*- coding: utf-8 -*-
"""
Usage:
    doubanhds <type> <time>

Options:
    -h --help show help
    --version show version
"""
import urllib,urllib2,hashlib
from bs4 import BeautifulSoup
import os,sys,re,random
from prettytable import PrettyTable
from collections import OrderedDict
import requests
from lxml import etree
from pprint import pprint
from prettytable import PrettyTable


reload(sys)
sys.setdefaultencoding('utf-8')
from docopt import docopt



#构建url
def cli():
    arguments = docopt(__doc__,version='hd 1.0')
    type = arguments['<type>']
    time = arguments['<time>']
    url = 'https://shanghai.douban.com/events/{}-{}?start='.format(type,time,p)
    return url


def get_page(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    return page


def get_hdinformations(page):
    #x = PrettyTable(["名字","开始时间","结束时间","地址","费用"])
    x = PrettyTable(["名称","开始时间","结束时间","地址","费用"])
    x.align = "l"
    x.padding_width = 2

    li = []
    soup = BeautifulSoup(page,'lxml')
    hds = soup.find('div',{'class':'article'}).find_all('li',{'class':'list-entry'})
    for hd in hds:
        name = hd.find('span',{'itemprop':'summary'}).string.strip()
        hs = hd.find_all('ul',{'class':'event-meta'})
        for h in hs:
            starttime = h.find('li',{'class':'event-time'}).find('time',{'itemprop':'startDate'}).get('datetime')
            starttime1 = re.sub(r'[a-zA-Z]',' ',starttime)
            endtime = h.find('li',{'class':'event-time'}).find('time',{'itemprop':'endDate'}).get('datetime')
            endtime1 = re.sub(r'[a-zA-Z]',' ',endtime)
            location = h.find('span',text="地点：").next_sibling.next_sibling.get('content')
            fee = h.find('li',{'class':'fee'}).find('strong').string.strip()
            li = [name,starttime1,endtime1,location,fee]
            x.add_row(li)

#            print name,starttime,endtime,location,fee
    print x


if __name__ == '__main__':

    print "查看几页内容："
    p = raw_input()
    myurl = cli()
    for i in range(0,int(p)*10,10):
        url = myurl + str(i)
        if get_page(url):
            mypage = get_page(url)
            get_hdinformations(mypage)
