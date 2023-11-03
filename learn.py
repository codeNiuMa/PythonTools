import cv2
import numpy as np


def read2byte(path):
    '''
    图片转二进制
    path：图片路径
    byte_data：二进制数据
    '''
    with open(path, "rb") as f:
        byte_data = f.read()
    return byte_data


def byte2numpy(byte_data):
    '''
    byte转numpy矩阵/cv格式
    byte_data：二进制数据
    image : numpy矩阵/cv格式图片
    '''
    image = np.asarray(bytearray(byte_data), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


image_path = "img.jpg"
byte_data = read2byte(image_path)
image = byte2numpy(byte_data)
