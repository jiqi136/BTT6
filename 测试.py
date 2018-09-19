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

    合名 = 名 + """故事发生在未来的时空之中，犬流感的肆虐让市长（野村训市 配音）颁布的狗狗流放法案，将城市里的所有犬类都投放到了“垃圾岛”之上，任它们自生自灭，市长家的护卫犬点点（列维·施瑞博尔 Liev Schreiber 饰）首当其冲。就这样，本来被养在家中锦衣玉食的狗狗们，都成为了要在垃圾堆里找食物吃的流浪狗。
首领（布莱恩·科兰斯顿 Bryan Cranston 配音）、君主（爱德华·诺顿 Edward Norton 配音）、老板（比尔·默瑞 Bill Murray 配音）、公爵（杰夫·高布伦 Jeff Goldblum 配音）和国王（鲍勃·巴拉班 Bob Balaban 配音）是岛上的五只流浪狗，它们通常结伴行动。一天，市长的养子阿塔里（科宇·兰金 Koyu Rankin 配音）忽然驾驶着飞机降落在了岛上，他要在这里寻找他一生的挚友点点。
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



