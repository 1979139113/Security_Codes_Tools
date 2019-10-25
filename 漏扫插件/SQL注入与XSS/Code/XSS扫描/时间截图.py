# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
from PIL import ImageGrab
try:
    pic = ImageGrab.grab(bbox=(20, 31, 1266, 1016))
    # 指定坐标 左上角和右下角
    # pic = ImageGrab.grab()
    # 全屏截图
    try:
        pic.save("code.png")
        # 图片保存为code.png
    except Exception as e:
        print(e)
except Exception as e:
    print(e)