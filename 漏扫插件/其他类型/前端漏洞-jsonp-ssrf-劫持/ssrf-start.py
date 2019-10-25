# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import re
import requests
from IPy import IP
import Queue
import threading
def get_url_queue():
    url = "http://www.sogou.com/reventondc/external?key=&objid=&type=2&charset=utf-8&url=http://"
    urllist = Queue.Queue()
    ip_list = IP('10.146.20.0/24')
    port_list = ['80','8000','8080']
    for ip_add in ip_list:
        ip_add = str(ip_add)
        for port in port_list:
            url_t = url + ip_add + ':' + port
            urllist.put(url_t)
    return urllist
def get_title(urllist):
    while not urllist.empty():
        url = urllist.get()
        html = requests.get(url).text
        patt = r'<title>(.*?)</title>'
        m = re.search(patt,html)
        if m:
            title = m.group(1)
            print "%s\t%s" % (url,title)
urllist = get_url_queue()
print "start get title..."
for x in xrange(1,30):
    t = threading.Thread(target=get_title,args=(urllist,))
    t.start()