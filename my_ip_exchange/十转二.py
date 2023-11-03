import os
import time

print('打开了十进制IP文件')
os.system(r'C:/Users/SZY/Desktop/temp/192.txt')
print('关闭了十进制IP文件')

with open(r'C:/Users/SZY/Desktop/temp/192.txt', 'r', encoding='utf-8') as f:
    with open("C:/Users/SZY/Desktop/temp/1010.txt", "w") as w:
        ip = f.readlines()

        # 辅助变量
        for line in ip:
            if line is not ip[-1]:
                a = 1
            else:
                a = 0

            # 输出源十进制IP

            print('十进制：', end='')
            print(line, end='')  # line后有一个换行,不end有两个换行

            # 输出二进制字符
            data = line.split('.')
            print('二进制：',end='')
            for single in data:
                # 转化二进制
                if single is not data[3]:
                    single = '{:08b}'.format(int(single))
                    w.write(str(single)+'.')
                    print(single, end='.')
                else:
                    single = '{:08b}'.format(int(single))
                    w.write(str(single))
                    if a:
                        print(single)
                    else:
                        print(single, end='')

            # 文件中换行
            w.write('\n')

os.startfile('C:/Users/SZY/Desktop/temp/1010.txt')