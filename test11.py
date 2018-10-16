# -*- coding: UTF-8 -*-
from selenium import webdriver
import csv
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

#准备好存储歌单的csv文件
csv_file = open("playlist.csv","wb")
write = csv.writer(csv_file)
write.writerow(['标题','播放数','连接']);

#用Phantomjs接口创建一个selenium的webdriver
driver = webdriver.PhantomJS()
#解析每一页，直到下一页为空
while url != 'javascript:void(0)':
    #用webdriver加载页面
    driver.get(url)
    #切换到内容的iframe
    driver.switch_to.frame('contentFrame')
    #定位歌单标签
    dataContain = driver.find_element_by_id('m-pl-container');
    # print  dataContain.text   find_element_by_tag_name 多个s和少个s是不一样的
    data = dataContain.find_elements_by_tag_name('li')

    #解析一页中所有的歌单
    for i in range(len(data)): #range 创建整数列表
        #获取播放数
        nb = data[i].find_element_by_class_name('nb').text
        if '万' in nb and int(nb.split('万')[0]) > 500:
            #获取播放量大于500的歌单封面
            msk = data[i].find_element_by_css_selector('a.msk')
            #把数据写入csv
            write.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
    url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
csv_file.close();















