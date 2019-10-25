通配符自定义文件名

格式如下

/{domain}.rar
/www.{domain}.rar
/data/{domain}.zip
/1.rar
/data.rar
....


通配符可以直接写在rar.txt中，会自动判断通配符

按照网址进行了筛选排除

---------------------------------------
	主域名匹配规则如下
1. http://www.baidu.com
	domain = baidu

2. http://www.zhidao.baidu.com
	domain1 = zhidao
	domain2 = baidu
	domain3 = zhidao.baidu

3. http://zhidao.baidu.com
	domain1 = zhidao
	domain2 = baidu
	domian3 = zhidao.baidu
---------------------------------------


开启时会询问：【是否全规则扫描(0/全规则扫描,1/自定义通配符扫描):1】

输入0的话 启用软件默认的全部规则检测扫描，包括rar.txt中启用了通配符和rar.txt中通配符之外的文件名也一起扫描。

输入1的话，从rar.txt中找到通配符匹配主域名，rar.txt中通配符之外的文件名也会加在一起扫描
