# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self,name,salary):
        self.name = name ;
        self.salary = salary ;
        Employee.empCount +=1 ;

    def dayin(self):
        print self

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"

emp = Employee('张三',1001);
emp.dayin();
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__