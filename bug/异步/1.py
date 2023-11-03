import asyncio


async def func():
    print('jntm')

result = func()


# 生成一个事件循环
loop = asyncio.get_event_loop()
# 任务放到循环里
loop.run_until_complete(result)
# asyncio.run(result)  # python 3.7新功能
