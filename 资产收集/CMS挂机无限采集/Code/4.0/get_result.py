# -*- coding: utf-8 -*-
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : main.py
# @Software: PyCharm

import pymysql
import configparser
import time
import os
import datetime


os.system('color a')
cfg = configparser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server", "db")
port = cfg.get("Server", "port")
port = int(port)

print ('''
         _                           _ 
        | |                         (_)
        | |     __ _ _ __   __ _ _____ 
        | |    / _` | '_ \ / _` |_  / |
        | |___| (_| | | | | (_| |/ /| |
        |______\__,_|_| |_|\__, /___|_|
                            __/ |      
                           |___/       

''')


print ('数据库地址 : '+ str(host))
print ('连接数据库 : '+ str(Dbname))
print ('数据库账号 : '+ str(user))
print ('数据库密码 : '+ str(passwd))
print ('数据库端口 : '+ str(port))
try:  # line:175
    coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, port=port, charset='utf8')  # line:176
    cur_svn = coon_svn.cursor()  # line:177
    cur_svn.close()  # line:178
    coon_svn.close()  # line:179
    print ('测试数据库连接......')
    time.sleep(1)
    print ('数据库连接成功......')  # line:180
    print ('\n')
except:
    print ('无法连接到数据库.....')  # line:182
    time.sleep(60)  # line:183
def get_result():

    try:
        os.remove('result.txt')
    except:
        pass
    try:
        os.remove('url.txt')
    except:
        pass
    try:
        print ('开始写入详细信息....')
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
        cur = coon.cursor()
        cur.execute("select urlway from url_cms order by cmstype")
        coon.commit()
        curs = cur.fetchall()
        with open('result.txt', 'a+')as a:
            for data in curs:
                a.write(str(data)+'\n')
        cur.close()
        coon.close()
        print ('写入完毕')
        time.sleep(3)
    except Exception as e:
        print(e)

    print ('开始写入分类CMS文本...')
    now = str(datetime.datetime.now()).replace(':','-').replace(' ','-').split('.')[0]
    os.mkdir(now)
    try:
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
        cur = coon.cursor()
        cur.execute("select * from url_cms order by cmstype")
        coon.commit()
        curs = cur.fetchall()
        for id, url, urlway, cmstype, urltitle, data in list(curs):
            txtname = now + '/' + str(cmstype) + ('.txt')
            with open(txtname, 'a+')as a:
                a.write(url + '\n')
        cur.close()
        coon.close()
        print ('写入完毕')
        time.sleep(3)
    except:
        pass

    print('开始写入所有网址')
    try:
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
        cur = coon.cursor()
        cur.execute("select url from url_index")
        coon.commit()
        curs = cur.fetchone()
        while curs:
            with open('url.txt', 'a+')as a:
                for data in curs:
                    a.write(str(data).replace("'",'').replace('"','').replace("\r",'').replace("\n",'').replace("(",'').replace(")",'').replace(" ",'').replace('\t','').replace(',','').lstrip().strip()+'\n')
            curs = cur.fetchone()
        cur.close()
        coon.close()
        print ('写入完毕')

    except Exception as e:
        print(e)
        pass

get_result()