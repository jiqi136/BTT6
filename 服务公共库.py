# -*- coding:utf-8

import re  # 正则式
import random  # 随机
import requests  # 网页浏览
import pymysql  # 数据库
import time  # 时间
import pyautogui  # 键盘控制
import win32gui  # 窗口控件
import os  # 本地操作
import win32api  # 操作本地文件
import win32con  # 提取剪切板内容

"""
import grequests  # 并发协程
import requests  # 网页浏览
import pymysql  # 数据库
import time  # 时间
import random  # 随机
import win32api  # 操作本地文件
import pyautogui  # 键盘控制
import win32gui #窗口控件
import win32con#提取剪切板内容
import os  # 本地操作


from 网页采集公共库 import 类一一采集公共库# 导入模块
import requests  # 网页浏览
import re  # 正则式

import datetime  # 时间
import os  # 本地操作

from lxml import etree  # 网页分析
import shutil  # 移动复制文件目录
from lxml import html  # 网页分析
from selenium import webdriver  # 浏览的驱动

import asyncio, aiohttp # 异步浏览


"""


class 类一一服务公共库:  # 调用 类的模具  self.模具一一查看变量输出文本值('变量名', self.测试打印, 8)
	def __init__(self):
		self.测试打印 = 'ew'

		self.模具一一换手机头部信息()

	def 模具一一示例(self):
		pass

		帖子链接 = ''
		self.模具一一查看变量输出文本值("过滤的网址", 帖子链接, 8)

		pass

		self.数据库名 = "影视发帖推广"
		self.sql语句 = "UPDATE `微博抽奖转发内容` SET `转发`='是' WHERE `ID`={}".format(self.数据库id)  # '代入 '{}' #'
		self.模具一一内容数据库("更新 转发栏为 是")
		self.数据库内容组列表 = self.数据库内容组列表

		pass
		文件路径 = ''
		操作类型 = ''
		内容 = ''
		写入类 = ''
		pass
		文本内容列表 =self.模具一一读取与写入文件(文件路径, 操作类型="每行读取" , 内容='', 写入类='')
		"""操作类型="每行读取" or     操作类型="读取"  
		操作类型="写入"  or   操作类型="格式写入"
		默认 内容=''
		默认 重写 'w'   or 追加 写入类='a' 
		"""

	def 模具一一换手机头部信息(self):
		def 模具一随机换头部信息():
			随机浏览器列表数 = [
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-G7106 Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI C8816 Build/HuaweiC8816) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Lingwin Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 8732 Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; N5117 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-N9008S Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M032 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} LIFE PLAY 2 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-N9002 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; 8190Q Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; TCL P331M Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I8262D Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'MQQBrowser/{浏览器版本号}/Adr (Linux; U; 4.2.1; zh-cn; HUAWEI G700-U00 Build/G700-U00 V100R001CHNC17B142;720*1280)',
				'MQQBrowser/3.6/Mozilla/5.0 (Linux; U; Android {安卓系统版本号} en-us; HUAWEI G700-U00 Build/HuaweiG700-U00) AppleWebKit/534.30 (KHTML, like Gecko) Version/{浏览器版本号} Mobile Safari/534.30',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 2 Build/JRO03L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025413 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D QQ/5.7.2.2490 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; V188 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M355 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SGH-I257M Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'mozilla/5.0 (iphone; cpu iphone {IP版本号} like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SGH-I257M Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI MT7-TL10 Build/HuaweiMT7-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'MQQBrowser/3.1/Mozilla/5.0 (Linux; U; Android {安卓系统版本号} en-us; Lenovo A789 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/{浏览器版本号} Mobile Safari/534.30',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 4LTE Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HM 1SW Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} QQ-Manager Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-S7572 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} XT1040 Build/KXB21.14-L1.54) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I8552 Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1 V1_AND_SQ_5.2.0_174_YYB_D QQ/5.2.0.2280 NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 3 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9502 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-G3588V Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 8297 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; vivo X3t Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 4LTE Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; LM-X21 Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} QQ-Manager Mobile Safari/537.3631313',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; 2013022 Build/HM2013022) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; R823T Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 8675 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 7295C Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Lenovo S850t Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; 2014501 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Lenovo A398t+ Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M463C Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025440 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/WIFI Language/zh_CN',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I8160 Build/GINGERBREAD) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 2S Build/JRO03L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025440 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/WIFI Language/zh_CN',
				'mozilla/5.0 (linux; u; android {安卓系统版本号} zh-cn; mi-one plus build/jzo54k) applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534.30 micromessenger/5.0.1.352',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M040 Build/JRO03H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D PA QQ/5.7.2.2490 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9500 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D PA QQ/5.7.2.2490 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; S1 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; vivo Y23L Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Lenovo A318t Build/GRK39F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI C8816D Build/HuaweiC8816D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SGH-I257M Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-G7106 Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D QQ/5.7.2.2490 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Che2-UL00 Build/HonorChe2-UL00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; vivo X1St Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-G7109 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I8552 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; ChanghongV5t Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} en-us; SPH-L710T Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1 V1_AND_SQ_5.4.0_216_HDBM_T QQ/5.4.0.2385 NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9300 Build/JSS15J) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; C8817D Build/HuaweiC8817D) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/ctlte Language/zh_CN',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-G7106 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9082 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 3W Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 2SC Build/JRO03L) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI G610-U00 Build/HuaweiG610-U00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9300 Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-S7278U Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI P7-L07 Build/HuaweiP7-L07) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} SGH-I257M Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} M463C Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 V1_AND_SQ_4.6.1_9_YYB_D QQ/5.3.1.544 NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 8297W Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025442 Mobile Safari/533.1 V1_AND_SQ_5.8.0_264_YYB_D QQ/5.8.0.2505 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I8552 Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} XT1040 Build/KXB21.14-L1.54) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 MicroMessenger/{微信版本号} NetType/NON_NETWORK',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 8705 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; InFocus M512 Build/*****) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D QQ/5.7.2.2490 NetType/3G',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} fr-ca; LG-E973 Build/IMM76L) AppleWebKit/534.30 (KHTML, like Gecko) Version/{浏览器版本号} Mobile Safari/534.30 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; 2013022 Build/HM2013022_NewBee_V4.1) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; LG-D802 Build/JDQ39B) AppleWebKit/534.30 (KHTML, like Gecko) Version/{浏览器版本号} Mobile Safari/534.30 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-N7100 Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} SM-T330NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Safari/537.36 MicroMessenger/{微信版本号} NetType/WIFI Language/zh_HK',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI Y518-T00 Build/HUAWEIY518-T00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 2S Build/JRO03L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025440 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/WIFI Language/ctwap',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M463C Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025440 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/ctwap Language/zh_CN',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-N9006 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HTC D610t Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 8297W Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025440 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/WIFI Language/zh_CN',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9300 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI C8813Q Build/HuaweiC8813Q) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HTC D820u Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; C8817D Build/HuaweiC8817D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; R6007 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; InFocus M512 Build/*****) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D QQ/5.7.2.2490 NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-S7572 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/{浏览器版本号} Mobile Safari/534.30 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HM NOTE 1LTETD Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'MQQBrowser/{浏览器版本号} (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HTC X920e Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'MQQBrowser/5.0/Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI G520-0000 Build/HuaweiG520-0000) AppleWebKit/534.30 (KHTML, like Gecko) Version/{浏览器版本号} Mobile Safari/534.30',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; K-Touch U81t Build/IMM76D) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/533.1',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; vivo X3L Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025442 Mobile Safari/533.1 V1_AND_SQ_5.5.1_236_YYB_D QQ/5.5.1.2435 NetType/UNKNOWN WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M040 Build/JRO03H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D gamecenter QQ/5.7.2.2490 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M355 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI C8815 Build/HuaweiC8815) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI P7-L07 Build/HuaweiP7-L07) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025413 Mobile Safari/533.1 V1_AND_SQ_5.5.1_236_YYB_D PA QQ/5.5.1.236 NetType/WIFI WebP/0.3.0',
				'MQQBrowser/{浏览器版本号}/Adr (Linux; U; 4.0.4; zh-cn; Lenovo A789 Build/A789_S235_130828;480*800)',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9500 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 V1_AND_SQ_5.7.2_260_YYB_D QQ/5.7.2.2490 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; T9200 Build/HuaweiT9200) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} M463C Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 V1_AND_SQ_4.6.1_9_YYB_D QQ/5.3.1.544 NetType/3G',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; HUAWEI P7-L07 Build/HuaweiP7-L07) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025413 Mobile Safari/533.1 V1_AND_SQ_5.5.1_236_YYB_D QQ/5.5.1.236 NetType/WIFI WebP/0.3.0',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} SM-G730W8 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9502 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Dalvik/1.6.0 (Linux; U; Android {安卓系统版本号} SGH-I257M Build/KOT49H) MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MG482ZP/A Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; Android {安卓系统版本号} zh-cn; MX4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{Chrome浏览器版本号} Mobile Safari/537.36 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; MI 2S Build/JRO03L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025440 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/3G Language/zh_CN',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; M355 Build/JOP40D) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025411 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/WIFI',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9152 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; SM-G3818 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; 100s Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; m1 note Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; ZTE U9180 Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} TBS/025438 Mobile Safari/533.1 MicroMessenger/{微信版本号} NetType/WIFI Language/zh_CN',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-I9300 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; Coolpad 8675-A Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36',
				'Mozilla/5.0 (Linux; U; Android {安卓系统版本号} zh-cn; GT-S7568 Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/{浏览器版本号} Mobile Safari/537.36']
			# 随机浏览器 = random.choice(随机浏览器列表数)
			随机数 = random.randrange(1, len(随机浏览器列表数))  # 整数
			随机浏览器 = 随机浏览器列表数[随机数]

			if '安卓系统版本号' in 随机浏览器:
				整数a = random.randrange(4, 10)  # 整数
				整数b = random.randrange(1, 10)  # 整数
				整数c = random.randrange(1, 10)  # 整数
				安卓系统版本号 = '{}.{}.{};'.format(整数a, 整数b, 整数c)  # '代入 '{}'
				# 随机浏览器=随机浏览器.format(安卓系统版本号=安卓系统版本号)#'代入 '{}'
				随机浏览器 = 随机浏览器.replace("{安卓系统版本号}", 安卓系统版本号)  # 替换   , 1) 次数 1

			if 'IP版本号' in 随机浏览器:
				整数a = random.randrange(6, 12)  # 整数
				整数b = random.randrange(1, 10)  # 整数

				IP版本号 = '{}_{};'.format(整数a, 整数b)  # '代入 '{}'
				# 随机浏览器 = 随机浏览器.format(IP版本号=IP版本号)  # '代入 '{}'
				随机浏览器 = 随机浏览器.replace("{IP版本号}", IP版本号)  # 替换   , 1) 次数 1

			if '微信版本号' in 随机浏览器:
				整数a = random.randrange(5, 10)  # 整数
				整数b = random.randrange(1, 10)  # 整数
				整数c = random.randrange(1, 10)  # 整数
				微信版本号 = '{}.{}.{};'.format(整数a, 整数b, 整数c)  # '代入 '{}'6.1.4
				# 随机浏览器=随机浏览器.format(微信版本号=微信版本号)#'代入 '{}'
				随机浏览器 = 随机浏览器.replace("{微信版本号}", 微信版本号)  # 替换   , 1) 次数 1

			if '浏览器版本号' in 随机浏览器:
				整数a = random.randrange(4, 10)  # 整数
				整数b = random.randrange(1, 10)  # 整数

				浏览器版本号 = '{}.{};'.format(整数a, 整数b)  # '代入 '{}'
				# 随机浏览器=随机浏览器.format(浏览器版本号=浏览器版本号)#'代入 '{}'
				随机浏览器 = 随机浏览器.replace("{浏览器版本号}", 浏览器版本号)  # 替换   , 1) 次数 1

			if 'Chrome浏览器版本' in 随机浏览器:
				整数a = random.randrange(10, 100)  # 整数
				整数b = random.randrange(1, 10)  # 整数
				整数c = random.randrange(10, 1000)  # 整数
				整数d = random.randrange(10, 1000)  # 整数

				Chrome浏览器版本号 = '{}.{}.{}.{};'.format(整数a, 整数b, 整数c, 整数d)  # '代入 '{}'
				# 随机浏览器=随机浏览器.format(Chrome浏览器版本号=Chrome浏览器版本号)#'代入 '{}'
				随机浏览器 = 随机浏览器.replace("{Chrome浏览器版本号}", Chrome浏览器版本号)  # 替换   , 1) 次数 1

			return 随机浏览器  # 返回

		头部信息 = 模具一随机换头部信息()
		self.手机头部信息 = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
			'Cache-Control': 'max-age=0',
			'User-Agent': '',
			'Connection': 'keep-alive',
			'Referer': 'http://www.baidu.com/'}

		self.模具一一查看变量输出文本值("手机头部信息", 头部信息)
		self.手机头部信息['User-Agent'] = 头部信息

		self.模具一一查看变量输出文本值("self.手机头部信息", self.手机头部信息, 8)

	def 模具一一查看变量输出文本值(self, 变量名, 变量文本值, 测试输入=0):

		if 测试输入 == 0:
			print(变量名, '： ', 变量文本值)
		elif len(self.测试打印) != 0:
			print(变量名, '： ', 变量文本值)

	def 模具一一高位换头部信息(self):  # 头部信息 def 函数模具内通行变量
		# nonlocal 头部信息  # def 函数模具内通行变量

		self.换IP时间计数 = int(time.time())
		# {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'}  被BT网站墙了
		随机3位数 = str(random.randrange(101, 1000))
		随机2位数 = str(random.randrange(41, 100))
		随机1位数 = str(random.randrange(1, 10))
		随机11位数 = str(random.randrange(1, 10))
		头部信息 = random.choice([{'User-Agent': 'Opera/随机2位数.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/随机2位数.11'},
							  {
								  'User-Agent': 'Opera/随机2位数.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/随机2位数.8.{随机3位数 Version/随机2位数.11'},
							  {
								  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.9Safari/536.5'},
							  {
								  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.9Safari/536.5'},
							  {
								  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
							  {
								  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
							  {
								  'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
							  {
								  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/随机3位数.11(KHTML,likeGecko)Chrome/随机2位数.0.1132.57Safari/536.11'},
							  {
								  'User-Agent': 'Mozilla/5.0(X11;CrOSi6862268.111.0)AppleWebKit/随机3位数.11(KHTML,likeGecko)Chrome/随机2位数.0.1132.57Safari/536.11'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.77.34.5Safari/537.1'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.77.34.5Safari/537.1'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/随机3位数.24(KHTML,likeGecko)Chrome/随机2位数.0.1055.1Safari/535.24'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1090.0Safari/536.6'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1090.0Safari/536.6'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.2)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.0.1207.1Safari/537.1'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.1(KHTML,likeGecko)Chrome/随机2位数.0.1207.1Safari/537.1'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1092.0Safari/536.6'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.6(KHTML,likeGecko)Chrome/随机2位数.0.1092.0Safari/536.6'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1062.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1061.1Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.36Safari/536.5'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/随机3位数.5(KHTML,likeGecko)Chrome/随机2位数.0.1084.36Safari/536.5'},
							  {
								  'User-Agent': 'Mozilla/5.0(WindowsNT5.1)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/随机3位数.3(KHTML,likeGecko)Chrome/随机2位数.0.1063.0Safari/536.3'},
							  {
								  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/随机3位数.50 (KHTML, like Gecko) Version/随机3位数.1 Safari/534.50'},
							  {
								  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'},
							  {
								  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50随机3位数; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:随机2位数.0) like Gecko'},
							  {
								  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:随机2位数.0) Gecko/201随机3位数01 Firefox/随机2位数.0'},
							  {
								  'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/随机3位数.50 (KHTML, like Gecko) Version/随机3位数.1 Safari/534.50'},

							  {
								  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/随机3位数.11 (KHTML, like Gecko) Chrome/随机2位数.0.963.56 Safari/535.11'},
							  {
								  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/201随机3位数01 Firefox/随机2位数.0.1'}

							  ])
		头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机1位数", 随机1位数)  # 替换   , 1) 次数 1
		头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机11位数", 随机11位数)  # 替换   , 1) 次数 1
		头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机2位数", 随机2位数)  # 替换   , 1) 次数 1
		头部信息['User-Agent'] = str(头部信息['User-Agent']).replace("随机3位数", 随机3位数)  # 替换   , 1) 次数 1
		self.头部信息 = 头部信息
		print(头部信息)

	def 模具一一换ip连接(self):
		self.模具一一高位换头部信息()
		# coding:gbk
		循环 = 0
		次数循环 = 0

		while 循环 == 0:  # 条件循环  post
			print('宽带连接进行时.....')
			os.system(r"rasphone -h 宽带连接")  # xxx0是你的拨号名称,xp下默认是"宽带连接”.
			os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859")  # xxx0同上,xxx1 拨号用户名 ,xxx2拨号密码.
			time.sleep(3)
			print('换ip再连接完成')

			try:
				返回网页内容 = requests.get('https://www.163.com/', headers=self.头部信息, timeout=3)
			except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
					requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout,
					requests.exceptions.ChunkedEncodingError, requests.exceptions.InvalidSchema,
					requests.exceptions.ContentDecodingError) as 异常:
				次数循环 += 1
				print('网络异常等待', 异常)
				print('倒数60秒再连接', 次数循环, '次')
				self.模具一一开关提醒声('网络异常等待')
				time.sleep(60)
				if 'None, 10053,' in str(异常):
					pass
			else:
				if '200' in str(返回网页内容):
					self.换IP时间计数 = int(time.time())

					break  # 结束循环
				else:
					print('网站网络异常,状态码:', 返回网页内容)
					print('等待60秒')
					self.模具一一开关提醒声('网络异常等待')
					time.sleep(60)

	def 模具一一读取与写入文件(self, 文件路径, 操作类型, 内容, 写入类):  # 内容='格式写入'  写入类='a'   追加
		pass
		"""self.模具一一读取与写入文件(文件路径, 操作类型="每行读取", 内容='', 写入类='w')  #
				操作类型="读取"  or    操作类型="每行读取"  
				操作类型="写入"  or   操作类型="格式写入"
				默认 内容=''
				默认 重写 'w'   or 追加 写入类='a' 
		"""
		文本内容列表 = ''
		if '读取' in 操作类型:
			if 操作类型 == '每行读取':
				try:  # 调用异常处理,应对易发生错误的位置 {}.format()#'代入 '{}'
					文本缓存 = open(文件路径, 'r', encoding='UTF-8')
					文本内容列表 = 文本缓存.readlines()  # read() #全部读取   readlines 每一行


				except UnicodeDecodeError as 异常原因:  # 异常处理

					self.模具一一查看变量输出文本值("{} 读取文本 ,异常原因".format(文件路径), 异常原因)

					文本缓存 = open(文件路径, 'r', encoding='gbk')
					文本内容列表 = 文本缓存.readlines()  # read() #全部读取   readlines 每一行


				else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
					文本缓存.close()

			else:  # 否则
				try:  # 调用异常处理,应对易发生错误的位置 {}.format()#'代入 '{}'
					文本缓存 = open(文件路径, 'r', encoding='UTF-8')
					文本内容列表 = 文本缓存.read()  # read() #全部读取   readlines 每一行

				except UnicodeDecodeError as 异常原因:  # 异常处理

					self.模具一一查看变量输出文本值("读取文本 ,异常原因", 异常原因, 8)
					文本缓存 = open(文件路径, 'r', encoding='gbk')
					文本内容列表 = 文本缓存.readlines()  # read() #全部读取   readlines 每一行



				else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
					文本缓存.close()



		elif '写入' in 操作类型:  # 其它条件.
			文件缓存 = open(文件路径, 写入类, encoding='UTF-8')  # 追加 a

			if 操作类型 == '格式写入':  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
				文件缓存.write(内容.content)  # read() #读取
			else:  # 否则
				文件缓存.write(内容)  # write 写入  read() #读取
			文件缓存.close()

			self.模具一一查看变量输出文本值("保存至文本", 文件路径, 8)

		return 文本内容列表  # 返回

	def 模具一一开关提醒声(self, 类型=''):
		if len(类型) == 0:
			win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\py快捷方式\简短提示音.wav', '', '', 1)
		else:  # 否则
			win32api.ShellExecute(0, 'open', r'E:\PY学习文件\BTT影视剧\py快捷方式\百度云下载完成提示音.wav', '', '', 1)
		time.sleep(3)  # 等待  # 增加延迟
		窗口标题 = "Windows Media Player"

		窗口句柄 = win32gui.FindWindow(None, 窗口标题)

		win32gui.ShowWindow(窗口句柄, 11)  # 即使拥有窗口的线程被挂起也会最小化。在从其他线程最小化窗口时才使用这个参数
		time.sleep(1)  # 等待  # 增加延迟
		win32gui.SendMessage(窗口句柄, win32con.WM_CLOSE)  # 关闭窗口

	def 模具一一内容数据库(self, 数据库操作类型=''):
		# self.sql语句 = """
		# print('打开数据库连接')
		# 打开数据库连接,
		数据库执行 = pymysql.connect("localhost", "root", "", self.数据库名, charset="utf8")
		# 使用cursor()方法获取操作游标
		操作游标 = 数据库执行.cursor()

		# 执行sql语句
		操作游标.execute(self.sql语句)

		if len(数据库操作类型) == 0 or 数据库操作类型 == '查询':  # 为查询
			# 获取所有记录列表
			self.数据库内容组列表 = 操作游标.fetchall()
			print('数据库完成查询')



		else:  # 否则 为      数据库操作类型

			try:
				# 提交到数据库执行
				数据库执行.commit()
				print(数据库操作类型, '=提交至保存数据库')
			except:

				# 如果发生错误则回滚
				print(数据库操作类型, '==========数据库执行发生错误:======')
				数据库执行.rollback()

		数据库执行.close()  # 关闭数据库连接


if __name__ == '__main__':
	采集公共库 = 类一一服务公共库()
