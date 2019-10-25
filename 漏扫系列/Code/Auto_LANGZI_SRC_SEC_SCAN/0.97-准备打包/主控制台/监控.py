# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import psutil
import time
import os

dlls = ['ExtrAut.dll','ExtrBc1.dll','ExtrBc2.dll','ExtrBc3.dll','ExtrCors.dll','ExtrGiS.dll',
                'ExtrLfi.dll','ExtrSLk.dll','ExtrSql.dll','ExtrSuB.dll','ExtrSuR.dll','ExtrSuS.dll',
                'ExtrUrl.dll','ExtrXss.dll','python.exe']
def check():
    while 1:
        try:
            list_ = []
            for pnum in psutil.pids():
                p = psutil.Process(pnum).name()
                list_.append(p)
            print(list_)
            time.sleep(1)
            if 'Langzi_SRC_Safe_Cruise.exe' in list_:
                print('{} : 正在运行...'.format('Langzi_SRC_Safe_Cruise.exe'))
                time.sleep(360)
                # 每18s检测一次
            else:
                print('{} : 停止运行....'.format('Langzi_SRC_Safe_Cruise.exe'))
                for dll in dlls:
                    try:
                        os.system('taskkill /F /IM ' + dll)
                    except Exception as e:
                        print(str(e))
                return
        except Exception as e:
            print(e)

check()
time.sleep(5)
check()
time.sleep(5)
check()
time.sleep(5)
check()


