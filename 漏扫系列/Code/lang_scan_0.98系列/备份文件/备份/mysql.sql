create database Yolanda_information_collection_02;
use Yolanda_information_collection_02;
#创建主数据库



#INSERT into url_index(url,urlget,datatime) select 'www.123123.com','0','2018' from dual where 'www.123123.com' not in (select url from url_index);
#sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)"%(str(xx),'0', str(timenow),str(xx))

#create table url(
#id int primary key auto_increment,
#urllist varchar(30),
#urlget int,
#cmsscan int
#)charset=utf8;
#创建储存网站的表  其中urllist为网址  urlget为是否爬行过作用是实现无限爬行认证  cmsscan为是否通过cms扫描验证


create table url_index(
id int primary key auto_increment,
url varchar(80),
urlget varchar(1),
datatime varchar(80)
)charset=utf8;

#这张表的作用是对用户原始输入的网址进行存储 然后采集所有爬行的网址
#urllist是网址列表  urlget是网址是否爬行过 0就是没有1就是有

create table url_check(
id int primary key auto_increment,
url varchar(80),
cmsscan varchar(1),
rarscan varchar(1),
sqlscan varchar(1),
st2scan varchar(1),
editorscan varchar(1),
portscan varchar(1),
datatime varchar(80)
)charset=utf8;

#这张表的作用是存储网址 cmsscan是否进行cms爬行  rarscan是否进行备份文件扫描  sql注入扫描


create table url_cms(
id int primary key auto_increment,
url varchar(80),
urlway varchar(100),
cmstype varchar(100),
datatime varchar(80)
)charset=utf8;

#这张表的作用是存储扫描并且认证成功的cms  在数据库保存也不是坏事


create table url_backup(
id int primary key auto_increment,
url varchar(80),
rarsize varchar(4294967294),
datatime varchar(80)
)charset=utf8;

#这张表的作用是存储扫描出来存在备份文件的网址  rarsize是备份文件大小  但是在数据库保存也不是坏事

create table url_sqlinj(
id int primary key auto_increment,
url varchar(80),
sqldatabase varchar(500),
datatime varchar(80)
)charset=utf8;

#不解释
create table url_sqlinj_log(
id int primary key auto_increment,
url varchar(80),
urlget varchar(1),
datatime varchar(80)
)charset=utf8;

create table url_st2(
id int primary key auto_increment,
url varchar(80),
datatime varchar(80)
)charset=utf8;

create table url_editor(
id int primary key auto_increment,
url varchar(80),
datatime varchar(80)
)charset=utf8;

create table url_port(
id int primary key auto_increment,
url varchar(80),
ip varchar(80),
port varchar(80),
datatime varchar(80)
)charset=utf8;













