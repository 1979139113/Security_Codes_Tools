import os
import time
import socket

os.system('pip install tornado')
os.system('pip install selenium')

 
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        print(ip)
    finally:
        s.close()
 
    return ip
def connect(t):
    name="宽带连接"
    username="123456"
    password="123456"
    cmd_str="rasdial %s %s %s" %(name,username,password)
    res=os.system(cmd_str)
    if res==0:
        print("connect successful")
    else:
        print(res)
    time.sleep(t)
def disconnect(t):
    cmd_str='rasdial 宽带连接 /disconnect'
    os.system(cmd_str)
    print('disconnect already')
    time.sleep(t)
while True:
    connect(5)
    get_host_ip()
    time.sleep(5)
    disconnect(0.1)
