create database Lang_cms;
use Lang_cms;
#���������ݿ�

INSERT INTO url_1(urllist) SELECT 'www.123.com' FROM DUAL WHERE NOT EXISTS(SELECT 'www.123.com' FROM url_1);

#create table url(
#id int primary key auto_increment,
#urllist varchar(30),
#urlget int,
#cmsscan int
#)charset=utf8;
#����������վ�ı�  ����urllistΪ��ַ  urlgetΪ�Ƿ����й�������ʵ������������֤  cmsscanΪ�Ƿ�ͨ��cmsɨ����֤


create table url_1(
id int primary key auto_increment,
urllist varchar(80),
urlget varchar(1),
urltime varchar(80)
)charset=utf8;

#���ű�������Ƕ��û�ԭʼ�������ַ���д洢 Ȼ��ɼ��������е���ַ
#urllist����ַ�б�  urlget����ַ�Ƿ����й� 0����û��1������

create table url_2(
id int primary key auto_increment,
urllist varchar(80),
cmsscan varchar(1),
rarscan varchar(1),
st2 varchar(1),
gettime varchar(80)
)charset=utf8;

#���ű�������Ǵ洢��ַ cmsscan�Ƿ����cms����  rarscan�Ƿ���б����ļ�ɨ��  st2�Ƿ�ʹ����st2���


create table url_3(
id int primary key auto_increment,
urllist varchar(80),
urllujin varchar(100),
cms varchar(100),
cmstime varchar(80)
)charset=utf8;

#���ű�������Ǵ洢ɨ�貢����֤�ɹ���cms  �����ݿⱣ��Ҳ���ǻ���


create table url_4(
id int primary key auto_increment,
urllist varchar(80),
rarsize varchar(4294967294),
rartime varchar(80)
)charset=utf8;

#���ű�������Ǵ洢ɨ��������ڱ����ļ�����ַ  rarsize�Ǳ����ļ���С  ���������ݿⱣ��Ҳ���ǻ���

create table url_5(
id int primary key auto_increment,
urllist varchar(80),
st varchar(5000),
st2time varchar(80)
)charset=utf8;

#������


#�����ݿ����泣�õ�����
# ���Ҫ�鿴���й���������վ select urllist from url_1;  
# ���Ҫ�鿴����������֤����ַ  select urllist from url_2 where cmsscan=1;
# ѧ������mysql  д�ĺ���  �������и��õ�д����ӭ��ϵ�����ұ��� QQ��982722261