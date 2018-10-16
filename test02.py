# -*- coding: UTF-8 -*-

#打开一个文件
fo = open("foo.txt",'w')
print '文件名',fo.name,fo.closed,fo.mode,fo.softspace
fo.write("www.runoob.com!\nVery good site!\n我哦我")

fo.close();
