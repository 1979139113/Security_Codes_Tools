# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import subprocess
import re

def scan_vlun(url):
    '''
    所有的伪静态注入，动态注入都加载一起扫描
    - 扫描等级 1 2 3
       -  扫描 url
            - 获取的结果进行判断，获取最终的结果
    :param url:
    '''
    common_0 = 'sqlmap.py -u '