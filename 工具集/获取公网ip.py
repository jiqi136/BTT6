# -*- coding:utf-8

from 网页采集公共库 import 类一一采集公共库# 导入模块

import re



class 类一一获取公网ip(类一一采集公共库): #调用 类的模具 self.模具一一数据库()
    def __init__(self):

        self.模具一一高位换头部信息()
      
        self.模具一一百度ip获取公网ip()


    def 模具一一百度ip获取公网ip(self):
        获取公网ip网址列表 = ['https://www.baidu.com/baidu?wd=ip&tn=monline_4_dg&ie=utf-8']

        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环
            返回网页一链接组列表 = self.模具一一gr无序网址列表请求返回网页内容(获取公网ip网址列表)

            try:  # 调用异常处理，应对易发生错误的位置
                百度ip返回网页一链接组 = 返回网页一链接组列表[0]
                百度ip返回网页内容 = 百度ip返回网页一链接组[0]


            except :  # 异常处理(,)as 异常原因
                print("列表分解异常")
                continue  # 跳过循环

            else:  # 必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
                条件循环 = 998
            # print('返回网页内容\n', 百度ip返回网页内容.text)
            文本=百度ip返回网页内容.text
            文本列表 = 文本.split("\n")
            for 行 in 文本列表:
                if '本机IP' in 行 and 'c-gap-right' in 行 and '/span' in 行:
                    ip行 = 行
                    # print("ip行",ip行)
                    break  # 结束循环
            规则 = '.{0,}&nbsp;'
            ip行 = re.sub(规则, '', ip行)  # 替换   ,count=0,re.S|re.I

            规则 = '<.{0,}'
            ip地址 = re.sub(规则, '', ip行)  # 替换   ,count=0,re.S|re.I

            规则 = '.{0,}>'
            ip城市 = re.sub(规则, '', ip行)  # 替换   ,count=0,re.S|re.I

            print("ip地址:", ip地址)
            print("ip城市:", ip城市)

if __name__ == '__main__':
    类=类一一获取公网ip()