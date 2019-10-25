# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 0010 19:07
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 扫描备份2.3.py
# @Software: PyCharm
import sys
import requests
import re,time,os
from bs4 import BeautifulSoup as bs
import multiprocessing
from multiprocessing import freeze_support

import random
reload(sys)
sys.setdefaultencoding('utf-8')

backup_dir = ['www', 'root', '备份', 'templates', 'upload', 'backup', 'data', 'web', 'ftp']
backup_suffix = ['.rar', '.zip', '.tar', '.tar.bz2', '.sql', '.7z', '.bak', '.txt', '.tar.gz', '.iso', '.gz','.sql', '.exe']
backup_name = ['hdocs', '2016', 'upfile', 'wwwroot', 'flashfxp', '2017', 'ftp', 'Release', 'website', '2015',
               'HYTop', 'backup', '0', 'tar.gz', 'wangzhan', 'test', 'data', 'bbs', 'web', 'www', 'www.root', 'wz',
               'beian', 'sql', 'gg', 'oa', 'admin', '123', 'template', '1gz', '1', 'fdsa', '2014', 'root', 'vip',
               'beifen', 'back', 'a', '%E5%A4%87%E4%BB%BD', 'bak', '2', 'db', '2018']
dict_list = list(set([x.replace('\n', '') for x in open('rar.txt', 'r').readlines()]))
os.system('color a')

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
# with open(str(result_name)+'.html','a+')as a:
#     a.write('''
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>Lang_BackUp_Scan_Result ver 2.3</title>
#     <link rel="stylesheet" href='https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap-theme.min.css'>
#     <link rel="stylesheet" href='https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css'>
#     </head>
#     <div class="container">
#         <div class="navbar navbar-default">
#     <div class="navbar-header">
#         <a class="navbar-brand" href="#">Lang</a>
#     </div>
#         <ul class="nav navbar-nav">
#             <li><a href="http://www.langzi.fun/Python%20批量扫描备份文件.html">项目地址</a></li>
#             <li><a href="http://www.langzi.fun/URL路径模糊测试.html">项目升级</a></li>
#             <li><a href="http://langzi.fun:9827">妹子</a></li>
#         </ul>
#
#         </div>
#     </div>
#     <div class="container">
#
#     ''')

# def start(func):
#     def inter(url_backup):
#         result = func(url_backup)
#         if result == []:
#             pass
#         else:
#             print (unicode(('该网站存在备份文件泄露:%s : ' + url_backup) % threading.current_thread().name, 'utf-8'))
#             with open(str(result_name)+'.html','a+')as a:
#                 for _ in result:
#                     a.write('<div class="col-md-10 font-weight-bold"><br>')
#                     a.write(str(_.decode('utf-8')))
#                     a.write('</div><br>')
#         return result
#     return inter



def scan(urlx,result_name):
    result_name=result_name
    list_result=[]
    dir_list = []
    file_list=[]
    dir_list.extend(backup_dir)
    dir_list.append(urlx.split('//')[1].split('.')[1])
    dir_list.append(urlx.split('//')[1].split('.')[1])
    file_list.append(urlx.split('//')[1].split('.')[1])
    file_list.append(urlx.split('//')[1].split('.')[0])
    k1 = urlx.split('//')[1]
    # www.langzi.fun
    k2 = urlx.split('//')[1].replace('.', '_')
    # www_langzi_fun
    k3 = urlx.split('.', 1)[1].replace('/', '')
    # langzi.fun
    k3_1 = urlx.split('.', 1)[1].replace('/', '').replace('.','_')
    # langzi_fun
    k3_2 = urlx.split('.', 1)[1].replace('/', '').replace('.','')
    # langzifun
    k3_3 = urlx.split('.', 1)[1].replace('/', '').replace('.','-')
    # langzi-fun
    k4 = urlx.split('//')[1].split('.')[1]
    # langzi
    k4_2 = urlx.split('//')[1].split('.')[0] if urlx.split('//')[1].split('.')[0] !='www' else urlx.split('//')[1].split('.')[1]
    # www
    if urlx.find('.')==3:
        k4_1 = urlx.split('//')[1].split('.')[2]
        # fun
        k29 = k4_1 + '2015'
        k30 = k4_1 + '2016'
        k31 = k4_1 + '2017'
        k32 = k4_1 + '2018'
        file_list.append(k4_1)
        file_list.append(k29)
        file_list.append(k30)
        file_list.append(k31)
        file_list.append(k32)

    k17 = k2 + '2015'
    k18 = k2 + '2016'
    k19 = k2 + '2017'
    k20 = k2 + '2018'

    k21 = k3_1 + '2015'
    k22 = k3_1 + '2016'
    k23 = k3_1 + '2017'
    k24 = k3_1 + '2018'

    k25 = k3_2 + '2015'
    k26 = k3_2 + '2016'
    k27 = k3_2 + '2017'
    k28 = k3_2 + '2018'

    k5 = k4 + '2015'
    k6 = k4 + '2016'
    k7 = k4 + '2017'
    k8 = k4 + '2018'
    # langzi2015
    k9 = k1 + '2015'
    k10 = k1 + '2016'
    k11 = k1 + '2017'
    k12 = k1 + '2018'
    # www.langzi.fun2015
    k13 = k3 + '2015'
    k14 = k3 + '2016'
    k15 = k3 + '2017'
    k16 = k3 + '2018'

    file_list.append(k1)
    file_list.append(k2)
    file_list.append(k3)
    file_list.append(k4)
    file_list.append(k5)
    file_list.append(k6)
    file_list.append(k7)
    file_list.append(k8)
    file_list.append(k9)
    file_list.append(k10)
    file_list.append(k11)
    file_list.append(k12)
    file_list.append(k13)
    file_list.append(k14)
    file_list.append(k15)
    file_list.append(k16)
    file_list.append(k17)
    file_list.append(k18)
    file_list.append(k19)
    file_list.append(k20)
    file_list.append(k21)
    file_list.append(k22)
    file_list.append(k23)
    file_list.append(k24)
    file_list.append(k25)
    file_list.append(k26)
    file_list.append(k27)
    file_list.append(k28)
    file_list.append(k3_1)
    file_list.append(k3_2)
    file_list.append(k3_3)
    file_list.append(k4_2)
    file_list.extend(backup_name)
    dir_list=list(set(dir_list))
    file_list=list(set(file_list))

    if urlx.endswith('/'):
        url = urlx
    else:
        url = urlx+'/'
    #print url
    try:
        web_title = '获取网站标题失败'
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info_top = requests.get(url=url, headers=headers, timeout=5)
        if r_info_top.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'GB2312':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'gb2312':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'GBK':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'gbk':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        else:
            web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                '</title>', '')
    except:
        try:
            web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                '</title>', '')
        except:
            web_title = '暂时无法获取网站标题'
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r = requests.get(url=url,headers=headers,timeout=10)
        bp = bs(r.content,'lxml')
        for _ in bp.find_all('a'):
            try:
                d = _['href']
            except Exception, e:
                #pass
                pass
            # 开始爬取目录
            if d and d!='' and d!=None:
                da = d.replace(url, '')
                if da.find('=') < 0 and da.find(':') < 0:
                    de =  da if da.startswith('/') else '/'+da
                    dex = de.split('/')[1] if '.' not in de else de.split('/')[0]
                    if dex.find('.')<0:
                        if dex != '/' and dex !='':
                            dir_list.append(dex)
                    else:
                        pass
    except Exception,e:
        pass
    dir_list=list(set(dir_list))
    file_list=list(set(file_list))
    url_svn = url + '.svn/entries'
    # print 'Cheaking>>>' + url_svn
    # 扫描svn源码泄露  组合成链接
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_svn = requests.head(url=url_svn, headers=headers, timeout=5)
        # 访问这个链接  超时设置5秒
        # print r_svn.url + " : " + str(r_svn.status_code)
        # 打印出这个网址 和 访问状态码
        dd1 =' [ Scan : '+ str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>'+ '' + ' ' + str(r_svn.status_code) + '    ' + str(url_svn)
        print dd1
        with open('log.txt','a+')as aaa:
            aaa.write(dd1 + '\n')
        if r_svn.status_code == 200:
            with open('log.txt', 'a+')as aaa:
                aaa.write(str(r_svn.headers) + '\n')
            # 如果状态码是200  表示访问成功
            try:
                r_svn_1 = requests.get(url=url_svn, headers=headers, timeout=5)
                with open('log.txt', 'a+')as aaa:
                    aaa.write(r_svn_1.content + '\n')
                if 'dir' in r_svn_1.content and 'svn://' in r_svn_1.content:
                    _ = (str(str(r_svn_1.url) + '------' + str('SVN源码泄露') + '------' + str(web_title)))
                    with open(result_name, 'a+')as a:
                        a.write('<div class="col-md-10 font-weight-bold"><br>')
                        a.write(str(_))
                        a.write('</div><br>')
            except Exception as e:
                pass
                pass
        else:
            pass
    except Exception as e:
        pass

        # pass
        ######################################
        # svn源码泄露扫描完毕
        ######################################

    url_git = url + '.git/config'
    # print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, timeout=5)
        # print r_git.url + " : " + str(r_git.status_code)
        dd2 = ' [ Scan : '+ str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>'+ '' + ' ' + str(r_git.status_code) + '    ' + str(url_git)
        print dd2
        with open('log.txt','a+')as aaa:
            aaa.write(dd2 + '\n')
        if r_git.status_code == 200:
            with open('log.txt', 'a+')as aaa:
                aaa.write(str(r_git.headers) + '\n')
            try:
                r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
                if 'repositoryformatversion' in r_git_1.content:
                    with open('log.txt', 'a+')as aaa:
                        aaa.write(r_git_1.content + '\n')
                    # repositoryformatversion 这个是git源码泄露的特征码
                    _ = (str(str(r_git_1.url) + '------' + str('GIT源码泄露') + '------' + str(web_title)))
                    with open(result_name, 'a+')as a:
                        a.write('<div class="col-md-10 font-weight-bold"><br>')
                        a.write(str(_))
                        a.write('</div><br>')
                else:
                    pass
            except Exception as e:
                pass
                pass
    except Exception as e:
        pass
        pass
    url_info = url + 'WEB-INF/web.xml'
    # print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info = requests.head(url=url_info, headers=headers, timeout=5)
        # print r_git.url + " : " + str(r_git.status_code)
        dd3 = ' [ Scan : '+ str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>'+ '' + ' ' + str(r_info.status_code) + '    ' + str(url_info)
        print dd3
        with open('log.txt','a+')as aaa:
            aaa.write(dd3 + '\n')
        if r_info.status_code == 200:
            with open('log.txt', 'a+')as aaa:
                aaa.write(str(r_info.headers) + '\n')
            try:
                r_info_1 = requests.get(url=url_info, headers=headers, timeout=5)
                with open('log.txt', 'a+')as aaa:
                    aaa.write(r_info_1.content + '\n')
                if '<web-app' in r_info_1.content:
                    _ = (str(str(r_info_1.url) + '------' + str('WEBinfo信息泄露') + '------' + str(web_title)))
                    with open(result_name, 'a+')as a:
                        a.write('<div class="col-md-10 font-weight-bold"><br>')
                        a.write(str(_))
                        a.write('</div><br>')
                else:
                    pass
            except Exception as e:
                pass
                pass
    except Exception as e:
        pass
        pass
    for x in file_list:
        for z in backup_suffix:
            urll = url.strip('/') + '/' +x + z
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                r_domain = requests.head(url=urll, headers=headers, timeout=5)
                dd4 = ' [ Scan : '+ str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>'+ '' + ' ' + str(r_domain.status_code) + '    ' + str(urll)
                print dd4
                with open('log.txt', 'a+')as aaa:
                    aaa.write(dd4 + '\n')
                if r_domain.status_code == 200:
                    with open('log.txt', 'a+')as aaa:
                        aaa.write(str(r_domain.headers) + '\n')
                    try:
                        if int(r_domain.headers["Content-Length"]) > 2000000:
                            rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                            list_result.append(str(str(r_domain.url) + '------' + str(rar_size) + '------' + str(web_title)))
                        else:
                            pass
                    except Exception as e:
                        pass
                        pass
                else:
                    pass
            except Exception, e:
                pass
                pass
    for x in dir_list:
        for y in file_list:
            for z in backup_suffix:
                urll = url.strip('/') + '/'  + x + '/' + y + z
                try:
                    UA = random.choice(headerss)
                    headers = {'User-Agent': UA}
                    r_domain = requests.head(url=urll, headers=headers, timeout=5)
                    # print 'Cheaking>>>' + r_domain.url
                    # print r_domain.url + " : " + str(r_domain.status_code)
                    dd5 = ' [ Scan : '+ str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>'+ '' + ' ' + str(r_domain.status_code) + '    ' + str(urll)
                    print dd5
                    with open('log.txt', 'a+')as aaa:
                        aaa.write(dd5 + '\n')
                    if r_domain.status_code == 200:
                        with open('log.txt', 'a+')as aaa:
                            aaa.write(str(r_domain.headers) + '\n')
                        try:
                            if int(r_domain.headers["Content-Length"]) > 2000000:
                                rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                                list_result.append(str(str(r_domain.url) + '------' + str(rar_size) + '------' + str(web_title)))
                            else:
                                pass
                        except Exception as e:
                            pass
                            pass
                    else:
                        pass
                except Exception,e:
                    pass
                    pass
    list_result=list(set(list_result))
    if list_result!=[] and list_result!= None:
        with open(result_name, 'a+')as a:
            for _ in list_result:
                a.write('<div class="col-md-10 font-weight-bold"><br>')
                a.write(str(_))
                a.write('</div><br>')

if __name__ == '__main__':
    freeze_support()
    print ('''

             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      
                               |___/       Version:2.3

    ''')
    time.sleep(3)
    result_name = str(time.strftime("%Y-%m-%d-%H", time.localtime())).replace(' ', '') + '.html'
    url_list = list(set([x.replace('\n', '') if x.startswith('http')  else 'http://' + x.replace('\n', '') for x in open('url.txt', 'r').readlines()]))
    with open(str(result_name),'a+')as a:
        a.write('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Lang_BackUp_Scan_Result ver 2.3</title>
        <link rel="stylesheet" href='https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap-theme.min.css'>
        <link rel="stylesheet" href='https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css'>
        </head>
        <div class="container">
            <div class="navbar navbar-default">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Lang</a>
        </div>
            <ul class="nav navbar-nav">
                <li><a href="http://www.langzi.fun/Python%20批量扫描备份文件.html">项目地址</a></li>
                <li><a href="http://www.langzi.fun/URL路径模糊测试.html">项目升级</a></li>
                <li><a href="http://langzi.fun:9827">妹子</a></li>
            </ul>

            </div>
        </div>
        <div class="container">

        ''')

    for _ in dict_list:
        backup_name.append(_.split('.')[0][1:])
    backup_name = list(set(backup_name))
    with open('log.txt','a+')as a:
        a.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'\n')
    smxc = int(input(unicode('设置线程池数量(8-1024):','utf-8').encode('gbk')))
    time.sleep(random.randint(1, 4))
    print unicode('线程池创建成功...', 'utf-8')
    print unicode('正在创建字典动态规则...', 'utf-8')
    time.sleep(random.randint(1,5))
    print unicode('正在创建目录动态规则...', 'utf-8')
    time.sleep(random.randint(1,5))
    print unicode('新规则创建成功，开始计算总任务量...', 'utf-8')
    time.sleep(random.randint(1,5))
    count = len(url_list)*(len(dict_list)+50)*13+15*len(url_list)*(len(dict_list)+50)*13
    count_time = count/72000/smxc
    print unicode('预计总任务量:%s'%count, 'utf-8')
    print unicode('预计耗时:%s小时'%count_time, 'utf-8')
    time.sleep(random.randint(1,5))
    p = multiprocessing.Pool(smxc)
    for _ in url_list:
        p.apply_async(scan,args=(_,result_name))
    p.close()
    p.join()
    os.system('pause')
