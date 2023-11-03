import os

a = os.popen('dir C:\Users\SZY')

print(a.read())