# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import pymysql
import codecs
import ConfigParser
import time
import os
reload(sys)
sys.setdefaultencoding('utf-8')
cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server","db")
print unicode('''
    查询所有的网址>>1
    查询所有已经爬行过的网址>>2
    查询所有扫描成功的CMS程序网址>>3
    查询所有扫描成功的备份文件网址>>4
    查询所有扫描成功使用ST2框架网址>>5
    删除所有已经爬行过外链的网址>>6
    删除所有表的所有内容(删除之后在配置文件设置new_start=0,重启程序)>>7
    删除数据库>>8

''','utf-8')
time.sleep(1)
queding = input(unicode('请选择要执行的选项:','utf-8').encode('gbk'))

qd = int(queding)
def select(sql):

    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
    cur = coon.cursor()
    #sql = "INSERT INTO url_1(urllist,urlget,urltime) VALUES ('" + str(xx) + "','" + str(0) + "','" + str(timenow) + "')"
    cur.execute(sql)
    coon.commit()
    for xx in cur:
        print xx
    cur.close()
    coon.close()

def delete(sql):
    coon1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
    cur1 = coon1.cursor()
    #sql = "INSERT INTO url_1(urllist,urlget,urltime) VALUES ('" + str(xx) + "','" + str(0) + "','" + str(timenow) + "')"
    cur1.execute(sql)
    coon1.commit()
    for xx in cur1:
        print xx
    cur1.close()
    coon1.close()
    print unicode('执行完毕', 'utf-8')

if qd == 1:
    sql = "select urllist from url_1"
    select(sql)
if qd == 2:
    sql = "select urllist from url_1 where urlget=1"
    select(sql)
if qd ==3:
    sql = "select urllist,cms from url_3"
    select(sql)
if qd == 4:
    sql = "select urllist,rarsize from url_4"
    select(sql)
if qd == 5:
    sql = "select urllist from url_5"
    select(sql)
if qd == 6:
    sql = "delete from url_1 where urlget=1"
    delete(sql)
if qd == 7:
    sql = 'delete from url_1 where urlget=1'
    sql2 = 'delete from url_1 where urlget=0'
    sql3 = 'delete from url_2 where st2=1'
    sql4 = 'delete from url_2 where st2=0'
    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
    cur = coon.cursor()
    #sql = "INSERT INTO url_1(urllist,urlget,urltime) VALUES ('" + str(xx) + "','" + str(0) + "','" + str(timenow) + "')"
    cur.execute(sql)
    coon.commit()
    cur.execute(sql2)
    coon.commit()
    cur.execute(sql3)
    coon.commit()
    cur.execute(sql4)
    coon.commit()
    for xx in cur:
        print xx
    cur.close()
    coon.close()
    print unicode('执行完毕', 'utf-8')

if qd ==8:
    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
    cur = coon.cursor()
    #sql = "INSERT INTO url_1(urllist,urlget,urltime) VALUES ('" + str(xx) + "','" + str(0) + "','" + str(timenow) + "')"
    cur.execute('drop database lang_cms')
    coon.commit()
    for xx in cur:
        print xx
    cur.close()
    coon.close()
    print unicode('执行完毕','utf-8')

os.system("pause")