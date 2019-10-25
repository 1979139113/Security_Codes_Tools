# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
url = 'http://127.0.0.1/xss/level1.php?name=<script>prompt(1)</script>'
try:
    driver = webdriver.Firefox()
    # 初始化浏览器
    driver.get(url)
    # 打开网址
    driver.set_page_load_timeout(20)
    # 设置超时
    try:
        result = EC.alert_is_present()(driver)
        # 如果弹窗则返回对象
        if result:
            print('完蛋啦~~存在弹窗~~')
    except:
        pass
except:
    pass
import time
time.sleep(20)