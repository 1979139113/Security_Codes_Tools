__author__ = 'junmoxiao'
#!/usr/bin/env python
#coding=utf-8
import glob, sys, requests
import threading
import Queue
import re
import signal
import os
import argparse


file_queue = Queue.Queue()
lock = threading.Lock()
threads = []

def request_cms(host, path, keyword, cms):   
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(host + path, headers=headers)
    if r.status_code != 200:
        return None
    data = r.text
    if re.compile(r'(?i)'+keyword).search(data):
        return cms
    else:
        return None


def get_cms_list():
    cms_list = glob.glob("./data/*")
    for cms in cms_list:
        file_queue.put(cms)


def check_cms(host):
    while not file_queue.empty():
        file_path = file_queue.get()
        for line in open(file_path):
            path, keyword, cms = line.split('------')
            result = request_cms(host, path, keyword, cms)      
            if result != None:
                lock.acquire()
                print "* This is %s" % result
                lock.release()
                os._exit(1)
        lock.acquire()
        print "This is not %s" % cms.strip()
        lock.release()


def handle_interrupt():
    for t in threads:
        t.join(0.3)
        if t.is_alive():
            return False
    return True
       
    
def scan(host, thread_count):
    get_cms_list()
    for i in range(thread_count):
        t = threading.Thread(target=check_cms, args=(host,))
        t.setDaemon(True)
        threads.append(t)
        t.start()
    while True:
        try:
            while not handle_interrupt():
                continue
            break
        except KeyboardInterrupt:
            print '! User Interrupt!'
            os._exit(1)
    print 'can\'t identify it......'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Hacking for fun! identify cms", version='0.2')
    parser.add_argument('host', help='must start with http(s)')
    parser.add_argument('-t', '--thread_count', default=5)
    args = parser.parse_args()
    if not args.host.lower().startswith('http'):
        parser.print_help()
        sys.exit(1)
    scan(args.host, args.thread_count)

