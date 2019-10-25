CREATE DATABASE IF NOT EXISTS lang_cms_find;
USE lang_cms_find;
create table if not EXISTS url_index(id int primary key auto_increment,
url varchar(80),
urlget varchar(1) default 0)
charset=utf8;

create table if not EXISTS url_cms(id int primary key auto_increment,
url varchar(80),
urlway varchar(200),
cmstype varchar(20),
urltitle varchar(100),
datetime varchar(80))
charset=utf8;
ALTER TABLE url_index ENGINE=INNODB;
alter table url_index add unique(url);

-- BEGIN;INSERT INTO url_index(url,urlget)VALUES('http://www.baidu.com','0');COMMIT WORK;
-- BEGIN;SELECT url FROM url_index WHERE urlget=0 LIMIT 0,1;UPDATE url_index set urlget=1 WHERE urlget=0 limit 1;COMMIT WORK;
insert into url_index(url) values ("http://www.hao123.com");
insert into url_index(url) values ("http://www.cn-hack.cn");
insert into url_index(url) values ("https://www.5566.net/hack-.htm");
insert into url_index(url) values ("https://hao.360.cn");
insert into url_index(url) values ("https://www.2345.com");
insert into url_index(url) values ("https://123.sogou.com");
insert into url_index(url) values ("http://www.26595.com");
insert into url_index(url) values ("http://www.dn1234.com");
insert into url_index(url) values ("http://www.best918.com");
insert into url_index(url) values ("http://www.baidu.us");
insert into url_index(url) values ("http://www.world68.com");
insert into url_index(url) values ("http://hao.199it.com");
insert into url_index(url) values ("http://www.meddir.cn");
insert into url_index(url) values ("http://www.36zhen.com/t?id=152");
insert into url_index(url) values ("http://www.21industry.com");
