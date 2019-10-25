需要配合 svn-git源码泄露扫描工具0.6 版本一起使用

 LANG_BACKUP_FILE_SCAN 3.9  负责批量自动化扫描备份文件，保存结果

Langzi_Auto_GIT_SVN_Scan v0.5 负责解析  svn-git源码泄露扫描工具0.6  的结果，并自动化生成报表

注意 扫描url的最后不能有/，即

	http://www.5xxx.com//.git/config
	http://xxx.org/.git//config

	这样不行

	http://www.xxx.com/.git/config
	http://xx.org/.git/config

	这样子可以

也是langzi安全巡航的独立衍生品