# coding:utf-8
import os
import time
try:
    result_dir = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())).replace(' ', '')
    os.mkdir(result_dir)
except Exception,e:
    print unicode('无法创建当前目标文件夹 : ', 'gbk')
    print e
    pass
result_name = result_dir + '/' +  str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())).replace(' ','') + '.txt'
print result_name
with open(result_name,'a+')as a:
    a.write('6666666666666666666666666666666666666')