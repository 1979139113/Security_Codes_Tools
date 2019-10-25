# coding:utf-8

f1 = [x.replace('\n','') for x in open('2018-09-04-01-26-17.txt','r')]
f2 = open('log.txt','r').read()

for _ in f1:
    if _.replace('http://','').replace('https://','').replace('http://www.','').replace('https://www.','') in f2:
        print '该网址 : ' + _ + '  :  存在'
    else:
        print '该网址 : ' + _ + '  :  不不不不不不不不不存在'
