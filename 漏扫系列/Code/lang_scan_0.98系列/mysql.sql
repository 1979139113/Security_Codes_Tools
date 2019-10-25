create database Yolanda_information_collection_09_main;
use Yolanda_information_collection_09_main;
#���������ݿ�


#create table url(
#id int primary key auto_increment,
#urllist varchar(30),
#urlget int,
#cmsscan int
#)charset=utf8;
#����������վ�ı�  ����urllistΪ��ַ  urlgetΪ�Ƿ����й�������ʵ������������֤  cmsscanΪ�Ƿ�ͨ��cmsɨ����֤


create table url_index(
id int primary key auto_increment,
url varchar(80),
urlget varchar(1),
datatime varchar(80),
index index_neme (urlget)
)charset=utf8,engine=MYISAM;

#���ű�������Ƕ��û�ԭʼ�������ַ���д洢 Ȼ��ɼ��������е���ַ
#urllist����ַ�б�  urlget����ַ�Ƿ����й� 0����û��1������

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

#���ű�������Ǵ洢��ַ cmsscan�Ƿ����cms����  rarscan�Ƿ���б����ļ�ɨ��  sqlע��ɨ��
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

#���ű�������Ǵ洢ɨ�貢����֤�ɹ���cms  �����ݿⱣ��Ҳ���ǻ���


create table url_backup(
id int primary key auto_increment,
url varchar(80),
rarsize varchar(80),
urltitle varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;

#���ű�������Ǵ洢ɨ��������ڱ����ļ�����ַ  rarsize�Ǳ����ļ���С  ���������ݿⱣ��Ҳ���ǻ���

create table url_sqlinj(
id int primary key auto_increment,
url varchar(80),
urltitle varchar(80),
sqldatabase varchar(80),
datatime varchar(80)
)charset=utf8,engine=MYISAM;
#������
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



#ɾ����������ʹ��ALTER TABLE��DROP INDEX�����ʵ�֡�DROP INDEX������ALTER TABLE�ڲ���Ϊһ����䴦�����ʽ���£�
#drop index index_name on table_name ;
#alter table table_name drop index index_name ;



#drop index index_name on url_index

