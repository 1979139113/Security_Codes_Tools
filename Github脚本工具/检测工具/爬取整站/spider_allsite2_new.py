# coding:utf8
import requests
from bs4 import BeautifulSoup
import urlparse
import re

'''
python 2.7
1.url管理器 UrlManager
  管理新URL、旧URL (元组)
  添加一个URL到新URL，要求不在新URL和旧URL里
  接收多个URL，调用上一步
  检测是否有新的URL
  获取一个新的URL，从新URL弹出一个到旧URL

2.html下载器 HtmlDownLoader
  requests get方式访问URL，如果状态码不是200就返回HTML内容

3.html解析器 HtmlParser
  urlparse解析出域名
  内部实现一个元组存放解析出来的新URL，从BeautifulSoup对象提取所有a标签里的href地址，判断是否是当前域名下的链接，如果不是就跳过(可以另存起来作为外链)，将上一层URL与提取出来的URL合并，写入内部的新URL，就是当前页面所提取出来的URL
  解析HTML内容调用 parse 函数

4.爬虫主程序 SpiderMain
  初始化一个URL管理器、HTML下载器、HTML解析器
  定义一个爬行函数，接收一个URL作为起始路径

5.main函数
  定义起始URL
  实例化爬虫主程序对象
  将起始URL作为参数传入爬虫对象的爬行函数，开始爬行
'''


class UrlManager:
    def __init__(self):
        self.new_urls = set()  # 存放新的URL，将被访问并解析response里的新链接，递归下去，直到没有新的URL存进来就退出整个程序
        self.old_urls = set()  # 存在已经爬取的，且属于本站的链接

    def add_new_url(self, url):
        if url is None:
            return None
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return None
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        #此处自己添加的
        if len(self.old_urls) > 100: #如果经爬取的链接大于100时，退出主程序
            self.new_urls = set()
            self.old_urls = set()

        return len(self.new_urls) != 0  # 返回新URL元组是否为空，False(不为空)或True(空)，空表示没有新的URL需要爬行了，会退出主程序

    def get_new_url(self):
        new_url = self.new_urls.pop()  # 从新URL元组中取一个URL
        self.old_urls.add(new_url)  # 把它移到旧的URL数组，
        return new_url


class HtmlDownLoader():
    def download(self, url):
        if url is None:
            return None
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.text


class HtmlParser:
    def __init__(self):
        self.foreign_urls = set()

    def _get_root_domain(self, url):
        # 是否应该在这里用正则判断传进来的URL是/开头，如果解析出来netloc是空，那也算是当前域名的链接
        if url is None:
            return None
        try:
            url_info = urlparse.urlparse(url)
            root_domain = url_info.netloc
            return root_domain
        except:
            pass

    def _get_new_urls(self, soup, current_url):
        new_urls = set()
        links = soup.find_all("a")
        for link in links:
            new_url = link.get('href')
            if new_url is not None:
                new_url = new_url.lstrip()

            new_url_root_domain = self._get_root_domain(new_url)
            if new_url_root_domain == '':
                pass
            elif new_url_root_domain is not None:
                if self._get_root_domain(current_url) != self._get_root_domain(new_url):
                    if self._get_root_domain(new_url):
                        self.foreign_urls.add(self._get_root_domain(new_url))
                    continue
            # elif new_url_root_domain is None:
            #     pass

            new_full_url = urlparse.urljoin(current_url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def parse(self, html_content, current_url):
        if html_content is None:
            return
        soup = BeautifulSoup(html_content, "html.parser")
        new_urls = self._get_new_urls(soup, current_url)
        return new_urls

    def get_foreign_urls(self):
        return self.foreign_urls


class SpiderMain:
    def __init__(self, ):
        self.urls = UrlManager()
        self.html_downloader = HtmlDownLoader()
        self.parser = HtmlParser()

    def craw(self, root_url,name):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            try:
                html_content = self.html_downloader.download(new_url)
                new_urls = self.parser.parse(html_content, new_url)
                self.urls.add_new_urls(new_urls)
                with open('%s_data.txt'%(name),'a') as f:
                    f.write(new_url+'\n')
                print "craw %s" % new_url
            except:
                print "错误！！"
        print len(self.urls.old_urls), self.urls.old_urls
        print len(self.parser.foreign_urls), self.parser.foreign_urls


if __name__ == "__main__":
    name = raw_input("name:")
    with open('%s.txt'%(name)) as fp:
        for u in fp:
            root_url = u.strip('\r\n')
            with open('%s_data.txt'%(name),'a') as f:
                pass
            #root_url = u if '://' in u else 'http://' + u
            #root_url = "http://www.zzyidc.com/"
            obj_spider = SpiderMain()
            obj_spider.craw(root_url,name)
