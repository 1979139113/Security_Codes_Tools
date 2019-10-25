# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 0029 18:53
# @Author  : Langzi
# @Blog    : www.langzi.fun
# @File    : 0.99注册机.py
# @Software: PyCharm
import sys
import uuid
import hashlib
import base64
import time
reload(sys)
sys.setdefaultencoding('utf-8')

mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
print mac
mac_address = '%s:%s:%s:%s:%s:%s' % (mac[0:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:])
print 'Current Computer MAC Address:' + mac_address
print '\n'
md5 = hashlib.md5()
md5.update(mac)
md7 = md5.hexdigest()[::-1]
md8 = md7[2:6] + 'zhaohan'+md7[5:10]
sha1 = hashlib.sha256(md8).hexdigest()
sha2 = hashlib.md5(sha1[2:12]).hexdigest()[5:15]
yonghukey=sha2.replace('0','L').replace('5','O').replace('2','E')
print 'Current Computer Key:' + yonghukey
time.sleep(1)
print '\n'
mac_address_1 = raw_input("input mac address:")
mac = mac_address_1.replace(":",'').replace('-','')
md5 = hashlib.md5()
md5.update(mac)
md7 = md5.hexdigest()[::-1]
md8 = md7[2:6] + 'zhaohan'+md7[5:10]
sha1 = hashlib.sha256(md8).hexdigest()
sha2 = hashlib.md5(sha1[2:12]).hexdigest()[5:15]
yonghukey=sha2.replace('0','L').replace('5','O').replace('2','E')
print 'Computer Key:' + yonghukey
time.sleep(60)
# 97 md8 = md7[2:6] + 'zhaohana'+md7[5:10]
