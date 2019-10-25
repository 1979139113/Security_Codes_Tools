# coding:utf-8
# code by Loid
from urlparse import urlparse, parse_qs, parse_qsl
from lxml import etree
import re

class URL(object):

    def __init__(self, full_url_string=""):
        f = full_url_string
        self.full_url_string = full_url_string if self.isHttp(f) else self.addHttp(f)
        self.path = self.get_path()
        self.query = self.get_query()
        self.domain = self.get_domain()
        self.ext = self.get_ext()
        self.queryDict = self.queryStringToDict()

    # 判断是否为http头的url
    def isHttp(self, host):
        return True if urlparse(host).scheme in ['http', 'https'] else False

    # 添加http头
    def addHttp(self, host):
        return "http://" + host

    # 不带路径和参数的url
    def url_load_scan(self):
        return "{}://{}/".format(self.get_scheme(), self.get_domain())

    # 移除 http
    @staticmethod
    def removeHttp(host):
        return host.split("://")[1]

    def get_url_string(self):
        return self.full_url_string

    def get_path(self):
        return urlparse(self.full_url_string).path

    def get_query(self):
        return urlparse(self.full_url_string).query

    def get_domain(self):
        return urlparse(self.full_url_string).netloc

    def get_ext(self):
        ext = self.path.split(".")
        return ext[-1] if len(ext) > 1 else None

    def get_scheme(self):
        return urlparse(self.full_url_string).scheme

    # 参数转dict
    def queryStringToDict(self):
        return {self.path: parse_qs(self.query)} if self.query != '' else None

    # 参数dict转字符串, 并且可以自己定义某个参数后面加入其他字符  扩展 xss sql等攻击
    def queryDictToStringWithParams(self, action="add", **kwargs):
        '''
        :param kwargs: 改变的参数值, eg: 传入 id=Fuzz
        :return: eg: id=11Fuzz&action=news
        '''
        stringList = []
        for path, querys in self.queryDict.items():
            for key, value in querys.items():
                if action.lower() == "add": q = "{}={}".format(key, value[0])
                else: q = "{}={}".format(key, "11")
                if key in kwargs:
                    q += kwargs[key]
                stringList.append(q)
        return "&".join(stringList)

    # 通过urllist 将参数去重, 并返回dict
    @staticmethod
    def urls_reset(urlList):
        urlDict = {}
        for url in urlList:
            u = URL(url)
            path, query = u.get_path(), u.get_query()
            # 1.php  id=1&filename=aa
            if path:
                if path not in urlDict:
                    urlDict[path] = {}
                # id:1   filename:aa
                for key, value in parse_qs(query).items():
                    urlDict[path][key] = value[0]
        return urlDict

    # 通过dict转字符串并拼接成完整url.
    @staticmethod
    def urls_reset_load_String(urlDict, root=""):
        querys = []
        for path, query in urlDict.items():
            path = path.replace("//", "/")
            stringList = []
            for key, value in query.items():
                stringList.append("{}={}".format(key, value))

            link = "{}{}?{}".format(root, path, "&".join(stringList)) if query != {} else root+path
            link = re.sub(r'//', "/", link, 0)
            link = re.sub(r':/', '://', link, 0)
            querys.append(link)
        return querys


# u = URL("aa")
# print u.urls_reset_load_String({'/news_view.php': {'id': '92'}, '/service.php': {}}, root="http://aaa.com")


# url = "http://www.pna.com.cn/index.asp?id=11&action=news"
# u = URL(url)
# print u.queryDictToStringWithParams(id="11", action="aaa")

class HTML(object):

    rules = [{"a": "href"}, {"form": "action"}]
    not_allow_exts = ['ico', 'jpg', 'png', 'css', 'pdf', 'gif', 'bmp', 'js', 'zip', 'flv', 'docx', '/', 'rar']

    def __init__(self, html, url=None):
        self._html = html
        self._retList = []
        url = url.replace("///", "/")
        u = URL(url)
        self._url = u.get_domain() if u.isHttp(url) else urlparse(url).path
        self._path = "/".join(u.get_path().split("/")[:-1]) if u.isHttp(url) and u.get_ext() else "/"
        self._schema = u.get_scheme()

    def findLink(self):
        try:
            html = etree.HTML(self._html)
        except etree.XMLSyntaxError as e:
            return []

        # 通过遍历定义的规则来取
        for rule in self.rules:
            for tag, attr in rule.items():
                xpathRule = "//{}[@{}]".format(tag, attr)
                ret = html.xpath(xpathRule)

                for r in ret:
                    if self.filterLink(r.get(attr)):
                        # print("filter before: {}".format(r))
                        # print("filter: {}".format(self.filterLink(r.get(attr))))
                        link = self.filterLink(r.get(attr))
                        # 拼接
                        if link.startswith("/"):
                            link = link
                        else:
                            link = self._path + link if self._path.endswith("/") else self._path + "/" + link

                        self._retList.append(link)
        return self._retList

    # 过滤
    def filterLink(self, link):
        try:
            # 这里懒得去判断编码了，报错就跳过
            full_link = "{}://{}{}{}".format(self._schema, self._url, self._path, link)
        except UnicodeEncodeError as e:
            return False
        if URL(full_link).get_ext() in self.not_allow_exts:
            return False
        elif URL(link).isHttp(link) and self._url in link:
            path, query = urlparse(link).path, urlparse(link).query
            return u"{}?{}".format(path, query) if query != "" else path
        elif "javascript:" in link:
            return False
        elif "mailto" in link:
            return False
        elif link == "":
            return False
        elif not URL(link).isHttp(link):
            return link
        else:
            return False

    def get_result(self):
        return self._retList


# print HTML("http://aa.com/aa", "http://aa.com/").filterLink("/upload/image/2016-12/20161230165459-0928-18885.jpg")
