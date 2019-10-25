# coding:utf-8
# code by Loid
from Request import Request
from Response import Response
from parse import URL, HTML

class Crawler(object):

    def __init__(self, depth_limit=2, **kwargs):

        self._already_spider_url = set()            # 已经爬行过的url
        self._already_seen_url = set()              #
        self._would_scan_urlList = set()            # 等待扫描的url

        self.depth_limit = depth_limit
        self.spider_num = 1
        self.kw = kwargs


    def crawl(self, root):
        u = URL(root)
        root_req = Request(u.full_url_string, **self.kw)
        uid = root_req.get_uuid()
        s = Response(root_req.get())
        retSpiderList_first = HTML(s.body, u.full_url_string).findLink()

        # 第一层
        print("[Request] {}".format(root))
        for spiderLink in retSpiderList_first:
            # 如果没有爬过, 就保存到已经爬到的列表里
            if spiderLink not in self._already_seen_url:

                print("[GET] {}".format(root+spiderLink))
                self._already_spider_url.add(root+spiderLink)
                self._already_seen_url.add(root)

        while True:

            print("第{}层爬行".format(self.spider_num+1))
            if self.spider_num >= self.depth_limit:
                print("[!] Spider is Already Finish.")
                break

            spiders = list(self._already_spider_url)
            for spiderLink in spiders:
                # 如果链接没有被爬行过,就继续爬
                if spiderLink not in self._already_seen_url:
                    print("[Request] {}".format(spiderLink))
                    uo = URL(spiderLink)
                    req = Request(uo.full_url_string)
                    res = Response(req.get())

                    retSpiderList_o = HTML(res.body, uo.full_url_string).findLink()
                    # 获取新的页面的链接
                    for spider in retSpiderList_o:
                        if spider not in self._already_seen_url:
                            link = root + spider
                            p = URL(link)
                            self._already_spider_url.add(p.full_url_string)
                        else:
                            print("[Not Request] The link is already Request")

                    self._already_seen_url.add(spiderLink)

            self.spider_num += 1

        ll = u.urls_reset(self._already_spider_url)
        # [self._would_scan_urlList.add(x) for x in u.urls_reset_load_String(ll)]
        return u.urls_reset_load_String(ll, root=root)


rets = Crawler(depth_limit=3).crawl("http://www.o2oxy.cn/")
for r in rets:
    print(r)
print("总共: " + str(len(rets)))