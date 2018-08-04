import os
import shutil
import re  #正则表达式
import fileinput


class 类一一集差查找未上传网盘的文件: #调用 类的模具 self.模具_数据库()

    def __init__(self):
        self.模具一一递归展开目录获取全部文件名()
        self.模具一一读取文本每一行()
        self.模具一一未上传网盘的文件集差并移动新目录()


    def 模具一一未上传网盘的文件集差并移动新目录(self):
        未上传网盘的文件集=self.目录文件名列表集-self.网盘文件名列表集

        print('未上传网盘的文件集数:', len(未上传网盘的文件集))
        for 未上传网盘的文件 in 未上传网盘的文件集:
            print('未上传网盘的文件:',未上传网盘的文件)
            未上传网盘的文件路径=r'F:/下载种子目录/上传网盘/打包文件/电影打包2/'+未上传网盘的文件
            移动目录的路径=r'F:\下载种子目录\下载保存\未上传网盘的文件'


            shutil.move(未上传网盘的文件路径,移动目录的路径)


    def 模具一一读取文本每一行(self):
        self.网盘文件名列表=[]

        for 网盘文件名与链接 in fileinput.input(r'F:\下载种子目录\ftp上传目录链接网页\合集打包电影.txt'):
            self.网盘文件名与链接 = str(网盘文件名与链接).replace(r"\n", "")
            self.模具一一读取文件名与http网页()

        self.网盘文件名列表集=set(self.网盘文件名列表)
        print('网盘文件名列表集', len(self.网盘文件名列表集))
        # 清空文本文件

    def 模具一一读取文件名与http网页(self):
        规则 = '(?<=blank">).{1,}(?=</a>)'  # 前后截取
        文本列表 = re.findall(规则, str(self.网盘文件名与链接))  # 提取
        if len(文本列表) == 0:
            return
        文件名 = 文本列表[0]


        self.网盘文件名列表.append(文件名)

    def 模具一一递归展开目录获取全部文件名(self):

        目标目录 = r"F:\下载种子目录\上传网盘\打包文件\电影打包2"
        目录文件名列表=[]
        for 根路径, 一层目录列表, 一层文件列表 in os.walk(目标目录, topdown=False):  # "."目录,topdown=False先子文件夹再到全层元组文件夹

            for 文件 in 一层文件列表:  # dirs遍历目录  files遍历文件
                目录文件名列表.append(文件)
        self.目录文件名列表集=set(目录文件名列表)


class 类_删除错的再复制电影目录: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.模具一一读取文本每一行()


    def 模具一一读取文本每一行(self):
        self.网盘文件名列表=[]

        for 文件名 in fileinput.input('C:/下载中转站/未上传.txt'):
            self.文件名 = str(文件名).replace(r"\n", "")
            self.模具一一复制文件()

    def 模具一一复制文件(self):
        复制文件路径=r'F:\下载种子目录\下载保存\旧电影'+'/'+self.文件名
        目录名=r'F:\下载种子目录\下载保存\未上传网盘的文件'



        shutil.copy(复制文件路径,目录名)
        print(复制文件路径, '复制文件:',目录名)


        # 清空文本文件
            


# 类=类一一集差查找未上传网盘的文件()
类B=类_删除错的再复制电影目录()





