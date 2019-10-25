# coding:utf-8

import requests

robots = ['EmpireCMS', 'PHPCMS v9', 'Discuz', 'joomla', 'siteserver', 'dedecms', 'php168', 'phpcms', 'emlog',
          '新为软件E-learning管理系统', '贷齐乐系统', '中企动力CMS', '全国烟草系统', 'Glassfish', 'phpvod', 'jieqi', '老Y文章管理系统', 'DedeCMS',
          '地平线CMS', 'qibosoft v7', 'oroCRM', 'Live800', '尘缘雅境图文系统', '方维团购', '科信邮件系统', 'jumbotcms', 'webEdition',
          'phpcmsv9', 'TRS身份认证系统', 'zoomla', 'iwebshop', 'ShopNum', 'SAPNetWeaver', '易点CMS', 'O2OCMS', '万众电子期刊CMS',
          'mymps', 'ASPCMS', 'AppCms', 'skypost', 'PHP168', 'Winmail Server', '万户网络', 'cutecms', '泛微E-office',
          'DotNetNuke', 'EmpireCMS', 'Destoon', '汇成企业建站CMS', 'CMSTop', '天柏在线考试系统', 'Emlog', 'BoyowCMS', '小蚂蚁',
          'diguoCMS帝国', 'XYCMS', 'Zoomla', 'ThinkSAAS', '青峰网络智能网站管理系统', '1039家校通', 'yidacms', 'XpShop', '北京清科锐华CEMIS',
          'ILoanP2P借贷系统', 'finecms', 'V2视频会议系统', 'MaticsoftSNS', 'phpmaps', '苹果CMS', 'qzdatasoft强智教务管理系统', 'Diferior',
          'plone', 'sdcms', 'tutucms', 'mlecms', 'IdeaCMS', '程氏舞曲CMS', 'PowerCreator在线教学系统', 'maccms', 'WebMail',
          '时代企业邮', 'Typecho', 'kuwebs', '悟空CRM系统', 'RCMS', '3gmeeting视讯系统', 'eShangBao易商宝', 'baocms', 'Shop7z',
          '北京阳光环球建站系统', 'TrsIDS', 'WebLogic', '金色校园', 'Wangzt', 'T-Site建站系统', '用友U8', 'abcms', 'ShopNc商城系统', 'beeCMS',
          'Chinacreator', '微门户', 'HJCMS企业网站管理系统', 'FoxPHP', 'webplus', 'emlog', '科迈RAS', 'CxCms', 'Dvbbs', '51Fax传真系统',
          '省级农机构置补贴信息管理系统', '创捷驾校系统', 'Gever', 'TCCMS', 'WordPress', '全程oa', '方维团购购物分享系统', '大米CMS', 'PageAdmin',
          'JTBC(CMS)', 'concrete5', '商家信息管理系统', 'VENSHOP2010凡人网络购物系统', 'qianbocms', 'yunyin', '汇文图书馆书目检索系统', '擎天政务系统',
          'Joomla', 'e创站', 'MallBuilder', 'PhpMyAdmin', '86cms', '味多美导航', 'WebOffice', '6KBBS', '网趣商城', 'WCM系统V6',
          '易创思ecs', 'fcms梦想建站', '微普外卖点餐系统', 'gxcms', '08cms', 'kesioncms', 'Epaper报刊系统', '1024 CMS', 'XPlus报社系统',
          'MediaWiki', 'HiMail', '智睿网站系统', 'southidc', 'nitc', 'PhpCMS', 'phpwind', '绿麻雀借贷系统', 'ASP168 欧虎', '金钱柜P2P',
          'drupal', 'hishop', '蓝凌EIS智慧协同平台', 'TWCMS', '菲斯特诺期刊系统', '捷点 JCMS', '用友FE管理系统', 'Live800插件', '金蝶OA',
          'IMO云办公室系统', '云因网上书店', 'Southidc', 'MetInfo', 'Insightsoft', '易创思教育建站系统', '北创图书检索系统', '方维众筹', '南方数据',
          'OpenSNS', 'fengcms', 'SiteServer', '浪潮CMS', 'Telerik Sitefinity', '青果学生综合系统', 'JEECMS', 'Tomcat',
          'pageadmin', '天融信Panabit', 'WS2004校园管理系统', 'Discuz!', 'E-Tiller', 'eadmin', 'PigCms', 'WilmarOA系统', '爱装网',
          '用友TurBCRM系统', 'DIYWAP', 'kingcms', 'WizBank', 'bluecms', '未知OEM安防监控系统', 'zcncms', 'qibosoft', 'IwmsCms',
          'nbcms', 'jishigou', 'KesionCMS', 'BeesCms', '25yi', 'Jspxcms', 'PHPMyWind', 'PIW内容管理系统', 'IMGCms',
          'Easysite', '科蚁CMS', '2z project', 'Discuz7.2', 'actcms', 'VOS3000', 'H5酒店管理系统', '宁志学校网站系统', 'Ecshop',
          '分类信息网bank.asp后门', '南方良精', 'DOYO通用建站系统', '青果软件教务系统', 'shopex', '三才期刊系统', 'phpCMS', 'JeeCMS', 'powereasy动易',
          'otcms', 'cmstop', '自动发卡平台', 'KingCms', 'Bit', 'unknown cms rcms', 'DayuCms', '记事狗', 'Kangle虚拟主机', 'Jboos',
          '商奇CMS', 'Yongyou', 'We7', 'gocdkey', 'dswjcms', '中国期刊先知网', '新秀', 'SEMcms', 'weiphp', '露珠文章管理系统', '乐彼多网店',
          'EspCMS', 'CactiEZ插件', 'wuzhicms', 'Yxcms', '用友FE协作办公平台', '众拓', '用友', '爱淘客', 'anmai安脉教务管理系统', 'Jingyi',
          'iDVR', 'dayrui系列CMS', 'phpshop', 'MvMmall', '易想CMS', '万欣高校管理系统', 'ESPCMS', 'Dolibarr', '万博网站管理系统2006',
          'FoosunCMS', 'metinfo', 'THEOL网络教学综合平台', '74cms', 'ideacms', '最土团购系统', 'expocms', 'VeryIde', 'KingCMS',
          'iPowerCMS', 'FoosunCms', 'dvbbs', '口福科技', '良精南方', 'Wordpress', '5UCMS', 'xycms', 'DswjCms', 'shopxp',
          'HDwiki', 'dtcms', 'AfterLogicWebMail系统', 'phpb2b', '八哥CMS', 'easy7视频监控平台', 'EasySite内容管理', 'luzhucms',
          'Phpwind网站程序', 'weebly', '易创思(ECS)教学系统', 'cmseasy', 'HiShop商城系统', '桃源相册管理系统', 'LeBiShop网上商城', 'LjCMS',
          'espcms', 'ayacms', 'Digital Campus2.0', '360webfacil 360WebManager', 'ADXStudio', '海洋CMS', '金蝶协作办公系统',
          'Discuz', '华夏创新AppEx系统', 'Webnet CMS', 'infoglue', '国家数字化学习资源中心系统', '易普拉格科研管理系统', 'SupeSite', '尘月企业网站管理系统',
          'phpcms', 'N点虚拟主机', 'Yidacms', 'TipAsk问答系统', 'shlcms', '讯时网站管理系统cms', 'beidou', '通达OA系统', 'phpmps', '集时通讯程序',
          'AspCMS', '速贝CMS', 'siteengine', 'phpMyAdmin', 'Mymps蚂蚁分类信息', '泛微OA', '凡诺企业网站管理系统', '网钛文章管理系统', 'DuomiCMS',
          'Z-Blog', 'chanzhi', 'qiboSoft', 'AdaptCMS', '悟空CRM', 'niucms', '万博网站管理系统', 'BookingeCMS酒店系统', 'siteserver',
          'qibocms', 'Drupal', 'TRS WCM', 'eims', '建站之星', '未知政府采购系统', 'zhuangxiu', 'DouPHP', 'TurboCMS', '大汉系统（Hanweb）',
          '汉码高校毕业生就业信息系统', 'ZCMS', 'netgather', 'liangjing', 'KessionCms', 'DK动科cms', '皓翰通用数字化校园平台', 'ecshop',
          'EC_word企业管理系统', 'CmsEasy', 'MoMoCMS', 'ILAS图书系统', '小计天空进销存管理系统', '安乐业房产系统', 'aspcms', 'maxcms', '杰奇小说连载系统',
          'foosun文章系统', 'JBOOS', 'MajExpress', 'YiDacms', 'akcms', 'Epoint', 'TurboMail邮箱系统', 'HdWiki', 'NITC',
          'joomla', 'joomle', 'appcms', 'anleye', 'ourphp', '非凡建站', 'PHPWind', '青云客CMS', 'phpok', '牛逼cms', 'EduSoho',
          'V5Shop', '171cms', 'dedecms', 'wordpress', '大汉JCMS', '贷齐乐p2p', '明腾CMS', 'Mailgard', 'myweb', 'PowerEasy',
          'Dolphin', '薄冰时期网站管理系统', 'FineCMS', '四通政府网站管理系统', '逐浪zoomla', '蓝科CMS', 'MinyooCMS', 'OurPhp', '宁志学校网站',
          'PHPWEB', '凡科建站', '微擎科技', '某通用型政府cms', '联众Mediinfo医院综合管理平台', 'DzzOffice', 'Tipask', '万户OA', 'Phpwind',
          'Soullon', 'Osclass', '未知查询系统', 'B2Bbuilder', 'HituxCMS', 'HIMS 酒店云计算服务', 'zmcms建站', 'Zabbix', '亿邮Email',
          'Foosun', 'Trunkey', 'phpweb', 'FengCms', 'phpshe', '企智通系列上网行为管理系统']

for x in robots:
    print "'" + x + "'" + ':' + "'" + x + "',"

# def scan(url):
#     for cmsxx in cms_rule:
#         cmshouzhui = cmsxx.split('|', 3)[0]
#         cmsmd5 = cmsxx.split('|', 3)[2]
#         cmsname = cmsxx.split('|', 3)[1]
#         urlcms = url + str(cmshouzhui)
#         try:
#             req1 = requests.head(url=urlcms, timeout=3, allow_redirects=False)
#             print unicode('    CMS类型识别:    ',
#                                                                   'utf-8') + '  ' + req1.url + '    ' + str(
#                 req1.status_code)
#             if req1.status_code == 200:
#                 req1_2 = requests.get(url=urlcms,  timeout=3, allow_redirects=False)
#                 md5 = hashlib.md5()
#                 md5.update(req1_2.content)
#                 rmd5 = md5.hexdigest()
#                 print rmd5 + ':::::::::::' + cmsmd5
#                 if rmd5 == cmsmd5:
#                     print '*********CMS IS :' + str(cmsname) + '*************'
#         except Exception,e:
#             print e
# scan('http://www.do1.com.cn')