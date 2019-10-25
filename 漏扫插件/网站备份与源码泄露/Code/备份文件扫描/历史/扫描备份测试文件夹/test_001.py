# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 0008 16:32
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : test_001.py
# @Software: PyCharm
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup as bp4
import lxml

# url = 'http://www.hntky.com/'
# r = requests.get(url).content
# bp = bs(r,'lxml')
# print bp.title.string
# d = bp.find_all('a')
# for x in d:
#     xx = x['href'].replace(url,'')
#     if xx.find(':')<0 and xx.find('java')<0 and xx.find('http')<0:
#         print xx
#         d = xx.split('/')
#         for _ in range(len(d)-1):
#             if d[_] != '':
#                 print d[_]


# ll = []
# backup_name_B = ['/a.zip','/web.zip','/web.rar','/1.rar','/bbs.rar','/www.root.rar','/123.rar','/data.rar','/bak.rar','/oa.rar','/admin.rar','/www.rar','/2014.rar','/2015.rar','/2016.rar','/2014.zip','/2015.zip','/2016.zip','/2017.zip','/1.zip','/1.gz','/1.tar.gz','/2.zip','/2.rar','/123.rar','/123.zip','/a.rar','/a.zip','/admin.rar','/back.rar','/backup.rar','/bak.rar','/bbs.rar','/bbs.zip','/beifen.rar','/beifen.zip','/beian.rar','/data.rar','/data.zip','/db.rar','/db.zip','/flashfxp.rar','/flashfxp.zip','/fdsa.rar','/ftp.rar','/gg.rar','/hdocs.rar','/hdocs.zip','/HYTop.mdb','/root.rar','/Release.rar','/Release.zip','/sql.rar','/test.rar','/template.rar','/template.zip','/upfile.rar','/vip.rar','/wangzhan.rar','/wangzhan.zip','/web.rar','/web.zip','/website.rar','/www.rar','/www.zip','/wwwroot.rar','/wwwroot.zip','/wz.rar']
# for _ in backup_name_B:
#     ll.append("'"+_.replace('/','').replace('zip','').replace('rar','').replace('mdb','').replace('.','')+"',")
#
# for _ in list(set(ll)):
#     sys.stdout.write(_)


def get_dir(url):
    list_a_dir = []
    try:
        bp = bp4(requests.get(url,timeout=5, allow_redirects=False).content, 'lxml')
        for _ in bp.find_all('a'):
            url_info = _['href'].replace(url, '')
            # url_info 就是href的内容 /aa/aaa
            # 接下来要对内容进行判断
            if url_info.find(':') < 0 and url_info.find('//')<0 and url_info.find('java') < 0 and url_info.find('http:') < 0 and url_info.find('=') < 0 and url_info.find('?') < 0 :
                # 这里是去除了没用的之后正确的目录
                if url_info.startswith('/'):
                   print (url_info.encode('utf-8').split('/')[-1].encode('utf-8').split('.')[0])
    except Exception,e:
        print e
    # try:
    #
    #     for _ in bp.find_all('img'):
    #         url_info = _['src'].replace(url, '')
    #         if url_info.startswith('/'):
    #             xx = url_info.split('/')[1]
    #             list_a_dir.append('/' + xx)
    #             count = len(url_info.split('/')) - 1
    #             print count
    #             # 完整的目录保存
    #             if count > 2:
    #                 list_a_dir.append('/' + url_info.split('/')[1] + '/' + url_info.split('/')[2])
    #             if count > 3:
    #                 list_a_dir.append(
    #                     '/' + url_info.split('/')[1] + '/' + url_info.split('/')[2] + '/' + url_info.split('/')[
    #                         3])
    #
    # except Exception, e:
    #     pass
    # return list(set(list_a_dir))


get_dir('http://www.langzi.fun')