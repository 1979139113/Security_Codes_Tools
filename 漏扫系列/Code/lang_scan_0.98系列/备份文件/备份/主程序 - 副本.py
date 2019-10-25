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
import os
reload(sys)
sys.setdefaultencoding('utf-8')
print '''
__    __  _____   _           ___   __   _   _____       ___  
\ \  / / /  _  \ | |         /   | |  \ | | |  _  \     /   | 
 \ \/ /  | | | | | |        / /| | |   \| | | | | |    / /| | 
  \  /   | | | | | |       / / | | | |\   | | | | |   / / | | 
  / /    | |_| | | |___   / /  | | | | \  | | |_| |  / /  | | 
 /_/     \_____/ |_____| /_/   |_| |_|  \_| |_____/ /_/   |_| 
                                                0.98纪念版本
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
        for _ in tqdm.tqdm(range(1, 3601)):
            time.sleep(1)
        os.popen('taskkill /f /t /im L0v1naHOAhz.dll')
        time.sleep(5)
        try:
            os.remove(unicode('./result/备份源码文件信息报告.html','utf-8'))
            os.remove(unicode('./result/SQL注入漏洞信息报告.html', 'utf-8'))
            os.remove(unicode('./result/未授权访问漏洞信息报告.html', 'utf-8'))
            os.remove(unicode('./result/网站编辑器漏洞信息报告.html', 'utf-8'))
            os.remove(unicode('./result/网站危险端口开放信息报告.html', 'utf-8'))
            os.remove(unicode('./result/STRUTS2框架网站信息报告.html', 'utf-8'))
            os.remove(unicode('./result/CMS类型信息报告.html', 'utf-8'))
        except:
            pass
        index = open(unicode('./result/备份源码文件信息报告.html','utf-8'), 'a+')
        index2 = open(unicode('./result/SQL注入漏洞信息报告.html', 'utf-8'), 'a+')
        index3 = open(unicode('./result/未授权访问漏洞信息报告.html', 'utf-8'), 'a+')
        index4 = open(unicode('./result/网站编辑器漏洞信息报告.html', 'utf-8'), 'a+')
        index5 = open(unicode('./result/网站危险端口开放信息报告.html', 'utf-8'), 'a+')
        index6 = open(unicode('./result/STRUTS2框架网站信息报告.html', 'utf-8'), 'a+')
        index7 = open(unicode('./result/CMS类型信息报告.html', 'utf-8'), 'a+')

        index.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.98纪念版   备份源码文件信息报告</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>
            <span style="color:#FF0000;font-size:18px;font-family:'Microsoft YaHei';">
            <span style="font-size:18px;">
    
            </span><span style="font-size:18px;"><strong>
    
    
            <span style="font-size:12px;style="color:#FF0000;"></span>
            <br />
    
        """)
        index2.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.98纪念版   SQL注入漏洞信息报告</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>
            <span style="color:#FF0000;font-size:18px;font-family:'Microsoft YaHei';">
            <span style="font-size:18px;">

            </span><span style="font-size:18px;"><strong>


            <span style="font-size:12px;style="color:#FF0000;"></span>
            <br />

        """)
        index3.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.98纪念版    未授权访问漏洞信息报告</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>
            <span style="color:#FF0000;font-size:18px;font-family:'Microsoft YaHei';">
            <span style="font-size:18px;">

            </span><span style="font-size:18px;"><strong>


            <span style="font-size:12px;style="color:#FF0000;"></span>
            <br />

        """)
        index4.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.98纪念版    网站编辑器漏洞信息报告</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>
            <span style="color:#FF0000;font-size:18px;font-family:'Microsoft YaHei';">
            <span style="font-size:18px;">

            </span><span style="font-size:18px;"><strong>


            <span style="font-size:12px;style="color:#FF0000;"></span>
            <br />

        """)

        index5.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.98纪念版    网站危险端口开放信息报告</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>
            
            <span style="font-size:18px;">
    
            </span><span style="font-size:18px;"><strong>
    
    
            
            <br />
    
        """)
        index6.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.98纪念版    STRUTS2框架网站信息报告</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>

            <span style="font-size:18px;">

            </span><span style="font-size:18px;"><strong>



            <br />

        """)
        index7.write("""
        <title>Report Yolanda_Scan</title>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h1 align="center">Yolanda0.98纪念版    CMS类型信息报告</h1>
        <HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>
        <h2 align="center">Blog:www.langzi.fun</h2>

            <span style="font-size:18px;">

            </span><span style="font-size:18px;"><strong>



            <br />

        """)
        get(index,index2,index3,index4,index5,index6,index7)
    except:
        print unicode('系统不兼容或动态库文件加载错误','utf-8')
        time.sleep(3)
        sys.exit()
def get(index,index2,index3,index4,index5,index6,index7):
    try:
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
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        index.write('<h3 align="center">自动生成报告时间:'+timenow+'</h3>')
        index.write('<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>')
        for id,url,size,title,data in list(curs):
            #print id,url,size,title,data
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
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        index4.write('<h3 align="center">自动生成报告时间:'+timenow+'</h3>')
        index4.write('<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>')
        for id,url,title,data in list(curs):
            #print id,url,title,data
            index4.write('<table border="1">')
            index4.write('<tr>')
            index4.write('<th>序号</th>')
            index4.write('<th>')
            index4.write(str(id))
            index4.write('</tr>')

            index4.write('<tr>')
            index4.write('<th>漏洞网址</th>')
            index4.write('<th>')
            index4.write(str(url))
            index4.write('</tr>')

            index4.write('<tr>')
            index4.write('<th>网址标题</th>')
            index4.write('<th>')
            index4.write(str(title))
            index4.write('</tr>')

            index4.write('<tr>')
            index4.write('<th>发现漏洞时间</th>')
            index4.write('<th>')
            index4.write(str(data))
            index4.write('</tr>')
            index4.write('</table>')
            index4.write('<br>')
            index4.write('<br>')
            index4.write('<br>')
            index4.write('<HR style="border:1 dashed #987cb9" width="80%" color=#987cb9 SIZE=1>')
        cur.execute(sql5)
        coon.commit()
        curs = cur.fetchall()
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        index2.write('<h3 align="center">自动生成报告时间:'+timenow+'</h3>')
        index2.write('<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>')
        for id, url, urltitle,sqldatabase, data in list(curs):
            #print id, url, urltitle,sqldatabase, data
            index2.write('<table border="1">')
            index2.write('<tr>')
            index2.write('<th>序号</th>')
            index2.write('<th>')
            index2.write(str(id))
            index2.write('</tr>')

            index2.write('<tr>')
            index2.write('<th>漏洞网址</th>')
            index2.write('<th>')
            index2.write(str(url))
            index2.write('</tr>')

            index2.write('<tr>')
            index2.write('<th>网址标题</th>')
            index2.write('<th>')
            index2.write(str(urltitle))
            index2.write('</tr>')

            index2.write('<tr>')
            index2.write('<th>数据库类型</th>')
            index2.write('<th>')
            index2.write(str(sqldatabase))
            index2.write('</tr>')

            index2.write('<tr>')
            index2.write('<th>发现漏洞时间</th>')
            index2.write('<th>')
            index2.write(str(data))
            index2.write('</tr>')
            index2.write('</table>')
            index2.write('<br>')
            index2.write('<br>')
            index2.write('<br>')
            index2.write('<HR style="border:1 dashed #987cb9" width="80%" color=#987cb9 SIZE=1>')

        cur.execute(sql7)
        coon.commit()
        curs = cur.fetchall()
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        index3.write('<h3 align="center">自动生成报告时间:'+timenow+'</h3>')
        index3.write('<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>')
        for id, url, ip,uath, urltitle,data in list(curs):
            index3.write('<table border="1">')
            index3.write('<tr>')
            index3.write('<th>序号</th>')
            index3.write('<th>')
            index3.write(str(id))
            index3.write('</tr>')

            index3.write('<tr>')
            index3.write('<th>漏洞网址</th>')
            index3.write('<th>')
            index3.write(str(url))
            index3.write('</tr>')

            index3.write('<tr>')
            index3.write('<th>网址所在IP</th>')
            index3.write('<th>')
            index3.write(str(ip))
            index3.write('</tr>')

            index3.write('<tr>')
            index3.write('<th>漏洞类型</th>')
            index3.write('<th>')
            index3.write(str(uath))
            index3.write('</tr>')

            index3.write('<tr>')
            index3.write('<th>网站标题</th>')
            index3.write('<th>')
            index3.write(str(urltitle))
            index3.write('</tr>')

            index3.write('<tr>')
            index3.write('<th>发现漏洞时间</th>')
            index3.write('<th>')
            index3.write(str(data))
            index3.write('</tr>')
            index3.write('</table>')
            index3.write('<br>')
            index3.write('<br>')
            index3.write('<br>')
            index3.write('<HR style="border:1 dashed #987cb9" width="80%" color=#987cb9 SIZE=1>')

        cur.execute(sql4)
        coon.commit()
        curs = cur.fetchall()
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        index5.write('<h3 align="center">自动生成报告时间:'+timenow+'</h3>')
        index5.write('<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>')
        index5.write('<br>')
        for id, url, ip,uath, urltitle,data in list(curs):
            #print id, url, ip,uath, urltitle,data
            index5.write(str(id)+'  :  ')
            index5.write(str(url)+'  :  ')
            index5.write(str(ip)+'  :  ')
            index5.write(str(uath)+'  :  ')
            index5.write(str(urltitle))
            index5.write('<br>')
        cur.execute(sql2)
        coon.commit()
        curs = cur.fetchall()
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        index7.write('<h3 align="center">自动生成报告时间:'+timenow+'</h3>')
        index7.write('<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>')
        index7.write('<br>')
        for id, url, ip, uath, urltitle, data in list(curs):
            index7.write(str(id)+'  :  ')
            index7.write(str(url)+'  :  ')
            index7.write(str(uath)+'  :  ')
            index7.write(str(urltitle))
            index7.write('<br>')
        cur.execute(sql6)
        coon.commit()
        curs = cur.fetchall()
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        index6.write('<h3 align="center">自动生成报告时间:'+timenow+'</h3>')
        index6.write('<HR style="FILTER: alpha(opacity=100,finishopacity=0,style=3)" width="80%" color=#987cb9 SIZE=3>')
        index6.write('<br>')
        for id, url, title, data in list(curs):
            index6.write(str(id)+'  :  ')
            index6.write(str(url)+'  :  ')
            index6.write(str(title))
            index6.write('<br>')
        cur.close()
        coon.close()

    except Exception,e:
        print e
        print unicode('无法连接数据库','utf-8')
    finally:
        index.close()
        index2.close()
        index3.close()
        index4.close()
        index5.close()
        index6.close()
        index7.close()

while 1:
    i+=1
    print unicode(str('[*]YolAnda_Scan: 第 '+str(i)+' 次扫描....'),'utf-8')
    start()

