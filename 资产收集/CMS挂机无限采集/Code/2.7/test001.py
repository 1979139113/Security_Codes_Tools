# coding:utf-8
# import requests
# url = 'http://dev.mumayi.com/Inc/NoSqlHack.Asp'
# md5s = 'd41d8cd98f00b204e9800998ecf8427e'
# import hashlib
# r = requests.get(url)
#
# md5 = hashlib.md5()
# md5.update(r.content)
# rmd5 = md5.hexdigest()
# print(rmd5)
#rcontent = str(r.content)

# md5.update(rcontent)
# dmd5 = md5.hexdigest()
# print(dmd5)
import asyncio
import aiohttp
import time

start = time.time()

async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=5) as resp:
            result = (await resp.read())
            return result

async def request(url):
    result = await get(url)
    print('Get response from', url, 'Result:', result)


urls = [
'http://www.php.cn',
'http://www.phphtm.com',
'http://www.thinkphp.cn',
'http://www.phpboke.com',
'https://www.52pojie.cn',
'http://www.douco.com'
]

tasks = [asyncio.ensure_future(request(url=_)) for _ in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
