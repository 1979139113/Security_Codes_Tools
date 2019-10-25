# -*- coding: utf-8 -*-
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : main.py
# @Software: PyCharm
import pymysql
import ConfigParser
import time
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

os.system('color a')
cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server", "db")
port = cfg.get("Server", "port")
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

# Version:3.0
#
#         CMS Automatic acquisition and recognition
#         Include 2.4K ways to recognition Url's CMS
#                                     Version:3.0
#                                     Welcome to Blog:langzi.fun
#                                     Date:2018/8/24
port = int(port)
time.sleep(2)

print (unicode('数据库地址 : ', 'utf-8')) + str(host)
print (unicode('连接数据库 : ', 'utf-8')) + str(Dbname)
print (unicode('数据库账号 : ', 'utf-8')) + str(user)
print (unicode('数据库密码 : ', 'utf-8')) + str(passwd)
print (unicode('数据库端口 : ', 'utf-8')) + str(port)
time.sleep(3)
try:  # line:175
    coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, port=port, charset='utf8')  # line:176
    cur_svn = coon_svn.cursor()  # line:177
    cur_svn.close()  # line:178
    coon_svn.close()  # line:179
    print (unicode('测试数据库连接......', 'utf-8'))
    time.sleep(1)
    print (unicode('数据库连接成功......', 'utf-8'))  # line:180
    print ('\n')
except:
    print (unicode('无法连接到数据库.....', 'utf-8'))  # line:182
    time.sleep(60)  # line:183
def get_result():
    try:
        os.mkdir('result')
    except Exception, e:
        pass
    #    time.sleep(60)
    # try:
    #     os.remove('result.txt')
    # except:
    #     pass
    # while 1:
    #     time.sleep(600)
    #     try:
    #         dd = os.listdir('result')
    #         for _ in dd:
    #             os.remove('result/' + _)
    #     except:
    #         pass
    try:
        print (unicode('开始写入详细信息....', 'utf-8'))
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
        cur = coon.cursor()
        cur.execute("select * from url_cms order by urlway")
        coon.commit()
        curs = cur.fetchall()
        for id, url, ip, uath, urltitle, data in list(curs):
            with open('result.txt', 'a+')as a:
                a.write(url + '|' + uath + '|' + str(urltitle) + '\n')
        cur.close()
        coon.close()
        print (unicode('写入完毕', 'utf-8'))
        time.sleep(3)
    except Exception,e:
        print e
        pass
    print (unicode('开始写入分类CMS文本...', 'utf-8'))
    try:
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
        cur = coon.cursor()
        cur.execute("select * from url_cms order by urlway")
        coon.commit()
        curs = cur.fetchall()
        for id, url, ip, uath, urltitle, data in list(curs):
            txtname = str('result/') + str(uath).decode('utf-8') + ('.txt')
            with open(txtname, 'a+')as a:
                a.write(url + '\n')
        cur.close()
        coon.close()
        print (unicode('写入完毕', 'utf-8'))
        time.sleep(3)
    except:
        pass
get_result()