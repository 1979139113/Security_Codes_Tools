#!/usr/bin/env python
# -*- conding:utf-8 -*- 
import re,os
import urllib.request,urllib.parse

def Obtain_url(): #爬抓bing获取url

    dir = 'http'

    page = ['', '&first=11&FORM=PERE', '&first=21&FORM=PERE1', '&first=31&FORM=PERE2',
            '&first=41&FORM=PERE3', '&first=51&FORM=PERE4']
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.baidu.com',
        'Connection': 'keep-alive'
    }
    name = input('filename=')
    with open('http/%s.txt'%(name),'r') as f:  #打开文件
        for i in f.readlines():
            crux = 'site:'+i
            print(crux)
            crux = urllib.parse.quote(crux)   #解决编码报错问题
            with open('http/%s_url.txt'%(name), 'a', encoding='utf-8') as f:
                for i in page:
                    try:
                        content = urllib.request.Request('https://cn.bing.com/search?q='+crux,headers=headers)
                        contents = urllib.request.urlopen(content,timeout=3).read().decode('utf-8')
                        res = re.compile(r'<h2><a target="_blank" href="(.*?)"')
                        data = res.findall(contents)
                    except:
                        print("出错了！！！！！！！！！！")
                    if data == []:
                        break
                    for i in data:
                        print(i)
                        f.write(i+'\n')

def url():  #处理bing爬抓下来的链接
    url = []
    dir = 'http'
    files= os.walk(dir)
    # print (os.walk(dir))
    # print(files[2])
    for files in os.walk(dir):
        filename = files[2]
    for i in filename:
        with open('http/%s'%(i),'r',encoding='utf-8') as f:  #读取文件内容到列表里
            for i in f.readlines():
                url.append(i)
        data = list(set(url))  #去重url列表
        data = sorted(data)    #排列顺序
        with open('http/new_url.txt','a',encoding='utf-8') as f:  #判断url是否有.php? .asp? .aspx? .jsp?
            for i in data:
                res = re.compile(r'login')
                datas = res.findall(i)
                if datas != []:
                    f.write(i)
                else:
                    res = re.compile(r'callback|admin|login|url=|manager|user|cookie|list|jquery|')
                    datas = res.findall(i)
                    if datas != []:
                        f.write(i)
                    # else:
                    #     res = re.compile(r'\.aspx\?')
                    #     datas = res.findall(i)
                    #     if datas != []:
                    #         f.write(i)
                    #     else:
                    #         res = re.compile(r'\.php\?')
                    #         datas = res.findall(i)
                    #         if datas != []:
                    #             f.write(i)
Obtain_url()
url()