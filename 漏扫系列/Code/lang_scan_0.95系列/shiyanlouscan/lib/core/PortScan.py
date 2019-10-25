#!/usr/bin/env python
# __author__= 'w8ay'

import socket
import threading
import Queue

class PortScan:
    def __init__(self,ip="localhotst",threadNum = 5):
        self.PORT = {80:"web",8080:"web",3311:"kangle",3312:"kangle",3389:"mstsc",4440:"rundeck",5672:"rabbitMQ",5900:"vnc",6082:"varnish",7001:"weblogic",8161:"activeMQ",8649:"ganglia",9000:"fastcgi",9090:"ibm",9200:"elasticsearch",9300:"elasticsearch",9999:"amg",10050:"zabbix",11211:"memcache",27017:"mongodb",28017:"mondodb",3777:"dahua jiankong",50000:"sap netweaver",50060:"hadoop",50070:"hadoop",21:"ftp",22:"ssh",23:"telnet",25:"smtp",53:"dns",123:"ntp",161:"snmp",8161:"snmp",162:"snmp",389:"ldap",443:"ssl",512:"rlogin",513:"rlogin",873:"rsync",1433:"mssql",1080:"socks",1521:"oracle",1900:"bes",2049:"nfs",2601:"zebra",2604:"zebra",2082:"cpanle",2083:"cpanle",3128:"squid",3312:"squid",3306:"mysql",4899:"radmin",8834:'nessus',4848:'glashfish'}
        self.threadNum = threadNum
        self.q = Queue.Queue()
        self.ip = ip
        for port in self.PORT.keys():
            self.q.put(port)

    def _th_scan(self): 
        while not self.q.empty():
            port = self.q.get()
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
            s.settimeout(1) 
            try:
                s.connect((self.ip, port))
                print "%s:%s OPEN [%s]"%(self.ip,port,self.PORT[port])
            except:
                print "%s:%s Close"%(self.ip,port)
            finally:
                s.close()

    def work(self):
        threads = []
        for i in range(self.threadNum):
            t = threading.Thread(target=self._th_scan())
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print('[*] The scan is complete!')