import os
path = r'E:\python27\CMS\chajian\plugins'
for filename in os.listdir(path):
    print(os.path.join(path,filename)).replace("E:\\python27\\CMS\\chajian\\cms\\","")
    d = (os.path.join(path,filename)).replace("E:\python27\CMS\chajian\plugins","")
    with open('cc.txt','a+')as a:
        a.write(str(d) + '\n')
