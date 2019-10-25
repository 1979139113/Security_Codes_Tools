# -*- coding: utf-8 -*-

import os
import time
result_name = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())).replace(' ', '') + '.txt'


def success(xx):
    with open(str(result_name),'a+')as a:
        a.write(xx + '\n')

def scan(x):
    a,b = x.split(' ',1)[0],x.split(' ',1)[1]
    a1,a2,a3,a4 = a.split('.')[0],a.split('.')[1],a.split('.')[2],a.split('.')[3]
    b1,b2,b3,b4 = b.split('.')[0],b.split('.')[1],b.split('.')[2],b.split('.')[3]
    try:
        for c1 in range(int(a1),int(b1)+1):
            for c2 in range(int(a2),int(b2)+1):
                for c3 in range(int(a3),int(b3)+1):
                    for c4 in range(int(a4),int(b4)+1):
                        dd = str(c1) + '.' + str(c2) + '.' + str(c3) + '.' + str(c4)
                        success(dd)
    except Exception,e:
        print e

print '\n'
urltxt = raw_input(unicode('输入网址文本名(可拖拽进来) : ', 'utf-8').encode('gbk'))
urllist = list(set([x.replace('\n', '') for x in open(urltxt, 'r').readlines()]))

# 单线程
print unicode('开始转换，稍等','utf-8')
for x in urllist:
    scan(x)
print unicode('转换完成','utf-8')



os.system('pause')
