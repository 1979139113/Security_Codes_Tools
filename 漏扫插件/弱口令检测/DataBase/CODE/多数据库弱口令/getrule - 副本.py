# -*- coding: utf-8 -*-
import multiprocessing
import time
import pymysql
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





def brute_mysql(ip,username,password,port=3306):
    print 'Checking>>>MYSQL:' + ip + '@' + username + ':' + password + ':'  + str(port)

    try:
        connx = pymysql.connect(host=ip, user=username, passwd=password, db='mysql', port=port)
        return 'MYSQL:'+ip + ':' + str(port) + '|' + username + ':' + password
    except Exception,e:
        print e
        return None






def scan(ip):
    for u in mysql_user_list:
        for p in mysql_password_list:
            res_mysql = brute_mysql(ip=ip,username=u,password=p)
            if res_mysql == None:
                pass
            else:
                print '66666666666666' + res_mysql + '66666666666666'




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

