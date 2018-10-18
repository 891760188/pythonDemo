# -*- coding: UTF-8 -*-
from selenium import webdriver
import csv
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

url = 'https://www.toutiao.com/a6612501672868446723/?tt_from=mobile_qq&utm_campaign=client_share&timestamp=1539844794&app=news_article&utm_source=mobile_qq&iid=45844404180&utm_medium=toutiao_ios&group_id=6612501672868446723'

#准备好存储歌单的csv文件
csv_file = open("itDetail.csv","wb")
write = csv.writer(csv_file)
write.writerow(['序号','公司','详情']);

#用Phantomjs接口创建一个selenium的webdriver
driver = webdriver.PhantomJS()
#用webdriver加载页面
driver.get(url)
# print  dataContain.text   find_element_by_tag_name 多个s和少个s是不一样的
contain = driver.find_element_by_css_selector('div.article-content');
data = contain.find_elements_by_tag_name('p')

#解析一页中所有的歌单
for i in range(len(data)): #range 创建整数列表
    str = data[i].text
    gs = str.split('，')[0]
    #把数据写入csv
    write.writerow([i,gs,str])
csv_file.close();















