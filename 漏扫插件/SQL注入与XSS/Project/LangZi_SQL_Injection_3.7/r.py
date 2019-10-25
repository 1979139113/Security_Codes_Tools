with open('urlsss.txt','a+')as a:
	a.writelines(filter(lambda x:'gov.cn' not in x and 'edu.cn' not in x,[x.lstrip() for x in open('url.txt','r').readlines()]))