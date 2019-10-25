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
import socket
import time
import threading
timeout = 5
socket.setdefaulttimeout(timeout)
print '''
-----------------------------------
    LANGziyanqing Port Scan
-----------------------------------
批量扫描IP的端口，是否开放
获取开放端口的banner
emmm....
就这样
ip放在ips.txt
'''
reload(sys)
sys.setdefaultencoding('utf-8')
scanport1=input("[+]Set Port you want to scan:")
scanport = int(scanport1)
def start():
    with open('ips.txt','r')as f:
        for ff1 in f:
            ff = ff1.replace('\n','')
            try:
                print '[*] Connect ' + ff +':' + str(scanport)
                s = socket.socket()
                s.connect((ff,scanport))
                s.send('langziyanqing \n')
                cc = s.recv(1024)
                if 'not allowed to' not in cc:
                    output1 = open('portbannerlog.txt', 'a+')
                    output = open('result.txt', 'a+')
                    output1.write(ff + ':' + str(scanport) + '  ' + str(cc) + '\n')
                    output.write(ff + '\n')
                else:
                    pass
                print cc
                s.close()
            except Exception,e:
                print e
t1=threading.Thread(target=start())
t1.start()
