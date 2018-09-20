# -*- coding:utf-8



import random,win32api # 随机

import pyautogui as pag #模拟鼠标键盘操作
import pyautogui#模拟鼠标键盘操作
import win32clipboard as w# 提取剪切板内容
import win32con#提取剪切板内容
import time  # 时间


def 模具一一写入剪切板内容(内容):  # 写入剪切板内容
    #内容 = str(内容).encode('gbk')  # encoding='UTF-8'为 WIN7 系统 的中文
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, 内容)
    w.CloseClipboard()


def 模具一一随机取名合并网址名():
    内容 = """柔蓉安蓝春语彤晴语菱霜紫莲翠烟南寻慕蕊雪海沛宛晓菡巧
            听卉靖枫梓晨丽丹佩惠月玉婉晓玲倩瑞静颖棋芹萍幻露灵含雅薇瑶丹丽云亿仪伊伶佳依俞俪倩偲兰冰凝凡凤叆呤
            爱姿惠娇媛妩萱娈瑷悠源赫晗贻楚梦琪忆柳桃慕兰岚香沛菡珊曼菱寒薇忆旋芷蕾代
            芙盼蝶筠瑶珍谷荷画嘉囡女如妃妍妙妮妹姐姑姗姝姞姣梅梦楠檀欢欣歆毓水洁涵淑清滟滢漪漫澜灵煜燕
            玉玥玫环玲珂珊珍珠姬娅娆娇娉娜娟娣娥娴婉婕婧婵婷媚媛嫔嫣嫱安宛宜宝容巧希彤彩心忆念怀怜思怡情惠
            慧敏旭春晴曼月琦琪琬琰琳琴琼瑗瑛瑜瑶瑾璇璐璟白盈盼碧秀筠红绮美翠艳芃芊芝芬芮芯芳芷芸苑若苹茗茜茵茹荔荭
            荷莉莎莲莹菁菡菲萍萱蓉蓓蔓蕊蕾薇诗语贞采钰银雅雨雪雯霏霖霜霞露青靖静音韵颖颜香馨黛"""

    内容 = 内容.replace("\n", "")
    内容 = 内容.replace(" ", "")

    名 = random.choice(内容)

    合名 = """译　　名　昆池岩/鬼病院：灵异直播(台)/疯人院逐个捉(港)/魂断疯人院


产　　地　韩国

　　原名南营神经精神医院的昆池岩精神病院，最早建立于20世纪60年代。在特殊的时代它曾经历了无比的辉煌，然而更为人熟知的则是该医院身上所发生的各类恐怖事件。现如今，早已废弃的昆池岩医院被CNN票选为全球七大恐怖之地之一，更由此吸引无数寻求刺激的青年男女来此探险。三个月前，两名青少年来此探险，结果在直播中遭遇诡异事件，下落不明。此后，《恐怖世代》剧组在魏河俊的召集下，网罗了吴雅妍、朴智贤、夏洛特（文艺媛 饰）、李丞旭、朴成勋、刘帝允等人前往昆池岩，更试图打开备受诅咒的402室。

　　夜幕降临，全球网友一道观看这场恐怖盛宴……
    
    """
    #合名 = 合名.encode('gbk')


    print('随机取名合并网址名\n', 合名)
    return 合名  # 返回
def 保存至文本(内容):
    文本 = open("F:\影视发帖推广\临时文本.txt", 'w', encoding='UTF-8')

    文本.write(内容)  # read() #读取
    文本.close()
    print('保存至文本;', 内容)

def 提取文本内容():
    win32api.ShellExecute(0, 'open', 'notepad.exe', 'F:\影视发帖推广\临时文本.txt', '', 1)
    time.sleep(1)  # 等待  # 增加延迟
    pag.hotkey('ctrlleft', 'a')  # press()一次完整的击键.hotkey('ctrl','c')
    time.sleep(1)  # 等待  # 增加延迟
    pag.hotkey('ctrlleft', 'c')  # press()一次完整的击键.hotkey('ctrl','c')
    time.sleep(1)  # 等待  # 增加延迟
    pag.hotkey('altleft', 'f4')  # press()一次完整的击键.hotkey('ctrl','c')



合名=模具一一随机取名合并网址名()

计数器=0
文本=''
for 每个字 in 合名:
    计数器 = 计数器+1
    if 计数器 ==5:
        符号表 = random.choice(' ↕↟↡↥↧↨↾↿⇂⇃⇞⇟⇡⇣´`ˆ')

        print('符号表', 符号表)
        文本 =文本+str(符号表)
        计数器 = 0
    文本 = 文本 + 每个字


print('文本\n', 文本)
保存至文本(文本)
time.sleep(1)  # 等待  # 增加延迟
提取文本内容()



