#coding:utf-8
import time
import sys
import random
import os
import requests
import pymysql
import re
import socket
user = 'root'
passwd='root'
host='127.0.0.1'
Dbname='yolanda_information_collection_02'
port=[80,1433,3306,8888,3389]
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

def scan_port(url):
    list_port=[]
    try:
        ip = socket.gethostbyname(url)
        print ip
        for iport in port:
            print 'Checking>>>' + str(ip) + ':' + str(iport)
            try:
                s = socket.socket()
                s.connect((str(ip), int(iport)))
                s.send('langziyanqing \n')
                cc = s.recv(1024)
                list_port.append(iport)
                s.close()
            except:
                pass
    except Exception,e:
        pass
    finally:
        try:
            list_port_string=str(list_port)
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            coon_port_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
            cur_port_1 = coon_port_1.cursor()
            sql_port_1 = "INSERT INTO url_port (url,ip,port,datatime) VALUES (%s,%s,%s,%s)"
            cur_port_1.execute(sql_port_1, (str(url),str(ip),str(list_port_string), str(timenow)))
            coon_port_1.commit()
            cur_port_1.close()
            coon_port_1.close()
        except Exception,e:
            pass

def porttiqu():
    try:
        time.sleep(2)
        coonport2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curport2 = coonport2.cursor()
        sql = "select url from url_check where portscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set portscan='1' where portscan = 0 limit 1"
        curport2.execute(sql)
        coonport2.commit()
        curs_port = curport2.fetchone()
        curport2.execute(sql1)
        coonport2.commit()
        try:
            for xx in curs_port:
                xxx1port = xx.replace("('","").replace("',)","").replace('http://','').replace('https://','')
                print xxx1port
                scan_port(xxx1port)
        except Exception,e:
            pass
        curport2.close()
        coonport2.close()
    except Exception,e:
        pass
porttiqu()