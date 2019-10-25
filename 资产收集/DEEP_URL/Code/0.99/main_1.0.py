# coding:gbk
import requests
import threading
from multiprocessing.dummy import Pool as ThreadPool
import time
import re
from bs4 import BeautifulSoup as bs
import ConfigParser
import sys
import urllib
import os
import chardet
import random
import datetime
import sqlite3
lo = threading.Lock()
requests.packages.urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('gbk')

first_cule = ['.com.cn', '.org.cn', '.net.cn', '.com', '.cn', '.cc', '.net', '.org', '.info', '.fun', '.one', '.xyz',
              '.name', '.io', '.top', '.me', '.club', '.tv']

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

UA = random.choice(headerss)
headers = {'User-Agent': UA, 'Connection': 'close'}

cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
users = cfg.get("User", "whoami")
titles = cfg.get('Config', 'title')
black_titles = cfg.get('Config', 'black_title')
urls = cfg.get('Config', 'url')
black_urls = cfg.get('Config', 'black_url')
contents = cfg.get('Config', 'content')
black_contents = cfg.get('Config', 'black_content')
forever = int(cfg.get('Config', 'forever'))
timeout = int(cfg.get('Config', 'timeout'))
url_threads = int(cfg.get('Config', 'url_thread'))
check_threads = int(cfg.get('Config', 'check_thread'))
track = int(cfg.get('Config', 'track'))
white = int(cfg.get('Config', 'white_or'))
print ('''
         _                           _ 
        | |                         (_)
        | |     __ _ _ __   __ _ _____ 
        | |    / _` | '_ \ / _` |_  / |
        | |___| (_| | | | | (_| |/ /| |
        |______\__,_|_| |_|\__, /___|_|
                            __/ |      
                           |___/            

                    URL collection V 0.99
                    Author : Langzi
                    Blog   : langzi.fun   
''')
time.sleep(2)

# �������ļ��У����ݿⱣ�����ļ�������

result_dir = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())).replace(' ', '')
os.mkdir(result_dir)
db = 'URLS.db'
result_name = result_dir + '/' + 'result.txt'





print unicode('��ǰ�û� : ', 'gbk') + users

def success_write(url):
    with open(result_dir + '/' +'result.txt','a+')as a:
        a.write(url + '\n')

def log(*args):
    with open('log.txt', 'a+')as aa:
        for x in args:
            aa.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + ':' + x + '\n')


with open('log.txt', 'a+')as aa:
    aa.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + ' - ' + '��ַ�ɼ���ʼ' + '\n')

log((' [*] �������� : ��ǰ�û� : ' + users).decode('gbk'))

first_list_for_test = []
first_list_for_test.append(urls)
first_list_for_test.append(black_urls)
first_list_for_test.append(titles)
first_list_for_test.append(black_titles)
first_list_for_test.append(contents)
first_list_for_test.append(black_contents)
list_for_and = []
list_for_or = []
for x in first_list_for_test:
    if x.find('&') > 0:
        list_for_and.append(x)
    if x.find('|') > 0:
        list_for_or.append(x)
    if x.find('|') > 0 and x.find('&') > 0:
        print unicode('�ð汾�ݲ�֧�ֶ������', 'gbk')
        log((' [*] �������� : ' + '�ð汾�ݲ�֧�ֶ������').decode('gbk'))
        print unicode('��ʵ����|��&����ͬʱ����ͬһ�������', 'gbk')
        log((' [*] �������� : ' + '��ʵ����|��&����ͬʱ����ͬһ�������').decode('gbk'))
        time.sleep(2000)

list_for_and_url = []
list_for_and_title = []
list_for_and_content = []
list_for_or_url = []
list_for_or_title = []
list_for_or_content = []
list_for_and_black_url = []
list_for_and_black_title = []
list_for_and_black_content = []
list_for_or_black_url = []
list_for_or_black_title = []
list_for_or_black_content = []

if users == 'Langzi':
    pass
else:
    os.system('color a')
print '\n'
if track == 0:
    print unicode('���������� : �ر�', 'gbk')
    log((' [*] �������� : ���������� : �ر�').decode('gbk'))
if track == 1:
    print unicode('���������� : ����', 'gbk')
    log((' [*] �������� : ���������� : ����').decode('gbk'))

if track != 0 and track != 1:
    print unicode('Config.ini �� track ���ô���', 'gbk')
    log((' [*] �������� : Config.ini �� track ���ô���').decode('gbk'))
    time.sleep(200)

if white == 0:
    print unicode('���������� : �ر�', 'gbk')
    log((' [*] �������� : ���������� : �ر�').decode('gbk'))
if white == 1:
    print unicode('���������� : ����', 'gbk')
    log((' [*] �������� : ���������� : ����').decode('gbk'))

if white != 0 and white != 1:
    print unicode('Config.ini �� white_or ���ô���', 'gbk')
    log((' [*] �������� : Config.ini �� white_or ���ô���').decode('gbk'))
    time.sleep(200)

if forever == 0:
    print unicode('���޲ɼ��� : �ر�', 'gbk')
    log((' [*] �������� : ���޲ɼ��� : �ر�').decode('gbk'))
if forever == 1:
    print unicode('���޲ɼ��� : ����', 'gbk')
    log((' [*] �������� : ���޲ɼ��� : ����').decode('gbk'))
if forever !=0 and forever != 1:
    print unicode('Config.ini �� forever ���ô���', 'gbk')
    log((' [*] �������� : Config.ini �� forever ���ô���').decode('gbk'))
    time.sleep(200)

if forever == 0 and track == 1:
    print unicode('[����] : �������п�����δ������������', 'gbk')
    log((' [*] �������� : [����] : �������п�����δ������������').decode('gbk'))
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)

if forever > 0 and track == 0:
    print unicode('[����] : ���д������� 0 ��δ������������', 'gbk')
    log((' [*] �������� : [����] : ���д������� 0 ��δ������������').decode('gbk'))
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)

if urls.find('&') > 0:
    d = urls.split('&')
    print unicode('��ַ������ : ��ַ����ͬʱ�������¹��򼴿ɱ����', 'gbk')
    for x, y in enumerate(d):
        list_for_and_url.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if urls.find('|') > 0:
    d = urls.split('|')
    print unicode('��ַ������ : ��ַ����������¹���֮һ���ɱ����', 'gbk')
    for x, y in enumerate(d):
        list_for_or_url.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if urls.find('&') < 0 and urls.find('|') < 0 and urls != 'None':
    print unicode('��ַ������ : ��ַ����������¹���֮һ���ɱ����', 'gbk')
    print  '     0:' + unicode(urls, 'gbk')
    list_for_and_url.append(urls)
if urls == 'None':
    print unicode('��ַ������ : �������ַ�������������ϵ', 'gbk')
if black_urls == 'None':
    print unicode('��ַ������ : �������ַ���ų���������ϵ', 'gbk')
if black_urls.find('&') > 0:
    d = black_urls.split('&')
    print unicode('��ַ������ : ��ַ����ͬʱ�������¹���Żᱻ�ų�', 'gbk')
    for x, y in enumerate(d):
        list_for_and_black_url.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if black_urls.find('|') > 0:
    d = black_urls.split('|')
    print unicode('��ַ������ : ��ַ����������¹���֮һ���ɱ��ų�', 'gbk')
    for x, y in enumerate(d):
        list_for_or_black_url.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if black_urls.find('&') < 0 and black_urls.find('|') < 0 and black_urls != 'None':
    print unicode('��ַ������ : ��ַ����������¹���֮һ���ɱ��ų�', 'gbk')
    print  '     0:' + unicode(black_urls, 'gbk')
    list_for_or_black_url.append(black_urls)

if titles.find('&') > 0:
    d = titles.split('&')
    print unicode('��������� : ��������ͬʱ�������¹��򼴿ɱ����', 'gbk')
    for x, y in enumerate(d):
        list_for_and_title.append(y)
        print '     ' + str(x) + ':' + unicode(y, 'gbk')

if titles.find('|') > 0:
    d = titles.split('|')
    print unicode('��������� : �������������¹���֮һ���ɱ����', 'gbk')
    for x, y in enumerate(d):
        list_for_or_title.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if titles == 'None':
    print unicode('��������� : ���������������������ϵ', 'gbk')
if titles.find('&') < 0 and titles.find('|') < 0 and titles != 'None':
    print unicode('��������� : �������������¹���֮һ���ɱ����', 'gbk')
    print  '     0:' + unicode(titles, 'gbk')
    list_for_and_title.append(titles)
if black_titles.find('&') > 0:
    d = black_titles.split('&')
    print unicode('��������� : ��������ͬʱ�������¹���Żᱻ�ų�', 'gbk')
    for x, y in enumerate(d):
        list_for_and_black_title.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if black_titles.find('|') > 0:
    d = black_titles.split('|')
    print unicode('��������� : �������������¹���֮һ���ɱ��ų�', 'gbk')
    for x, y in enumerate(d):
        list_for_or_black_title.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if black_titles == 'None':
    print unicode('��������� : �����������ų���������ϵ', 'gbk')
if black_titles.find('&') < 0 and black_titles.find('|') < 0 and black_titles != 'None':
    print unicode('��������� : �������������¹���֮һ���ɱ��ų�', 'gbk')
    print  '     0:' + unicode(black_titles, 'gbk')
    list_for_or_black_title.append(black_titles)

if contents.find('&') > 0:
    d = contents.split('&')
    print unicode('��ҳ������ : ��ҳ����ͬʱ�������¹��򼴿ɱ����', 'gbk')
    for x, y in enumerate(d):
        list_for_and_content.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if contents.find('|') > 0:
    d = contents.split('|')
    print unicode('��ҳ������ : ��ҳ����������¹���֮һ���ɱ����', 'gbk')
    for x, y in enumerate(d):
        list_for_or_content.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if contents == 'None':
    print unicode('��ҳ������ : �������ҳ�������������ϵ', 'gbk')
if contents.find('&') < 0 and contents.find('|') < 0 and contents != 'None':
    print unicode('��ҳ������ : ��ҳ����������¹���֮һ���ɱ����', 'gbk')
    print  '     0:' + unicode(contents, 'gbk')
    list_for_and_content.append(contents)

if black_contents.find('&') > 0:
    d = black_contents.split('&')
    print unicode('��ҳ������ : ��ҳ����ͬʱ�������¹���Żᱻ�ų�', 'gbk')
    for x, y in enumerate(d):
        list_for_and_black_content.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if black_contents.find('|') > 0:
    d = black_contents.split('|')
    print unicode('��ҳ������ : ��ҳ����������¹���֮һ���ɱ��ų�', 'gbk')
    for x, y in enumerate(d):
        list_for_or_black_content.append(y)
        print  '     ' + str(x) + ':' + unicode(y, 'gbk')
if black_contents == 'None':
    print unicode('��ҳ������ : �������ҳ���ų���������ϵ', 'gbk')
if black_contents.find('&') < 0 and black_contents.find('|') < 0 and black_contents != 'None':
    print unicode('��ҳ������ : ��ҳ����������¹���֮һ���ɱ��ų�', 'gbk')
    print  '     0:' + unicode(black_contents, 'gbk')
    list_for_or_black_content.append(black_contents)

list_for_and_url = list(set(list_for_and_url))
list_for_and_title = list(set(list_for_and_title))
list_for_and_content = list(set(list_for_and_content))
list_for_or_url = list(set(list_for_or_url))
list_for_or_title = list(set(list_for_or_title))
list_for_or_content = list(set(list_for_or_content))
list_for_and_black_url = list(set(list_for_and_black_url))
list_for_and_black_title = list(set(list_for_and_black_title))
list_for_and_black_content = list(set(list_for_and_black_content))
list_for_or_black_url = list(set(list_for_or_black_url))
list_for_or_black_title = list(set(list_for_or_black_title))
list_for_or_black_content = list(set(list_for_or_black_content))


# ���й����жϣ�����Ҫ��Ļ�д�뱾��
def cure(url, title, content):
    if white == 0:
        # print unicode('�ų���ַ����������������ַ : ', 'gbk') + url
        if list_for_or_black_url != []:
            for x in list_for_or_black_url:
                if x in url:
                    print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�д��� : %s', 'gbk') % x
                    log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�д��� : %s', 'gbk') % x))
                    return False
        if list_for_and_black_url != []:
            i = 0
            for x in list_for_and_black_url:
                if x in url:
                    i += 1
                else:
                    i = 0
            if i == len(list_for_and_black_url):
                print url + ' : ' + unicode('�ų�ԭ�� : ��ַ��ͬʱ���� : %s', 'gbk') % '|'.join(list_for_and_black_url).decode(
                    'gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ��ͬʱ���� : %s', 'gbk') % '|'.join(
                    list_for_and_black_url).decode('gbk')))
                return False
        if list_for_and_url != []:
            i = 0
            for x in list_for_and_url:
                if x in url:
                    pass
                else:
                    xx = x
                    i = 1
            if i == 1:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�в����� : %s', 'gbk') % xx
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�в����� : %s', 'gbk') % xx))
                return False
            else:
                pass
        # print unicode('�ų���ַ����������������ַ : ', 'gbk') + url
        if list_for_or_black_title != []:
            for x in list_for_or_black_title:
                if x.decode('gbk') in title:
                    print url + ' : ' + unicode('�ų�ԭ�� : �����д��� : %s', 'gbk') % x
                    log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : �����д��� : %s', 'gbk') % x))
                    return False
        if list_for_and_black_title != []:
            i = 0
            for x in list_for_and_black_title:
                if x.decode('gbk') in title:
                    i += 1
                else:
                    i = 0
            if i == len(list_for_and_black_title):
                print url + ' : ' + unicode('�ų�ԭ�� : ������ͬʱ���� : %s', 'gbk') % '|'.join(list_for_and_black_title).decode(
                    'gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ������ͬʱ���� : %s', 'gbk') % '|'.join(
                    list_for_and_black_title).decode('gbk')))
                return False

        if list_for_or_black_content != []:
            for x in list_for_or_black_content:
                if x.decode('gbk') in content:
                    print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�д��� : %s', 'gbk') % x
                    log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�д��� : %s', 'gbk') % x))
                    return False
        if list_for_and_black_content != []:
            i = 0
            for x in list_for_and_black_content:
                if x.decode('gbk') in content:
                    i += 1
                else:
                    i = 0
            if i == len(list_for_and_black_content):
                print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ��ͬʱ���� : %s', 'gbk') % '|'.join(list_for_and_black_content).decode(
                    'gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ��ͬʱ���� : %s', 'gbk') % '|'.join(
                    list_for_and_black_content).decode('gbk')))
                return False
        ##--------------------------��ɶ��

        if list_for_and_title != []:
            i = 0
            for x in list_for_and_title:
                if x.decode('gbk') in title:
                    pass
                else:
                    xx = x
                    i = 1
            if i == 1:
                print url + ' : ' + unicode('�ų�ԭ�� : �����в����� : %s', 'gbk') % xx
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : �����в����� : %s', 'gbk') % xx))
                return False
            else:
                pass
        if list_for_and_content != []:
            i = 0
            for x in list_for_and_content:
                if x.decode('gbk') in content:
                    pass
                else:
                    xx = x
                    i = 1
            if i == 1:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�в����� : %s', 'gbk') % xx
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�в����� : %s', 'gbk') % xx))
                return False
            else:
                pass

        if list_for_or_url != []:
            i = 0
            for x in list_for_or_url:
                if x in url:
                    i = 1
            if i == 0:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�нԲ����� : %s', 'gbk') % '|'.join(list_for_or_url).decode('gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�нԲ����� : %s', 'gbk') % '|'.join(
                    list_for_or_url).decode('gbk')))
                return False
        if list_for_or_title != []:
            i = 0
            for x in list_for_or_title:
                if x.decode('gbk') in title:
                    i = 1
            if i == 0:
                print url + ' : ' + unicode('�ų�ԭ�� : �����нԲ����� : %s', 'gbk') % '|'.join(list_for_or_title).decode('gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : �����нԲ����� : %s', 'gbk') % '|'.join(
                    list_for_or_title).decode('gbk')))
                return False
        if list_for_or_content != []:
            i = 0
            for x in list_for_or_content:
                if x.decode('gbk') in content:
                    i = 1
            if i == 0:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�нԲ����� : %s', 'gbk') % '|'.join(list_for_or_content).decode('gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�нԲ����� : %s', 'gbk') % '|'.join(
                    list_for_or_content).decode('gbk')))
                return False

        try:
            print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
            log((' [+] ��ַд�� : ' + url).decode('gbk'))
            success_write(url)
        except Exception, e:
            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
            pass

    if white == 1:
        if list_for_or_black_url != []:
            for x in list_for_or_black_url:
                if x in url:
                    print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�д��� : %s', 'gbk') % x
                    log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�д��� : %s', 'gbk') % x))
                    return False
        if list_for_and_black_url != []:
            i = 0
            for x in list_for_and_black_url:
                if x in url:
                    i += 1
                else:
                    i = 0
            if i == len(list_for_and_black_url):
                print url + ' : ' + unicode('�ų�ԭ�� : ��ַ��ͬʱ���� : %s', 'gbk') % '|'.join(list_for_and_black_url).decode(
                    'gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ��ͬʱ���� : %s', 'gbk') % '|'.join(
                    list_for_and_black_url).decode('gbk')))
                return False
        if list_for_or_black_title != []:
            for x in list_for_or_black_title:
                if x.decode('gbk') in title:
                    print url + ' : ' + unicode('�ų�ԭ�� : �����д��� : %s', 'gbk') % x
                    log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : �����д��� : %s', 'gbk') % x))
                    return False
        if list_for_and_black_title != []:
            i = 0
            for x in list_for_and_black_title:
                if x.decode('gbk') in title:
                    i += 1
                else:
                    i = 0
            if i == len(list_for_and_black_title):
                print url + ' : ' + unicode('�ų�ԭ�� : ������ͬʱ���� : %s', 'gbk') % '|'.join(list_for_and_black_title).decode(
                    'gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ������ͬʱ���� : %s', 'gbk') % '|'.join(
                    list_for_and_black_title).decode('gbk')))
                return False

        if list_for_or_black_content != []:
            for x in list_for_or_black_content:
                if x.decode('gbk') in content:
                    print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�д��� : %s', 'gbk') % x
                    log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�д��� : %s', 'gbk') % x))
                    return False
        if list_for_and_black_content != []:
            i = 0
            for x in list_for_and_black_content:
                if x.decode('gbk') in content:
                    i += 1
                else:
                    i = 0
            if i == len(list_for_and_black_content):
                print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ��ͬʱ���� : %s', 'gbk') % '|'.join(list_for_and_black_content).decode(
                    'gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ��ͬʱ���� : %s', 'gbk') % '|'.join(
                    list_for_and_black_content).decode('gbk')))
                return False

        if list_for_and_url != []:
            i = 0
            for x in list_for_and_url:
                if x in url:
                    pass
                else:
                    xx = x
                    i = 1
            if i == 1:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�в����� : %s', 'gbk') % xx
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�в����� : %s', 'gbk') % xx))
            else:
                try:
                    print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                    log((' [+] ��ַд�� : ' + url).decode('gbk'))
                    success_write(url)
                    return ''
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
        if list_for_and_title != []:
            i = 0
            for x in list_for_and_title:
                if x.decode('gbk') in title:
                    pass
                else:
                    xx = x
                    i = 1
            if i == 1:
                print url + ' : ' + unicode('�ų�ԭ�� : �����в����� : %s', 'gbk') % xx
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : �����в����� : %s', 'gbk') % xx))
            else:
                try:
                    print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                    log((' [+] ��ַд�� : ' + url).decode('gbk'))
                    success_write(url)
                    return ''
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
        if list_for_and_content != []:
            i = 0
            for x in list_for_and_content:
                if x.decode('gbk') in content:
                    pass
                else:
                    xx = x
                    i = 1
            if i == 1:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�в����� : %s', 'gbk') % xx
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�в����� : %s', 'gbk') % xx))
            else:
                try:
                    print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                    log((' [+] ��ַд�� : ' + url).decode('gbk'))
                    success_write(url)
                    return ''
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))

        if list_for_or_url != []:
            i = 0
            for x in list_for_or_url:
                if x in url:
                    i = 1
            if i == 0:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�нԲ����� : %s', 'gbk') % '|'.join(list_for_or_url).decode('gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�нԲ����� : %s', 'gbk') % '|'.join(
                    list_for_or_url).decode('gbk')))
            else:
                try:
                    print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                    log((' [+] ��ַд�� : ' + url).decode('gbk'))
                    success_write(url)
                    return ''
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
        if list_for_or_title != []:
            i = 0
            for x in list_for_or_title:
                if x.decode('gbk') in title:
                    i = 1
            if i == 0:
                print url + ' : ' + unicode('�ų�ԭ�� : �����нԲ����� : %s', 'gbk') % '|'.join(list_for_or_title).decode('gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : �����нԲ����� : %s', 'gbk') % '|'.join(
                    list_for_or_title).decode('gbk')))
            else:
                try:
                    print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                    log((' [+] ��ַд�� : ' + url).decode('gbk'))
                    success_write(url)
                    return ''
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))

        if list_for_or_content != []:
            i = 0
            for x in list_for_or_content:
                if x.decode('gbk') in content:
                    i = 1
            if i == 0:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�нԲ����� : %s', 'gbk') % '|'.join(list_for_or_content).decode('gbk')
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ҳ�нԲ����� : %s', 'gbk') % '|'.join(
                    list_for_or_content).decode('gbk')))
            else:
                try:
                    print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                    log((' [+] ��ַд�� : ' + url).decode('gbk'))
                    success_write(url)
                    return ''
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
        try:
            print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
            log((' [+] ��ַд�� : ' + url).decode('gbk'))
            success_write(url)
            return ''
        except Exception, e:
            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
            pass

def get_url(url):
    if list_for_or_black_url != []:
        for x in list_for_or_black_url:
            if x in url:
                print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�д��� : %s', 'gbk') % x
                log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�д��� : %s', 'gbk') % x))
                return False
    if list_for_and_black_url != []:
        i = 0
        for x in list_for_and_black_url:
            if x in url:
                i += 1
            else:
                i = 0
        if i == len(list_for_and_black_url):
            print url + ' : ' + unicode('�ų�ԭ�� : ��ַ��ͬʱ���� : %s', 'gbk') % '|'.join(
                list_for_and_black_url).decode('gbk')
            log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ��ͬʱ���� : %s', 'gbk') % '|'.join(
                list_for_and_black_url).decode('gbk')))
            return False

    if list_for_and_url != []:
        i = 0
        for x in list_for_and_url:
            if x in url:
                pass
            else:
                xx = x
                i = 1
        if i == 1:
            print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�в����� : %s', 'gbk') % xx
            log((' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�в����� : %s', 'gbk') % xx))
            return False
        else:
            try:
                print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                log((' [+] ��ַд�� : ' + url).decode('gbk'))
                success_write(url)
                return ''
            except Exception, e:
                log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                pass
    if list_for_or_url != []:
        i = 0
        for x in list_for_or_url:
            if x in url:
                i = 1
        if i == 0:
            print url + ' : ' + unicode('�ų�ԭ�� : ��ַ�нԲ����� : %s', 'gbk') % '|'.join(list_for_or_url).decode(
                'gbk')
            log((
                ' [-] ��ַ�ų� : ' + url + ' : ' + unicode('�ų�ԭ�� : ��ַ�нԲ����� : %s', 'gbk') % '|'.join(
                    list_for_or_url).decode(
                    'gbk')))
            return False
        else:
            try:
                print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
                log((' [+] ��ַд�� : ' + url).decode('gbk'))
                success_write(url)
                return ''
            except Exception, e:
                log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                pass
    try:
        print url + ' : ' + unicode('����Ҫ����ַд�뱾��', 'gbk')
        log((' [+] ��ַд�� : ' + url).decode('gbk'))
        success_write(url)
        return ''
    except Exception, e:
        log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
        pass


# �ú�������һ����ַ����ȡ�������ҳ����������Ĺ���

def get_info(url):
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA, 'Connection': 'close'}
        try:
            cms_title = 'title_error'
            r_cms_top = requests.get(url=url, headers=headers, verify=False, timeout=timeout)
            time.sleep(0.02)
            if isinstance(r_cms_top.content, unicode):
                ucontent = r_cms_top.content
            else:
                code = chardet.detect(r_cms_top.content)['encoding']
                ucontent = r_cms_top.content.decode(code)
            cms_title = re.search('<title>(.*?)</title>', ucontent, re.S | re.I).group().replace('<title>', '').replace(
                '</title>', '').replace('<TITLE>', '').replace('</TITLE>', '')
        except Exception, e:
            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
        try:
            if cms_title == 'title_error':
                cure(url=url, title=cms_title, content=ucontent)
                log((' [*] �쳣״̬ : ' + '��ʱ�޷���ȡ��վ����').decode('gbk'))
                pass
            else:
                cure(url=url, title=cms_title, content=ucontent)
        except Exception, e:
            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
    except Exception, e:
        log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))


def scan_baidu(keyword):
    list_001 = []
    print (unicode(' [*] �ؼ�����ַ�ɼ���������......', 'gbk'))
    log((' [*] �������� : ' + unicode(' [*] �ؼ�����ַ�ɼ���������......', 'gbk')).decode('gbk'))
    urlx = 'https://www.baidu.com/s?wd='
    for i in range(0, 100, 10):
        UA = random.choice(headerss)
        headers = {'User-Agent': UA, 'Connection': 'close'}
        url = str(urlx + str(keyword) + '&pn=' + str(i))
        try:
            r = requests.get(url=url, headers=headers, verify=False, timeout=timeout)
            time.sleep(0.02)
            rr = re.findall(r'<a target="_blank" href="(.*?)"', r.content, re.S)
            for xx in rr:
                if xx.find('link') > 0:
                    try:
                        rxr = requests.get(url=xx, headers=headers, verify=False, timeout=timeout)
                        time.sleep(0.02)
                        if rxr.status_code == 200:
                            print (' [+] Baidu Found Url: ' + rxr.url.split('://')[0] + '://' +
                                   rxr.url.split('://')[1].split('/')[0])
                            dxdx = rxr.url.split('://')[0] + '://' + rxr.url.split('://')[1].split('/')[0]
                            list_001.append(dxdx)
                            log((' [+] Baidu Found Url: ' + rxr.url.split('://')[0] + '://' +
                                 rxr.url.split('://')[1].split('/')[0]))
                    except Exception, e:
                        log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                        pass
        except Exception, e:
            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
            pass
    list_001 = list(set(list_001))
    return list_001


# ���޲ɼ���

def wuxiancaiji(url):
    result_list = []
    result_list.append(url)
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA, 'Connection': 'close'}
        r = requests.get(url=url, headers=headers, verify=False, timeout=timeout)
        time.sleep(0.02)
        print str(threading.current_thread().name) + (unicode('    ��ʼ����:      ', 'gbk')) + r.url + '      ' + str(
            r.status_code)
        bp = bs(r.content, 'html.parser')
        for x in bp.select('li > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                    pass
            else:
                pass
        for x in bp.select('td > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                    pass
            else:
                pass
        for x in bp.select('p > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                    pass
            else:
                pass
        for x in bp.select('div > a'):
            d = str(x)
            if 'nofollow' not in d and 'java' not in d and ';' not in d and '?' not in d and '#' not in d:
                try:
                    ddd = x['href']
                    for x in first_cule:
                        if x in ddd:
                            if 'http' in ddd:
                                # print ddd.split(x)[0] + x
                                result_list.append(ddd.split(x)[0] + x)
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                    pass
            else:
                pass
    except Exception, e:
        log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
        pass

    result_list = list(set(result_list))

    # Ȼ�����е����ݱ��浽���ݿ⼴��
    for x in result_list:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA, 'Connection': 'close'}
            live = int(requests.head(url=x,headers=headers,timeout=timeout).status_code)
            if live == 200:
                try:
                    coon = sqlite3.connect(db)
                    cur = coon.cursor()
                    sql = 'INSERT into urls(url,get) VALUES ("%s","%s")' % (x, '0')
                    sql2 = 'INSERT into urlss(url,get) VALUES ("%s","%s")' % (x, '0')
                    try:
                        cur.execute(sql)
                        cur.execute(sql2)
                    except sqlite3.IntegrityError:
                        print str(threading.current_thread().name) + (unicode('    ���ݿ��Ѵ��ڸ���ַ:      ', 'gbk')) + x
                        log((' [*] �쳣״̬ : ���ݿ��Ѵ��ڸ���ַ').decode('gbk'))
                    coon.commit()
                    coon.close()
                except:
                    pass
                finally:
                    coon.close()
        except Exception, e:
            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
            pass


def scan_url():
    while 1:
        time.sleep(random.randint(1,3))
        try:
            lo.acquire()
            coon = sqlite3.connect(db)
            cur = coon.cursor()
            sql1 = 'select url from urls where get=0  limit 0,1'
            sql2 = 'update urls set get=1 where url=(select url from urls where get=0 limit 0,1)'
            fet = cur.execute(sql1).fetchone()
            cur.execute(sql2)
            coon.commit()
            coon.close()
            lo.release()
        except:
            print (unicode('���ݿ���ʱû�ж������ַ����ȴ��Զ��ɼ�', 'gbk'))
            time.sleep(random.randint(1, 8))
            time.sleep(random.randint(1, 8))
        finally:
            coon.close()

        url = str(fet).replace("(u'","").replace("',)",'')
        if str(url) == 'None':
            time.sleep(10)
        wuxiancaiji(url)


def check_url():
    while 1:
        time.sleep(random.randint(1,3))
        time.sleep(random.randint(1,3))
        time.sleep(random.randint(1,3))
        try:
            lo.acquire()
            coon = sqlite3.connect(db)
            cur = coon.cursor()
            sql1 = 'select url from urlss where get=0 limit 0,1'
            sql2 = 'update urlss set get=1 where url=(select url from urlss where get=0 limit 0,1)'
            fet = cur.execute(sql1).fetchone()
            cur.execute(sql2)
            coon.commit()
            coon.close()
            url = str(fet).replace("(u'","").replace("',)",'')
            lo.release()
        except:
            print (unicode('���ݿ���ʱû�ж������ַ����ȴ��Զ��ɼ�', 'gbk'))
            time.sleep(random.randint(1, 8))
            time.sleep(random.randint(1, 8))
            time.sleep(random.randint(1, 8))
            coon.close()
        if str(url) != 'None':
            if urls != 'None' or black_urls != 'None':
                if titles == 'None' and black_titles == 'None' and contents == 'None' and black_contents == 'None':
                    get_url(url)

            if titles == 'None' and black_titles == 'None' and contents == 'None' and black_contents == 'None' and urls == 'None' and black_urls == 'None':
                success_write(url)

            if urls != 'None' or black_urls != 'None' or titles != 'None' or black_titles != 'None' or contents != 'None' or black_contents != 'None':
                try:
                    UA = random.choice(headerss)
                    headers = {'User-Agent': UA, 'Connection': 'close'}
                    cms_title = 'title_error'
                    r_cms_top = requests.get(url=url, headers=headers, verify=False, timeout=timeout)
                    time.sleep(0.02)
                    if isinstance(r_cms_top.content, unicode):
                        ucontent = r_cms_top.content
                    else:
                        code = chardet.detect(r_cms_top.content)['encoding']
                        ucontent = r_cms_top.content.decode(code)
                        cms_title = re.search('<title>(.*?)</title>', ucontent, re.S | re.I).group().replace('<title>',
                                                                                                             '').replace(
                            '</title>', '').replace('<TITLE>', '').replace('</TITLE>', '')
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                try:
                    if cms_title == 'title_error':
                        cure(url=url, title=cms_title, content=ucontent)
                        log((' [*] �쳣״̬ : ' + '��ʱ�޷���ȡ��վ����').decode('gbk'))
                        pass
                    else:
                        cure(url=url, title=cms_title, content=ucontent)
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                    pass
        else:
            time.sleep(20)






if __name__ == '__main__':
    print '\n'
    if os.path.exists('URLS.db'):
        if os.path.getsize('urls.db') < 28675:
            print unicode('     ���ݿ������ݹ��٣�ɾ�����ݿ�', 'gbk')
            os.remove('urls.db')
        else:
            print unicode('     Ŀ¼�´������ݿ��ļ�', 'gbk')
            print unicode('     ���������ݿ��м�����ȡ��ַɨ�������� 0', 'gbk')
            print unicode('     ����ɾ���������¼��ɨ�������� 1', 'gbk')
            start = raw_input(unicode('��ѡ��(ѡ��:0/1):', 'gbk').encode('gbk'))
            if int(start) != 0 and int(start) != 1:
                time.sleep(3)
                os.system('shutdown -s -t 20')
                time.sleep(10)
                os.system('shutdown -a')
                print unicode('��ʵ�㣬���� 0/1', 'gbk')
            if int(start) == 0:
                if int(url_threads) > 0:
                    for _ in range(int(url_threads)):
                        t = threading.Thread(target=scan_url).start()
                else:
                    pass
                if int(check_threads) > 0:
                    for _ in range(int(check_threads)):
                        t = threading.Thread(target=check_url).start()
            if int(start) == 1:
                os.remove('URLS.db')
                print unicode('     ���ݿ�ɾ���ɹ�', 'gbk')
    if not os.path.exists('urls.db'):
        try:
            coon = sqlite3.connect(db)
            cur = coon.cursor()
            cur.execute('CREATE TABLE urls(\
                              url VARCHAR(30) , \
                              get VARCHAR(1))')
            cur.execute('CREATE UNIQUE INDEX index_name ON urls (url) ')
            cur.execute('CREATE INDEX index_nname ON urls (get)')

            cur.execute('CREATE TABLE urlss(\
                              url VARCHAR(30) , \
                              get VARCHAR(1))')
            cur.execute('CREATE UNIQUE INDEX indexs_name ON urlss (url) ')
            cur.execute('CREATE INDEX indexs_nname ON urlss (get)')
            cur.close()
            coon.commit()
            coon.close()
            print unicode('     ���ݿⴴ���ɹ�', 'gbk')
        except Exception, e:
            print unicode('�޷�������ǰĿ���ļ��л����ݿ� : ', 'gbk')
            print e
            time.sleep(600)
            pass
        finally:
            coon.close()



        try:
            print '\n'
            print (unicode('����������ַ���� 0 (���ɼ��õ���ַ�ı���ק����)   �Զ��ɼ��ؼ������� 1 (�ٶȽӿڹؼ��ʲɼ�)', 'gbk'))  # line:185
            time.sleep(3)
            setstart = raw_input(unicode('��ѡ��������ʽ(ѡ��:0/1):', 'gbk').encode('gbk'))
            log((' [*] �������� : ' + '����������ַ���� 0 (���ɼ��õ���ַ�ı���ק����)   �Զ��ɼ��ؼ������� 1 (�ٶȽӿڹؼ��ʲɼ�)').decode('gbk'))
            log((' [*] �������� : ' + '��ѡ��������ʽ(ѡ��:0/1):' + str(setstart)).decode('gbk'))
            time.sleep(1)
            setstart = int(setstart)
            if setstart != 0 and setstart != 1:
                print unicode('�Ǻ���~�����������ʲô������~', 'gbk')
                log((' [*] �������� : ' + '�Ǻ���~�����������ʲô������~').decode('gbk'))
                time.sleep(2)
                print unicode('һ���Ҹ�:����رձ�����Ӵ~', 'gbk')
                log((' [*] �������� : ' + 'һ���Ҹ�:����رձ�����Ӵ~').decode('gbk'))
                time.sleep(3)
                print unicode('�d(������)Bye~Bye~', 'gbk')
                log((' [*] �������� : ' + '�d(������)Bye~Bye~').decode('gbk'))
                os.system('shutdown -s -t 60')
                log((' [*] �������� : ' + '60 ����Զ��ػ�').decode('gbk'))
                time.sleep(55)
                log((' [*] �������� : ' + '�ȴ� 55 ����').decode('gbk'))
                os.system('shutdown -a')
                log((' [*] �������� : ' + 'ȡ���Զ��ػ�').decode('gbk'))
                time.sleep(2)
                print unicode('����~', 'gbk')
                log((' [*] �������� : ' + '����~').decode('gbk'))

            if setstart == 1:
                keywords = urllib.quote(
                    str(raw_input(
                        unicode('����ؼ���,�ɼ���ַ��(����:inurl:php/����˧��/AT2@32D^%$):', 'gbk').encode('gbk'))))
                log((' [*] �������� : ' + '����ؼ���,�ɼ���ַ��(����:inurl:php/����˧��/AT2@32D^%$):' + str(keywords)).decode(
                    'gbk'))
                bbaidu = scan_baidu(str(keywords))

                if track == 0:
                    if urls != 'None' or black_urls != 'None':
                        if titles == 'None' and black_titles == 'None' and contents == 'None' and black_contents == 'None':
                            for x in bbaidu:
                                get_url(x)

                    if titles != 'None' or black_titles != 'None' or contents != 'None' or black_contents != 'None':
                            for x in bbaidu:
                                get_info(x)

                    else:
                        for x in bbaidu:
                            get_info(x)

                if track == 1:
                    for x in bbaidu:
                        print x + ':' + (unicode('��ַ�ϴ����ݿ���...', 'gbk'))
                        try:
                            coon = sqlite3.connect(db)
                            cur = coon.cursor()
                            sql = 'INSERT into urls(url,get) VALUES ("%s","%s")' % (x, '0')
                            sql2 = 'INSERT into urlss(url,get) VALUES ("%s","%s")' % (x, '0')
                            try:
                                cur.execute(sql)
                                cur.execute(sql2)
                            except sqlite3.IntegrityError:
                                print str(threading.current_thread().name) + (
                                unicode('    ���ݿ��Ѵ��ڸ���ַ:      ', 'gbk')) + x
                                log((' [*] �쳣״̬ : ���ݿ��Ѵ��ڸ���ַ').decode('gbk'))
                            coon.commit()
                            coon.close()
                        except Exception, e:
                            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                            pass
                        finally:
                            coon.close()
                    if int(url_threads)>0:
                        for _ in range(int(url_threads)):
                            t = threading.Thread(target=scan_url).start()
                    else:
                        pass
                    if int(check_threads)>0:
                        for _ in range(int(check_threads)):
                            t = threading.Thread(target=check_url).start()
                    else:
                        pass


            if setstart == 0:
                try:
                    urltxt = raw_input(unicode('������ַ�ı���(����ק����) : ', 'gbk').encode('gbk'))
                    urllist = list(set(
                        [x.replace('\n', '') if x.startswith('http') else 'http://' + x.replace('\n', '')
                         for x in
                         open(urltxt, 'r').readlines()]))
                    count = int(len(urllist))
                    log((' [*] �������� : ������ַ�ı���(����ק����) :' + str(urltxt)).decode('gbk'))
                    time.sleep(2)
                    if track == 0:
                        if urls != 'None' or black_urls != 'None':
                            if titles == 'None' and black_titles == 'None' and contents == 'None' and black_contents == 'None':
                                for x in urllist:
                                    get_url(x)

                        if titles != 'None' or black_titles != 'None' or contents != 'None' or black_contents != 'None':
                            for x in urllist:
                                get_info(x)

                        if titles == 'None' and black_titles == 'None' and contents == 'None' and black_contents == 'None' and urls == 'None' and black_urls == 'None':
                            print unicode('���ع�����ַ������δ���ù��˹���', 'gbk')
                            log((' [*] �������� : ' + '���ع�����ַ������δ���ù��˹���').decode('gbk'))
                            time.sleep(500)

                    if track == 1:
                        for x in urllist:
                            print  x + ':' + (unicode('��ַ�ϴ����ݿ���...', 'gbk'))
                            try:
                                coon = sqlite3.connect(db)
                                cur = coon.cursor()
                                sql = 'INSERT into urls(url,get) VALUES ("%s","%s")' % (x, '0')
                                sql2 = 'INSERT into urlss(url,get) VALUES ("%s","%s")' % (x, '0')
                                try:
                                    cur.execute(sql)
                                    cur.execute(sql2)
                                except sqlite3.IntegrityError:
                                    print str(threading.current_thread().name) + (
                                    unicode('    ���ݿ��Ѵ��ڸ���ַ:      ', 'gbk')) + x
                                    log((' [*] �쳣״̬ : ���ݿ��Ѵ��ڸ���ַ').decode('gbk'))
                                coon.commit()
                                coon.close()
                            except Exception, e:
                                log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                                pass
                            finally:
                                coon.close()
                        if int(url_threads) > 0:
                            for _ in range(int(url_threads)):
                                t = threading.Thread(target=scan_url).start()
                        else:
                            pass
                        if int(check_threads) > 0:
                            for _ in range(int(check_threads)):
                                t = threading.Thread(target=check_url).start()
                        else:
                            pass
                except Exception, e:
                    log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
                    pass
        except Exception, e:
            log((' [*] �쳣״̬ : ' + str(e)).decode('gbk'))
            pass

