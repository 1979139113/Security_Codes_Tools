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
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
list_gov = []
with open('edu.txt','r')as a:
    for x in a:
        if len(x) > 15:
            if 'cnhtt' in str(x):
                pass
            if ',' in str(x):
                pass
            if ';' in str(x):
                pass
            if '.http' in str(x):
                pass
            if '，' in str(x):
                pass
            if 'gov.cn' in str(x):
                list_gov.append(x.replace('\n',''))
        else:
            pass
listgov = list(set(list_gov))
with open('edu_2.txt','a+')as aa:
    for x in listgov:
        try:
            r = requests.head(url=x,timeout=4)
            print str(x) + '   ' + str(r.status_code)
            if r.status_code == 200:
                aa.write(x + '\n')
        except Exception,e:
            print e

