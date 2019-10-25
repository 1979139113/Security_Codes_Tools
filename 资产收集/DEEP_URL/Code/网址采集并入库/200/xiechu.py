# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 0016 18:46
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : xiechu.py
# @Software: PyCharm
import sys
import pymysql
import ConfigParser,time
import os
reload(sys)
sys.setdefaultencoding('utf-8')
cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server","db")
thread_s = cfg.get("Config","thread_s")
black = cfg.get("Config","black")
blackname=black.lstrip('|').rstrip('|').split('|')
def writein():
    try:
        print  (unicode('开始清理缓存文件','utf-8'))
        os.remove(('全部友链网址.txt').decode('utf-8'))
        os.remove(('主域名友链网址.txt').decode('utf-8'))
        os.remove(('二级域名友链网址.txt').decode('utf-8'))
        print  (unicode('缓存清理完毕 ','utf-8'))
    except Exception,e:
        print e
    #time.sleep(500)
    try:
        coon = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        cur = coon.cursor()
        sql1 = 'select url from result'
        sql2 = 'select url from url_domain'
        sql3 = 'select url from url_subdomain'
        cur.execute(sql1)
        coon.commit()
        res1 = cur.fetchall()

        for _ in res1:
            with open(('全部友链网址.txt').decode('utf-8'),'a+')as a:
                d = str(_)
                print d
                a.write(d.replace("('","").replace("',)","") + '\n')
        cur.execute(sql2)
        coon.commit()
        res2 = cur.fetchall()
        for _ in res2:
            with open(('主域名友链网址.txt').decode('utf-8'),'a+')as a:
                d = str(_)
                a.write(d.replace("('","").replace("',)","") + '\n')
        cur.execute(sql3)
        coon.commit()
        res3 = cur.fetchall()
        for _ in res3:
            with open(('二级域名友链网址.txt').decode('utf-8'),'a+')as a:
                d = str(_)
                a.write(d.replace("('","").replace("',)","") + '\n')
    except Exception,e:
        print e
        pass
writein()