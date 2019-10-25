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
#coding:utf-8
import time
import sys
import random
import os
i=0
setpid = str(raw_input("SET name:"))
settime = int(raw_input("SET time:"))
def start():
    time.sleep(10)
    os.popen('start '+ setpid + '.exe')
    time.sleep(int(settime))
    os.popen('taskkill /f /t /im '+str(setpid)+ '.exe')

while 1:
    i+=1
    print unicode(str('[*]程序第 '+str(i)+' 次运行....'),'utf-8')
    start()
