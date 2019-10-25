import os
li = []
li=list(set([i.replace("\n","") for i in open("cc.txt","r").readlines()]))
with open('c.txt','a+')as s:
    for x in li:
        s.write(x + '\n')

