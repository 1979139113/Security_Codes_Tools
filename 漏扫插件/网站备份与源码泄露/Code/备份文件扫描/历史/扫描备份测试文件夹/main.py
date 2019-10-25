# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 0008 16:27
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : main.py
# @Software: PyCharm
import sys
import requests
import time
import difflib
from bs4 import BeautifulSoup as bp4
import random
reload(sys)
sys.setdefaultencoding('utf-8')

dir_list=list(set([x.replace('\n','')  for x in open('dir_dict.txt','r').readlines()]))
file_list = list(set([x.replace('\n','')  for x in open('file_dict.txt','r').readlines()]))

backup_suffix = ['.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt','.tar.gz','.iso','.gz','.sql','.exe']
backup_name = ['hdocs','2016','upfile','wwwroot','flashfxp','2017','ftp','Release','website','2015','HYTop','backup','0','tar.gz','wangzhan','test','data','bbs','web','www','www.root','wz','beian','sql','gg','oa','admin','123','template','1gz','1','fdsa','2014','root','vip','beifen','back','a','%E5%A4%87%E4%BB%BD','bak','2','db','2018']

file_suffix=['.php','.asp','.aspx','.yml','.ini','.swp','.jsp','.do','.action','.sh','.html','.txt','.htm','.shtml','.xml','.json','.api','.config','.configs','.xmls']

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

class scan:
    def __init__(self,url):
        self.url=url
        try:
            self.web_title = '获取网址标题失败'
            bp = bp4(requests.get(self.url, timeout=5).content, 'lxml')
            self.web_title = bp.title.string
        except Exception,e:
            print e
    def get_dir(self,uuiu=None):
        if uuiu == None:
            self.url=self.url
        else:
            self.url =uuiu
        list_a_dir = []
        print self.url
        try:
            bp = bp4(requests.get(self.url, timeout=5).content, 'lxml')
            for _ in bp.find_all('a'):
                url_info = _['href'].replace(self.url, '')
                # url_info 就是href的内容 /aa/aaa
                # 接下来要对内容进行判断
                if url_info.find(':') < 0 and url_info.find('//') < 0 and url_info.find('java') < 0 and url_info.find(
                        'http:') < 0 and url_info.find('=') < 0 and url_info.find('?') < 0:
                    # 这里是去除了没用的之后正确的目录
                    if url_info.startswith('/'):
                        count = len(url_info.split('/')) - 1
                        # print url_info
                        if '.' not in url_info.split('/')[-1]:
                            list_a_dir.append('/' + url_info.strip('/'))
                        # 完整的目录保存
                        if count > 2:
                            list_a_dir.append(('/' + url_info.split('/')[1] + '/' + url_info.split('/')[2].strip('/')))
                        if count > 3:
                            list_a_dir.append(('/' + url_info.split('/')[1] + '/' + url_info.split('/')[2] + '/' +
                                               url_info.split('/')[3].strip('/')))
                    else:
                        pass
                        # print url_info
        except Exception, e:
            print e
        try:
            for _ in bp.find_all('img'):
                url_info = _['src'].replace(self.url, '')
                if url_info.startswith('/'):
                    xx = url_info.split('/')[1]
                    list_a_dir.append('/' + xx)
                    count = len(url_info.split('/')) - 1
                    # 完整的目录保存
                    if count > 2:
                        list_a_dir.append('/' + url_info.split('/')[1] + '/' + url_info.split('/')[2])
                    if count > 3:
                        list_a_dir.append(
                            '/' + url_info.split('/')[1] + '/' + url_info.split('/')[2] + '/' + url_info.split('/')[
                                3])
        except Exception, e:
            pass
        return list(set(list_a_dir))

    def get_404(self,urli):
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r = requests.get(self.url + '/langzilove', timeout=5).content
            try:
                r1 = requests.get(url=urli, timeout=5)
                did = (difflib.SequenceMatcher(None, r, r1.content).quick_ratio())
                didx = int(str(difflib.SequenceMatcher(None, r, r1.content).quick_ratio()*10000).split('.')[0])
                print '【DifferentPG Check:%s】'%str(r1.status_code) + '    ' + r1.url + '  404页面相似度:' + str(did)
                if didx < 4321:
                    #print '<<<<<<<'
                    return True
                    # 相似度大于0.5 就说明是错误的网址
                else:
                    #print '>>>>>>>>>>>'
                    return False
            except Exception, e:
                print e
                return False
        except Exception,e:
            print e
            print '获取404页面失败'
            return False

    def get_keyword(self):
        backup_name1 = []
        #'http://www.langzi.fun'
        k1 = self.url.split('//')[1]
        # www.langzi.fun
        k2 = self.url.split('//')[1].replace('.','')
        # wwwlangzifun
        k3 = self.url.split('.', 1)[1].replace('/', '')
        # langzi.fun
        k4 = self.url.split('//')[1].split('.')[1]
        # langzi
        k5 = k4 + '2015'
        k6 = k4 + '2016'
        k7 = k4 + '2017'
        k8 = k4 + '2018'
        # langzi2015
        k9 =  k1 + '2015'
        k10 = k1 + '2016'
        k11 = k1 + '2017'
        k12 = k1 + '2018'
        # www.langzi.fun2015
        k13 = k3 + '2015'
        k14 = k3 + '2016'
        k15 = k3 + '2017'
        k16 = k3 + '2018'
        # langzi.fun2015
        k17 = self.url
        k18 = k3.replace('.','')
        # langzifun
        backup_name1.append(k1)
        backup_name1.append(k2)
        backup_name1.append(k3)
        backup_name1.append(k4)
        backup_name1.append(k5)
        backup_name1.append(k6)
        backup_name1.append(k7)
        backup_name1.append(k8)
        backup_name1.append(k9)
        backup_name1.append(k10)
        backup_name1.append(k11)
        backup_name1.append(k12)
        backup_name1.append(k13)
        backup_name1.append(k14)
        backup_name1.append(k15)
        backup_name1.append(k16)
        backup_name1.append(k17)
        backup_name1.append(k18)
        return backup_name1


    def get_active_name(self,uxu=None):
        if uxu == None:
            url = self.url
        else:
            url = self.url + uxu
        print url
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        list_a_dir=[]
        try:
            bp = bp4(requests.get(url, timeout=5).content, 'lxml')
            for _ in bp.find_all('a'):
                url_info = _['href'].replace(url, '')
                # url_info 就是href的内容 /aa/aaa
                # 接下来要对内容进行判断
                if url_info.find(':') < 0 and url_info.find('//') < 0 and url_info.find('java') < 0 and url_info.find(
                        'http:') < 0 and url_info.find('=') < 0 and url_info.find('?') < 0:
                    # 这里是去除了没用的之后正确的目录
                    if url_info.startswith('/'):
                        try:
                            list_a_dir.append(url_info.decode('utf-8').split('/')[-1].decode('utf-8').split('.')[-1])
                        except Exception,e:
                            print e
            return list(set(list_a_dir))
        except Exception, e:
            print e

    def ckeck_backup_file(self,urlx):
        url = self.url + urlx
        print url
        try:
            r_domain = requests.head(url, timeout=10)
            print '【Status_Code Ckeck:%s】' % str(r_domain.status_code) + '    ' + r_domain.url
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        return str(r_domain.url + '     ' + str(rar_size) +'    ' +  self.web_title )
                    else:
                        pass
                except Exception as e:
                    pass
        except Exception, e:
            print e

    def check_file(self,urll):
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        url = self.url + urll
        try:
            r_domain = requests.head(url,timeout=10)
            print '【Status_Code Ckeck:%s】' % str(r_domain.status_code) + '    ' + r_domain.url
            if r_domain.status_code !=404:
                try:
                    result = self.get_404(url)
                    if result == True:
                        return True
                    else:
                        return False
                except Exception as e:
                    pass
        except Exception,e:
            print e
            return False


    def check_dir(self,urla):
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        url = self.url + urla +'/'
        try:
            r_domain = requests.head(url,timeout=10)
            print '【Status_Code ckeck:%s】' % str(r_domain.status_code) + '    ' + r_domain.url
            if r_domain.status_code != 404:
                try:
                    result = self.get_404(url)
                    if result == True:
                        # 这是正确的存在的页面
                        return True
                    else:
                        return False
                except Exception as e:
                    pass
        except Exception,e:
            print e
            return False

url007 = "http://www.hntky.com"
start = scan(url=url007)

backup_files = start.get_keyword()
dirs = start.get_dir()
files = start.get_active_name()

dir_list.extend(dirs)
file_list.extend(files)
backup_name.extend(backup_files)

dir_list = list(set(dir_list))
file_list = list(set(file_list))
backup_name = list(set(backup_name))


def check_dir():
    global dir_list
    global file_list
    global backup_name
    for _ in dir_list:
        dd = start.check_dir(_)
        if dd == True:
            with open('result.txt', 'a+')as a:
                a.write(url007 + '\n')
        # 如果第一个目录存在
            da = start.get_active_name(_)
            # 获取正确目录下的文件名
            if da !=None:
                file_list.extend(da)
                backup_name.extend(da)
                #dir_list.extend(da)
                dir_list = list(set(dir_list))
                file_list = list(set(file_list))
                backup_name = list(set(backup_name))
                for x in file_list:
                    for z in file_suffix:
                        houzhui = _ + '/' +x + z
                        ee = start.check_file(houzhui)
                        if ee == True:
                            with open('result.txt', 'a+')as a:
                                a.write(url007 + houzhui+ '\n')
                        # 如果这个网址存在的话
                            de = start.get_active_name(houzhui)
                            if de!= None:
                                file_list.extend(da)
                                backup_name.extend(da)
                                # dir_list.extend(da)
                                dir_list = list(set(dir_list))
                                file_list = list(set(file_list))
                                backup_name = list(set(backup_name))
                for x in backup_name:
                    for y in backup_suffix:
                        houzhui = _ + '/' + x + y
                        db = start.ckeck_backup_file(houzhui)
                        if db!=None:
                            with open('result.txt','a+')as a:
                                a.write(url007 + houzhui + '\n')
            else:
                for x in file_list:
                    for z in file_suffix:
                        houzhui = _ + '/' +x + z
                        ee = start.check_file(houzhui)
                        if ee == True:
                            with open('result.txt', 'a+')as a:
                                a.write(url007 + houzhui+ '\n')
                        # 如果这个网址存在的话
                            de = start.get_active_name(houzhui)
                            if de!= None:
                                file_list.extend(da)
                                backup_name.extend(da)
                                # dir_list.extend(da)
                                dir_list = list(set(dir_list))
                                file_list = list(set(file_list))
                                backup_name = list(set(backup_name))
                for x in backup_name:
                    for y in backup_suffix:
                        houzhui = _ + '/' + x + y
                        db = start.ckeck_backup_file(houzhui)
                        if db!=None:
                            with open('result.txt','a+')as a:
                                a.write(url007 + houzhui + '\n')
        else:
            print False

check_dir()


def check_file():
    for x in dir_list:
        for y in file_list:
            for z in file_suffix:
                houzhui =  x +'/' + y  + z
                if start.check_file(houzhui) ==True:
                    with open('resutl_url.txt','a+') as a:
                        a.write('http://www.langzi.fun' + houzhui + '\n')
                else:
                    print False


def check_backup():
    for x in dir_list:
        print x
        for y in backup_name:
            for z in backup_suffix:
                houzhui = x +'/' + y+z
                ress = start.ckeck_backup_file(houzhui)
                if ress !=None:
                    with open('result_backup.txt','a+')as a:
                        a.write('http://www.langzi.fun' + houzhui + '\n')


















