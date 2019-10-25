create database Lang_cms;
use Lang_cms;
#创建主数据库

INSERT INTO url_1(urllist) SELECT 'www.123.com' FROM DUAL WHERE NOT EXISTS(SELECT 'www.123.com' FROM url_1);

#create table url(
#id int primary key auto_increment,
#urllist varchar(30),
#urlget int,
#cmsscan int
#)charset=utf8;
#创建储存网站的表  其中urllist为网址  urlget为是否爬行过作用是实现无限爬行认证  cmsscan为是否通过cms扫描验证


create table url_1(
id int primary key auto_increment,
urllist varchar(80),
urlget varchar(1),
urltime varchar(80)
)charset=utf8;

#这张表的作用是对用户原始输入的网址进行存储 然后采集所有爬行的网址
#urllist是网址列表  urlget是网址是否爬行过 0就是没有1就是有

create table url_2(
id int primary key auto_increment,
urllist varchar(80),
cmsscan varchar(1),
rarscan varchar(1),
st2 varchar(1),
gettime varchar(80)
)charset=utf8;

#这张表的作用是存储网址 cmsscan是否进行cms爬行  rarscan是否进行备份文件扫描  st2是否使用了st2框架


create table url_3(
id int primary key auto_increment,
urllist varchar(80),
urllujin varchar(100),
cms varchar(100),
cmstime varchar(80)
)charset=utf8;

#这张表的作用是存储扫描并且认证成功的cms  在数据库保存也不是坏事


create table url_4(
id int primary key auto_increment,
urllist varchar(80),
rarsize varchar(4294967294),
rartime varchar(80)
)charset=utf8;

#这张表的作用是存储扫描出来存在备份文件的网址  rarsize是备份文件大小  但是在数据库保存也不是坏事

create table url_5(
id int primary key auto_increment,
urllist varchar(80),
st varchar(5000),
st2time varchar(80)
)charset=utf8;

#不解释


#在数据库里面常用的命令
# 如果要查看爬行过的所有网站 select urllist from url_1;  
# 如果要查看所有爬行验证的网址  select urllist from url_2 where cmsscan=1;
# 学了两天mysql  写的很乱  如果大家有更好的写法欢迎联系浪子我本人 QQ：982722261