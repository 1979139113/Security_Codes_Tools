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
import pymysql
import random
import socket
import ConfigParser
import hashlib
import urllib2
import codecs
import requests
import re
import datetime
import time
import threading
reload(sys)
sys.setdefaultencoding('utf-8')
timeout = 5
socket.setdefaulttimeout(timeout)
print '''
__    __  _____   _           ___   __   _   _____       ___  
\ \  / / /  _  \ | |         /   | |  \ | | |  _  \     /   | 
 \ \/ /  | | | | | |        / /| | |   \| | | | | |    / /| | 
  \  /   | | | | | |       / / | | | |\   | | | | |   / / | | 
  / /    | |_| | | |___   / /  | | | | \  | | |_| |  / /  | | 
 /_/     \_____/ |_____| /_/   |_| |_|  \_| |_____/ /_/   |_| 

'''
time.sleep(5)
print '''
    Author:Yolanda_Liu
    Debug:Langzi
    Data:2018-3-14
'''
time.sleep(2)
cfg = ConfigParser.ConfigParser()
cfg.read('Config.ini')
user = cfg.get("Server", "username")
passwd = cfg.get("Server", "password")
host = cfg.get("Server", "host")
New_start=cfg.get("Config","new_start")
Rarscan=cfg.get("Config","rarscan")
Sqlscan=cfg.get("Config","sqlscan")
Cmsscan=cfg.get("Config","cmsscan")
Urlcj= cfg.get("Config","urlcaiji")
Dbname = cfg.get("Server","db")
thread_s = cfg.get("Config","thread_s")

list_001 = []
url_gets = int(raw_input(unicode('设置网站爬行次数(10-500):', 'utf-8').encode('gbk')))
if 9<url_gets<501:
    pass
else:
    sys.exit()
backup_name_A = ['.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt']
#要和域名组合在一起拼接的后缀
backup_name_B = list(set([i.replace("\n","") for i in open("rar.txt","r").readlines()]))
#常见的后缀
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


payloads = ("'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C")
sql_errors = {'SQL syntax':'mysql','syntax to use near':'mysql','MySQLSyntaxErrorException':'mysql','valid MySQL result':'mysql',
              'Access Database Engine':'Access','JET Database Engine':'Access','Microsoft Access Driver':'Access',
            'SQLServerException':'mssql','SqlException':'mssql','SQLServer JDBC Driver':'mssql','Incorrect syntax':'mssql',
              'SELECT':'mysql','MySQL Query fail':'mysql'
         }

def scan_backupfile(url):
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
                r_svn_1 = requests.get(url=url_svn, headers=headers, timeout=5)
                # 访问这个链接
                if 'dir' in r_svn_1.content and 'svn' in r_svn_1.content:
                    # 判断关键词 dir 和svn 是不是在这个网页中
                    try:
                        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        coon_svn = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                        cur_svn = coon_svn.cursor()
                        sql_svn = "INSERT INTO url_backup (url,rarsize,datatime) VALUES (%s,%s,%s)"
                        cur_svn.execute(sql_svn, (str(r_svn_1.url), str('svn'), str(timenow)))
                        coon_svn.commit()
                        cur_svn.close()
                        coon_svn.close()
                    except:
                        pass
                else:
                    pass
            except Exception, e:
                # 异常处理机制
                #print e
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
                        coon_git = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                        cur_git = coon_git.cursor()
                        sql_git = "INSERT INTO url_backup (url,rarsize,datatime) VALUES (%s,%s,%s)"
                        cur_git.execute(sql_git, (str(r_git_1.url), str('git'), str(timenow)))
                        coon_git.commit()
                        cur_git.close()
                        coon_git.close()
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
    url_domain = url + '/' + url.split(".", 2)[1]
    # http://www.baidu.com/baidu.
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
                        # 这一行的意思是返回的对象的头部信息中 返回的大小大于2M
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                            cur_bf = coon_bf.cursor()
                            sql_bf = "INSERT INTO url_backup (url,rarsize,datatime) VALUES (%s,%s,%s)"
                            cur_bf.execute(sql_bf, (str(r_domain.url), str(r_domain.headers["Content-Length"]), str(timenow)))
                            coon_bf.commit()
                            cur_bf.close()
                            coon_bf.close()
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
                        try:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            coon_bf1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                            cur_bf1 = coon_bf1.cursor()
                            sql_bf1 = "INSERT INTO url_backup (url,rarsize,datatime) VALUES (%s,%s,%s)"
                            cur_bf1.execute(sql_bf1, (str(r_rar.url), str(r_rar.headers["Content-Length"]), str(timenow)))
                            coon_bf1.commit()
                            cur_bf1.close()
                            coon_bf1.close()
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



def scan_cms(url):
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        req3 = requests.get(url=url, headers=headers, timeout=5)
        #print 'Cheaking>>>' + req3.url + '  ' + str(req3.status_code)
        print str(threading.current_thread().name) + ' ' + str(req3.url).strip('/') + '  ' + str(req3.status_code)
        for key,valu in body.iteritems():
            if key in req3.content:
                try:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    coon_cms_1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                    cur_cms_1 = coon_cms_1.cursor()
                    sql_cms_1 = "INSERT INTO url_cms (url,urlway,cmstype,datatime) VALUES (%s,%s,%s,%s)"
                    cur_cms_1.execute(sql_cms_1, (str(url), str(key),str(valu), str(timenow)))
                    coon_cms_1.commit()
                    cur_cms_1.close()
                    coon_cms_1.close()
                    return ''
                except:
                    pass
            else:
                pass
        ###########################################################
    except Exception,e:
        pass
         #print e

    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        urlx = str(url) + '/robots.txt'
        req2 = requests.get(url=urlx,headers=headers,timeout=3,allow_redirects=False)
        #print 'Cheaking>>>' + req2.url + '  ' + str(req2.status_code)
        print str(threading.current_thread().name) + ' ' + str(req2.url) + '  ' + str(req2.status_code)
        for x_x in robots:
            if x_x in req2.content:
                try:
                    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    coon_cms_2 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname,charset='utf8')
                    cur_cms_2 = coon_cms_2.cursor()
                    sql_cms_2 = "INSERT INTO url_cms (url,urlway,cmstype,datatime) VALUES (%s,%s,%s,%s)"
                    cur_cms_2.execute(sql_cms_2, (str(url), str('robots.txt'),str(x_x), str(timenow)))
                    coon_cms_2.commit()
                    cur_cms_2.close()
                    coon_cms_2.close()
                    return ''
                except:
                    pass
            else:
                pass
        ###########################################################

    except Exception,e:
        pass
         #print e

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
                        sql_cms_3 = "INSERT INTO url_cms (url,urlway,cmstype,datatime) VALUES (%s,%s,%s,%s)"
                        cur_cms_3.execute(sql_cms_3, (str(url), str(urlcms), str(cmsname), str(timenow)))
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

def scan_sql(url):
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r_crawl = requests.get(url=url, headers=headers, timeout=5).content
        try:
            r_sql = re.findall('href="(.*?)"', r_crawl)
            list_none = []
            for sql_sql in r_sql:
                if 'php?' in sql_sql:
                    if not '/' in sql_sql:
                        list_none.append(sql_sql)
            for sql_sql in r_sql:
                if 'asp?' in sql_sql:
                    if not '/' in sql_sql:
                        list_none.append(sql_sql)
            for sql_sql in r_sql:
                if 'jsp?' in sql_sql:
                    if not '/' in sql_sql:
                        list_none.append(sql_sql)
            for sql_sql in r_sql:
                if 'aspx?' in sql_sql:
                    if not '/' in sql_sql:
                        list_none.append(sql_sql)
            sql_address = url + '/' + list_none[1]
            try:
                UA = random.choice(headerss)
                headers = {'User-Agent': UA}
                for inj in payloads:
                    url_inj = sql_address + str(inj)
                    r_inj = requests.get(url=url_inj, headers=headers, timeout=5)
                    print str(threading.current_thread().name) + ' ' + str(r_inj.url) + '  ' + str(r_inj.status_code)
                    for key, vlue in sql_errors.iteritems():
                        if str(key) in r_inj.content:
                            try:
                                timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                coon_sql_2 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                                cur_sql_2 = coon_sql_2.cursor()
                                sql_sql_2 = "INSERT INTO url_sqlinj (url,sqldatabase,datatime) VALUES (%s,%s,%s)"
                                cur_sql_2.execute(sql_sql_2, (str(url_inj), str(vlue), str(timenow)))
                                coon_sql_2.commit()
                                cur_sql_2.close()
                                coon_sql_2.close()
                                return ''
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
    except Exception, e:
        #print e
        pass



#核心扫描功能完成

def first_scan(url):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    try:
        first_r = requests.get(url=url,headers=headers,timeout=timeout)
        for first_url in first_cule:
            patt = re.compile(str('http' +'.*?' + str(first_url)))
            try:
                first_re = re.findall(patt, first_r.content)
                for first_u_url in first_re:
                    first_u_url_1 = first_u_url.replace('%3A%2F%2F', '//').replace('\/\/', '//').replace('">','').replace("/'>", "").replace('/"', '')
                    if ' ' in first_u_url_1:
                        pass
                    if len(first_u_url_1) < 52:
                        list_001.append(first_u_url_1)
            except Exception, e:
                pass
                #print e
    except Exception,e:
        pass
        #print e


if int(New_start) == 1:
    list_001 = []
    first_input = str(raw_input(unicode('输入当前目录下导入原始网址文本名称:', 'utf-8').encode('gbk')))
    first_input = str(first_input + str('.txt'))
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
                    #sql001 = "INSERT INTO url_2 (urllist,cmsscan,rarscan,st2,gettime) VALUES (%s,%s,%s,%s,%s)"
                    sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)"%(str(xx),'0', str(timenow),str(xx))
                    cur.execute(sql)
                    coon.commit()
                    sql001 = "INSERT INTO url_check(url,cmsscan,rarscan,sqlscan,datatime) select '%s','%s','%s','%s','%s' from dual where '%s' not in (select url from url_check)"%((str(xx),0,0,0,str(timenow),str(xx)))
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
                cooncaiji1 = pymysql.connect(user=user, passwd=passwd, host=host, db=Dbname)
                #curcaiji1 = cooncaiji1.cursor(pymysql.cursors.SSCursor)
                curcaiji1 = cooncaiji1.cursor()
                for xx_x0 in list_002_1:
                    xxx = xx_x0.strip('/')
                    try:
                        UA = random.choice(headerss)
                        headers = {'User-Agent': UA}
                        xieru2 = requests.head(url=str(xxx), headers=headers, timeout=5)
                        print str(threading.current_thread().name) + ' ' + str(xieru2.url).strip('/') + '  ' + str(xieru2.status_code)
                        if xieru2.status_code == 200:
                            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            sqlcaiji1 = "INSERT INTO url_check(url,cmsscan,rarscan,sqlscan,datatime) select '%s','%s','%s','%s','%s' from dual where '%s' not in (select url from url_check)" % ((str(xxx), 0, 0, 0, str(timenow), str(xxx)))
                            sqlcaiji1_1 = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)" % (str(xxx), '0', str(timenow), str(xxx))
                            curcaiji1.execute(sqlcaiji1)
                            cooncaiji1.commit()
                            curcaiji1.execute(sqlcaiji1_1)
                            cooncaiji1.commit()
                        else:
                            pass
                    except Exception, e:
                        pass
                        #print e
                curcaiji1.close()
                cooncaiji1.close()
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
        time.sleep(1500)



def rartiqu():
    try:
        time.sleep(random.randint(1, 4))
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
        time.sleep(1500)
        lock.release()

def cmstiqu():
    try:
        time.sleep(random.randint(2, 6))
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
        time.sleep(random.randint(2, 6))
    except Exception,e:
        print e
        time.sleep(1500)
        lock.release()


def sqltiqu():
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
                scan_sql(xxx1sql)
        except Exception,e:
            pass
    except Exception,e:
        print e
        time.sleep(600)
        lock.release()



def xc1():
    for _ in range(url_gets):
        i = 1
        print unicode(str("[+] 第 %d 次爬行网站......"%i),'utf-8')
        time.sleep(random.randint(2,7))
        zairu()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1,3))
        i+=1
def xc2():
    while 1:
        time.sleep(random.randint(2, 6))
        rartiqu()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 4))
def xc3():
    while 1:
        time.sleep(random.randint(2, 6))
        cmstiqu()   #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 3))
def xc4():
    while 1: #
        time.sleep(random.randint(2, 7))
        sqltiqu()  #这里已经从数据库的到了到了10个网址
        time.sleep(random.randint(1, 3))

if int(thread_s) == 1:
    threads=[]
    t1 = threading.Thread(target=xc1)
    t2 = threading.Thread(target=xc2)
    t3 = threading.Thread(target=xc3)
    t4 = threading.Thread(target=xc4)
    if int(Urlcj) == 1:
        print unicode('\n[+] 无限URL采集进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t1)
    if int(Rarscan) == 1:
        print unicode('\n[+] 备份文件扫描进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t2)
    if int(Cmsscan) == 1:
        print unicode('\n[+] CMS扫描认证进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t3)
    if int(Sqlscan) == 1:
        print unicode('\n[+] SQL注入扫描进程加载成功...', 'utf-8')
        time.sleep(1)
        threads.append(t4)
    else:
        print unicode('\n[+]  未加载任何扫描任务 ','utf-8')
        time.sleep(100000)
        pass
    for x in threads:
        x.start()
    x.join()   #线程不堵塞  但是会出现不匀称的表现  并且会修改不同线程中的变量


lock = threading.Lock()
if int(thread_s) > 1:
    if int(Urlcj) == 1:
        print unicode('\n[+] 无限URL采集进程加载成功...', 'utf-8')
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
if int(thread_s) > 2:
    for i in range(int(thread_s)):
        if int(Urlcj) == 1:
            t1 = threading.Thread(target=xc1, args=(), name='URL Scan Thread -' + str(i)).start()
        if int(Rarscan) == 1:
            t2 = threading.Thread(target=xc2, args=(), name='RAR Scan Thread -' + str(i)).start()
        if int(Cmsscan) == 1:
            t3 = threading.Thread(target=xc3, args=(), name='CMS Scan Thread -' + str(i)).start()
        if int(Sqlscan) == 1:
            t4 = threading.Thread(target=xc4, args=(), name='SQL Scan Thread -' + str(i)).start()
