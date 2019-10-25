# -*- coding: utf-8 -*-
"""
__author__ = 'Langziyanqin'
__QQ__ = '982722261'
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import sys
import time
import string
reload(sys)
sys.setdefaultencoding('utf-8')
list_jindu= string.ascii_letters+string.digits+'.'+'_'+' '
jindu ='YolAnda_Scan 0.98 Console Start up...'
jindud = ''
for xx in jindu:
    for x in list_jindu:
        sys.stdout.write(jindud+"\r")
        if xx == x:
            jindud=jindud+x
            sys.stdout.write(jindud+"\r")
            time.sleep(0.03)
            break
        else:
            sys.stdout.write(jindud+x+"\r")
            time.sleep(0.03)
            sys.stdout.flush()
        sys.stdout.write(jindud+"\r")
sys.stdout.write(jindud+'\r')
