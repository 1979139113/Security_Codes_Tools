# coding:utf-8
a = list(set(x.replace('\n','') for x in open('1.txt','r').readlines()))
import sys
for x in a:
    sys.stdout.write('|'+x)
