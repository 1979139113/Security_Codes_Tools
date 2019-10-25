# coding:gbk
import requests
import sys
import chardet
requests.packages.urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('gbk')
a = ['你好','啊','世界']
print '|'.join(a).decode('gbk')
# b = str(a).replace('[','').replace(']','').replace(',',' ').decode('gbk')
# print b
# print chardet.detect(b)


# import re
# def scan(x):
#     url = 'http://jygh.fxedu.cn'
#     headers = 'None'
#     try:
#         cms_title = '暂时无法获取网站标题'
#         r_cms_top = requests.get(url=url, timeout=5)
#         if isinstance(r_cms_top.content,unicode):
#             ucontent = r_cms_top.content
#         else:
#             code = chardet.detect(r_cms_top.content)['encoding']
#             ucontent = r_cms_top.content.decode(code)
#         cms_title = re.search('<title>(.*?)</title>', ucontent, re.S).group().replace('<title>','').replace('</title>', '')
#     except:
#         pass
#     if '奉贤工会视窗'.decode('gbk') == cms_title:
#         print '奉贤工会视窗'.decode('gbk')
#
# scan('a')
