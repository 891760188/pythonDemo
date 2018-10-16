# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
from urllib import  urlopen

#打开地址获取HTML内容
html = urlopen('http://jr.jd.com/')
#获取页面代码str
htmlStr = html.read()
#把网页转成beautifulSoup对象
bs_obj = BeautifulSoup(htmlStr,'html.parser');

testList = bs_obj.find_all('a','nav-item-primary')
dhl_list = []
for dom in testList:
    text = dom.get_text()
    dhl_list.append(text)
    print dom

for dhl in dhl_list :
    print  dhl
print len(dhl)
html.close()
