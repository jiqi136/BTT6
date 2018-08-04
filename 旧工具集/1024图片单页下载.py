

import requests
import os #处理电脑系统文件和目录
import re
from lxml import etree #解析与定位网页


def 模具_收藏图片(帖子内容html):
    规则 = '//*[@id="main"]/div[3]/table/tbody/tr[1]/th[2]/table/tbody/tr/td/h4/text()'
    规则 = str(规则).replace("/tbody", "")
    帖子标题列表 = 帖子内容html.xpath(规则)


    规则 = "[\',？,。]{1}"
    图片下载目录=re.sub(规则,'',str(帖子标题列表))

    保存目录路径 ='D:\\桌面\\下载\\目录\\'
    图片下载目录 = str(保存目录路径).replace("目录", 图片下载目录)
    创建图片下载目录 = str(图片下载目录).strip('\\')

    if not os.path.exists(创建图片下载目录):  # 必有条件选择，否则出错
        os.makedirs(创建图片下载目录)  # makedirs 创建多级目录文件夹，mkdir创建一个文件夹


    规则 = '//*[@id="main"]/div[3]/table/tbody/tr[1]/th[2]/table/tbody/tr/td/div[4]//@src'
    规则 = str(规则).replace("/tbody", "")
    图片下载地址列表 = 帖子内容html.xpath(规则)
    if len(图片下载地址列表)==0:
        print("提取图片下载地址失败")
        input('请按任意键 退出')
        return





    for 图片下载地址 in 图片下载地址列表:
        if 'to/2017/12/03/' in 图片下载地址:
            continue  # 跳过当前循环，继续进行下一轮循环
        返回图片下载内容 = requests.get(图片下载地址,timeout=10)

        规则 = ".{0,}/"
        图片名 = re.sub(规则, '', str(图片下载地址))
        #图片名 = str(计数器) + '.jpg'
        目录与种子名 = str(图片下载目录) + str(图片名)
        with open(目录与种子名, 'wb') as fout:
            fout.write(返回图片下载内容.content)
            fout.close()
            print('已下载', 图片名)
    print('图片下载完成，保存在:', 创建图片下载目录)
    os.startfile(str(创建图片下载目录))  # 打开目录


var = 1
while var == 1:
#打开的网址='http://cl.m7y.xyz/htm_data/7/1801/2955164.html'
    打开的网址=input('请输入要下载的图片网址:\n')
    print('正在下载........')
    返回网页内容 = requests.get(打开的网址,timeout=10)
    返回网页内容.encoding = "gbk"
    帖子内容html = etree.HTML(返回网页内容.text)  # (encoding='utf-8')

    模具_收藏图片(帖子内容html)