# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 0012 17:31
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 扫描备份1.0.py
# @Software: PyCharm
import sys
import requests
import multiprocessing
import re
import os
import time
import random

reload(sys)
sys.setdefaultencoding('utf-8')

os.system('color a')

dir_list = ['www', 'data', 'backup']

backup_name_A = ['.rar', '.zip', '.tar', '.tar.bz2', '.sql', '.7z', '.bak', '.txt', '.tar.gz', '.iso', '.gz']

backup_name_C = list(set([x.replace('\n', '') for x in open('rar.txt', 'r').readlines()]))

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


def scan(urlx, result_name):
    result_name = result_name
    backup_name_B = []
    # result_list=[]
    # http://www.langzi.fun 或者 http://www.hao.langzi.fun
    k1 = urlx.split('//')[1]
    # www.langzi.fun
    k2 = urlx.split('//')[1].replace('.', '_')
    # www_langzi_fun
    k3 = urlx.split('.', 1)[1].replace('/', '')
    # langzi.fun
    k3_1 = urlx.split('.', 1)[1].replace('/', '').replace('.', '_')
    # langzi_fun
    k3_2 = urlx.split('.', 1)[1].replace('/', '').replace('.', '')
    # langzifun
    k3_3 = urlx.split('.', 1)[1].replace('/', '').replace('.', '-')
    # langzi-fun
    k4 = urlx.split('//')[1].split('.')[1]
    # langzi
    k4_2 = urlx.split('//')[1].split('.')[0] if urlx.split('//')[1].split('.')[0] != 'www' else \
    urlx.split('//')[1].split('.')[1]
    # www
    if urlx.find('.') == 3:
        k4_1 = urlx.split('//')[1].split('.')[2]
        # fun
        k29 = k4_1 + '2015'
        k30 = k4_1 + '2016'
        k31 = k4_1 + '2017'
        k32 = k4_1 + '2018'
        backup_name_B.append(k4_1)
        backup_name_B.append(k29)
        backup_name_B.append(k30)
        backup_name_B.append(k31)
        backup_name_B.append(k32)

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

    backup_name_B.append(k1)
    backup_name_B.append(k2)
    backup_name_B.append(k3)
    backup_name_B.append(k4)
    backup_name_B.append(k5)
    backup_name_B.append(k6)
    backup_name_B.append(k7)
    backup_name_B.append(k8)
    backup_name_B.append(k9)
    backup_name_B.append(k10)
    backup_name_B.append(k11)
    backup_name_B.append(k12)
    backup_name_B.append(k13)
    backup_name_B.append(k14)
    backup_name_B.append(k15)
    backup_name_B.append(k16)
    backup_name_B.append(k17)
    backup_name_B.append(k18)
    backup_name_B.append(k19)
    backup_name_B.append(k20)
    backup_name_B.append(k21)
    backup_name_B.append(k22)
    backup_name_B.append(k23)
    backup_name_B.append(k24)
    backup_name_B.append(k25)
    backup_name_B.append(k26)
    backup_name_B.append(k27)
    backup_name_B.append(k28)
    backup_name_B.append(k3_3)
    backup_name_B.append(k3_2)
    backup_name_B.append(k3_1)
    backup_name_B.append(k4_2)
    try:
        backup_name_B = list(set(backup_name_B))
    except:
        pass
    if urlx.endswith('/'):
        url = urlx
    else:
        url = urlx + '/'
    # try:
    #     web_title = '获取网站标题失败'
    #     UA = random.choice(headerss)
    #     headers = {'User-Agent': UA}
    #     r_info_top = requests.get(url=url, headers=headers, timeout=5)
    #     if r_info_top.encoding == 'ISO-8859-1':
    #         encodings = requests.utils.get_encodings_from_content(r_info_top.text)
    #         if encodings:
    #             encoding = encodings[0]
    #         else:
    #             encoding = r_info_top.apparent_encoding
    #         encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    #         web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
    #             '</title>', '')
    #     elif r_info_top.encoding == 'GB2312':
    #         encodings = requests.utils.get_encodings_from_content(r_info_top.text)
    #         if encodings:
    #             encoding = encodings[0]
    #         else:
    #             encoding = r_info_top.apparent_encoding
    #         encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    #         web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
    #             '</title>', '')
    #     elif r_info_top.encoding == 'gb2312':
    #         encodings = requests.utils.get_encodings_from_content(r_info_top.text)
    #         if encodings:
    #             encoding = encodings[0]
    #         else:
    #             encoding = r_info_top.apparent_encoding
    #         encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    #         web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
    #             '</title>', '')
    #     elif r_info_top.encoding == 'GBK':
    #         encodings = requests.utils.get_encodings_from_content(r_info_top.text)
    #         if encodings:
    #             encoding = encodings[0]
    #         else:
    #             encoding = r_info_top.apparent_encoding
    #         encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    #         web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
    #             '</title>', '')
    #     elif r_info_top.encoding == 'gbk':
    #         encodings = requests.utils.get_encodings_from_content(r_info_top.text)
    #         if encodings:
    #             encoding = encodings[0]
    #         else:
    #             encoding = r_info_top.apparent_encoding
    #         encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    #         web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
    #             '</title>', '')
    #     else:
    #         web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
    #                                                                                                 '').replace(
    #             '</title>', '')
    # except:
    #     try:
    #         web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
    #                                                                                                 '').replace(
    #             '</title>', '')
    #     except:
    #         web_title = '暂时无法获取网站标题'

    # url_svn = url + '.svn/entries'
    # # print 'Cheaking>>>' + url_svn
    # # 扫描svn源码泄露  组合成链接
    # try:
    #     UA = random.choice(headerss)
    #     headers = {'User-Agent': UA}
    #     r_svn = requests.head(url=url_svn, headers=headers, timeout=5)
    #     # 访问这个链接  超时设置5秒
    #     # print r_svn.url + " : " + str(r_svn.status_code)
    #     # 打印出这个网址 和 访问状态码
    #     dd1 = ' [ Scan : ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>' + '' + ' ' + str(
    #         r_svn.status_code) + '    ' + str(url_svn)
    #     print dd1
    #     with open('log.txt', 'a+')as aaa:
    #         aaa.write(dd1 + '\n')
    #     if r_svn.status_code == 200:
    #         with open('log.txt', 'a+')as aaa:
    #             aaa.write(str(r_svn.headers) + '\n')
    #         # 如果状态码是200  表示访问成功
    #         try:
    #             r_svn_1 = requests.get(url=url_svn, headers=headers, timeout=5)
    #             with open('log.txt', 'a+')as aaa:
    #                 aaa.write(r_svn_1.content + '\n')
    #             if 'dir' in r_svn_1.content and 'svn://' in r_svn_1.content:
    #                 _ = (str(str(r_svn_1.url) + '------' + str('SVN源码泄露') + '------' + str(web_title)))
    #                 with open(result_name, 'a+')as a:
    #                     a.write('<div class="col-md-10 font-weight-bold"><br>')
    #                     a.write(str(_))
    #                     a.write('</div><br>')
    #         except Exception as e:
    #             pass
    #             pass
    #     else:
    #         pass
    # except Exception as e:
    #     pass
    #
    #     # pass
    #     ######################################
    #     # svn源码泄露扫描完毕
    #     ######################################
    #
    # url_git = url + '.git/config'
    # # print 'Cheaking>>>' + url_git
    # try:
    #     UA = random.choice(headerss)
    #     headers = {'User-Agent': UA}
    #     r_git = requests.head(url=url_git, headers=headers, timeout=5)
    #     # print r_git.url + " : " + str(r_git.status_code)
    #     dd2 = ' [ Scan : ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>' + '' + ' ' + str(
    #         r_git.status_code) + '    ' + str(url_git)
    #     print dd2
    #     with open('log.txt', 'a+')as aaa:
    #         aaa.write(dd2 + '\n')
    #     if r_git.status_code == 200:
    #         with open('log.txt', 'a+')as aaa:
    #             aaa.write(str(r_git.headers) + '\n')
    #         try:
    #             r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
    #             if 'repositoryformatversion' in r_git_1.content:
    #                 with open('log.txt', 'a+')as aaa:
    #                     aaa.write(r_git_1.content + '\n')
    #                 # repositoryformatversion 这个是git源码泄露的特征码
    #                 _ = (str(str(r_git_1.url) + '------' + str('GIT源码泄露') + '------' + str(web_title)))
    #                 with open(result_name, 'a+')as a:
    #                     a.write('<div class="col-md-10 font-weight-bold"><br>')
    #                     a.write(str(_))
    #                     a.write('</div><br>')
    #             else:
    #                 pass
    #         except Exception as e:
    #             pass
    #             pass
    # except Exception as e:
    #     pass
    #     pass
    # url_info = url + 'WEB-INF/web.xml'
    # # print 'Cheaking>>>' + url_git
    # try:
    #     UA = random.choice(headerss)
    #     headers = {'User-Agent': UA}
    #     r_info = requests.head(url=url_info, headers=headers, timeout=5)
    #     # print r_git.url + " : " + str(r_git.status_code)
    #     dd3 = ' [ Scan : ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>' + '' + ' ' + str(
    #         r_info.status_code) + '    ' + str(url_info)
    #     print dd3
    #
    #     with open('log.txt', 'a+')as aaa:
    #         aaa.write(dd3 + '\n')
    #     if r_info.status_code == 200:
    #         with open('log.txt', 'a+')as aaa:
    #             aaa.write(str(r_info.headers) + '\n')
    #         try:
    #             r_info_1 = requests.get(url=url_info, headers=headers, timeout=5)
    #             with open('log.txt', 'a+')as aaa:
    #                 aaa.write(r_info_1.content + '\n')
    #             if '<web-app' in r_info_1.content:
    #                 _ = (str(str(r_info_1.url) + '------' + str('WEBinfo信息泄露') + '------' + str(web_title)))
    #                 with open(result_name, 'a+')as a:
    #                     a.write('<div class="col-md-10 font-weight-bold"><br>')
    #                     a.write(str(_))
    #                     a.write('</div><br>')
    #             else:
    #                 pass
    #         except Exception as e:
    #             pass
    #             pass
    # except Exception as e:
    #     pass
    #     pass
    for x in backup_name_B:
        for y in backup_name_A:
            urll = url.strip('/') + '/' + x + y
            with open('log.txt', 'a+')as aaa:
                aaa.write(urll +'\n')
    #         try:
    #             UA = random.choice(headerss)
    #             headers = {'User-Agent': UA}
    #             r_domain = requests.head(url=urll, headers=headers, timeout=5)
    #             dd4 = ' [ Scan : ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>' + '' + ' ' + str(
    #                 r_domain.status_code) + '    ' + str(urll)
    #             print dd4
    #             with open('log.txt', 'a+')as aaa:
    #                 aaa.write(dd4 + '\n')
    #             if r_domain.status_code == 200:
    #                 with open('log.txt', 'a+')as aaa:
    #                     aaa.write(str(r_domain.headers) + '\n')
    #                 try:
    #                     if int(r_domain.headers["Content-Length"]) > 2000000:
    #                         rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
    #                         _ = (str(str(r_domain.url) + '------' + str(rar_size) + '------' + str(web_title)))
    #                         with open(result_name, 'a+')as a:
    #                             a.write('<div class="col-md-10 font-weight-bold"><br>')
    #                             a.write(str(_))
    #                             a.write('</div><br>')
    #                     else:
    #                         pass
    #                 except Exception as e:
    #                     pass
    #                     pass
    #             else:
    #                 pass
    #         except Exception, e:
    #             pass
    #
    for x in backup_name_C:
        urll = url.strip('/') + x
        with open('log.txt', 'a+')as aaa:
            aaa.write(urll +'\n')
    #     try:
    #         UA = random.choice(headerss)
    #         headers = {'User-Agent': UA}
    #         r_domain = requests.head(url=urll, headers=headers, timeout=5)
    #         dd4 = ' [ Scan : ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>' + '' + ' ' + str(
    #             r_domain.status_code) + '    ' + str(urll)
    #         print dd4
    #         with open('log.txt', 'a+')as aaa:
    #             aaa.write(dd4 + '\n')
    #         if r_domain.status_code == 200:
    #             with open('log.txt', 'a+')as aaa:
    #                 aaa.write(str(r_domain.headers) + '\n')
    #             try:
    #                 if int(r_domain.headers["Content-Length"]) > 2000000:
    #                     rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
    #                     _ = (str(str(r_domain.url) + '------' + str(rar_size) + '------' + str(web_title)))
    #                     with open(result_name, 'a+')as a:
    #                         a.write('<div class="col-md-10 font-weight-bold"><br>')
    #                         a.write(str(_))
    #                         a.write('</div><br>')
    #                 else:
    #                     pass
    #             except Exception as e:
    #                 pass
    #                 pass
    #         else:
    #             pass
    #     except Exception, e:
    #         pass
    #
    for x in dir_list:
        for y in backup_name_B:
            for z in backup_name_A:
                urll = url.strip('/') + '/' + x + '/' + y + z
                with open('log.txt', 'a+')as aaa:
                    aaa.write(urll + '\n')
    #             try:
    #                 UA = random.choice(headerss)
    #                 headers = {'User-Agent': UA}
    #                 r_domain = requests.head(url=urll, headers=headers, timeout=5)
    #                 dd4 = ' [ Scan : ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>' + '' + ' ' + str(
    #                     r_domain.status_code) + '    ' + str(urll)
    #                 print dd4
    #                 with open('log.txt', 'a+')as aaa:
    #                     aaa.write(dd4 + '\n')
    #                 if r_domain.status_code == 200:
    #                     with open('log.txt', 'a+')as aaa:
    #                         aaa.write(str(r_domain.headers) + '\n')
    #                     try:
    #                         if int(r_domain.headers["Content-Length"]) > 2000000:
    #                             rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
    #                             _ = (str(str(r_domain.url) + '------' + str(rar_size) + '------' + str(web_title)))
    #                             with open(result_name, 'a+')as a:
    #                                 a.write('<div class="col-md-10 font-weight-bold"><br>')
    #                                 a.write(str(_))
    #                                 a.write('</div><br>')
    #                         else:
    #                             pass
    #                     except Exception as e:
    #                         pass
    #                         pass
    #                 else:
    #                     pass
    #             except Exception, e:
    #                 pass
    #
    for x in dir_list:
        for y in backup_name_C:
            urll = url.strip('/') + '/' + x + y
            with open('log.txt', 'a+')as aaa:
                aaa.write(urll +'\n')
    #         try:
    #             UA = random.choice(headerss)
    #             headers = {'User-Agent': UA}
    #             r_domain = requests.head(url=urll, headers=headers, timeout=5)
    #             dd4 = ' [ Scan : ' + str(time.strftime("%H:%M:%S", time.localtime())) + ' ]   >>>' + '' + ' ' + str(
    #                 r_domain.status_code) + '    ' + str(urll)
    #             print dd4
    #             with open('log.txt', 'a+')as aaa:
    #                 aaa.write(dd4 + '\n')
    #             if r_domain.status_code == 200:
    #                 with open('log.txt', 'a+')as aaa:
    #                     aaa.write(str(r_domain.headers) + '\n')
    #                 try:
    #                     if int(r_domain.headers["Content-Length"]) > 2000000:
    #                         rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
    #                         _ = (str(str(r_domain.url) + '------' + str(rar_size) + '------' + str(web_title)))
    #                         with open(result_name, 'a+')as a:
    #                             a.write('<div class="col-md-10 font-weight-bold"><br>')
    #                             a.write(str(_))
    #                             a.write('</div><br>')
    #                     else:
    #                         pass
    #                 except Exception as e:
    #                     pass
    #                     pass
    #             else:
    #                 pass
    #         except Exception, e:
    #             pass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print ('''

             _                           _ 
            | |                         (_)
            | |     __ _ _ __   __ _ _____ 
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      
                               |___/       Version:1.0

    ''')
    time.sleep(3)
    result_name = str(time.strftime("%Y-%m-%d-%H", time.localtime())).replace(' ', '') + '.html'
    with open('log.txt', 'a+')as a:
        a.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
    url_list = list(set([x.replace('\n', '') if x.startswith('http')  else 'http://' + x.replace('\n', '') for x in open('url.txt', 'r').readlines()]))
    for x in url_list:
        scan(x,result_name)
    # with open(str(result_name), 'a+')as a:
    #     a.write('''
    #     <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <title>Lang_BackUp_Scan_Result ver 1.0</title>
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
    # smxc = int(input(unicode('设置线程池数量(8-1024):', 'utf-8').encode('gbk')))
    # p = multiprocessing.Pool(smxc)
    # for _ in url_list:
    #     p.apply_async(scan, args=(_, result_name))
    # p.close()
    # p.join()
    os.system('pause')


