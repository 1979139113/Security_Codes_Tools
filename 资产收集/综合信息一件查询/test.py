# -*- coding: utf-8 -*-
import multiprocessing
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import requests
import random
import time
import masscan
import os
import socket

from tinydb import TinyDB, where
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
from collections import namedtuple

Port = namedtuple("Port", ["name", "port", "protocol", "description"])

__BASE_PATH__ = os.path.dirname(os.path.abspath(__file__))
__DATABASE_PATH__ = os.path.join(__BASE_PATH__, 'ports.json')
__DB__ = TinyDB(__DATABASE_PATH__, storage=CachingMiddleware(JSONStorage))


def get_ports(port, like=False):
    """
    This function creates the SQL query depending on the specified port and
    the --like option.

    :param port: the specified port
    :param like: the --like option
    :return: all ports matching the given ``port``
    :rtype: list
    """
    where_field = "port" if port.isdigit() else "name"
    if like:
        ports = __DB__.search(where(where_field).search(port))
    else:
        ports = __DB__.search(where(where_field) == port)
    try:
        return ports[0]  # flake8: noqa (F812)
    except:
        return []

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

# url,title,weights,ip,ages,whois_id,whois_type,whois_name,whois_time
# 网址，标题，百度权重，ip信息，年龄，备案号，备案性质，备案名称，备案时间
# include_baidu,request,text,service,language
# 百度收录，，协议类型，页面类型，服务器类型，程序语言
title_parrten = 'class="w61-0"><div class="ball">(.*?)</div></td>'  # group(1) 正常
ip_parrten = '>IP：(.*?)</a></div>'  # group(1) 正常
# 下面会报错
ages = '" target="_blank">(.*?)</a></div></div>'  # group(1)
whois_id = '备案号：</span><a href=.*?" target="_blank">(.*?)</a></div>'  # 需group(1)
whois_type = '<span>性质：</span><strong>(.*?)</strong></div>'  # 需group(1)
whois_name = '<span>名称：</span><strong>(.*?)</strong></div>'  # 需group(1)
whois_time = '<span>审核时间：</span><strong>(.*?)</strong></div>'  # 需group(1)
include_baidu = '<div class="Ma01LiRow w12-1 ">(.*?)</div>'  # group(1)
infos = '<div class="MaLi03Row w180">(.*?)</div>'  # 要findall 0，1，2，3



def get_ipinfomation(lis):
    # 该函数的作用是传入一个列表
    infos_ = []
    for ip in lis:
        print ip
        d = get_ports(str(ip))
        print d
        if d != []:
            infos_.append('端口:' + str(ip) + '\n服务:' + str(d['name']) + '\n功能:' + str(d['description']) + '\n')
        else:
            infos_.append(str(ip) + ':' + str('识别失败'))

    return infos_

print get_ipinfomation([49152, 49153, 49154, 49155, 49156, 135, 80, 3389])

def get_ips(ip):
    url_ip = ip
    url_port = []
    try:
        mas = masscan.PortScanner()
        mas.scan(url_ip)
        url_port = mas.scan_result['scan'][url_ip]['tcp'].keys()
    except:
        url_port = [80]

    if 80 in url_port:
        pass
    else:
        url_port.append(80)
    print url_port
    try:
        infos = {}
        infos['开放端口'] = str(url_port)
        infos['端口信息'] = str(get_ipinfomation(url_port))
        return infos
    except Exception,e:
        print e


# print get_ips('118.24.11.235')






def get_info(pattren, result):
    try:
        res = re.search(pattren, result).group(1)
        return res
    # return str(res.encode('utf-8'))
    except:
        return '暂无信息'


def iiip(url):
    try:
        return socket.gethostbyname(url.replace('https://', '').replace('http://', '').replace('/', '').replace('www.', ''))
    except:
        return '获取失败'

def scan_seo(url):
    print 'Scan : ' + url
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    urls = 'http://seo.chinaz.com/' + url.replace('https://', '').replace('http://', '').replace('/', '').replace(
        'www.', '')
    # url,title,weights,ip,ages,whois_id,whois_type,whois_name,whois_time
    # 网址，标题，百度权重，ip信息，年龄，备案号，备案性质，备案名称，备案时间
    # include_baidu,request,text,service,language
    # 百度收录，，协议类型，页面类型，服务器类型，程序语言
    res = {}
    try:
        r = requests.get(urls, headers, timeout=5).content
    except Exception, e:
        print e
        return False
    res['百度权重'] = str(get_baidu_weights(url))
    res['网站网址'] = url
    res['网站标题'] = get_info(title_parrten, r)
    ip_infos= get_info(ip_parrten, r)
    if '[' in ip_infos:
        ip,address = ip_infos.split('[')[0],ip_infos.split('[')[1]
        ress = get_ips(ip)
        res['IP__坐标'] = address.replace(']','')
        res['所属__IP'] = ip
        res.update(ress)
    else:
        res['IP__坐标'] = '暂无信息'
        res['所属__IP'] = iiip(url)
        ress = get_ips(iiip(url))
        res.update(ress)
    res['网站年龄'] = get_info(ages, r)
    res['备案编号'] = get_info(whois_id, r)
    res['备案性质'] = get_info(whois_type, r)
    res['备案名称'] = get_info(whois_name, r)
    res['备案时间'] = get_info(whois_time, r)
    res['百度收录'] = get_info(include_baidu, r)

    dd = re.findall(infos, r, re.S)
    resu = ['暂无信息' if x.replace(' ', '') is '' else x for x in dd]
    res['协议类型'] = resu[0]
    res['页面类型'] = resu[1]
    res['服务类型'] = resu[2]
    res['程序语言'] = resu[3]
    return res

