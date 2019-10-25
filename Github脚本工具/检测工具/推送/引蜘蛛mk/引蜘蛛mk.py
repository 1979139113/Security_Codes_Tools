from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import time
import string
def id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def urls(i):    ##生成i个url组成的list#
    aaa=id(random.choice(range(3,8)),'1234567890QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuiopasdfghjklmnbvcxz')
    bbb=id(random.choice(range(3,8)),'1234567890QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuiopasdfghjklmnbvcxz')
    
    link='http://so.sooopu.com/feng'+aaa+'/'+time.strftime("%Y%m%d%H%M", time.localtime())+'/'+bbb+'/'
    return link
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
driver = webdriver.PhantomJS(desired_capabilities=dcap)
while True:
    try:
        url=urls(1)
        print('加载%s成功'%(url))
        driver.get(url)
        driver.set_page_load_timeout(10)
        driver.set_script_timeout(10)
        driver.delete_all_cookies()
        time.sleep(random.choice(range(1,5)))
        print(url)
    except:
        driver.quit()
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        driver=webdriver.PhantomJS(desired_capabilities=dcap)
