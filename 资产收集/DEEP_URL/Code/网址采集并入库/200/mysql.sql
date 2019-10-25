
create database url;
use url;

create table url_index(
id int primary key auto_increment,
url varchar(80),
urlget varchar(1),
datatime varchar(80)
)charset=utf8;

create table url_domain(
id int primary key auto_increment,
url varchar(80) UNIQUE,
datatime varchar(80)
)charset=utf8;

create table url_subdomain(
id int primary key auto_increment,
url varchar(80) UNIQUE,
datatime varchar(80)
)charset=utf8;

create table result(
id int primary key auto_increment,
url varchar(80) UNIQUE,
datatime varchar(80)
)charset=utf8;

create table die(
id int primary key auto_increment,
url varchar(80) UNIQUE,
datatime varchar(80)
)charset=utf8;
