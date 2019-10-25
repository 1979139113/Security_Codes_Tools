# coding:utf-8
import pymysql
try:
    coon = pymysql.connect(host='118.24.11.235',user='root',passwd='zhaohan0.0',port=9435)
except Exception,e:
    print e