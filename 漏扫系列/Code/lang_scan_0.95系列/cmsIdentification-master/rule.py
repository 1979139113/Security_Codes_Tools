#coding:utf-8
f = open('cccc.txt','a+')
with open('cms.txt','r')as c:
    for cc in c:
        ccc = cc.replace('\n','')
        if ccc.endswith('|'):
            f.write(cc)
        else:
            f.write(ccc + '|\n')
f.close()
print 'over'
