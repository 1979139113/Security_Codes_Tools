import sys
import pymysql
import threading
import ConfigParser
import time
reload(sys)
sys.setdefaultencoding('utf-8')
cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server","db")
thread_s = cfg.get("Config","thread_s")
listip=[]
iip = str(raw_input('Set IP Address:'))

def start(iip):
    iip_1, iip_2, iip_3, iip_4 = int(iip.split('.')[0]),int(iip.split('.')[1]),int(iip.split('.')[2]),int(iip.split('.')[3])
    for x in range(iip_1,iip_1+1):
        diyi = str(x) + '.'
        for xx in range(0,iip_2+1):
            dier = diyi + str(xx) + '.'
            for xxx in range(0,iip_3+1):
                disan = dier + str(xxx) + '.'
                for xxxx in range(0,iip_4+1):
                    disi = disan + str(xxxx)
                    print '[+] Insert : ' + str(disi)
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_svn = coon_svn.cursor()
                        sql_svn = "INSERT INTO indexx(ip,ipget,datatime) VALUES (%s,%s,%s)"
                        cur_svn.execute(sql_svn, (str(disi), str(0), str(timenow)))
                        coon_svn.commit()
                        cur_svn.close()
                        coon_svn.close()
                    except Exception, e:
                        print e
t1 = threading.Thread(target=start).start()


# def start():
#     for x in range(1,255):
#         diyi = str(x) + '.'
#         for xx in range(1,254):
#             dier = diyi + str(xx) + '.'
#             for xxx in range(1,254):
#                 disan = dier + str(xxx) + '.'
#                 for xxxx in range(1,254):
#                     disi = disan + str(xxxx)
#                     print '[+] Insert : ' + str(disi)
#                     try:
#                         timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#                         coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
#                         cur_svn = coon_svn.cursor()
#                         sql_svn = "INSERT INTO indexx(ip,ipget,datatime) VALUES (%s,%s,%s)"
#                         cur_svn.execute(sql_svn, (str(disi), str(0), str(timenow)))
#                         coon_svn.commit()
#                         cur_svn.close()
#                         coon_svn.close()
#                     except Exception, e:
#                         print e
#t1 = threading.Thread(target=start).start()