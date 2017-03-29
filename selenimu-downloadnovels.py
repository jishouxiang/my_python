#-*- coding=utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time,re,os,sys
reload(sys)
sys.setdefaultencoding('utf-8')



BASE_DIR = os.getcwd()
#print  BASE_DIR




url='http://www.kanunu8.com/files/writer/3845.html'
novel_url = 'http://www.kanunu8.com/book/3865/40210.html'


###获取小说的所有url  并且写入到file
def get_chapter_urls(novel_urls,filename):
    fopen = open(filename,'a')
    broswer = webdriver.Firefox()
    broswer.get(novel_urls)
    novel1_chas = broswer.find_elements_by_xpath('//td[@width="25%"]/a')
    #print novel1_chas
    for novel in novel1_chas:
        u = str(novel.get_attribute('href'))
        fopen.write(u + '\n')


    novel2_chas = broswer.find_elements_by_xpath('//td/a')
    for novel in novel2_chas:
        nov = str(novel.get_attribute('href'))
        if re.search('3865',nov):
            u = str(novel.get_attribute('href'))
            fopen.write(u + '\n')
    broswer.quit()
    fopen.close()

###获取小说的文本内容
def get_novel(urlflie,novelfile):
    fopen1 = open(urlflie,'r')
    fopen2 = open(novelfile,'a')
    for eachline in fopen1:
        broswer = webdriver.Firefox()
        broswer.get(eachline)
        t = broswer.find_element_by_tag_name('p').text
        fopen2.write(t + '\n')
        broswer.quit()




###读取文件
def read_file(filename):
    fopen = open(filename,'r')
    for eachLine in fopen:
        print eachLine
    fopen.close()


####写入文件
def write_file(filename):
    fopne = open(filename,'w')
    while True:
        aline = raw_input()
        if aline != ".":
            fopne.write('%s%s' %(aline,os.linesep))
        else:
            break
    fopne.close()







if __name__ == '__main__':
    novel_urls = 'http://www.kanunu8.com/book/3865/index.html'
#    get_chapter_urls(novel_urls,'novel.txt')
    get_novel('novel.txt','noveltext.txt')






