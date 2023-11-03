import time
from multiprocessing.dummy import Pool
from time import sleep


def op(url):
    print('start '+ url)
    sleep(2)
    print('end')

url_list = ['111',
            '222',
            '333',
            '444']

start = time.time()
# 实例化一个线程池
pool = Pool(3)
pool.map(op, url_list)
end = time.time()

print(str(end-start)+'s')

pool.close()  # 关闭线程池
pool.join()  # 等子线程结束再结束主线程

'''
start 111
start 222
start 333
end
end
start 444
end
end
4.028931379318237s
'''
