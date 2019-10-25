create database Yolanda_information_collection_09_main;
use Yolanda_information_collection_09_main;
#创建主数据库


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
datatime varchar(80),
index index_neme (urlget)
)charset=utf8,engine=MYISAM;

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
unauthorizedscan varchar(1),
datatime varchar(80),
index index_name (cmsscan,rarscan,sqlscan,st2scan,editorscan,portscan,unauthorizedscan)
)charset=utf8,engine=MYISAM;

#这张表的作用是存储网址 cmsscan是否进行cms爬行  rarscan是否进行备份文件扫描  sql注入扫描
create table url_unauthorizedscan(
id int primary key auto_increment,
url varchar(80),
ip varchar(80),
uauth varchar(100),
urltitle varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;

create table url_cms(
id int primary key auto_increment,
url varchar(80),
urlway varchar(100),
cmstype varchar(100),
urltitle varchar(100),
datatime varchar(80)
)charset=utf8,engine=MYISAM;

#这张表的作用是存储扫描并且认证成功的cms  在数据库保存也不是坏事


create table url_backup(
id int primary key auto_increment,
url varchar(80),
rarsize varchar(80),
urltitle varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;

#这张表的作用是存储扫描出来存在备份文件的网址  rarsize是备份文件大小  但是在数据库保存也不是坏事

create table url_sqlinj(
id int primary key auto_increment,
url varchar(80),
urltitle varchar(80),
sqldatabase varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;
#不解释
create table url_sqlinj_log(
id int primary key auto_increment,
url varchar(80),
urlget varchar(1),
datatime varchar(80),
index index_name (urlget)
)charset=utf8,engine=MYISAM;

create table url_st2(
id int primary key auto_increment,
url varchar(80),
urltitle varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;

create table url_editor(
id int primary key auto_increment,
url varchar(100),
urltitle varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;

create table url_port(
id int primary key auto_increment,
url varchar(80),
ip varchar(80),
port varchar(400),
urltitle varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;

create table url_2check(
id int primary key auto_increment,
url varchar(80),
cmsscan varchar(1),
rarscan varchar(1),
sqlscan varchar(1),
st2scan varchar(1),
editorscan varchar(1),
portscan varchar(1),
unauthorizedscan varchar(1),
datatime varchar(80),
index index_name (cmsscan,rarscan,sqlscan,st2scan,editorscan,portscan,unauthorizedscan)
)charset=utf8,engine=MYISAM;


create table url_2index(
id int primary key auto_increment,
url varchar(80),
urlget varchar(1),
datatime varchar(80),
index index_name (urlget)
)charset=utf8,engine=MYISAM;


#ALTER TABLE url_index ADD INDEX index_name (urlget);
#ALTER TABLE url_2index ADD INDEX index_name (urlget);
#ALTER TABLE url_check ADD INDEX index_name (cmsscan,rarscan,sqlscan,st2scan,editorscan,portscan,unauthorizedscan);
#ALTER TABLE url_2check ADD INDEX index_name (cmsscan,rarscan,sqlscan,st2scan,editorscan,portscan,unauthorizedscan);



#删除索引可以使用ALTER TABLE或DROP INDEX语句来实现。DROP INDEX可以在ALTER TABLE内部作为一条语句处理，其格式如下：
#drop index index_name on table_name ;
#alter table table_name drop index index_name ;



#drop index index_name on url_index

