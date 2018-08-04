# -*- coding:utf-8

import re  # 正则式
import os  # 本地操作
import random  # 随机
import shutil  # 移动复制文件目录
import win32api  # 操作本地文件
from PIL import Image, ImageDraw
#import Matplotlib


def 图片对角线():
    图片位置=r"C:\snapshot20170405002519.jpg"
    处理的图片 = Image.open(图片位置)
    绘图 = ImageDraw.Draw(处理的图片)
    绘图.line((0, 0) + 处理的图片.size, fill=128)
    绘图.line((0, 处理的图片.size[1], 处理的图片.size[0], 0), fill=128)
    处理的图片.show()

    del 绘图

def 在开始和结束角度之间绘制一条弧():
    图片位置 = r"C:\snapshot20170405002519.jpg"
    处理的图片 = Image.open(图片位置)
    绘图 = ImageDraw.Draw(处理的图片)
    绘图.arc((0, 0, 200, 200), 0, 90, fill=(255, 0, 45))
    绘图.arc((300, 300, 500, 500), 0, -90, fill=(0, 255, 85))
    绘图.arc((200, 200, 300, 300), -90, 0, fill=(0, 0, 55))
    del 绘图
    处理的图片.save('c:/dog2.jpg')  # 另存为
    处理的图片.show()

def 在给定的坐标点上画一些点():
    图片位置 = r"C:\snapshot20170405002519.jpg"
    fp = open(图片位置, "rb");
    处理的图片 = Image.open(fp)
    #处理的图片 = Image.open(图片位置)
    print('处理的图片：',处理的图片)
    绘图 = ImageDraw.Draw(处理的图片)
    绘图.point([(0, 0), (100, 150), (110, 50)], fill=(255, 0, 0))

    绘图.point([0, 10, 100, 110, 210, 150], fill=(0, 255, 0))

    绘图.point([0, 10, 105, 110, 215, 150], fill=(0, 0, 255))
    绘图.point([0, 10, 109, 110, 218, 150], fill=(0, 255, 85))
    绘图.point([0, 10, 105, 110, 218, 150], fill=(0, 255, 0))
    绘图.point([0, 10, 108, 110, 215, 150], fill=(0, 255, 0))


    处理的图片.show()#显示图片，须 关闭后才能下一步操作
    处理的图片.save('c:/dog.jpg') #另存为
    del 绘图

def 添加字符串():
    图片位置 = r"C:\snapshot20170405002519.jpg"
    处理的图片 = Image.open(图片位置)
    绘图 = ImageDraw.Draw(处理的图片)
    字符串='ffe过热过'(encoding='UTF-8')

    绘图.text((10, 10), 字符串, fill=(255, 0, 0))

    处理的图片.show()
def 绘制图像点和线():
    图片位置 = r"C:\snapshot20170405002519.jpg"
    处理的图片 = Image.open(图片位置)
    im = array(处理的图片)

    imshow(im)

    # 一些点
    x = [100, 100, 400, 400]
    y = [200, 500, 200, 500]

    # 使用红色星状标记绘制点
    plot(x, y, 'r*')

    # 绘制连接前两个点的线
    plot(x[:2], y[:2])

    # 添加标题,显示绘制的图像
    title('Plotting: "empire.jpg"')
    show()
#图片对角线()
在开始和结束角度之间绘制一条弧()
#在给定的坐标点上画一些点()
#添加字符串()
#绘制图像点和线()