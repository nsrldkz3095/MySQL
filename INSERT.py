#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
dbhost='192.168.10.8'
dbuser='test'
dbpass='test'
dbname='test'
db=pymysql.connect(host=dbhost,user=dbuser,password=dbpass,database=dbname)
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()