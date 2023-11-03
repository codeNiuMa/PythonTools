import os

dir = 'G:/'


import random
def add():
    # 生成一个包含10个在0到100之间随机整数的列表
    random_list = [i+1 for i in range(len(os.listdir(dir)))]
    print(random_list)
    random.shuffle(random_list)

    print(random_list)

    cnt=0
    for filename in os.listdir(dir):
        src_file_path = os.path.join(dir, filename)  # 拼接完整的源文件路径
        new = str(random_list[cnt]) + '-' + filename
        dst_file_path = os.path.join(dir, new)  # 拼接完整的目标文件路径
        os.rename(src_file_path, dst_file_path)  # 使用完整的文件路径进行重命名操作
        cnt += 1
        print(new)



import re
import os
def remove():
    def remove_numbers_from_filename(filename):
        # 使用正则表达式匹配文件名中的数字部分
        pattern = re.compile(r'^\d+\s*-?\s*')
        new_filename = re.sub(pattern, '', filename)
        return new_filename

    # 获取文件夹中的所有文件
    folder_path = 'G:/'
    file_list = os.listdir(folder_path)

    # 遍历文件列表并重命名文件
    for filename in file_list:
        new_filename = remove_numbers_from_filename(filename)
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(new_filename)

if __name__ == '__main__':
    remove()
    add()
