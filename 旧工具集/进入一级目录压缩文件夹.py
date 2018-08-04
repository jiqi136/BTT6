

import os #处理电脑系统文件和目录
import time #时间

import zipfile
import unrar
import rarfile
import shutil
import re  #正则表达式


class 类_进入一级目录压缩文件夹并移动到文件夹: #调用 类的模具 self.模具_数据库()
    def __init__(self):
        self.模具_目标目录展开子目录()

    def 模具_目标目录展开子目录(self):

        目标目录 = r'F:\电影模板\下载种子目录4\动漫'
        self.移动文件目录前缀 = r'F:\电影模板\压缩-下载种子\动漫'+'\\'
        self.打包的移动文件目录名 = r'F:\电影模板\压缩-下载种子\动漫打包'

        子目录列表与文件列表 = os.listdir(目标目录)  # 分离出目录列表与文件列表
        for 子目录或文件 in 子目录列表与文件列表:
            根目录的子目录或文件路径 = os.path.join(目标目录, 子目录或文件)
            if os.path.isdir(根目录的子目录或文件路径):  # 判断为 目录 文件夹

                self.子目录 = 根目录的子目录或文件路径
                self.移动文件目录名=self.移动文件目录前缀+str(子目录或文件)

                self.模具_判断子目录元组目录列表个数()


    def 模具_判断子目录元组目录列表个数(self):
        print('==================')
        for 根路径, 元组目录列表, 文件列表 in os.walk(self.子目录):  # "."目录,topdown=False先子文件夹再到元组文件夹
            print('一层元组目录列表:', 元组目录列表)
            if len(元组目录列表) != 0:  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环

                元组目录列表与文件列表 = os.listdir(self.子目录)  # 分离出目录列表与文件列表
                for 子目录或文件 in 元组目录列表与文件列表:
                    元组目录的子目录或文件路径 = os.path.join(self.子目录, 子目录或文件)# 合并为完全 的 访问路径
                    if os.path.isdir(元组目录的子目录或文件路径):  # 判断为 目录 文件夹
                        self.目录路径=元组目录的子目录或文件路径

                        self.模具_压缩()
                        self.模具_创建移动文件目录()
                        try:

                            移动文件名 = str(self.压缩目录名).replace("下载种子目录4", "压缩-下载种子")  # 替换   , 1) 次数 1
                            if not os.path.exists(移动文件名):  # 必有条件选择,否则出错
                                shutil.move(self.压缩目录名, self.移动文件目录名)
                            else:  # 否则
                                os.unlink(移动文件名)
                                shutil.move(self.压缩目录名, self.移动文件目录名)
                            print('移动至目录:', self.移动文件目录名)

                        except (FileNotFoundError, OSError) as 异常:
                            print('异常# 跳过当前循环,继续进行', 异常)
                            continue  # 跳过当前循环,继续进行下一轮循环


                    else:  # 否则 为文件
                        文件路径 = 元组目录的子目录或文件路径
                        self.模具_创建移动文件目录()

                        移动文件名 = str(文件路径).replace("下载种子目录4", "压缩-下载种子")  # 替换   , 1) 次数 1
                        if not os.path.exists(移动文件名):  # 必有条件选择,否则出错
                            try:
                                shutil.copy(文件路径, self.移动文件目录名)
                                print(文件路径, '复制文件:', self.移动文件目录名)
                            except (FileNotFoundError, OSError) as 异常:
                                print('异常# 跳过当前循环,继续进行', 异常)
                                continue  # 跳过当前循环,继续进行下一轮循环
                        else:  # 否则
                            print('复制文件已存在:跳过当前文件')
                            continue  # 跳过当前循环,继续进行下一轮循环


            else:  # 否则
                if len(文件列表) != 0:
                    self.目录路径 = self.子目录
                    self.模具_压缩()

                移动文件名 = str(self.压缩目录名).replace("下载种子目录4\动漫", "压缩-下载种子\动漫打包")  # 替换   , 1) 次数 1
                try:
                    if not os.path.exists(移动文件名):  # 必有条件选择,否则出错
                        shutil.move(self.压缩目录名, self.移动文件目录名)
                    else:  # 否则
                        os.unlink(移动文件名)#删除原来 文件
                        shutil.move(self.压缩目录名, self.移动文件目录名)
                except (FileNotFoundError, OSError) as 异常:
                    print('异常# 跳过当前循环,继续进行', 异常)
                    continue  # 跳过当前循环,继续进行下一轮循环
                print('移动至目录:',移动文件名)


            break  # 结束循环

    def 模具_压缩(self):

        self.压缩目录名 = str(self.目录路径) + '.zip'  # 压缩后文件夹的名字

        z = zipfile.ZipFile(self.压缩目录名, 'w', zipfile.ZIP_DEFLATED)  # 参数一:文件夹名
        for dirpath, dirnames, filenames in os.walk(self.目录路径):
            fpath = dirpath.replace(self.目录路径, '')  # 这一句很重要,不replace的话,就从根目录开始复制
            fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷,实现当前文件夹以及包含的所有文件的压缩
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
        z.close()
        print('成功压缩文件:', self.压缩目录名)

    def 模具_创建移动文件目录(self):
        if not os.path.exists(self.移动文件目录名):  # 必有条件选择,否则出错
            try:
                os.makedirs(self.移动文件目录名)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except (FileNotFoundError, OSError) as 异常:
                print('异常:', 异常)






class 类_: #调用 类的模具 self.模具_数据库() 
    def __init__(self,data):
        self.data =data

    def 模具_递归目标目录与文件(self):
        子目录列表与文件列表 = os.listdir(self.目标目录)# 分离出目录列表与文件列表
        for 子目录或文件 in 子目录列表与文件列表:
            根目录的子目录或文件路径 = os.path.join(self.目标目录, 子目录或文件)
            if os.path.isdir(根目录的子目录或文件路径):# 判断是不是文件夹
                子目录=根目录的子目录或文件路径
                二级子目录列表与文件列表 = os.listdir(子目录) # 分离出目录列表与文件列表
                for 二级子目录或文件 in 二级子目录列表与文件列表:
                    二级子目录或文件路径 = os.path.join(子目录, 二级子目录或文件)
                    if os.path.isdir(二级子目录或文件路径):  # 判断是不是文件夹
                        self.二级子目录 = 二级子目录或文件路径
                        self.模具_压缩()
                        self.模具_二级子目录移动文件夹()


                    else:# 否则 为文件
                        self.二级子目录文件 =二级子目录或文件路径
                        self.移动文件目录名 = 子目录
                        self.模具_子目录移动文件夹()
    def 模具_二级子目录移动文件夹(self):

        # 移动文件
        移动文件目录名 = str(self.二级子目录).replace("下载种子目录4", "压缩-下载种子")
        规则 = r'.{1,}(?=\\.*)'  # .*(文本)  *号是贪婪的,放置在最前方会消耗尽可能多的字符.
        文本列表 = re.findall(规则, str(移动文件目录名))  # 提取 前面
        移动文件目录名 = 文本列表[0]

        if not os.path.exists(移动文件目录名):  # 必有条件选择,否则出错
            try:
                os.makedirs(移动文件目录名)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except (FileNotFoundError, OSError) as 异常:
                print('异常:', 异常)
        #移动压缩文件
        shutil.move(self.压缩二级子目录为文件的名, 移动文件目录名)

        print('移动压缩文件到目录:', 移动文件目录名)
        print('=========================')

    def 模具_子目录移动文件夹(self):
        移动文件目录名 = str(self.移动文件目录名).replace("下载种子目录4", "压缩-下载种子")

        if not os.path.exists(移动文件目录名):  # 必有条件选择,否则出错
            try:
                os.makedirs(移动文件目录名)  # makedirs 创建多级目录文件夹,mkdir创建一个文件夹
            except (FileNotFoundError, OSError) as 异常:
                print('异常:', 异常)


        # 复制文件到新目录
        shutil.copy(self.二级子目录文件, 移动文件目录名)
        print('复制文件:',self.二级子目录文件)
        print('到目录:', 移动文件目录名)
        print('=========================')

    def 递归展开目录与文件(self):
        for root, dirs, files in os.walk("F:\电影模板\下载种子目录2\动漫", topdown=False):  # "."目录,topdown=False先子文件夹再到元组文件夹

            for name in dirs:  # dirs遍历目录  files遍历文件
                name2 = 模具_符号清洗(name)

                旧目录 = os.path.join(root, name)# 合并成为 完全的地址
                新目录 = os.path.join(root, name2)
                # print(旧目录)
                # print(新目录)


类_进入一级目录压缩文件夹并移动到文件夹()





