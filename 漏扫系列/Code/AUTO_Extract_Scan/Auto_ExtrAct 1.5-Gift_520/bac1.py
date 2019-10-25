# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import requests
import time
import aiohttp
import aiofiles
import aiomultiprocess
import multiprocessing
import asyncio

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3', 'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Cache-Control': 'max-age=0', 'referer': 'http://www.soso.com', 'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3'}
backup_suffix = ['.rar', '.zip', '.tar', '.tar.bz2', '.sql', '.7z', '.bak',  '.tar.gz','.gz',]


async def run(urls):
    async with asyncio.Semaphore(1000):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            try:
                async with session.head(urls,timeout=10) as resp:
                    #print(resp.headers.get("Content-Length"))
                    #if int(resp.headers.get("Content-Length")) > 1500000:
                        #print('存在备份文件!!!!!!!!!!!!!!!!!!')
                    if int(resp.headers.get('Content-Length')) > 1500000:
                        print('当前检测:{}  状态:{}'.format(resp.url, resp.status))
                        async with aiofiles.open('result.txt','a+',encoding='utf-8')as f:
                            await f.write(urls + '   ' + str(int(resp.headers["Content-Length"]) / 1024000).split('.')[0] + 'M' +'\n')
            except:
                pass



async def main(urls,backs):

    all_tasks = []
    for b in backs:
        for u in urls:
            all_tasks.append(u+b)
    for b in backup_suffix:
        for u in urls:
            try:
                all_tasks.append(u+'/'+u.split('//')[1].split('.')[1]  + b)
            except:
                pass
            try:
                all_tasks.append(u+'/'+u.split('//')[1]  + b)
            except:
                pass
            try:
                all_tasks.append(u+'/'+u.split('.', 1)[1].replace('/', '') + b)
            except:
                pass
    print('目标数量:{}'.format(len(all_tasks)))
    time.sleep(2)
    if len(all_tasks)>2000000:
        print('目标数量过于庞大，可能会导致扫描过程中内存溢出')
    async with aiomultiprocess.Pool() as pool:
        await pool.map(run,all_tasks)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    import os
    os.system('color 1')
    print('''
         _____  __    __  _____   _____        ___   _____   _____  
        | ____| \ \  / / |_   _| |  _  \      /   | /  ___| |_   _| 
        | |__    \ \/ /    | |   | |_| |     / /| | | |       | |   
        |  __|    }  {     | |   |  _  /    / / | | | |       | |   
        | |___   / /\ \    | |   | | \ \   / /  | | | |___    | |   
        |_____| /_/  \_\   |_|   |_|  \_\ /_/   |_| \_____|   |_|   

                                        19年5月20礼物之源码泄露扫描    

                                                           
    ''')
    time.sleep(3)
    inp = 'urls.txt'
    urls = []
    urlss = [x.rstrip('/').strip() for x  in open(inp, 'r', encoding='utf-8').readlines()]
    for  i in urlss:
        if 'gov.cn' not in i and 'edu.cn' not in i:
            urls.append(i)
    #urls = [x.rstrip('/').strip() for x in open(inp, 'r', encoding='utf-8').readlines()]
    #inp_p = input('INPUT YOUR BACKUP_FILE.Dict:')
    inp_p = 'rar.txt'
    backs = [x.rstrip('/').strip() for x in open(inp_p, 'r', encoding='utf-8').readlines()]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls,backs))
    import sys
    sys.exit()


