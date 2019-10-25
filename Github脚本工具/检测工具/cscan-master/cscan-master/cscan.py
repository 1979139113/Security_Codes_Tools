#coding:gb2312
import os
import re
import Queue
import threading

q=Queue.Queue()

class getCSgement:
    #初始化
    def __init__(self,url):
        if "http" in url:
            pattern = re.compile(r'(?<=//).+(?<!/)')
            match = pattern.search(url)
            try:
                url = match.group()
            except:
                print "正则error"
            self.url = url
        else:
            self.url = url
        
    def cSgment(self):
        lookStr = self.nsLookUp(self.url)
        listIp = self.fetIp(lookStr)
        
        if len(listIp)==0:
            return "networkbad"      

        if self.checkCdn(listIp):
            strIp = ""
            for i in listIp:
                strIp = strIp + i + ","
            return strIp[:-1] + " (可能使用了cdn)"
        
        return self.makeCSeg(listIp)
    
    
    #使用nslookup命令进行查询
    def nsLookUp(self,url): 
        cmd = 'nslookup %s 8.8.8.8' % url
        handle = os.popen(cmd , 'r')
        result = handle.read()
        return result
    
    #获取nslookup命令查询的结果里面的ip
    def fetIp(self,result):
        ips =  re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', result)
        if '8.8.8.8' in ips:
            ips.remove('8.8.8.8')
        return ips
        
    #检测是否使用cdn
    def checkCdn(self,ips):
        if len(ips)>1:
            return True
        return False
    
    #生成c段
    def makeCSeg(self,ips):
        if not self.checkCdn(ips):
            ipStr = "".join(ips)
            end = ipStr.rfind(".") 
            return ipStr[0:end+1] + "1-" + ipStr[0:end+1] + "254"

#开始扫描        
def scaner():
    while not q.empty():
        url=q.get()
        t = getCSgement(url)
        result = t.cSgment()
        
        if not "networkbad" in result:
            print url + ":" + result
            if not "cdn" in result:
                writeFile("result.txt", result + "\n")
        else:
            t = getCSgement(url)
            result2 = t.cSgment()
            if not "networkbad" in result2:
                print url + ":" + result2
                if not "cdn" in result2:
                    writeFile("result.txt", result2 + "\n")
            else:
                print url + ":不能访问 或者 网络不稳定"
                
    if q.empty():
        delRep()
                
#保存记录
def writeFile(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()

#去重复
def delRep():
    buff = []
    for ln in open('result.txt'):
        if ln in buff:
            continue
        buff.append(ln)
    with open('result2.txt', 'w') as handle:
        handle.writelines(buff)
        
        
#判断文件是否创建
def isExist():
    if not os.path.exists(r'result.txt'):
        f = open('result.txt', 'w')
        f.close()
    else:
        os.remove('result.txt')
        
    if os.path.exists(r'result2.txt'):
        os.remove('result2.txt')    

if __name__=="__main__":
    isExist()
    
    #读取网址
    lines = open("domains.txt","r")
    for line in lines:
        line=line.rstrip()
        q.put(line)
        
    #开启线程
    for i in range(3): 
        t = threading.Thread(target=scaner)
        t.start()
        
        
    


