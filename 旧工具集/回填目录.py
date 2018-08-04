import fileinput
import os
import re
import shutil

def 读写文本为列表():

    旧目录列表=[]
    for 旧目录 in fileinput.input("D:\桌面\遍历修改目录名.txt"):

        if '旧目录' in 旧目录:

            旧目录 = str(旧目录).replace("旧目录： F:/电影模板/下载种子目录2\动漫", "F:/电影模板/下载种子目录3/10/动漫")
            旧目录 = str(旧目录).replace("\n", "")
            旧目录 = str(旧目录).replace("\\\\", "/")
            旧目录 = str(旧目录).replace("\\", "/")


            if not os.path.exists(旧目录):  # 必有条件选择，否则出错
                try:
                    os.makedirs(旧目录)  # makedirs 创建多级目录文件夹，mkdir创建一个文件夹

                    print('成功空的创建旧目录',旧目录)
                    旧目录=旧目录+'\n'
                    旧目录列表.append(旧目录)

                    fout=open("D:\桌面\空的旧目录列表.txt", 'a+')  # 返回值 随后 被赋值给as后面的变量
                    fout.write(str(旧目录))  # read() #读取
                    fout.close()
                    print('完成创建目录')


                except (FileNotFoundError, OSError) as f:
                    print('创建目录失败原因', f)
                    print('创建旧目录失败', 旧目录)
    print(旧目录列表)

def 回填文件回空目录():

    空目录列表=[]
    文件数列表 = []
    for 旧目录 in fileinput.input("D:\桌面\空的旧目录列表.txt"):
        旧目录 = str(旧目录).replace("成功空的创建旧目录 ", "")
        旧目录 = str(旧目录).replace("\n", "")
        空目录列表.append(旧目录)

        规则 = r'.{1,}(?=/.*)'
        旧目录上层列表 = re.findall(规则, str(旧目录))  # 提取
        旧目录上层 = 旧目录上层列表[0]
        print('旧目录上层',旧目录上层)

        fileList = os.listdir(旧目录上层)  # 获取path目录下所有文件
        for filename in fileList:
            失散文件 = os.path.join(旧目录上层, filename)  # 获取path与filename组合后的路径
            if os.path.isdir(失散文件):  # 如果是目录
                continue  # 跳过当前循环，继续进行下一轮循环
            else:
                try:
                    shutil.move(失散文件, 旧目录)#移动文件
                    print("失散文件：", 失散文件)
                    print("完成回填目录：", 旧目录)
                    文件数列表.append(失散文件)

                except (shutil.Error) as f:
                    print("失败：", f)
                    print("回填目录失败：", 旧目录)
                    continue  # 跳过当前循环，继续进行下一轮循环
    print("完成目录数：",len(空目录列表))
    print("完成失散文件数：", len(文件数列表))


#读写文本为列表()
回填文件回空目录()