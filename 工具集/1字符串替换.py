
import re
import os
import time

def 模具一一文件翻译PY语言():
    文件路径= input("粘贴修改文件路径：\n")
    var = 1
    while var == 1:  # 表达式永远为 true的无限循环 否则
        文本=open(文件路径, 'r', encoding='UTF-8')
        文本2 = 文本.read()  # read() #读取

        文本.close()

        #   与种子名清洗 冲突，弃用  '（':'(','）':')',
        符号字典 = { '=':'=','。':'.','？':'?', '｛':'{','｝':'}',
             '……':'^','，':',','：':':','%':'%', '（':'(','）':')', '【':'[','】':']',
              '“': '\"','‘': '\'','’': '\'','编码': 'encoding=\'UTF-8\'','编码G': 'encoding=\'gbk\''}#'   ,'时间':'time'
        py语法字典= {'输入':'input','时间':'time','返回':'return#返回','异常':'except #异常','断言':'assert #断言','结束':'assert #结束','否则':'else:  #否则',
             '文本前后':'strip(\'\')','以':'with','文本列表':'文本列表 = 文本.split("n")','列表最大值':'max(列表) #列表最大值 ',
              '范围':'range','从':'from','等待':'time.sleep(1) # 等待',
             '不换行':'end','自用':'if __name__ == \'__main__\':',
              '例':'self','浮点数':'float','打印':'print(\'：\',)','类型': 'print(\'类型:\',type(aaa))',
                '文本': 'str()', '整数': 'int()', '点数': 'float()', '集合': 'set()', '列表转': 'list()',
                 '结束循环':'break # 结束循环','跳过循环':'continue#跳过循环','全局变量':'global','局域变量':'enclosing ','前后截取':'规则=\'(?<=前文本).{1,}(?=后文本)\''}
        结构字典= { '库2': """
# -*- coding:utf-8
import grequests  # 并发协程
import requests  # 网页浏览
import re  # 正则式
import time  # 时间
import datetime  # 时间
import os  # 本地操作
import pymysql  # 数据库
import random  # 随机
from lxml import etree  # 网页分析
import shutil  # 移动复制文件目录
from lxml import html  # 网页分析
from selenium import webdriver  # 浏览的驱动
import win32api  # 操作本地文件
import asyncio, aiohttp # 异步浏览""",
            '如果2':"""
                if '' in (): #  break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环   
                    
                elif '' in str(字符):# 其它条件。
                    
                else:# 否则
                    """
        , '遍历2': """ 
        for 字符 in :  # 范围 range"""
        , '条件循环2': """
        条件循环 = 1
        while 条件循环 == 1:  # 条件循环  break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环   
            
        else:  # 否则
            """
        , '代入2': """{}.format()#不换行 end="" """
        , '安装2': """pip install """
        , '尝试2': """
            try:  #调用异常处理，应对易发生错误的位置
   
    
        except (,)as 异常原因 :#异常处理
            print(异常原因 )
     
        else:#必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。"""
        , '替换2': """文本 =re.sub(规则, 替换的文本, str(原文本))#替换   ,count=0,re.S|re.I"""
        , '替换3': """文本 = str(原文本).replace("25", "120") #替换   , 1) 次数 1"""
        , '提取2': """
        规则=''
        文本列表 = re.findall(规则, str(原文本))  # 提取列表
             文本 = 文本列表[0]"""
        , '类2': """
class 类一一: #调用 类的模具 self.模具一一数据库() 
    def __init__(self):
        self.模具一一换头部信息()
        
            """
        , '模具2': """
    def 模具一一浏览器(self):"""
    , '创建目录2':"""
    创建种子目录 = str(种子目录).strip('/')
        if not os.path.exists(创建种子目录):  # 必有条件选择，否则出错
            try:
                os.makedirs(创建种子目录)  # makedirs 创建多级目录文件夹，mkdir创建一个文件夹
            except (FileNotFoundError,OSError) as 异常原因:
                 print('异常原因',异常原因)
                 continue # 跳过当前循环，继续进行下一轮循环 """
            , '移动目录2': """            try:
                os.renames(旧目录, 新目录)
                print("成功修改：",新目录)
            except (FileNotFoundError,FileExistsError,PermissionError):
                continue  # 跳过当前循环，继续进行下一轮循环"""
            , '展开目录2': """ fileList = os.listdir(旧目录上层)  # 获取path目录下所有文件
    for filename in fileList:
        失散文件 = os.path.join(旧目录上层, filename)  # 获取path与filename组合后的路径
        if os.path.isdir(失散文件):  # 如果是目录
            continue  # 跳过当前循环，继续进行下一轮循环
        else:
            try:
                shutil.move(失散文件, 旧目录)#移动文件
                print("完成回填目录：", 旧目录)
                文件数列表.append(失散文件)
            except (shutil.Error) as 异常原因:
                print("失败：", 异常原因)
                print("回填目录失败：", 旧目录)
                continue  # 跳过当前循环，继续进行下一轮循环"""
        , '全展开目录2': """ 
        for root, dirs, files in os.walk("F:\电影模板\下载种子目录2\电视剧", topdown=False):  # "."目录，topdown=False先子文件夹再到元组文件夹
            for name in dirs:  # dirs遍历目录  files遍历文件
                name2 = 模具一一符号清洗(name)
                旧目录 = os.path.join(root, name)# 合并成为 完全的地址
                新目录 = os.path.join(root, name2)"""
        , '列表增2':"""短标题列表.append(短标题)"""
        , '随机数2': """从给定的范围返回随机项=random.randrange(100, 1000)"""
        , '读取每行2': """
         import fileinput
    空目录列表 = []
    for 旧目录 in fileinput.input("D:\桌面\空的旧目录列表.txt"):
        旧目录 = str(旧目录).replace("成功空的创建旧目录 ", "")
        旧目录 = str(旧目录).replace(r"\n", "")
        空目录列表.append(旧目录)"""
        , '读取文件2': """
        文本 = open("E:\PY学习文件\PyCharm文件\测试.py", 'r')# 读取编码utf8的文件, encoding='UTF-8'
    文本2 = 文本.read()  # read() 读取  write(返回网页请求内容.content)写入
    文本.close()"""
        , '下载文件2': """
        返回网页请求内容='r'
    种子目录='r'
    种子名='r'
    目录与种子名 = str(种子目录) + str(种子名)
    with open( 目录与种子名, 'wb') as fout:#返回值 随后 被赋值给as后面的变量
        fout.write(返回网页请求内容.content)  #  read() #读取
        fout.close()
        print('完成下载', 目录与种子名)"""
        , '数据库增加2': """    
    def 模具一一插入数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql =\"\"\"INSERT INTO 已下载内容页网址(已下载内容页网址)
                       VALUES ('%s')\"\"\" % (各帖子链接)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()"""
        , '数据库查找2': """ 
    def 模具一一查找数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql =\"\"\"SELECT * FROM 中文表 
                    WHERE B列=10086;\"\"\" #数值条件查找后选取
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        数据库记录列表 = cursor.fetchall()
         # 关闭数据库连接
        db.close()"""
    , '数据库更改2': """
    def 模具一一更改数据库(self):
        db = pymysql.connect("localhost", "root", "", "综合影视剧", charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql =\ "\"\"UPDATE 中文表 
            SET B列='方格数据2', D列='方格数据4' #想要修改的内容
            WHERE A='方格数据1';\"\"\" #省略了 WHERE 子句没有具体条件的更新，将会修改表中所有 列的 数据
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()"""
        , '解析网页2': """
        帖子内容html = etree.HTML(返回网页内容.text)
        规则= "//*[@id=]/div/table[2]/tr[1]/td[3]/div[1]/h2/text()"
        规则 = str(规则).replace("/tbody", "")
        图片下载地址列表 = 帖子内容html.xpath(规则)"""
        , '如e果2': """time"""
            }#     , '如r果2':"""time"""
        for 键值 in 符号字典:
            规则 = r"{}".format(键值)
            #规则 = str(规则).replace("规则", 键值)
            文本2 =re.sub(规则,符号字典[键值], str(文本2))
        for 键值 in 结构字典:
            规则 = r"{}".format(键值)
            # 规则 = str(规则).replace("规则", 键值)
            文本2 = re.sub(规则, 结构字典[键值], str(文本2))
        for 键值 in py语法字典:
            规则 = r"{}2".format(键值)
            # 规则 = str(规则).replace("规则", 键值)
            文本2 = re.sub(规则, py语法字典[键值], str(文本2))


        文本2 = str(文本2).replace("+", "+")
        文本2 = str(文本2).replace("-", "-")
        文本2 = str(文本2).replace("*", "*")
        文本2 = str(文本2).replace("｜", "\\")

        with open(文件路径, 'w',encoding=("UTF-8")) as fout:  # 返回值 随后 被赋值给as后面的变量
            fout.write(文本2)  # read() #读取
            fout.close()
            print('完成修改',文件路径)
        等待用户输入 = input("======按下确认键enter 后 继续修改======\n\n")
        #time.sleep(10)  # 等待



模具一一文件翻译PY语言()








