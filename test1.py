#!/usr/bin/python3
# Python 3
# -*- coding: UTF-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "Ciara", "Ciara", "Music")

# 使用 cursor() 方法创建一个游标对象 cursor
Cur1 = db.cursor()

# 使用 execute()  方法执行 SQL 查询
Cur1.execute("SELECT * FROM Songs_List")

# 使用 fetchone() 方法获取单条数据.
Result1 = Cur1.fetchall()

print (Result1)
print("456")
Cur1.close()
print ("123")
#print("Database version : %s " % data)

# 关闭数据库连接

db.close()