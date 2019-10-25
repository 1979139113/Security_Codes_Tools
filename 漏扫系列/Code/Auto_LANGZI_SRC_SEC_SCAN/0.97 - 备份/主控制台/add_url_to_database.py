# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import contextlib
import pymysql
from concurrent.futures import ThreadPoolExecutor
# user = 'root'
# passwd = 'root'
# host = '127.0.0.1'
# Dbname = 'langzi_scan_5'
# port = 3306
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
import time
import random
import configparser
cfg = configparser.ConfigParser()
cfg.read('../Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server", "db")
port = int(cfg.get("Server", "port"))

thread_s = int(cfg.get("Common_Config", "threads"))

check_alive =  int(cfg.get("Start_Console", "check_alive"))


@contextlib.contextmanager
def connect_mysql():
    coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, port=port, charset='utf8')
    cursor = coon.cursor()

    try:
        yield cursor
    except Exception as e:
        print(e)
        pass
    finally:
        coon.commit()
        cursor.close()
        coon.close()

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
    print(url)
    try:
        if check_alive == 1:
            print('开始对网址存活性检测')
            time.sleep(1)
            res = Get_Resp_EN(url)
            if res == None:
                time.sleep(random.randint(5,15))
                time.sleep(random.randint(5,15))
                res = Get_Resp_EN(url)
                if res == None:
                    print('该网址暂时无法访问.....')
                    with open('暂时无法访问的URL.xt','a+',encoding='utf-8')as a:
                        a.write(url+'\n')

                    with connect_mysql() as coon:
                        sql1 = 'insert into Sec_Fail_Links(url) values ("{}")'.format(url.rstrip('/'))
                        coon.execute(sql1)
                else:
                    print('该网址访问成功...')
                    with connect_mysql() as coon:
                        sql = "insert into Sec_Index(url) values  ('{}')".format(url.rstrip('/'))
                        # print(sql)
                        coon.execute(sql)
            else:
                print('该网址访问成功...')
                with connect_mysql() as coon:
                    sql = "insert into Sec_Index(url) values  ('{}')".format(url.rstrip('/'))
                    # print(sql)
                    coon.execute(sql)

        else:
            print('不对网址存活性检测')
            time.sleep(1)
            with connect_mysql() as coon:
                sql = "insert into Sec_Index(url) values  ('{}')".format(url.rstrip('/'))
                # print(sql)
                coon.execute(sql)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    All_Urls = list(set([x.strip().rstrip('/') for x in open('src.txt','r',encoding='utf-8').readlines()]))
    print('总行数:{}'.format(len(All_Urls)))
    time.sleep(2)
    with ThreadPoolExecutor(thread_s*10) as p:
        p.map(run,All_Urls)
    #for Urls in All_Urls:
        #run(Urls)