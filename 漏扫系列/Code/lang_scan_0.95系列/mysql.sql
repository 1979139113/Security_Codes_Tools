create database Yolanda_information_collection;
use Yolanda_information_collection;
#���������ݿ�

#INSERT INTO url_1(urllist) SELECT 'www.123.com' FROM DUAL WHERE NOT EXISTS(SELECT 'www.123.com' FROM url_1);
#INSERT INTO url_1(urllist) SELECT 'www.1234.com' FROM DUAL WHERE NOT EXISTS(SELECT * FROM url_1 where urllist='www.1234.com');

#sql = "INSERT INTO url_index(url,urlget,datatime) select (%s,%s,%s) from dual where not exists(select * from url_index where url = str(xx))"
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



#�����ݿ����泣�õ�����
# ���Ҫ�鿴���й���������վ select urllist from url_1;  
# ���Ҫ�鿴����������֤����ַ  select urllist from url_2 where cmsscan=1;
# ѧ������mysql  д�ĺ���  �������и��õ�д����ӭ��ϵ�����ұ��� QQ��982722261















sql001 = "insert into url_check(url,cmsscan,rarscan,sqlscan,datatime) select (%s,%s,%s,%s,%s) from dual where not exists(select * from url_check where url = str(xx))"
sql = "INSERT INTO url_index(url,urlget,datatime) select (%s,%s,%s) from dual where not exists(select * from url_index where url = str(xx))"





























