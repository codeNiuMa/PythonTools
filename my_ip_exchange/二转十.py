with open(r'C:/Users/SZY/Desktop/temp/1010.txt', 'r', encoding='utf-8') as f:
    with open("C:/Users/SZY/Desktop/temp/192.txt", "w") as w:
        for line in f.readlines():
            data = line.split('.')
            for single in data:
                # 转化十进制
                if single is not data[3]:
                    single = int(single, 2)
                    w.write(str(single)+'.')
                    print(single, end='.')
                else:
                    single = int(single, 2)
                    w.write(str(single))
                    print(single)
            w.write('\n')
        print(line, end='')