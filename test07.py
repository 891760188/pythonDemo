# -*- coding: UTF-8 -*-

import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "pythondemo01", charset='utf8' )
print db
cursor=db.cursor();
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s " % data

cursor.execute("drop table if exists employee ")
sql = """ CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT ) """
cursor.execute(sql)

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    cursor.execute(sql);
    db.commit()
except:
    db.rollback()
finally:
    db.close()


print 1
print 1
print 1
print 1