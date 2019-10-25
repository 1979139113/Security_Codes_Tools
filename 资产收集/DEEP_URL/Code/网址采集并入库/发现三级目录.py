# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 0004 9:19
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 发现三级目录.py
# @Software: PyCharm
import sys
import re
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
#links = re.findall(r'(\w*\:\/\/[a-zA-Z0-9\.\-\_\/]+)', content)
#links = re.findall(r'(\w*\:\/\/[a-zA-Z0-9\.\-\_\/]+)', content)
def scan(url):
    liss = []
    uu = url.split('//')[1].split('/')[0]
    print uu
    r = requests.get(url).content
    r1 = re.findall('href="(.*?)"',r)
    r2 = re.findall(r'href=."/(.*?/.*?)"',r)
    r3 = re.findall('src="(.*?)" ',r)
    for x in r3:
        if uu in x:
            diyi = x.split('://')[1].split('/')[1]
            if uu in diyi:
                pass
            else:
                dier = url + '/' + diyi
                liss.append(dier)
    for x in r1:
        if uu in x and x.find('=')<0 and x.find('#')<0 and x.find('javascript')<0 :
            if not '.' in x.split('/')[-1]:
                if x.startswith('http://'):
                    if uu == x.split('//')[1].split('/')[0]:
                        #print x
                        liss.append(x)
                else:
                    if uu == str('http://'+x.replace('//','')).split('//')[1].split('/')[0]:
                        xxxr = str('http://'+x.replace('//',''))
                        #print xxxr
                        liss.append(xxxr)
    for x in r2:
        #print x
        if x.find('.')>1 or x.find('www.')>0 or x.find('javascript')>0 or x.find('http')>0 or x.find(' ')>0:
            pass
        else:
            dd = x.split('/')[0]
            liss.append(url+'/'+dd+'/')
            dddd = x.split('/')[0:2]
            e = '/'
            for aa in dddd:
                e+=aa+'/'
            liss.append(url+e)
            ddd = x.split('/')[0:3]
            e = '/'
            for aa in ddd:
                e+=aa+'/'
            liss.append(url+e)
    for x in list(set(liss)): print x + '\n'

scan('http://www.qualityclub.cn')



