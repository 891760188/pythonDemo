# -*- coding: UTF-8 -*-
import time;  # 引入time模块

print "你好，世界" ; print "你好，世界" ;

if True:
    print "True"# 第一个注释
    print "True"
else:
    print "False"
# raw_input("按下 enter 键退出，其他任意键显示...\n")

task = time.time();
print  task

localtime = time.localtime(time.time())
print "本地时间为 :", localtime

localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime


Money = 2000
def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1
print Money
AddMoney()
print Money

# 导入内置math模块
import math
content = dir(math)
print content;
print __name__;