# -*- coding:utf-8 -*-
# __author__:langzi
# __blog__:www.langzi.fun
import pymysql
import random
from selenium import webdriver
import os
import shutil
import re
import datetime

import configparser
import contextlib
import pymysql
import time
import contextlib
import pymysql
import re
import time
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
from urllib.parse import urlparse,urljoin
import random
from concurrent.futures import ThreadPoolExecutor
import psutil
import os
import time
import shutil
import urllib.parse,os.path,re
import psutil
import os
import time
import shutil


try:
    cfg = configparser.ConfigParser()
    cfg.read('Config.ini')
    user = cfg.get("Server", "username")
    passwd = cfg.get("Server", "password")
    host = cfg.get("Server", "host")
    Dbname = cfg.get("Server", "db")
    port = int(cfg.get("Server", "port"))

    thread_s = int(cfg.get("Common_Config", "threads"))
    check_env = int(cfg.get("Common_Config", "check_env"))

    start_on = int(cfg.get("Start_Console", "start_on"))
    check_alive = int(cfg.get("Start_Console", "check_alive"))

    check_ = '不检测运行环境' if check_env == 0 else '检测运行环境'
    start_ = '从数据库加载数据扫描' if start_on == 1 else '导入文本扫描'


    ExtrUrs = int(cfg.get("Scan_Modules", "ExtrUrs"))
    ExtrSql = int(cfg.get("Scan_Modules", "ExtrSql"))
    ExtrXss = int(cfg.get("Scan_Modules", "ExtrXss"))
    ExtrUrl = int(cfg.get("Scan_Modules", "ExtrUrl"))
    ExtrBac = int(cfg.get("Scan_Modules", "ExtrBac"))
    ExtrLfi = int(cfg.get("Scan_Modules", "ExtrLfi"))
    ExtrAut = int(cfg.get("Scan_Modules", "ExtrAut"))
    ExtrCor = int(cfg.get("Scan_Modules", "ExtrCor"))
    ExtrGis = int(cfg.get("Scan_Modules", "ExtrGis"))
    ExtrSub_Brute = int(cfg.get("Scan_Modules", "ExtrSub_Brute"))
    ExtrSub_Baidu = int(cfg.get("Scan_Modules", "ExtrSub_Baidu"))
    ExtrSub_Web = int(cfg.get("Scan_Modules", "ExtrSub_Web"))
    Keep_Scan = int(cfg.get("Scan_Modules", "Keep_Scan"))

    Scan_Level = int(cfg.get("Scan_Levels", "Scan_Level"))
    Xss_Level = int(cfg.get("Scan_Levels", "Xss_Level"))
    Back_Level = int(cfg.get("Scan_Levels", "Back_Level"))

except Exception as e:
    print('配置文件读取错误 : [{}]'.format(str(e)))
    os.system('pause')
    while 1:
        time.sleep(500)

def run_xss():
    if 'Modules' not in os.getcwd():
        os.chdir('Modules')
    start = 'start ExtrXss.dll'
    end = 'taskkill /F /im ExtrXss.dll'
    while 1:
        os.system(start)
        time.sleep(1800)
        os.system(end)
        time.sleep(3)


def run_app():
    if 'Modules' not in os.getcwd():
        os.chdir('Modules')

    os.system('start ConSole.dll')
    if ExtrUrs == 0:
        print('\033[31;1m超链接提取 : 关闭\033[0m')
    else:
        print('\033[34;1m超链接提取 : 开启\033[0m')
        os.system('start ExtrSLk.dll')

    if ExtrSql == 0:
        print('\033[31;1mSQL注入扫描 : 关闭\033[0m')
    else:
        print('\033[34;1mSQL注入扫描 : 开启\033[0m')
        os.system('start ExtrSql.dll')






    if ExtrUrl == 0:
        print('\033[31;1mURL跳转扫描 : 关闭\033[0m')
    else:
        print('\033[34;1mURL跳转扫描 : 开启\033[0m')
        os.system('start ExtrUrl.dll')


    if ExtrGis == 0:
        print('\033[31;1mGIT/SVN源码扫描 : 关闭\033[0m')
    else:
        print('\033[34;1mGIT/SVN源码扫描 : 开启\033[0m')
        os.system('start ExtrGiS.dll')


##
    if ExtrBac == 0:
        print('\033[31;1m备份源码扫描 : 关闭\033[0m')
    else:
        print('\033[34;1m备份源码扫描 : 开启\033[0m')
        if Back_Level == 1:
            print('备份源码等级 : 1')
            os.system('start ExtrBc1.dll')
        if Back_Level == 2:
            print('备份源码等级 : 2')
            os.system('start ExtrBc2.dll')
        if Back_Level == 3:
            print('备份源码等级 : 3')
            os.system('start ExtrBc3.dll')

    if ExtrXss == 0:
        print('\033[31;1mXSS扫描检测 : 关闭\033[0m')
    else:
        print('\033[34;1mXSS扫描检测 : 开启\033[0m')
        print('XSS扫描检测等级 : '+str(Xss_Level))

#####

    if ExtrLfi == 0:
        print('\033[31;1m任意文件读取 : 关闭\033[0m')
    else:
        print('\033[34;1m任意文件读取 : 开启\033[0m')
        os.system('start ExtrLfi.dll')

####################

    if ExtrAut == 0:
        print('\033[31;1m未授权访问 : 关闭\033[0m')
    else:
        print('\033[34;1m未授权访问 : 开启\033[0m')
        os.system('start ExtrAut.dll')

#########################

    if ExtrCor == 0:
        print('\033[31;1mCORS劫持扫描 : 关闭\033[0m')
    else:
        print('\033[34;1mCORS劫持扫描 : 开启\033[0m')
        os.system('start ExtrCors.dll')

######################

    if ExtrSub_Brute == 0:
        print('\033[31;1m子域名监控 之 子域名爆破 : 关闭\033[0m')
    else:
        print('\033[34;1m子域名监控 之 子域名爆破 : 开启\033[0m')
        os.system('start ExtrSuR.dll')


    if ExtrSub_Baidu == 0:
        print('\033[31;1m子域名监控 之 搜索引擎提取 : 关闭\033[0m')
    else:
        print('\033[34;1m子域名监控 之 搜索引擎提取 : 开启\033[0m')
        os.system('start ExtrSuB.dll')



    if ExtrSub_Web == 0:
        print('\033[31;1m子域名监控 之 网页爬行提取 : 关闭\033[0m')
    else:
        print('\033[34;1m子域名监控 之 网页爬行提取 : 开启\033[0m')
        os.system('start ExtrSuS.dll')


        #run_xss()
        #os.system('start ExtrXss.dll')
#

@contextlib.contextmanager
def connect_mysql():
    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
    cursor = coon.cursor()
    try:
        yield cursor
    except Exception as e:
        if 'Duplicate entry' in str(e):
            print('数据库已存在该网址')
    finally:
        coon.commit()
        cursor.close()
        coon.close()


class Check_Env:
    def __init__(self):
        print('\n')
        print('******配置文件相关信息***')
        print(f'账号:{user}')
        print(f'密码:{passwd}')
        print(f'线程:{thread_s}')
        print(f'端口号:{port}')
        print(f'数据库:{Dbname}')
        print(f'检测环境:{check_}')
        print(f'扫描文件:{start_}')
        print('******配置文件相关信息******')
        self.envinu = 1
        print('\n')

        time.sleep(5)

    def check_mysql(self):
        try:
            time.sleep(2)
            print('\n')
            print('[*] 开始数据库检测......')
            coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
            print('[+] 数据库连接成功')
            coon.close()
        except Exception as e:
            print('[-] 数据库连接失败[{}]'.format(str(e)))
            self.envinu = 0
            os.system('pause')

    def check_python(self):
        try:
            time.sleep(2)
            print('\n')
            print('[*] 开始Python2环境检测......')
            content = os.popen('python _py2.py')
            res = int(content.read())
            if res == 2:
                print('[+] Python 2.x 环境安装成功')
            else:
                print('[-] Python 2.x 环境未安装')
                self.envinu = 0

                os.system('pause')
        except Exception as e:
            print('[-] Python 2.x 环境检查失败[{}]'.format(str(e)))
            self.envinu = 0

            os.system('pause')

    def check_mod(self):
        dlls = ['ExtrAut.dll','ExtrBc1.dll','ExtrBc2.dll','ExtrBc3.dll','ExtrCors.dll','ExtrGiS.dll',
                'ExtrLfi.dll','ExtrSLk.dll','ExtrSql.dll','ExtrSuB.dll','ExtrSuR.dll','ExtrSuS.dll',
                'ExtrUrl.dll','ExtrXss.dll']
        _ck = 0
        try:
            time.sleep(2)

            print('\n')

            print('[*] 开始扫描功能模块......')
            if 'Modules' not in os.getcwd():
                os.chdir('Modules')
            all_files = os.listdir()
            for i in dlls:
                if i in all_files:
                    pass
                else:
                    _ck = 1
            if _ck == 0:
                print('[+] 扫描功能模块齐全')
            else:
                print('[-] 扫描功能模块不齐全')
                self.envinu = 0
                os.system('pause')
        except Exception as e:
            print('[-] 扫描功能模块检测失败[{}]'.format(str(e)))
            self.envinu = 0
            os.system('pause')

    def check_selenium(self):
        try:
            time.sleep(2)

            print('\n')

            print('[*] 开始FireFox浏览器检测......')
            dirver = webdriver.Firefox()
            dirver.get('http://www.langzi.fun')
            time.sleep(3)
            dirver.close()
            print('[+] FireFox 安装成功')
        except Exception as e:
            print('[-] FireFox 未成功安装 [{}]'.format(str(e)))
            self.envinu = 0

            os.system('pause')

    def check_docx(self):
        try:
            time.sleep(2)

            print('\n')

            print('[*] 开始原DOCX报表文件检测......')
            if os.path.exists('default.docx'):
                print('[+] 存在自动报表目标文件')
            else:
                print('[-] 当前目录不存在自动报表目标文件')
                self.envinu = 0

                os.system('pause')
        except Exception as e:
            print('[-] 检查文档失败 [{}]'.format(str(e)))
            self.envinu = 0

            os.system('pause')

    def start_check(self):
        self.check_mysql()
        self.check_python()
        self.check_mod()
        self.check_docx()
        self.check_selenium()

        if self.envinu == 1:
            print('\n----------------------------------------------------')
            print('-------------运行环境检测完毕状态正常---------------')
            print('----------------------------------------------------')
            time.sleep(5)
            print('\n')
        else:
            print('----------------------------------------------------')
            print('-------------运行环境检测完毕状态异常---------------')
            print('----------------------------------------------------')
            os.system('pause')
            while 1:
                time.sleep(500)




def Get_Resp_EN(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    try:
        r = requests.get(url,headers=headers,timeout=20,verify=False)
        return r.content
    except:
        return None

def run(url):

    try:
        if check_alive == 1:
            time.sleep(1)
            res = Get_Resp_EN(url)
            if res == None:
                time.sleep(random.randint(5,15))
                time.sleep(random.randint(5,15))
                res = Get_Resp_EN(url)
                if res == None:
                    print('该网址暂时无法访问 : {}'.format(url))
                    with open('暂时无法访问的URL.xt','a+',encoding='utf-8')as a:
                        a.write(url+'\n')
                    with connect_mysql() as coon:
                        sql1 = 'insert into Sec_Fail_Links(url) values ("{}")'.format(url.rstrip('/'))
                        coon.execute(sql1)
                else:
                    print('该网址访问成功 : {}'.format(url))
                    with connect_mysql() as coon:
                        sql = "insert into Sec_Index(url) values  ('{}')".format(url.rstrip('/'))
                        # print(sql)
                        coon.execute(sql)
            else:
                print('该网址访问成功 : {}'.format(url))
                with connect_mysql() as coon:
                    sql = "insert into Sec_Index(url) values  ('{}')".format(url.rstrip('/'))
                    # print(sql)
                    coon.execute(sql)

        else:
            print('插入网址到数据库 : {}'.format(url))
            with connect_mysql() as coon:
                sql = "insert into Sec_Index(url) values  ('{}')".format(url.rstrip('/'))
                coon.execute(sql)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    print(r'''
         __                                              
        /\ \                                       __    
        \ \ \         __      ___      __   ____  /\_\   
         \ \ \  __  /'__`\  /' _ `\  /'_ `\/\_ ,`\\/\ \  
          \ \ \L\ \/\ \L\.\_/\ \/\ \/\ \L\ \/_/  /_\ \ \ 
           \ \____/\ \__/.\_\ \_\ \_\ \____ \/\____\\ \_\
            \/___/  \/__/\/_/\/_/\/_/\/___L\ \/____/ \/_/
                                       /\____/           
                                       \_/__/           
                                       
                                       Langzi_SRC_Safe_Cruise_0.97
                                       
    ''')
    time.sleep(3)

    a = Check_Env()
    if check_env == 1:
        a.start_check()
    import threading
    run_app()
    time.sleep(5)

    if 'Modules' in os.getcwd():
        os.chdir('..')

    if start_on == 0:
        print('\n\n')
        print('导入网址准备入库扫描')
        inp_url = input('Input Target Url.txt:')
        All_Urls = []
        try:
            #All_Url = list(set([x.strip() for x in open(inp_url.replace('"',''),'r',encoding='utf-8').readlines()]))
            All_Url = filter(lambda x: 'gov.cn' not in x and 'edu.cn' not in x,
                   list(set([x.strip() for x in open(inp_url.replace('"',''),'r',encoding='utf-8').readlines()])))
        except Exception as e:
            print('文件打开错误 : [{}]'.format(str(e)))
            os.system('pause')
            while 1:
                time.sleep(500)

        All_Urls = All_Url


        if check_alive == 1:
            print('开始对网址存活性检测')
        else:
            print('不对网址存活性检测')

        with ThreadPoolExecutor(5) as p:
            p.map(run,All_Urls)

        print('\n\n----------------------------------------------------')
        print('--------------[+] 网址保存到数据库成功--------------')
        print('----------------------------------------------------\n\n')
        print('保持主控制台运行状态......')

        if ExtrXss == 1:
            run_xss()

        os.system('color a')
        while 1:
            time.sleep(500)
    if start_on == 1:
        print('\n\n----------------------------------------------------')
        print('--------------开始从数据库提取数据扫描--------------')
        print('----------------------------------------------------\n\n')

        time.sleep(5)
        print('保持主控制台运行状态......')
        os.system('color a')
        if ExtrXss == 1:
            run_xss()
        while 1:
            time.sleep(500)