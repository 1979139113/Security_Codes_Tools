# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import time
import asyncio
import aiohttp
import aiomultiprocess
import aiofiles
import multiprocessing

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3'}
async def run(url):
    async with asyncio.Semaphore(2000):
        async with aiohttp.ClientSession()as session:
            try:
                async with session.head(url,headers=headers,timeout=5) as resp:
                    print('网址:{}  状态:{}'.format(resp.url, resp.status))
                    await resp.text()
                    if resp.status == 200:
                        async with aiofiles.open('result.txt','a+',encoding='utf-8')as a:
                            await a.write(url + '\n')

                    else:
                        async with aiofiles.open('log.txt', 'a+', encoding='utf-8')as a:
                            await a.write(url + ':' + str(resp.status)+'\n')

            except:
                pass

async def main(url):
    #url = 'https://www.52pojie.cn:{}'
    url = url+':{}'
    tasks = [url.format(i)for i in range(50,50000)]
    #time.sleep(50000)
    async with aiomultiprocess.Pool() as pool:
        # 开启进程池
        await pool.map(run, tasks)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    print('''

             _                           _
            | |                         (_)
            | |     __ _ _ __   __ _ _____
            | |    / _` | '_ \ / _` |_  / |
            | |___| (_| | | | | (_| |/ /| |
            |______\__,_|_| |_|\__, /___|_|
                                __/ |      Langzi_URL_port_SCAN
                               |___/       Version:0.5 
                                           Datetime:2019-05-01
                                           域名端口盲测工具


    ''')
    time.sleep(1)

    inp = input('Set Your Target url : ')
    if inp.find('http')<0:
        inp = 'http://'+inp.rstrip('/')
    else:
        inp = inp.rstrip('/')
    print('\n')
    print('Target Was Set : {}'.format(inp))
    print('\n')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(inp))
    print('SCAN OVER')
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)
    time.sleep(500)
