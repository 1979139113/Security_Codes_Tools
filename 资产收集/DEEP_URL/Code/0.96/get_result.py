# -*- coding: utf-8 -*-
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : main.py
# @Software: PyCharm
import time
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def finset(result_name):
    try:
        timenow = time.time()
        f1  = len([x for x in open(result_name, 'r').readlines()])
        print unicode('     原始数量 : %s','utf-8')%str(f1)
        f = list(set([x.replace('\n', '').replace(' ', '') for x in open(result_name, 'r').readlines()]))
        print unicode('     去重后数量 : %s', 'utf-8') % str(len(f))
        print unicode('     耗时 : %s 秒', 'utf-8') % str(time.time() - timenow)
        print unicode('     开始写入保存', 'utf-8')
        with open(result_name,'w')as a:
            pass
        for x in f:
            with open(result_name, 'a+')as aaa:
                #print x
                if len(x) > 5 and 'http' in x:
                    aaa.write(x.replace('\n', '').replace(' ', '') + '\n')
    except Exception,e:
        print e
        time.sleep(20)
        pass
print unicode('''

    文本去重复，去掉多余空格,去掉不带http的结果
    把文本直接拖拽进来即可
            2018年9月3日16:30:20

''', 'utf-8')

result = raw_input(unicode('文本名 : ', 'utf-8').encode('gbk'))
finset(result)
print unicode('     写入保存完毕', 'utf-8')
os.system('pause')