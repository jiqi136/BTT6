# -*- coding:utf-8

import re  # 正则式
import os  # 本地操作
import random  # 随机
import shutil  # 移动复制文件目录
import win32api  # 操作本地文件
from PIL import Image, ImageDraw



class 类一一图片添加颜色点: #调用 类的模具 self.模具一一数据库()
    def __init__(self):

        self.模具一一递归展开目录与文件()


    def 模具一一递归展开目录与文件(self):
        目标目录=r"C:\下载中转站\图3"

        for 根路径, 一层目录列表, 一层文件列表 in os.walk(目标目录, topdown=False):  # "."目录，topdown=False先子文件夹再到全层元组文件夹

            for 纯文件名 in 一层文件列表:  # dirs遍历目录  files遍历文件
                self.文件路径 = os.path.join(根路径, 纯文件名)  # 合并成为 完全的地址
                print('文件路径',self.文件路径)
                self.模具一一在给定的坐标点上画一些点()

    def 模具一一在给定的坐标点上画一些点(self):
        随机A = random.randrange(0, 255)
        随机B = random.randrange(0, 255)
        随机C = random.randrange(0, 255)
        随机D = random.randrange(0, 255)
        随机E = random.randrange(0, 255)
        随机F = random.randrange(0, 255)
        随机G= random.randrange(0, 255)


        fp = open(self.文件路径, "rb");
        处理的图片 = Image.open(fp)
        # 处理的图片 = Image.open(图片位置)

        绘图 = ImageDraw.Draw(处理的图片)
        绘图.point([(随机A, 随机B), (随机C, 随机D), (随机E, 随机F)], fill=(随机G, 随机A, 随机D))


        处理的图片.save(self.文件路径)  # 另存为
        del 绘图
类=类一一图片添加颜色点()