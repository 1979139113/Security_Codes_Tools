# coding:gbk
import requests
import sys
import chardet
requests.packages.urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('gbk')
a = ['���','��','����']
print '|'.join(a).decode('gbk')
# b = str(a).replace('[','').replace(']','').replace(',',' ').decode('gbk')
# print b
# print chardet.detect(b)


# import re
# def scan(x):
#     url = 'http://jygh.fxedu.cn'
#     headers = 'None'
#     try:
#         cms_title = '��ʱ�޷���ȡ��վ����'
#         r_cms_top = requests.get(url=url, timeout=5)
#         if isinstance(r_cms_top.content,unicode):
#             ucontent = r_cms_top.content
#         else:
#             code = chardet.detect(r_cms_top.content)['encoding']
#             ucontent = r_cms_top.content.decode(code)
#         cms_title = re.search('<title>(.*?)</title>', ucontent, re.S).group().replace('<title>','').replace('</title>', '')
#     except:
#         pass
#     if '���͹����Ӵ�'.decode('gbk') == cms_title:
#         print '���͹����Ӵ�'.decode('gbk')
#
# scan('a')
