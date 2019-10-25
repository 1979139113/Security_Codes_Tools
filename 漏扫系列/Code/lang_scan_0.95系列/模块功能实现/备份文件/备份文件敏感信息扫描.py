# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
#http头部信息  用来告诉对方服务器我是用浏览器查看你的网站的  不加这个有可能不让访问
backup_name_A = ['.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt']
#定义一个列表  名字是 backup_name_A  里面的内容是要和域名组合在一起拼接的后缀
backup_name_B = list(set([i.replace("\n","") for i in open("rar.txt","r").readlines()]))
#常见的后缀 rar.txt当中每一行载入到这个列表当中
def scan_backupfile(url):
# 这个函数是专门扫描备份文件 敏感信息泄露  接受的参数是url
    url_svn = url + '/.svn/entries'
    print 'Cheaking>>>' + url_svn
#扫描svn源码泄露  组合成链接
    try:
        r_svn = requests.head(url=url_svn,headers=headers,timeout=5)
        #访问这个链接  超时设置5秒
        print r_svn.url + " : " + str(r_svn.status_code)
        #打印出这个网址 和 访问状态码
        if r_svn.status_code == 200:
        #如果状态码是200  表示访问成功
            try:
                r_svn_1 = requests.get(url=url_svn,headers=headers,timeout=5)
                #访问这个链接
                if 'dir' and 'svn' in r_svn_1.content:
                #判断关键词 dir 和svn 是不是在这个网页中
                    with open('svn.txt', 'a+')as a:
                    #如果存在 就写入本地的一个txt文件中【等全部模块实现后修改代码，存储数据库】
                        a.write(r_svn_1.url + '\n')
                else:
                    pass
            except Exception,e:
            #异常处理机制
                print e
        else:
            pass
    except Exception,e:
        print e
######################################
#svn源码泄露扫描完毕
######################################
    url_git = url + '/.git/config'
    print 'Cheaking>>>' + url_git
    try:
        r_git = requests.head(url=url_git,headers=headers,timeout=5)
        print r_git.url + " : " + str(r_git.status_code)
        if r_git.status_code == 200:
            try:
                r_git_1 = requests.get(url=url_git,headers=headers,timeout=5)
                if 'repositoryformatversion' in r_git_1.content:
                #repositoryformatversion 这个是git源码泄露的特征码
                    with open('git.txt','a+')as aa:
                        #同理写入本地
                        aa.write(r_git_1.url + '\n')
                else:
                    pass
            except Exception,e:
                print e
    except Exception,e:
        print e
######################################
#git源码泄露扫描完毕
######################################
    url_domain = url + '/' + url.split(".",2)[1]
    #http://www.baidu.com/baidu.
    for back_A in backup_name_A:
        try:
            r_domain = requests.head(url=str(url_domain + back_A),headers=headers,timeout=5)
            print 'Cheaking>>>' + r_domain.url
            print r_domain.url + " : " + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        print '---------------------------------'
                        print int(r_domain.headers["Content-Length"])
                        print '----------------------------------'
                    #这一行的意思是返回的对象的头部信息中 返回的大小大于2M
                        with open('beifen.txt','a+')as a:
                            a.write(str(r_domain.url + str(int(r_domain.headers["Content-Length"])) + '\n'))
                    else:
                        pass
                except Exception,e:
                    print e
            else:
                pass
        except Exception,e:
            print e
######################################
#域名加常见后缀组合扫描完毕
######################################
    for back_B in backup_name_B:
        url_rar = url + back_B
        #http://www.baidu.com/root.rar
        print 'Cheaking>>>' + url_rar
        try:
            r_rar = requests.head(url=str(url_rar),headers=headers,timeout=5)
            print r_rar.url + " : " + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        print '---------------------------------'
                        print int(r_rar.headers["Content-Length"])
                        print '----------------------------------'
                    #这一行的意思是返回的对象的头部信息中 返回的大小大于2M
                        with open('beifen.txt','a+')as a:
                            a.write(str(r_rar.url + str((r_rar.headers["Content-Length"])) + '\n'))
                    else:
                        pass
                except Exception,e:
                    print e
            else:
                pass
        except Exception,e:
            print e
######################################
#常见后缀组合扫描完毕
######################################
scan_backupfile('http://www.ptscz.gov.cn')
