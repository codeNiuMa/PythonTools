count = 1

with open(r'D:\txt\datawhole.csv', 'rw', encoding='utf-8') as f1:
    with open(r'D:\txt\data-little.txt', 'rw', encoding='utf-8') as f2:

        for t1 in f1.readlines():
            # t1 = str(t1)
            t11 = t1[t1.find('y'):t1.find('y') + 9]
            flag = False
            for t2 in f2.readlines():
                # t2 = str(t2)
                t22 = t2[t2.find('y'):t2.find('y') + 9]
                if t22 == t11:
                    flag = True
            if flag is False:
                print(str(count) + ' ' + t11+',')
                count += 1


