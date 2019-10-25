# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bp
#url = 'http://admin.xhmwxy.com/index.php/login'
#url = 'http://admin.51smart.com/login.php'
#url = 'http://zulg.zju.edu.cn/admin.php?c=Index&a=login'
#url = 'http://w.cxzg.com/admin.php/Index/login.html'
#url = 'http://schooladmin.wephp.com/auth/'
#url = 'http://focus-login.focus.cn/login?ru=http://admin.focus.cn'
##url = 'http://admin.zunxiangvpn.com/index.php'
url = 'http://admin.feieyun.com/login.php'
#url = 'http://www.kjxc.cc/'
r = requests.get(url).content
print(r)
bs = bp(r,'html.parser')
#print(bs)
print(len(bs.find_all('input',type="text")))
print(bs.title.text)
# for x in bs.find_all('input',type="text"):
#     print(x['name'])
#
# print ('---')
#
for x in bs.find_all('input',type="password"):
    print(x['name'])

def get_user_password_name(content):
    try:
        users = ''
        bs = bp(content, 'html.parser')
        username = bs.find_all('input',type="text")

        if len(username) == 1:
            users = username[0]['name']


        if not users:
            for n in username:
                if 'user' in n['name'].lower():
                    users = n['name']
                    break
                if 'name' in n['name'].lower():
                    users = n['name']
                    break
                if 'account' in n['name'].lower():
                    users = n['name']
                    break


        password = bs.find_all('input',type="password")

        if len(password) == 1:
            try:
                passs = password[0]['name']
            except:
                passs = 'password'
        else:
            passs = 'password'
        return users,passs
    except Exception as e:
        print(e)

#print(get_user_password_name(r))