
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

reload(sys)
sys.setdefaultencoding('utf-8')
import pymssql

common_weak_password = ('', '123456', 'test', 'root', 'admin', 'user')  # 密码字典
mssql_username = ('sa', 'test', 'admin', 'mssql')  # 账号字典

success = False
host = "127.0.0.1"  # 数据库IP地址
port = 1443
for username in mssql_username:
    for password in common_weak_password:
        print 'ip:' + host + 'Username:' + username
        try:
            db = pymssql.connect(server=host, port=port, user=username, password=password)
            success = True
            if success:
                print username, password
        except Exception, e:
            pass
