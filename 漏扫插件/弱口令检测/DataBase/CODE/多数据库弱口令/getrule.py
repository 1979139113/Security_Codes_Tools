# -*- coding: utf-8 -*-
import multiprocessing
import re
import time
import pymysql
import pymssql
import psycopg2
import cx_Oracle
import telnetlib
import paramiko
paramiko.util.logging.getLogger('paramiko.transport').addHandler(paramiko.util.logging.NullHandler())
from ftplib import FTP
from smb.SMBConnection import SMBConnection
import socket
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
timeout = 5
socket.setdefaulttimeout(timeout)

system_user_list=['root','ubuntu']

system_passwords_list=['root','Passw0rd','admin123!@#','admin123','admin@123','admin#123','123456','password','12345','1234','123','qwerty','test','1q2w3e4r','1qaz2wsx','qazwsx','123qwe','123qaz','0000','oracle','1234567','123456qwerty','password123','12345678','1q2w3e','abc123','okmnji','test123','123456789','postgres','q1w2e3r4','a123456','a123456789','111111','123123','woaini1314','zxcvbnm','qq123456','abc123456','123456a','123456789a','000000','iloveyou']

oracle_user_list = ['sys', 'system', 'sysman', 'scott', 'aqadm', 'Dbsnmp']

oracle_password_list = ['', 'manager', 'oem_temp', 'tiger', 'aqadm', 'dbsnmp','root']

mysql_user_list = ['root']

mysql_password_list = ['root','admin123!@#', 'test123', 'qazwsx', 'zxcvbnm', 'admin12345', 'admin123', 'qwerty', '1q2w3e', 'mysql', '123qaz', '123456', 'postgres', 'admin@123', '1234567', 'abc123456', 'okmnji', '1qaz2wsx', 'test', 'qq123456', '1234', 'woaini1314', '0000', '123456qwerty', 'password123', '123456789a', '12345678', 'Passw0rd', '123', 'admin#123', '123456789', 'password', '1q2w3e4r', 'a123456789', '000000', '123123', 'q1w2e3r4', '111111', '123456a', 'iloveyou', 'admin1234', 'abc123', 'oracle', 'a123456', '12345', '123qwe']

mssql_user_list = ['sa']

mssql_password_list = ['root','Sa123','Sa123456','Sa1234','admin123!@#', 'test123', 'qazwsx', 'zxcvbnm', 'admin12345', 'admin123', 'qwerty', '1q2w3e', 'mysql', '123qaz', '123456', 'postgres', 'admin@123', '1234567', 'abc123456', 'okmnji', '1qaz2wsx', 'test', 'qq123456', '1234', 'woaini1314', '0000', '123456qwerty', 'password123', '123456789a', '12345678', 'Passw0rd', '123', 'admin#123', '123456789', 'password', '1q2w3e4r', 'a123456789', '000000', '123123', 'q1w2e3r4', '111111', '123456a', 'iloveyou', 'admin1234', 'abc123', 'oracle', 'a123456', '12345', '123qwe']

postql_user_list = ['postgres','root','admin']

postql_password_list = ['root','admin123!@#', 'test123', 'qazwsx', 'zxcvbnm', 'admin12345', 'admin123', 'qwerty', '1q2w3e', 'mysql', '123qaz', '123456', 'postgres', 'admin@123', '1234567', 'abc123456', 'okmnji', '1qaz2wsx', 'test', 'qq123456', '1234', 'woaini1314', '0000', '123456qwerty', 'password123', '123456789a', '12345678', 'Passw0rd', '123', 'admin#123', '123456789', 'password', '1q2w3e4r', 'a123456789', '000000', '123123', 'q1w2e3r4', '111111', '123456a', 'iloveyou', 'admin1234', 'abc123', 'oracle', 'a123456', '12345', '123qwe']



def brute_mssql(ip,username,password,port=1433):
    print 'Checking>>>MSSQL:' + ip + '@' + username + ':' + password + ':'  + str(port)
    try:
        connx = pymssql.connect(server=str(ip), port=port, user=username, password=password)
        return 'MSSQL:'+ip + ':' + str(port) + '|' + username + ':' + password
    except Exception,e:
        print e

def brute_mysql(ip,username,password,port=3306):
    print 'Checking>>>MYSQL:' + ip + '@' + username + ':' + password + ':'  + str(port)

    try:
        connx = pymysql.connect(host=ip, user=username, passwd=password, db='mysql', port=port)
        return 'MYSQL:'+ip + ':' + str(port) + '|' + username + ':' + password
    except Exception,e:
        print e



def brute_postql(ip,username,password,port=5432):
    print 'Checking>>>POSTQL:' + ip + '@' + username + ':' + password + ':'  + str(port)

    try:
        connx = psycopg2.connect(host=ip, port=port, user=username, password=password,dbname='postgres')
        return 'POSTQL:'+ip + ':' + str(port) + '|' + username + ':' + password
    except Exception,e:
        print e
        return None




def brute_oralce(ip,username,password,port=1521):
    print 'Checking>>>ORACLE:' + ip + '@' + username + ':' + password + ':'  + str(port)

    try:
        connx = cx_Oracle.connect(username, password, ip + ':%s/orcl' % str(port))
        return 'ORACLE:'+ip + ':' + str(port) + '|' + username + ':' + password
    except Exception,e:
        print e
        return None


def brute_ssh(ip,username,password,port=22):
    print 'Checking>>>SSH:' + ip + '@' + username + ':' + password + ':'  + str(port)

    try:
        # telnetlib.Telnet(ip, 111, timeout=2)#判断额外端口的
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
        ssh.connect(ip, 22, '', '', timeout=timeout)
        ssh.close()
    except Exception as e:
        if 'Authentication' in str(e):  # 捕获所有的异常，根据返回信息，判断是否是ssh的，决定是否往下爆破。
            try:
                ssh.connect(ip, 22, username, password, timeout=timeout)
                # print(colored(ip + ' ' + us + ' ' + pa + ' ' + '连接成功~~~~~~~', 'red'))
                # open(outfile, 'a', encoding='utf-8').write(ip + ' ' + us + ' ' + pa + '\n')  # 成功了，就写入文本
                # data_text = ip + ' ' + us + ' ' + pa
                ssh.close()
                return 'SSH:'+ip + ':' + str(port) + '|' + username + ':' + password
            except Exception as e:
                ssh.close()
                print e
        else:
            print e
            return None
            #print(ip, str(e))



def brute_ftp(ip,username,password,port=21):
    print 'Checking>>>FTP:' + ip + '@' + username + ':' + password + ':'  + str(port)
    try:
        ftp = FTP(ip)
        ftp.connect(ip, port)
        ftp.login(username, password)
        if 'Not implemented' in ftp.dir():
            pass
        else:
            return 'FTP:'+ip + ':' + str(port) + '|' + username + ':' + password
        ftp.quit()
    except Exception, e:
        print e
        return None


def brute_telnet(ip,username,password,port=23):
    print 'Checking>>>TELNET:' + ip + '@' + username + ':' + password + ':'  + str(port)

    try:
        res = ''
        tn = telnetlib.Telnet(ip,timeout=timeout)
        tn.set_debuglevel(5)
        time.sleep(0.5)
        oss = tn.read_some()
        user_match = "(?i)(login|user|username)"
        pass_match = '(?i)(password|pass)'
        login_match = '#|\$|>'
        if re.search(user_match, oss):
            try:
                tn.write(username + '\r\n')
                tn.read_until(pass_match, timeout=2)
                tn.write(password + '\r\n')
                login_info = tn.read_until(login_match, timeout=3)
                tn.close()
                if re.search(login_match, login_info):
                    res = 'TELNET:'+ip + ':' + str(port) + '|' + username + ':' + password
            except Exception, e:
                print e
                pass
        else:
            try:
                info = tn.read_until(user_match, timeout=2)
            except Exception, e:
                print e
                pass
            if re.search(user_match, info):
                try:
                    tn.write(username + '\r\n')
                    tn.read_until(pass_match, timeout=2)
                    tn.write(password + '\r\n')
                    login_info = tn.read_until(login_match, timeout=3)
                    tn.close()
                    if re.search(login_match, login_info):
                        res = 'TELNET:'+ ip + ':' + str(port) + '|' + username + ':' + password
                except Exception, e:
                    print e
                    pass
            elif re.search(pass_match, info):
                tn.read_until(pass_match, timeout=2)
                tn.write(password + '\r\n')
                login_info = tn.read_until(login_match, timeout=3)
                tn.close()
                if re.search(login_match, login_info):
                    res = 'TELNET:'+ip + ':' + str(port) + '|' + username + ':' + password
    except Exception ,e:
        print e
        pass

    if res == '':
        return None
    else:
        return res



def ip2hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except Exception,e:
        pass
    try:
        query_data = "\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x20\x43\x4b\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\x00\x21\x00\x01"
        dport = 137
        _s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _s.sendto(query_data, (ip, dport))
        x = _s.recvfrom(1024)
        tmp = x[0][57:]
        hostname = tmp.split("\x00", 2)[0].strip()
        hostname = hostname.split()[0]
        return hostname
    except Exception,e:
        pass

def brute_smb(ip,username,password,port=445):
    print 'Checking>>>SMB:' + ip + '@' + username + ':' + password + ':'  + str(port)

    try:
        hostname = ip2hostname(ip)
        if hostname:
            try:
                conn = SMBConnection(username,password, 'xunfeng', hostname)
                if conn.connect(ip) == True:
                    return 'SMB:'+ip + ':' + str(port) + '|' + username + ':' + password
            except Exception, e:
                return None
    except Exception, e:
        print e
        return None

def write_data(x):
    with open('result.txt','a+')as a:
        a.write(x + '\n')


def scan(ip):
    for u in mysql_user_list:
        for p in mysql_password_list:
            res_mysql = brute_mysql(ip=ip,username=u,password=p)
            if res_mysql == None:
                pass
            else:
                write_data(res_mysql)

    for u in mssql_user_list:
        for p in mssql_password_list:
            res_mssql = brute_mssql(ip=ip,username=u,password=p)
            if res_mssql == None:
                pass
            else:
                write_data(res_mssql)

    for u in oracle_user_list:
        for p in oracle_password_list:
            res_oracle = brute_oralce(ip=ip,username=u,password=p)
            if res_oracle == None:
                pass
            else:
                write_data(res_oracle)

    for u in postql_user_list:
        for p in postql_password_list:
            res_posql = brute_postql(ip=ip,username=u,password=p)
            if res_posql == None:
                pass
            else:
                write_data(res_posql)

    for u in system_user_list:
        for p in system_passwords_list:
            res_ssh = brute_ssh(ip=ip,username=u,password=p)
            if res_ssh == None:
                pass
            else:
                write_data(res_ssh)

            res_ftp = brute_ftp(ip=ip,username=u,password=p)
            if res_ftp == None:
                pass
            else:
                write_data(res_ftp)

            res_smb = brute_smb(ip=ip,username=u,password=p)
            if res_smb == None:
                pass
            else:
                write_data(res_smb)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print ('''
    
             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_Database_Weak_passwords
                               |___/       Version:1.0
                                           Datetime:2018-11-22-13:05:36
    
    ''')
    print unicode('             数据库弱口令自动化识别','utf-8')
    print unicode('             支持检测验证下列数据库:','utf-8')
    print '''
        FTP,MSSQL,MYSQL,ORACLE,POSTQL,SSH,SMB
    '''

    New_start = raw_input(unicode('待需验证IP文本拖拽进来:', 'utf-8').encode('gbk'))
    smxc = int(input(unicode('设置线程池数量(2-128):', 'utf-8').encode('gbk')))
    list_ = list(set(
        [x.replace('\n', '') for x in open(New_start, 'r').readlines()]))

    p = multiprocessing.Pool(smxc)
    for _ in list_:
        p.apply_async(scan,args=(_,))
    p.close()
    p.join()



# New_start = raw_input(unicode('待需验证url文本拖拽进来:', 'utf-8').encode('gbk'))
#
# list_ = list(set(
#             [x.replace('\n', '') if x.startswith('http') else 'http://' + x.replace('\n', '') for x in
#              open(New_start, 'r').readlines()]))
#
# for x in list_:
#     scan(x)

