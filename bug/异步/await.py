import asyncio
import time

import requests


async def test2(i):
    print('test', i)
    # r = await other_test(i)
    await asyncio.sleep(2)
    r = requests.get(i)
    print(i, r)


async def other_test(i):
    re = requests.get(i)
    print(i)
    await asyncio.sleep(2)
    print(time.time() - start)
    return re


url = ["https://segmentfault.com/p/1210000013564725",
       "https://www.jianshu.com/p/83badc8028bd",
       "https://www.baidu.com/"]

loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(test2(i)) for i in url]
start = time.time()
loop.run_until_complete(asyncio.wait(task))
endtime = time.time() - start
print(endtime)
loop.close()
