create database Yolanda_information_collection_02;
use Yolanda_information_collection_02;
#���������ݿ�



#INSERT into url_index(url,urlget,datatime) select 'www.123123.com','0','2018' from dual where 'www.123123.com' not in (select url from url_index);
#sql = "INSERT INTO url_index(url,urlget,datatime) select '%s','%s','%s' from dual where '%s' not in (select url from url_index)"%(str(xx),'0', str(timenow),str(xx))

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
datatime varchar(80)
)charset=utf8;

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
datatime varchar(80)
)charset=utf8;

#���ű�������Ǵ洢��ַ cmsscan�Ƿ����cms����  rarscan�Ƿ���б����ļ�ɨ��  sqlע��ɨ��


create table url_cms(
id int primary key auto_increment,
url varchar(80),
urlway varchar(100),
cmstype varchar(100),
datatime varchar(80)
)charset=utf8;

#���ű�������Ǵ洢ɨ�貢����֤�ɹ���cms  �����ݿⱣ��Ҳ���ǻ���


create table url_backup(
id int primary key auto_increment,
url varchar(80),
rarsize varchar(4294967294),
datatime varchar(80)
)charset=utf8;

#���ű�������Ǵ洢ɨ��������ڱ����ļ�����ַ  rarsize�Ǳ����ļ���С  ���������ݿⱣ��Ҳ���ǻ���

create table url_sqlinj(
id int primary key auto_increment,
url varchar(80),
sqldatabase varchar(500),
datatime varchar(80)
)charset=utf8;

#������
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













