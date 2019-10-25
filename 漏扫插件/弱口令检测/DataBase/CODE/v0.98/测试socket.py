# coding:utf-8
import pymysql
from ftplib import FTP
import socket

def ip2hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except:
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
    except:
        pass
dic_pass=['123456','00000']
dic_user=['root','admin']
from smb.SMBConnection import SMBConnection
ip = '127.0.0.1'
# try:
#     print('SMB弱口令漏洞 : ' + str(ip))
#     hostname = ip2hostname(ip)
#     dic_pass.insert(0, 'anonymous')
#     if hostname:
#         for user in dic_user:
#             for pass_ in dic_pass:
#                 try:
#                     conn = SMBConnection(user, pass_, 'xunfeng', hostname)
#                     if conn.connect(ip) == True:
#                         res = 'SMB弱口令漏洞 : ' + str(ip) + ':' + str(user) + '|' + str(pass_)
#                         print res
#                 except Exception, e:
#                     print e
# except Exception, e:
#     print e

# try:
#     ip = '221.204.15.124'
#     print('FTP弱口令漏洞 : ' + str(ip))
#     s = socket.socket()
#     s.connect((str(ip), 21))
#     s.send('langzi \n')
#     cc = s.recv(1024)
#     try:
#         ftp = FTP(ip)
#         ftp.connect(ip, 21)  # 连接 服务器名  端口号
#         ftp.login(str('test'), str('anonymous'))
#         d = ftp.nlst() # ftpB.quit() #退出ftp服务器
#         print d
#
#
#     except Exception,e:
#         print e
# except Exception,e:
#     print e

# try:
#     coon = pymysql.connect(host='61.240.142.124',user='root',passwd='anonymous')
#     cur = coon.cursor()
#     sql = 'show databases;'
#     cur.execute(sql)
#     res = cur.fetchall()
#     if 'Learn' in res:
#         print res
#     else:
#         print 'eooro'
# except Exception,e:
#     print e
# import socket
# ip = '61.240.142.124'
# s = socket.socket()
# s.connect((str(ip), 3306))
# s.send('langzi \n')
# cc = s.recv(1024)
# import chardet
# cd = chardet.detect(cc)
# print cd
# print cc.decode('ISO-8859-1').encode('utf-8')