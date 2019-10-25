# -*- coding:utf-8 -*-
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


def get_baidu_weights(url):
    time.sleep(random.randint(1,5))
    x = str(random.randint(1, 9))
    data = {
        't': 'rankall',
        'on': 1,
        'type': 'baidupc',
        'callback': 'jQuery111303146901980779846_154444474116%s' % (x),
        'host': url
    }

    headers = {

        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=165af67ee6f352-07238a34ed3941-9393265-1fa400-165af67ee70473; CNZZDATA5082706=cnzz_eid%3D832961605-1544438317-null%26ntime%3D1544443717; Hm_lvt_aecc9715b0f5d5f7f34fba48a3c511d6=1544443985; Hm_lpvt_aecc9715b0f5d5f7f34fba48a3c511d6=1544443985; qHistory=aHR0cDovL3JhbmsuY2hpbmF6LmNvbS9iYWlkdW1vYmlsZS8r55m+5bqm56e75Yqo5p2D6YeNfGh0dHA6Ly9yYW5rLmNoaW5hei5jb20vcmFua2FsbC8r5p2D6YeN57u85ZCI5p+l6K+ifGh0dHA6Ly9yYW5rLmNoaW5hei5jb20r55m+5bqm5p2D6YeN5p+l6K+ifGh0dHA6Ly9pbmRleC5jaGluYXouY29tLyvlhbPplK7or43lhajnvZHmjIfmlbB8aHR0cDovL3JhbmsuY2hpbmF6LmNvbS9yYW5rL2hpc3RvcnkuYXNweCvmnYPph43ljoblj7Lmn6Xor6I=',
        'Host': 'rank.chinaz.com',
        'Origin': 'http://rank.chinaz.com',
        'Referer': 'http://rank.chinaz.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'

    }
    try:
        urls = 'http://rank.chinaz.com/ajaxseo.aspx?t=rankall&on=1&type=undefined&callback=jQuery111303146901980779846_154444474116%s' % (
            x)

        r = requests.post(url=urls, headers=headers, data=data)
        try:
            res = re.search(b',"br":(\d),"beforBr', r.content).group(1)
        except:
            pass
        if res:
            return res.decode()
        else:
            return '0'
    except:
        return '获取失败'

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


def get_info(pattren, result):
    try:
        res = re.search(pattren, result).group(1)
        return res
    # return str(res.encode('utf-8'))
    except:
        return '暂无信息'


def scan_seo(url):
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
        req = requests.get(urls, headers, timeout=20)
        encoding = requests.utils.get_encodings_from_content(req.text)[0]
        r = req.content.decode(encoding, 'replace')
    except Exception as e:
        writedata(str(e))
        return None

    res['百度权重'] = str(get_baidu_weights(url))
    res['网站网址'] = url

    try:
        req1 = requests.get(url=url,headers=headers,verify=False,timeout=10)
        encoding = requests.utils.get_encodings_from_content(req1.text)[0]
        rress = req1.content.decode(encoding, 'replace')
        title_pattern = '<title>(.*?)</title>'
        title = re.search(title_pattern, rress, re.S | re.I)
        res['网站标题'] = str(title.group(1))
    except:
        res['网站标题'] = url

    ip_infos = get_info(ip_parrten, r)
    if '[' in ip_infos:
        ip, address = ip_infos.split('[')[0], ip_infos.split('[')[1]
        res['IP__坐标'] = address.replace(']', '')
        res['所属__IP'] = ip
    else:
        res['IP__坐标'] = '获取失败'
        res['所属__IP'] = '获取失败'

    res['网站年龄'] = get_info(ages, r)
    res['备案编号'] = get_info(whois_id, r)
    res['备案性质'] = get_info(whois_type, r)
    res['备案名称'] = get_info(whois_name, r)
    res['备案时间'] = get_info(whois_time, r)
    res['百度收录'] = get_info(include_baidu, r)

    dd = re.findall(infos, r, re.S)
    resu = ['暂无信息' if x.replace(' ', '') is '' else x for x in dd]
    try:
        res['协议类型'] = resu[0]
    except:
        res['协议类型'] = '获取失败'

    try:
        res['页面类型'] = resu[1]
    except:
        res['页面类型'] = '获取失败'

    try:
        res['服务类型'] = resu[2]
    except:
        res['服务类型'] = '获取失败'

    try:
        res['程序语言'] = resu[3]
    except:
        res['程序语言'] = '获取失败'
    return res


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
    time.sleep(random.randint(1, 6))
    if 'gov.cn' in url or 'edu.cn' in url:
        return 0
    domain = url.split('//')[1].strip('/').replace('www.', '')
    result = []
    id_links = []
    html_links = []
    result_links = {}
    html_links_s = []
    # result_links['title'] = '网址标题获取失败'
    idid = []
    htht = []
    try:
        headers = {
            'User-Agent': random.choice(headerss),
            'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
        }
        rxww = requests.get(url, headers=headers, verify=False, timeout=10)
        soup = BeautifulSoup(rxww.content, 'html.parser', from_encoding='iso-8859-1')

        try:
            encoding = requests.utils.get_encodings_from_content(rxww.text)[0]
            res = rxww.content.decode(encoding, 'replace')
            # title_pattern = '<title>(.*?)</title>'
            # title = re.search(title_pattern, res, re.S | re.I)
            # result_links['title'] = str(title.group(1))
        except:
            pass

        #
        # if result_links['title'] == '' or result_links['title'] == None:
        #     result_links['title'] = '网址标题获取失败'

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
                    rx1 = requests.head(url=x1, headers=headers, verify=False, timeout=15).status_code
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
                with open('result.txt', 'a+', encoding='utf-8') as ae:
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
                with open('result.txt', 'a+', encoding='utf-8') as ae:
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




if __name__ == '__main__':
    print(get_links('http://www.hntky.com/'))
