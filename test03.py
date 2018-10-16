# -*- coding: UTF-8 -*-

#打开一个文件 	打开一个文件用于读写。文件指针将会放在文件的开头。
fo = open('foo.txt','r+');
str = fo.read(10)
print '读取的内容==',str

#查找当前位置
position = fo.tell()
print  '当前的位置：',position
position = fo.seek(0,0)

str = fo.read(10);
print '读取的内容==',str

fo.close()