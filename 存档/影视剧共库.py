
import asyncio # import 异步框架
import aiomysql  # import 异步数据库
import aiohttp # import 异步浏览器
import requests  # 人性化的 浏览器
import re  # 正则表达式
import time  # 时间
import os  # 处理电脑系统文件和目录
import pymysql  # mysql数据库
import random  # 随机数
from lxml import etree#解析与定位网页
import datetime  # 时间


class 类_共用库:  # 调用 类的模具 self.模具_数据库()
    def __init__(self):
        print('夜深了223')


    def 模具_符号清洗(self ,原文):
        列表 = ["[", "]", "\'", "\"", ":", "*", "/", "\\", "#", "\"", "?", ".", "\'", "'", "\'", "'", '', ',', ':', ':',
              '！', '\\n', '\n', '>', '<', '%', '?', ':', '｜', '|', '！'  ]# 英中字符
        for 符号 in 列表:
            原文 = str(原文).replace(符号, '')
        return 原文  # 返回


    def 模具_正文清洗(self):
        # ===========先去掉相同换行的字符=====================
        正文 =self.正文
        正文 = str(正文).replace("\'\\n-->\\n\\n\',", "")
        正文 = str(正文).replace("\\n", "")
        正文 = str(正文).replace("\\u3000", "")
        # ===========正文杂乱字符至行尾的整行处理===============
        规则列表 =['(?<=◎BT).{10,30}(?=\', \')', '(?<=上季).{1,}(?=\', \')', '(?<=迅雷).{1,}(?=\', \')', '(?<=百度网盘).{1,}(?=\', \')' ,'(?<=网盘下载).{1,}(?=\', \')', '(?<=http://pan.baidu.com).{1,}(?=\', \')',
                '(?<=https: /pan.baidu.com).{1,}(?=\', \')','(?<=ed2k:// ).{1,}(?=\', \')'
            , '(?<=https://yunpan.cn).{1,}(?=\', \')', '(?<=http://yunpan.cn).{1,}(?=\', \')',
                '(?<=ftp://).{1,}(?=\', \')','(?<=http:// www.bt).{1,}(?=\', \')'
            ,'(?<=magnet) .{1,}(?=\', \')', '(?<=磁力).{1,}(?=\', \')',
                '(?<=本帖最后由).{10}(?=\', \')', '(?<=迅雷).{1,}(?=\', \')']

        for 规则 in 规则列表:  # 范围 range

            正文 = re.sub(规则, '', str(正文))
        # ===========替换行尾,进行换行=====================
        正文 = str(正文).replace("\', \'", "\n")
        # ===========正文杂乱字符的处理===============
        杂乱字符列表=["◎BT","上季" , "迅雷","百 度网盘", "网盘下载 ","http ://pan. baidu.com","https://pan .baidu.com","ed2k://",
                  "https://yunpan.cn","http://yunp an.cn","ftp://","ht tp://www. bt","磁力","magnet ","本帖 最后由","\\x a0",
                "\'","\"", \
                  " \\","\"", "ufe ff",]

        for 字符 in 杂乱字符列表:  # 范围 range

            正文 = str(正文).replace(字符, "")

        self.正文 = str(正文)

    def 模具_种子名清洗(self):
        种子名规则 = '\[bt.{1,}\]'
        种子名 = re.sub(种子名规则, '', str(self.种子名))
        种子名规则 = '\.bt.{1,}torrent'
        种子名 = re.sub(种子名规则, '.torrent', str(种子名))
        列表 = ["\'", "\"", ":", "*", "/", "\\", "#", "\"", "?",':', '?', ':', '｜', '|', '！']
        for 符号 in 列表:
            种子名 = str(种子名).replace(符号, '')

        self. 种子名=种子名

    def 模具_帖子正文清洗(self):
        # 规则 = '(?<=648542).{1,}(?=BAIDU_CLB_SLOT_ID)'

        一楼内容 = str(self.帖子内容)
        规则 = '(?<=643755).{1,}(?=648546)'
        一楼内容 = re.findall(规则, str(一楼内容), re.S)
        规则列表 = ['(?<=◎BT).{1,300}(?=a>)', '(?<=上季).{1,}(?=</p>)', '(?<=<a href).{1,}(?=a>)',
                '(?<=</script>).{1,}(?=</script>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=百度网盘).{1,}(?=</p>)',
                '(?<=网盘下载).{1,}(?=</p>)', '(?<=http://pan.baidu.com).{1,}(?=</p>)',
                '(?<=https://pan.baidu.com).{1,}(?=</p>)',
                '(?<=ed2k://).{1,}(?=</p>)', '(?<=https://yunpan.cn).{1,}(?=</p>)',
                '(?<=http://yunpan.cn).{1,}(?=</p>)', '(?<=ftp://).{1,}(?=</p>)',
                '(?<=本帖).{1,50}(?=编辑)', '(?<=<i>).{1,}(?=i>)', '(?<=magnet).{1,}(?=</p>)',
                '(?<=磁力).{1,}(?=</p>)', '(?<=本帖最后由).{10}(?=</p>)', '(?<=迅雷).{1,}(?=</p>)', '(?<=链接).{1,300}(?=</p>)']
        for 规则 in 规则列表:
            一楼内容 = re.sub(规则, '', str(一楼内容))

        # ========字符替换=========
        列表 = ["迅雷", "百度网盘", "网盘下载", "http://pan.baidu.com", "https://pan.baidu.com", "ed2k://", "https://yunpan.cn",
              "http://yunpan.cn", "ftp://", "本帖最后由", "上季", "<scripttype=\"text/javascript\">BAIDU_CLB_SLOT_ID=\"",
              "<script type=\"text/javascript\">BAIDU_CLB_SLOT_ID = ",
              "◎BT", "之家整理", "</script>", "\'\";", "<ahrefa>", "a>", "BT之家", "本帖编辑", "<i>i>", "\\u3000", "\\n", "链接"]
        for 符号 in 列表:
            一楼内容 = str(一楼内容).replace(符号, '')
        一楼内容 = str(一楼内容).strip('\'')
        if 'src=\"/upload' in 一楼内容:
            一楼内容 = str(一楼内容).replace("/upload", "http://btbtt.co/upload")
        if 'HQC' in 一楼内容:
            次数 = 一楼内容.count('src=')
            if int(次数) > 1:
                规则 = '(?<=<img).{1,}(?=<img)'
                一楼内容 = re.sub(规则, '', str(一楼内容), count=1)
                一楼内容 = str(一楼内容).replace("<img", "")
                一楼内容 = str(一楼内容).replace("src", "<img src")
                一楼内容 = str(一楼内容).replace("HQC小组", "")
                一楼内容 = str(一楼内容).replace("[]的所有压制整合作品,均为小组成员合力精心制作.欢迎转载,但禁止私自取消小组的专用印记,需注明出处.", "")
        一楼内容 = str(一楼内容).replace("\'", "")
        self.帖子内容=str(一楼内容)

    def 模具_提取一楼种子名进行过滤(self):
        if '个附件' in str(self.帖子内容html).xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[1]/td[1]/text()'):
            一楼种子名列表 = str(self.帖子内容html).xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[2]/table/tr[*]/td[1]/a/text()')
            种子名列表文本 = str(一楼种子名列表)
            if '謦灵 风软'or 'ww w. 'or'.c om'or '.net' in 种子名列表文本:
                print('标记其它网站,跳过循环')
                print('=====================')
                self.模具_保存过滤帖子网址()
                self.循环结束=0
                return  # 返回None空值,跳过循环
        # 电影的过滤
        # 謦灵风软www.|.com|先版|鲜版|鲜版|删减版|TS|TC|抢先|清晰|公映版|网盘下载|电驴|迅雷|[email /span

    def 模具_短标题的再次清洗(self):
        短标题 = str(self.短标题).replace("] ", ']')
        if '][' in str(短标题):
            规则 = '(?<=\]\[).{1,}'
            短标题 = re.findall(规则, str(短标题))
        if '/' in str(短标题):
            # 规则5 = '(?<=/).{1,}'
            # 短标题4 = re.sub(规则4, '', str(短标题3))
            规则 = '/{1}'
            短标题 = re.sub(规则, '%', str(短标题), count=1)
            规则 = '.{1,}(?=%)'
            短标题 = re.findall(规则, str(短标题))
        if '.' in str(短标题):
            规则 = '(?<=\.).{0,}'
            帖子标题 = re.sub(规则, '', str(短标题))
            帖子标题 = str(帖子标题).replace(".", '')
        elif ' ' in str(短标题):
            # 规则4 = '.*(?=)'
            规则 = '\s{1}'
            短标题 = re.sub(规则, '%', str(短标题), count=1)
            规则 = '.{1,}(?=%)'
            短标题 = re.findall(规则, str(短标题))

        if '第'and '季' in str(短标题):

            规则 = '.{1,}(?=第)'
            短标题 = re.findall(规则, str(短标题))
        self.短标题=短标题

    def 模具_长标题(self):
        长标题规则 = '(?<=\]\[).{1,}'
        长标题 = re.findall(长标题规则, str(self.帖子标题))
        长标题 = str(长标题).replace("\'", "")
        if '][更' in str(长标题):
            规则 = '更\d{1,}集'
            长标题 = re.sub(规则, '', str(长标题))
        # 符号清洗
        长标题 = self.模具_符号清洗(长标题)

        assert len(长标题) ==0 , '长标题为空'
        # 长标题 = str(self.短标题)
        print('长标题', 长标题)
        self.帖子标题=长标题


