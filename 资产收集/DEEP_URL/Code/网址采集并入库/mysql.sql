create database url_get;
use url_get;
#创建主数据库



create table url_index(
id int primary key auto_increment,
url varchar(80),
urlip varchar(80),
urlget varchar(1),
datatime varchar(80)
)charset=utf8;

create table url_result(
id int primary key auto_increment,
url varchar(80),
urlget varchar(1),
datatime varchar(80)
)charset=utf8;

create table result(
id int primary key auto_increment,
url varchar(80),
datatime varchar(80)
)charset=utf8;

