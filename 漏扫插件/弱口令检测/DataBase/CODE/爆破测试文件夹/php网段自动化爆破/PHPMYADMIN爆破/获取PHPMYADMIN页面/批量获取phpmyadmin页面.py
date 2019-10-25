# coding:utf-8
import asyncio
import aiomultiprocess
import aiohttp
import aiofiles
import time
async def run(url):
    async with asyncio.Semaphore(1000):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url,timeout=20) as resp:
                    print('{}: {}'.format(resp.url, resp.status))
                    if resp.status == 200:
                        result = await resp.text()
                        if 'Documentation.html' in result:
                            async with aiofiles.open('asyncio_urls.txt', 'a+')as f:
                                await f.write(url+'\n')
            except Exception as e:
                print(e)

async def main(urls):
    async with aiomultiprocess.Pool()as pool:
        await pool.map(run,urls)
if __name__ == '__main__':
    urls = [x.strip() + '/phpmyadmin/index.php' for x in open('all_url.txt', 'r').readlines()]+[x.strip() + ':999/phpmyadmin/index.php' for x in open('all_url.txt', 'r').readlines()]
    start_time = time.time()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
    print('总共耗时: {} 扫描网址个数: {}'.format(time.time()-start_time),len(urls))