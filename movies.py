# -*- coding: utf-8 -*-

import requests,urllib,urllib2,hashlib
from bs4 import BeautifulSoup
import os,sys,re,random
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')

heads= \
 [{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
 {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
 {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]






####获取网页信息
####urllib2.urlopne(url).read().decode("utf-8")
####httplib2.Http().request(url,'GET')
####requests.get(url,headers=heads).content.decode('utf-8')


def movies():
    url = 'https://movie.douban.com/nowplaying/shanghai/'

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()

    soup = BeautifulSoup(page,'lxml')
    lists = soup.find('ul',  "lists")

    for movie_info in lists.find_all('li',"list-item"):
        m_name = movie_info.find('a',{'data-psource':'title'}).string.strip()
        print m_name


def moive250():
    url = 'https://movie.douban.com/top250'
    next = ''

    req = urllib2.Request(url + next)
    response = urllib2.urlopen(req)
    page = response.read()

    soup = BeautifulSoup(page,'lxml')
    mpage = soup.find('div',{'id':'content'}).find('div',{'class':'article'})
    page = mpage.find('span',{'class':'next'}).tag('href')
    print page
    movs = mpage.find_all('li')
    for mov in movs:
        num = mov.find('em').string.strip()
        name = mov.find('span',{'class':'title'}).string.strip()
        rating = mov.find('span',{'class':'rating_num'}).string.strip()
        print num + '\t' + name + '\t' + rating
     #   print mov.find('span',{'class':'next'})



moive250()



