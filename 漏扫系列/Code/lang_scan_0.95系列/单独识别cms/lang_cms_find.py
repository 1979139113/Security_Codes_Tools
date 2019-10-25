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
import requests
import re
import time
from multiprocessing.dummy import Pool as threadpool
import random
import hashlib
import codecs
import os
reload(sys)
sys.setdefaultencoding('utf-8')
print '''

        |    __   __   __  
        |_, (__( |  ) (__| 
                       __/  0.92

'''
time.sleep(5)
os.system('color a')
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
        '_ZCMS_ShowNewMessage':'ZCMS','zcms_skin':'ZCMS','ZCMS泽元内容管理':'ZCMS',
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
def start(url):
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        req3 = requests.get(url=url, headers=headers, timeout=5)
        print 'Cheaking>>>' + req3.url + '  ' + str(req3.status_code)
        for key,valu in body.iteritems():
            if key in req3.content:
                file_name = str(valu)
                with open(str(file_name + str('.txt')),'a+') as aa:
                    aa.write(url + '\n')
                    return ''
            else:
                pass
        ###########################################################
    except Exception,e:
         print e
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        urlx = str(url) + '/robots.txt'
        req2 = requests.get(url=urlx,headers=headers,timeout=3,allow_redirects=False)
        print 'Cheaking>>>' + req2.url + '  ' + str(req2.status_code)
        for x_x in robots:
            if x_x in req2.content:
                filename = str(x_x)
                with open(str(filename + str('.txt')),'a+') as aaa:
                    aaa.write(url + '\n')
                    return ''
            else:
                pass
        ###########################################################

    except Exception,e:
         print e

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
            print 'Cheaking>>>' + req1.url + '  ' + str(req1.status_code)
            if req1.status_code == 200:
                req2 = requests.get(url=urlcms,headers=headers,timeout=5,allow_redirects=False)
                md5 = hashlib.md5()
                md5.update(req2.content)
                rmd5 = md5.hexdigest()
                if rmd5 == cmsmd5:
                    fn = str(cmsname)
                    with open(str(fn + str('.txt')), 'a+') as aa1:
                        aa1.write(url + '\n')
                        return ''
            else:
                pass
        except Exception,e:
            print e
smxc = int(input(unicode('设置扫描线程数(10-500):','utf-8').encode('gbk')))
url_list=list(set([i.replace("\n","") for i in open("url.txt","r").readlines()]))
pool = threadpool(processes=smxc)  #线程数量
result = pool.map(start, url_list)
pool.close()
pool.join()