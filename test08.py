# -*- coding: UTF-8 -*-

import MySQLdb

#打开数据库
db = MySQLdb.connect("localhost", "root", "root", "pythondemo01", charset='utf8' )
cursor = db.cursor()

sql = "select * from employee where income > '%d' "  % (999)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print row
except:
    print "Error: unable to fecth data"
finally:
    db.close()