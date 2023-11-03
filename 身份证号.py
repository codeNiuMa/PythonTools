# # 打开txt文件
# with open('./data/身份证号.txt', 'r', encoding='utf-8') as file:
#     # 逐行读取文件内容
#     for line in file:
#         # 剥离行末尾的空白字符（如换行符）
#         line = line.strip()
#         # 检查行的最后5个字符是否都是数字或字母
#         if len(line)>5 and line[-5:].isdigit():
#             # 如果是，打印该行
#             print(line)
#         if line[-1:] == "X":
#             print(line)

# # 打开txt文件
# with open('./data/身份证号-1.txt', 'r', encoding='utf-8') as file:
#     # 逐行读取文件内容
#     for line in file:
#         # 输入字符串
#         # 使用find()方法查找句号的索引
#         index = line.find(".")
#         if index != -1:
#             print(line[index+1:].strip().replace(" ", ""))
#         else:
#             print(line.strip().replace(" ", ""))


# # # 打开txt文件
# with open('./data/身份证号-2.txt', 'r', encoding='utf-8') as file:
#     first_digit_index = None
#     for line in file:
#         for index, char in enumerate(line):
#             if char.isdigit():
#                 first_digit_index = index
#                 break  # 找到第一个数字后，退出循环
#         new_string = line[:first_digit_index] + ',' + line[first_digit_index:]
#         print(new_string.strip())

# 打开CSV文件
import pandas as pd

# 读取CSV文件
df = pd.read_csv('./data/姓名身份证.csv')

# 取出每一列数据
column_name = df.columns[1]
column_data = df[column_name]
for i in list(column_data):
    if len(i) != 18:
        print(i)








