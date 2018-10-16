# -*- coding: UTF-8 -*-

import urllib2
url  =  "http://www.baidu.com"
response1 = urllib2.urlopen(url)
print response1.getcode();
print response1.read()