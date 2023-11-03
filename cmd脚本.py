import re
import subprocess

import os
import shutil

# 定义文件夹路径
from time import sleep

folder_paths = ['./tmp_frames', './out_frames']
videoname = 'input.mp4'

for folder_path in folder_paths:
    # 检查文件夹是否存在
    if os.path.exists(folder_path):
        # 如果文件夹存在，清空文件夹内容
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print(f"无法删除 {file_path}: {e}")
        print(f"==============文件夹 {folder_path} 已清空。================")

    else:
        # 如果文件夹不存在，创建新文件夹
        os.makedirs(folder_path)
        print(f"==============文件夹 {folder_path} 已创建好。================")

    sleep(1)



# 定义要执行的CMD命令
cmd1 = f'ffmpeg -i {videoname} -qscale:v 1 -qmin 1 -qmax 1 -vsync 0 tmp_frames/frame%08d.png'
cmd2 = 'realesrgan-ncnn-vulkan.exe -i tmp_frames -o out_frames -n realesr-animevideov3 -s 2 -f jpg'
cmd3 = f'ffmpeg -i {videoname}'

# 使用subprocess执行CMD命令
try:
    subprocess.run(cmd1, shell=True, check=True)
    print('=================提取视频帧完成==============')
    subprocess.run(cmd2, shell=True, check=True)
    print('================ 修复视频帧完成=====================')

    result = subprocess.run(cmd3, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print("命令执行成功！")

except subprocess.CalledProcessError as e:
    print("==================命令执行失败：", e)
    # 获取错误输出
    stderr = e.stderr

    stderr = stderr.decode('utf-8')
    print('stderr', stderr)
    text = stderr

    # 提取 "fps" 之前的数字

    fps_match = re.search(r'(\d+\.\d+) fps', text)

    if fps_match:
        fps_value = fps_match.group(1)
        print(f"fps: {fps_value}")
    else:
        fps_value = '23.98'


    cmd5 = f'ffmpeg -r {fps_value} -i out_frames/frame%08d.jpg -i {videoname} -map 0:v:0 -map 1:a:0 -c:a copy -c:v libx264 -r {fps_value} -pix_fmt yuv420p output.mp4'

    # subprocess.run(cmd4, shell=True, check=True)
    subprocess.run(cmd5, shell=True, check=True)



de = input('是否删除缓存文件？y/n')
if de is 'y':
    for folder_path in folder_paths:
        # 检查文件夹是否存在
        if os.path.exists(folder_path):
            # 如果文件夹存在，清空文件夹内容
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"无法删除 {file_path}: {e}")
            print(f"==============文件夹 {folder_path} 已清空。================")

        else:
            # 如果文件夹不存在，创建新文件夹
            os.makedirs(folder_path)
            print(f"==============文件夹 {folder_path} 已创建好。================")
        sleep(1)