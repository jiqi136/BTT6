# -*- coding:utf-8



import re,random
from lxml import etree,html #解析与定位网页

内容 = ""

进程已结束,退出代码0

 """
def 整理内页内容(内容):
    帖子内容html = etree.HTML(内容)  #
    #print(内容)
    规则 = '//*[@id="list"]/table/tbody/tr[*]/td[1]/text()'
    #规则 = str(规则).replace("/tbody", "")
    IP列表 = 帖子内容html.xpath(规则)
    print(IP列表)


    规则 = '//*[@id="list"]/table/tbody/tr[*]/td[2]/text()'
    #规则 = str(规则).replace("/tbody", "")
    端口列表 = 帖子内容html.xpath(规则)
    print(端口列表)


    规则 = '//*[@id="list"]/table/tbody/tr[*]/td[4]/text()'
    #规则 = str(规则).replace("/tbody", "")
    代理类型列表 = 帖子内容html.xpath(规则)
    print(代理类型列表)


    代理类型IP端口列表=[]
    print('IP列表数',len(IP列表))
    print('端口列表数', len(端口列表))
    print('代理类型列表', len(代理类型列表))
    if len(IP列表)!=len(端口列表) and len(IP列表)!=len(代理类型列表):
        print('ip端口数据组不匹配，结束程序')
        等待用户输入 = input("\n按下 enter 确认键后继续")
    for 代理类型,IP,端口 in zip(代理类型列表,IP列表, 端口列表):
        IP端口 = "{}://{}:{}".format(代理类型,IP,端口)#'代入 '{}'

        代理类型IP端口列表.append(IP端口)



    for IP端口 in 代理类型IP端口列表:
        print(IP端口)


def 读取文本():
    try:  # 调用异常处理，应对易发生错误的位置
        文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'r', encoding='UTF-8')
        文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
    except UnicodeDecodeError as 异常原因:  # 异常处理
        print(异常原因)
        文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'r', encoding='gbk')
        文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
    else:  # 必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
        文本.close()
    print('文本内容列表\n',文本内容列表)

    for 行内容 in 文本内容列表:
        if '正常' in 行内容:
            行内容 =行内容.replace("//", "")  # 替换   , 1) 次数 1
            文本列表 = 行内容.split(":")
            类型=文本列表[0]
            IP = 文本列表[1]
            端口 = 文本列表[2]
            print(类型, IP,端口)

        else:
            pass

内容 = """柔蓉安蓝春语彤晴语菱霜紫莲翠烟南寻慕蕊雪海沛宛晓菡巧
    听卉靖枫梓晨丽丹佩惠月玉婉晓玲倩瑞静颖棋芹萍幻露灵含雅薇瑶丹丽云亿仪伊伶佳依俞俪倩偲兰冰凝凡凤叆呤
    爱姿惠娇媛妩萱娈瑷悠源赫晗贻楚梦琪忆柳桃慕兰岚香沛菡珊曼菱寒薇忆旋芷蕾代
    芙盼蝶筠瑶珍谷荷画嘉囡女如妃妍妙妮妹姐姑姗姝姞姣梅梦楠檀欢欣歆毓水洁涵淑清滟滢漪漫澜灵煜燕
    玉玥玫环玲珂珊珍珠姬娅娆娇娉娜娟娣娥娴婉婕婧婵婷媚媛嫔嫣嫱安宛宜宝容巧希彤彩心忆念怀怜思怡情惠
    慧敏旭春晴曼月琦琪琬琰琳琴琼瑗瑛瑜瑶瑾璇璐璟白盈盼碧秀筠红绮美翠艳芃芊芝芬芮芯芳芷芸苑若苹茗茜茵茹荔荭
    荷莉莎莲莹菁菡菲萍萱蓉蓓蔓蕊蕾薇诗语贞采钰银雅雨雪雯霏霖霜霞露青靖静音韵颖颜香馨黛"""
内容 = 内容.replace("\n", "")
内容 = 内容.replace(" ", "")

随机 = random.randrange(0, len(内容))
字符 =内容[随机]
print(字符)

列表=[1,2,3,4,5,6]
for 列表值 in 列表:
    if 列表值 == 1:
        列表数 = '{}st'.format(列表值)
        print(列表数)
    elif 列表值 == 2:
        列表数 = '{}nd'.format(列表值)
        print(列表数)
    elif 列表值 == 3:
        列表数 = '{}rd'.format(列表值)
        print(列表数)
    else:
        列表数 = '{}th'.format(列表值)
