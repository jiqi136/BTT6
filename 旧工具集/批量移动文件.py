
import os
import shutil


def 展开下一层目录与文件():
    目标目录= r'C:\下载中转站\新建文件夹2\dying'
    子目录列表与文件列表 = os.listdir(目标目录)  # 分离出目录列表与文件列表
    for 子目录或文件 in 子目录列表与文件列表[0:8000]:
        根目录的子目录或文件路径 = os.path.join(目标目录, 子目录或文件)

        if os.path.isfile(根目录的子目录或文件路径):  # 判断文件 os.path.isfile
            shutil.move(根目录的子目录或文件路径, r'C:\下载中转站\新建文件夹\dying')
            print('成功移动文件',子目录或文件)
        else:  # 否则 为文件
           pass
展开下一层目录与文件()





