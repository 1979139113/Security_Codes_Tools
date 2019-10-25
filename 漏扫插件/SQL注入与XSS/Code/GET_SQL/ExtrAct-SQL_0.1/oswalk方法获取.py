# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import os.path
for root, dirs, files in os.walk('.',True):
    for name in files:
        res = (os.path.join(root, name) )
        res = (res.replace('.\\',''))
        #print(res)
        try:
            with open(res,'r',encoding='utf-8')as a:
                if 'do you want to use common table existence check?' in a.read():
                    print(res)

        except Exception as e:
            #print(e)
            pass
# 结果在database。py