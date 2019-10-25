# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
# -*- coding: utf-8 -*


from Tkinter import Button,Label,Text,N,W,E,S,Frame,StringVar,Tk,END,BOTH

import  re
from  requests import get


class App(object):
    def __init__(self,master):
        frame=Frame(master)
        frame.pack(fill=BOTH,expand=True)
        label=Label(frame,text='URL:',fg='green',font=('Courier New',16))
        label.grid(row=0,column=0,sticky=W)
        self.url=''
        self.text=Text(frame,width=60,height=7,font=('Courier New',12))
        self.text.grid(row=1,columnspan=2)

        self.button=Button(frame,text='检测',font=('Courier New',12))
        self.button.grid(row=2,column=1,sticky=E)

        self.response=Text(frame,font=('Courier New',12),width=60,height=10)
        self.response.grid(row=3, column=0,columnspan=2)

        self.msg=StringVar()
        self.result=Label(frame,textvariable=self.msg,fg='blue',font=('Courier New',12))
        self.result.grid(row=4,column=0,columnspan=2,sticky=N+S+W+E)

        self.button.bind('<Button-1>',self.check)
        self.pattern=re.compile('^(?:http|https)://(?:\w+\.)+.+')
        self.header= {

              "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
            }
        self.payload=''
    def check(self,event):
        self.msg.set('')
        self.url=self.text.get(1.0,END).strip()
        chek_url=self.pattern.match(self.url)
        # print chek_url.group()
        if  not chek_url  :
            # print ('123')
            self.msg.set('请输入正确的(GET)URL!')
        else:
            try:
                response =get(self.url,headers=self.header)
                self.response.delete(1.0,END)
                self.response.insert(END,response.text)
                # print response.content
                req_pattern=re.compile('\s*?\w+\([\w\W]+?\)|;$')
                res_match=req_pattern.match(response.text)
                if res_match:
                    self.result.config(fg='red')
                    self.msg.set('该URL 存在 JSONP劫持 漏洞！！！ payload生成后期有时间会完善！')
                else:
                    self.msg.set('该URL 不存在 JSONP劫持 漏洞。')
            except :
                self.result.config(fg='red')
                self.msg.set('网络资源请求失败，请确保已经接入互联网和网址的有效性！')


root=Tk()
root.title('JSONP漏洞检测工具 by WD(WX:13503941314)  Topsec V2 ')
root.geometry('700x500+100+100')

app=App(root)
root.mainloop()






if __name__ == '__main__':
    pass