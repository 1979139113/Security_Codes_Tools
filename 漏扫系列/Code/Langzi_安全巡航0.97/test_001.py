# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import time
url = 'http://www.baidu.com'
common = 'run'
def check(result,url,common,title='error'):
    url = url.replace('^','')
    if '---' in result:
        if 'sqlmap was not able to fingerprint the back-end database management syste' not in result:
            try:
                result_info = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[',result,re.S)
                inj = result_info.group(1)
                dbs = result_info.group(2)
                print(inj.replace('Parameter: ','注入参数(方式) : ').replace('Type: ','注入方式 : ').replace('Title: ','注入标题 : ').replace('Payload: ','注入攻击 : ') + '\n')
                if 'back-end DBMS' in dbs:
                    print(dbs.replace('the back-end DBMS is ','数据库类型 : ').replace('web server operating system: ','服务器版本 : ').replace('web application technology: ','服务器语言 : ').replace('back-end DBMS: ','数据库版本 : ') + '\n')
                else:
                    print('\n' + '可能存在注入但被拦截,或者无法识别数据库版本' + '\n')
                print('---------------------------' + '\n')
            except Exception,e:
                print e
        else:
            result_info = re.search('---(.*?)---.*?INFO\] (.*?)\[', result, re.S)
            inj = result_info.group(1)
            print(inj.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace('Title: ','注入标题 : ').replace('Payload: ', '注入攻击 : ') + '\n')
            print('\n' + '可能存在注入但被拦截,或者无法识别数据库版本' + '\n')
            print('---------------------------' + '\n')


result = '''
to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:45:29 /2018-12-05/

[14:45:29] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.0.8) Gecko/20061210 Firefox/1.5.0.8' from file 'C:\Users\Administrator\Desktop\LangZi_SQL_Injection_3.3\lib\sqlmap\txt\user-agents.txt'
[14:45:29] [INFO] testing connection to the target URL
[14:45:30] [INFO] checking if the target is protected by some kind of WAF/IPS
[14:45:30] [INFO] testing if the target URL content is stable
[14:45:31] [INFO] target URL content is stable
[14:45:31] [INFO] testing if GET parameter 'channel' is dynamic
[14:45:31] [INFO] GET parameter 'channel' appears to be dynamic
[14:45:32] [WARNING] heuristic (basic) test shows that GET parameter 'channel' might not be injectable
[14:45:32] [INFO] testing for SQL injection on GET parameter 'channel'
[14:45:32] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[14:45:40] [INFO] GET parameter 'channel' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[14:45:46] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[14:45:46] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[14:45:47] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[14:45:47] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[14:45:48] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[14:45:48] [INFO] testing 'MySQL inline queries'
[14:45:48] [INFO] testing 'PostgreSQL inline queries'
[14:45:49] [INFO] testing 'Microsoft SQL Server/Sybase inline queries'
[14:45:49] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[14:45:49] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[14:45:50] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[14:45:50] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[14:45:51] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[14:45:51] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[14:45:51] [INFO] testing 'Oracle AND time-based blind'
[14:45:52] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[14:45:52] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[14:46:01] [INFO] checking if the injection point on GET parameter 'channel' is a false positive
[14:46:04] [WARNING] parameter length constraining mechanism detected (e.g. Suhosin patch). Potential problems in enumeration phase can be expected
[14:46:05] [WARNING] it appears that the character '>' is filtered by the back-end server. You are strongly advised to rerun with the '--tamper=between'
GET parameter 'channel' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 67 HTTP(s) requests:
---
Parameter: channel (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: channel=S AND 8464=8464-- WzFK&py=F
---
[14:46:05] [INFO] testing MySQL
[14:46:05] [WARNING] the back-end DBMS is not MySQL
[14:46:05] [INFO] testing Oracle
[14:46:07] [WARNING] the back-end DBMS is not Oracle
[14:46:07] [INFO] testing PostgreSQL
[14:46:07] [WARNING] the back-end DBMS is not PostgreSQL
[14:46:07] [INFO] testing Microsoft SQL Server
[14:46:08] [WARNING] the back-end DBMS is not Microsoft SQL Server
[14:46:08] [INFO] testing SQLite
[14:46:08] [WARNING] the back-end DBMS is not SQLite
[14:46:08] [INFO] testing Microsoft Access
[14:46:09] [INFO] confirming Microsoft Access
[14:46:09] [WARNING] the back-end DBMS is not Microsoft Access
[14:46:09] [INFO] testing Firebird
[14:46:10] [WARNING] the back-end DBMS is not Firebird
[14:46:10] [INFO] testing SAP MaxDB
[14:46:10] [WARNING] the back-end DBMS is not SAP MaxDB
[14:46:10] [INFO] testing Sybase
[14:46:11] [WARNING] the back-end DBMS is not Sybase
[14:46:11] [INFO] testing IBM DB2
[14:46:11] [WARNING] the back-end DBMS is not IBM DB2
[14:46:11] [INFO] testing HSQLDB
[14:46:11] [WARNING] the back-end DBMS is not HSQLDB
[14:46:11] [INFO] testing H2
[14:46:12] [WARNING] the back-end DBMS is not H2
[14:46:12] [INFO] testing Informix
[14:46:12] [WARNING] the back-end DBMS is not Informix
[14:46:12] [CRITICAL] sqlmap was not able to fingerprint the back-end database management system

'''
check(result,url,common)