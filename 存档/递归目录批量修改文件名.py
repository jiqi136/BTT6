
import re  #正则表达式

import os #处理电脑系统文件和目录

import random #随机数



递归文件名列表 = []
def 递归展开目录与文件(展开目录):
    子目录名与文件名列表 = os.listdir(展开目录)
    for 子目录名与文件名 in 子目录名与文件名列表:
        根目录的子目录名与文件名 = os.path.join(展开目录, 子目录名与文件名)

        if os.path.isdir(根目录的子目录名与文件名):# 判断是不是文件夹
            递归展开目录与文件(根目录的子目录名与文件名)
        递归文件名列表.append(根目录的子目录名与文件名)
    return 递归文件名列表

展开目录="F:/电影模板/下载种子目录4"
递归文件名列表=递归展开目录与文件(展开目录)

for 文件名 in 递归文件名列表:
    列表 = ["www.517ww.com", "www.117hm.com", "www.15bx.com", "www.hanmi520.com", "www.hanmi.cc"]

    for 符号 in 列表:
        if 符号 in str(文件名):
            修改后文件名 = str(文件名).replace(符号, '')
            os.rename(文件名, 修改后文件名)
            print('修改后文件名：', 修改后文件名)
