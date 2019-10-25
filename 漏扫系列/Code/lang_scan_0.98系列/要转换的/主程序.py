# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 0025 9:53
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 主程序.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import pymysql
import time
import sys
import ConfigParser
import tqdm
import string
import os
reload(sys)
sys.setdefaultencoding('utf-8')
list_jindu= string.ascii_letters+string.digits+'.'+'_'+' '
jindu ='YolAnda_Scan 0.98 Console Start up...'
jindud = ''
for xx in jindu:
    for x in list_jindu:
        sys.stdout.write(jindud+"\r")
        if xx == x:
            jindud=jindud+x
            sys.stdout.write(jindud+"\r")
            time.sleep(0.03)
            break
        else:
            sys.stdout.write(jindud+x+"\r")
            time.sleep(0.03)
            sys.stdout.flush()
        sys.stdout.write(jindud+"\r")
sys.stdout.write(jindud+'\r')
time.sleep(3)
print '''
__    __  _____   _           ___   __   _   _____       ___  
\ \  / / /  _  \ | |         /   | |  \ | | |  _  \     /   | 
 \ \/ /  | | | | | |        / /| | |   \| | | | | |    / /| | 
  \  /   | | | | | |       / / | | | |\   | | | | |   / / | | 
  / /    | |_| | | |___   / /  | | | | \  | | |_| |  / /  | | 
 /_/     \_____/ |_____| /_/   |_| |_|  \_| |_____/ /_/   |_| 

'''

cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
Dbname = cfg.get("Server","db")
time.sleep(2)
i=0
def start():
    time.sleep(3)
    try:
        os.popen('start L0v1naHOAhz.dll')
        for i in tqdm.tqdm(range(1, 3601)):
            time.sleep(1)
        os.popen('taskkill /f /t /im L0v1naHOAhz.dll')
        time.sleep(5)
        try:
            os.remove('index.html')
            os.remove('information.html')
        except:
            pass
        index = open('index.html', 'a+')
        index.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.99测试版   漏洞详情报导页面</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>
            <span style="color:#FF0000;font-size:18px;font-family:'Microsoft YaHei';">
            <span style="font-size:18px;">
    
            </span><span style="font-size:18px;"><strong>
    
    
            <span style="font-size:12px;style="color:#FF0000;"></span>
            <br />
    
        """)
        infor=open('information.html', 'a+')
        infor.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.99测试版   敏感信息报导页面</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>
            
            <span style="font-size:18px;">
    
            </span><span style="font-size:18px;"><strong>
    
    
            
            <br />
    
        """)
        get(index,infor)
    except:
        print unicode('系统不兼容或动态库文件加载错误','utf-8')
        time.sleep(3)
        sys.exit()
def get(index,infor):
    try:
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        coon = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
        cur = coon.cursor()
        sql1 = "SELECT * FROM url_backup"
        sql2 = "select * from url_cms order by urlway"
        sql3 = "select * from url_editor"
        sql4 = "select * from url_port"
        sql5 = "select * from url_sqlinj"
        sql6 = "select * from url_st2"
        sql7 = "select * from url_unauthorizedscan"
        cur.execute(sql1)
        coon.commit()
        curs=cur.fetchall()
        for id,url,size,title,data in list(curs):
            #print id,url,size,title,data
            index.write('【备份文件以及源码泄漏】')
            index.write('<table border="1">')
            index.write('<tr>')
            index.write('<th>序号</th>')
            index.write('<th>')
            index.write(str(id))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>漏洞网址</th>')
            index.write('<th>')
            index.write(str(url))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>备份文件大小及源码泄露类型</th>')
            index.write('<th>')
            index.write(str(size))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>网址标题</th>')
            index.write('<th>')
            index.write(str(title))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>发现漏洞时间</th>')
            index.write('<th>')
            index.write(str(data))
            index.write('</tr>')
            index.write('</table>')
            index.write('<br>')
            index.write('<br>')
            index.write('<br>')
            index.write('<br>')
            index.write('<HR style="border:1 dashed #987cb9" width="80%" color=#987cb9 SIZE=1>')

        cur.execute(sql3)
        coon.commit()
        curs=cur.fetchall()
        for id,url,title,data in list(curs):
            #print id,url,title,data
            index.write('【编辑器漏洞】')
            index.write('<table border="1">')
            index.write('<tr>')
            index.write('<th>序号</th>')
            index.write('<th>')
            index.write(str(id))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>漏洞网址</th>')
            index.write('<th>')
            index.write(str(url))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>网址标题</th>')
            index.write('<th>')
            index.write(str(title))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>发现漏洞时间</th>')
            index.write('<th>')
            index.write(str(data))
            index.write('</tr>')
            index.write('</table>')
            index.write('<br>')
            index.write('<br>')
            index.write('<br>')
            index.write('<HR style="border:1 dashed #987cb9" width="80%" color=#987cb9 SIZE=1>')
        cur.execute(sql5)
        coon.commit()
        curs = cur.fetchall()
        for id, url, urltitle,sqldatabase, data in list(curs):
            #print id, url, urltitle,sqldatabase, data
            index.write('【Sql注入漏洞】')
            index.write('<table border="1">')
            index.write('<tr>')
            index.write('<th>序号</th>')
            index.write('<th>')
            index.write(str(id))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>漏洞网址</th>')
            index.write('<th>')
            index.write(str(url))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>网址标题</th>')
            index.write('<th>')
            index.write(str(urltitle))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>数据库类型</th>')
            index.write('<th>')
            index.write(str(sqldatabase))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>发现漏洞时间</th>')
            index.write('<th>')
            index.write(str(data))
            index.write('</tr>')
            index.write('</table>')
            index.write('<br>')
            index.write('<br>')
            index.write('<br>')
            index.write('<HR style="border:1 dashed #987cb9" width="80%" color=#987cb9 SIZE=1>')

        cur.execute(sql7)
        coon.commit()
        curs = cur.fetchall()
        for id, url, ip,uath, urltitle,data in list(curs):
            #print id, url, ip,uath, urltitle,data
            index.write('【未授权访问漏洞】')
            index.write('<table border="1">')
            index.write('<tr>')
            index.write('<th>序号</th>')
            index.write('<th>')
            index.write(str(id))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>漏洞网址</th>')
            index.write('<th>')
            index.write(str(url))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>网址所在IP</th>')
            index.write('<th>')
            index.write(str(ip))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>漏洞类型</th>')
            index.write('<th>')
            index.write(str(uath))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>网站标题</th>')
            index.write('<th>')
            index.write(str(urltitle))
            index.write('</tr>')

            index.write('<tr>')
            index.write('<th>发现漏洞时间</th>')
            index.write('<th>')
            index.write(str(data))
            index.write('</tr>')
            index.write('</table>')
            index.write('<br>')
            index.write('<br>')
            index.write('<br>')
            index.write('<HR style="border:1 dashed #987cb9" width="80%" color=#987cb9 SIZE=1>')

        cur.execute(sql4)
        coon.commit()
        curs = cur.fetchall()
        infor.write('【网站IP端口扫描】')
        infor.write('<br>')
        for id, url, ip,uath, urltitle,data in list(curs):
            #print id, url, ip,uath, urltitle,data
            infor.write(str(id)+'  :  ')
            infor.write(str(url)+'  :  ')
            infor.write(str(ip)+'  :  ')
            infor.write(str(uath)+'  :  ')
            infor.write(str(urltitle))
            infor.write('<br>')
        cur.execute(sql2)
        coon.commit()
        curs = cur.fetchall()
        infor.write('<br>')
        infor.write('<br>')
        infor.write('<br>')
        infor.write('【CMS类型识别，如需要批量刷dedecms的exp请在数据库中select url from url_cms where cmstype=\'dedecms\'】')
        infor.write('<br>')
        for id, url, ip, uath, urltitle, data in list(curs):
            infor.write(str(id)+'  :  ')
            infor.write(str(url)+'  :  ')
            infor.write(str(uath)+'  :  ')
            infor.write(str(urltitle))
            infor.write('<br>')
        cur.execute(sql6)
        coon.commit()
        curs = cur.fetchall()
        infor.write('<br>')
        infor.write('<br>')
        infor.write('<br>')
        infor.write('【使用St2框架的网址,如果出现了新的ST2漏洞，在数据库直接导出url_st2这张表的网址，然后批量刷】')
        infor.write('<br>')
        for id, url, title, data in list(curs):
            infor.write(str(id)+'  :  ')
            infor.write(str(url)+'  :  ')
            infor.write(str(title))
            infor.write('<br>')
        cur.close()
        coon.close()

    except Exception,e:
        print e
        print unicode('无法连接数据库','utf-8')
    finally:
        index.close()
        infor.close()

while 1:
    i+=1
    print unicode(str('[*]YolAnda_Scan: 第 '+str(i)+' 次扫描....'),'utf-8')
    start()

