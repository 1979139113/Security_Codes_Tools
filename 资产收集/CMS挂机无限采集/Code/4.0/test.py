# -*- coding:utf-8 -*-
# __author__:langzi
# __blog__:www.langzi.fun

def send_url_database(level, waf, check_cms):
    time.sleep(random.randint(1, 20))
    time.sleep(random.randint(1, 20))
    time.sleep(random.randint(1, 20))
    time.sleep(random.randint(1, 20))

    while 1:
        with connect_mysql() as cursor:
            select_url_sql = 'SELECT url FROM url_index WHERE urlget=0 LIMIT 0,1;'
            update_url_sql = 'UPDATE url_index set urlget=1 WHERE urlget=0 limit 1'
            cursor.execute(select_url_sql)
            url = cursor.fetchone()[0]
            cursor.execute(update_url_sql)
        urls = get_url_from_content(url)
        print('[ {} ] 爬取新网址 :{} 个'.format(datetime.datetime.now(), len(urls))
        if urls:
            for u in urls:
                with connect_mysql() as cursor:
                sqls = 'insert into url_index(url) values ("{}")'.format(u)
                cursor.execute(sqls)

        if check_cms == 1:
        # 注释下面的代码，则不会进行cms检测
            cms = scan_url_cms(url, level, waf)
            if cms:
                sqls = f'insert into url_cms(url,urlway,cmstype,urltitle,datetime)values ("{url}","{cms[0]}","{cms[1]}","{cms[2]}","{datetime.datetime.now()}")'
                with connect_mysql() as cursor:
                    cursor.execute(sqls)











        if urls:
            for u in urls:
                with connect_mysql() as cursor:
                sqls = 'insert into url_index(url) values ("{}")'.format(u)
                cursor.execute(sqls)

        if check_cms == 1:
        # 注释下面的代码，则不会进行cms检测
            cms = scan_url_cms(url, level, waf)
            if cms:
                sqls = f'insert into url_cms(url,urlway,cmstype,urltitle,datetime)values ("{url}","{cms[0]}","{cms[1]}","{cms[2]}","{datetime.datetime.now()}")'
                with connect_mysql() as cursor:
                    cursor.execute(sqls)




        cfg = configparser.ConfigParser()
        cfg.read('Config.ini')
        user = cfg.get("Server", "username")
        passwd = cfg.get("Server", "password")
        host = cfg.get("Server", "host")
        Dbname = cfg.get("Server", "db")
        thread_s = int(cfg.get("Config", "thread_s"))
        level = int(cfg.get("Config", "level"))
        port = int(cfg.get("Server", "port"))
        waf = int(cfg.get("Config", "check_waf"))
        check_cms = int(cfg.get("Config", "check_cms"))
        test_connect_database(user, passwd, host, port, Dbname)
        time.sleep(3)

        p = ThreadPoolExecutor()
        for i in range(thread_s):
            p.submit(send_url_database, level, waf, check_cms)



