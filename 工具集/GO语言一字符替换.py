# -*- coding:utf-8

import re  # 正则式

import os  # 本地操作

import random  # 随机

import pyautogui  # 弹窗

import win32api  # 操作本地文件

import win32gui  # 窗口控件

import time # 时间

from 工具集服务公共库 import 类一一服务公共库# 导入模块


class 类一一GO语言一字符替换(类一一服务公共库):  # 调用 类的模具 self.模具一一数据库()
	def __init__(self):
		self.测试打印 = 'ew'
		self.循环 = 0

		self.循环的弹窗内容 = '输入要替换字符的文本路径,\n ⑴直接点"ok”:重复替换上次文本 \n⑵ 更换替换文本: 输入文本路径,点"ok” '

		self.跳过循环 = ''
		self.文本路径 = ''
		self.循环的弹窗 = 0
		self.全局定义变量名列表=[]

		while self.循环 == 0:  # 条件循环
			#time.sleep(1.5)# 等待  # 增加延迟
			time.sleep(1)  # 等待

			self.文本内容合成 = ''
			self.变量定义更替等号 = '空白开始'
			self.全局定义变量名列表 = []
			self.模具重开始定义变量名列表 = []
			

			self.模具一一弹窗输入字符串()
			if self.循环 == 998:
				break  # 结束循环

			elif '跳过循环 ' in self.跳过循环:
				continue  # 跳过循环

			self.循环的弹窗 = 1

			for self.文本内容 in self.文本内容列表:
				
				self.文本内容 = self.文本内容.replace('\t', '')  # 替换   , 1) 次数 1
			
				
				self.无空格文本内容 = self.文本内容.rstrip()  # 指定删除的字符串末尾的字符(默认为空格)
				self.模具一一导入标准库替换()
				print('模具一一导入标准库替换',self.文本内容)
				self.模具一一类型声明替换清洗()
				print('模具一一类型声明替换清洗', self.文本内容)
				self.模具一一变量定义声明更替清洗()
				print('模具一一变量定义声明更替清洗', self.文本内容)
				self.模具一一符号字典替换清洗()
				print('模具一一符号字典替换清洗', self.文本内容)
				self.模具一一导入模具替换清洗()
				print('模具一一导入模具替换清洗', self.文本内容)
				self.模具一一文本关键词替换清洗()
				print('模具一一文本关键词替换清洗', self.文本内容)

				self.文本内容合成 = self.文本内容合成 + self.文本内容

			self.文本内容合成 = self.文本内容合成.rstrip('\n')  # 指定删除的字符串末尾的字符(默认为空格)+ '\n'

			self.模具一一保存至文本()
			print('替换并保存至文本')

			self.模具一一消息弹窗最小化()



	def 模具一一消息弹窗最小化(self):
		#self.模具一一变量定义声明更替清洗()

		os.startfile(r"E:\PY学习文件\BTT影视剧\工具集\消息弹窗最少化.py")  # 打开文件
	def 模具一一弹窗输入字符串(self):
		self.上次文本位置文件 = r"E:\go学习文件\src\GO语言替换字符保存地址.txt"
		self.模具一一读取上次文本位置文件()



		self.文本路径 = pyautogui.prompt(self.循环的弹窗内容)

		if 'None' in str(self.文本路径):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
			self.循环 = 998
			return  # 返回



		elif len(self.文本路径) == 0:
			self.模具一一读取上次文本位置文件()
			self.模具一一读取GO文件()



		else:  # 否则
			self.模具一一读取GO文件()

	def 模具一一保存本次位置至文本(self):
		文本 = open(self.上次文本位置文件, 'w', encoding='UTF-8')  # 追加 a

		文本.write(self.文本路径)  # write 写入  read() #读取
		文本.close()

	def 模具一一读取上次文本位置文件(self):

		文本内容列表 = self.模具一一读取与写入文件(self.上次文本位置文件, 操作类型="每行读取", 内容='', 写入类='')
		""" 操作类型="每行读取 " or   操作类型="读取"  
        操作类型="写入"  or   操作类型="格式写入"
        默认 内容=''
        默认 重写 'w'   or 追加 写入类='a' 
        """
		self.文本路径 = 文本内容列表[0]
		if self.跳过循环 == '':
			self.循环的弹窗内容 = '输入要替换字符的文本路径,\n ⑴直接点"ok”:重复替换上次文本{} \n⑵ 更换替换文本: 输入文本路径,点"ok” '.format(
				self.文本路径)
			self.跳过循环 = 'F'
		else:  # 否则
			self.循环的弹窗内容 = """{}:\n=======完成替换并保存至文本=======\n⑴ 直接点"ok”:重复替换上次文本 \n⑵ 更换替换文本: 输入文本路径,点"ok”\n⑶ 点否"Cancel”: 退出替换程序 """.format(
				self.文本路径)


	def 模具一一读取GO文件(self):
		# self.文本路径 =input("输入要替换字符的文本路径:\n按下 enter 确认键后继续 \n")
		# 文本路径=r"E:\go学习文件\src\测试\main.go"
		try:  # 调用异常处理,应对易发生错误的位置 {}.format()#'代入 '{}'
			文本 = open(self.文本路径, 'r', encoding='UTF-8')
			文本内容列表 = 文本.readlines()  # read() #全部读取   readlines 每一行
		except UnicodeDecodeError as 异常原因:  # 异常处理
			print(异常原因)
			文本 = open(self.文本路径, 'r', encoding='gbk')
			文本内容列表 = 文本.readlines()  # read() #全部读取   readlines 每一行

		except FileNotFoundError as 异常原因:  # 异常处理 FileNotFoundError
			print(异常原因)
			self.循环的弹窗内容 = '{}:\n=======错误的文本路径=======\n⑴ 直接点"ok”:重复替换上次文本 \n⑵ 更换替换文本: 输入文本路径,点"ok”\n⑶ 点否"Cancel”: 退出替换程序 '.format(
				self.文本路径)

			self.跳过循环 = '跳过循环 '

			return  # 返回

		else:  # 必须放在所有的except子句之后.这个子句将在try子句没有发生任何异常的时候执行.
			文本.close()

		# self.模具一一保存本次位置至文本()
		文本内容列表一弃 = self.模具一一读取与写入文件(self.上次文本位置文件, 操作类型="写入", 内容=self.文本路径, 写入类='w')
		""" 操作类型="每行读取 " or   操作类型="读取"  
        操作类型="写入"  or   操作类型="格式写入"
        默认 内容=''
        默认 重写 'w'   or 追加 写入类='a' 
        """


		self.文本内容列表 = 文本内容列表
		self.循环的弹窗内容 = """{}:\n=======完成替换并保存至文本=======\n⑴ 直接点"ok”:重复替换上次文本 \n⑵ 更换替换文本: 输入文本路径,点"ok”\n⑶ 点否"Cancel”: 退出替换程序 """.format(
			self.文本路径)


	def 模具一一保存至文本(self):
		文本 = open(self.文本路径, 'w', encoding='UTF-8')  # 追加 a

		文本.write(self.文本内容合成)  # write 写入  read() #读取
		文本.close()


	def 模具一一导入标准库替换(self):
		库文本 = """
			import (
		"errors"
		"fmt"
		"math"
		"strings"
		"strconv"
		"time"
		"regexp"
		"bufio"
		"os"
		"io"
		"io/ioutil"
	) //
	func 模具一一模板() {
		模具一一类型()
		fmt.Printf(" ",)  //
			}
			
			"""
		if '库' == self.无空格文本内容:
			self.文本内容 = self.文本内容.replace('库', 库文本)  # 替换   , 1) 次数 1


	def 模具一一类型声明替换清洗(self):
		类型声明字典 = {}  # 关键词字典['字']='典'  符号字典[] =

		类型声明字典['整数列表'] = '整数列表 = []int{1, 2, 3}'
		类型声明字典['文本列表'] = '文本列表 = []string{"文","文","文"}'
		类型声明字典['点数列表'] = '点数列表 = []float32{1.0, 2, 3}'
		类型声明字典['字典'] = '字典 = map[string]string{"文": "文", "文文": "文"} //int 定义/'
		类型声明字典['字典键'] = '字典["to"] = ""'
		类型声明字典['对否'] = '对否=true //false'
		类型声明字典['数组'] = '数组 = [...]string{"a", "b", "c", "d"} //int 定义/'

		if 'for ' in self.文本内容 or '不替换' in self.文本内容:
			return  # 返回

		try:
			self.文本内容 = str(self.文本内容).replace(self.无空格文本内容, 类型声明字典[self.无空格文本内容])  # 替换   , 1) 次数 1

		except KeyError:  # 异常处理
			
			return  # 返回
		else:

			self.文本内容 = self.文本内容 + '//定义/ '
			return  # 返回


	def 模具一一变量定义声明更替清洗(self):

		def 模具一一类型声明等号统一为单一等号():
			文本内容 = self.文本内容
			类型声明等号列表=['；=',':=',';=',';=',':=',':=','：=',':=','=']
			for 类型声明等号 in 类型声明等号列表:
				if 类型声明等号 in self.文本内容:

					文本内容 =文本内容.replace(类型声明等号, "=")  # 替换   , 1) 次数 1

			return 文本内容 #返回


		if 'func ' in self.文本内容 :  # 条件.
			if '模具一一' in self.文本内容 or 'main' in self.文本内容:  # 条件.
				self.变量定义更替等号 = '模具重开始'
				self.模具重开始定义变量名列表 = []
				self.模具重开始定义变量名列表 = self.模具重开始定义变量名列表 +self.全局定义变量名列表



		self.文本内容=模具一一类型声明等号统一为单一等号()

		self.模具一一追加入模具重开始定义变量名列表()
		等号前加帽号 = ''


		if '不替换' in self.文本内容:
			return  # 返回
		elif '==' in self.文本内容 or '!=' in self.文本内容:  # 其它条件.
			return  # 返回

		elif '=' in self.文本内容:


			文本内容 = self.文本内容.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）
			文本内容列表 = 文本内容.split("=")
			定义变量名 = 文本内容列表[0]

			if ',' in 定义变量名:
				for 每个变量名 in 定义变量名.split(","):
					每个变量名 = 每个变量名.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）
					每个变量名 = 每个变量名.replace(" ", "")  # 替换   , 1) 次数 1
					if 每个变量名 not in self.模具重开始定义变量名列表:
						等号前加帽号='加帽号'

						self.模具重开始定义变量名列表.append(每个变量名)  # 列表追加


			else:  # 否则
				定义变量名 = 定义变量名.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）
				定义变量名 =定义变量名.replace(" ", "")  # 替换   , 1) 次数 1
				if 定义变量名 not in self.模具重开始定义变量名列表:
					等号前加帽号 ='加帽号'
					print('定义变量名', 定义变量名)

					self.模具重开始定义变量名列表.append(定义变量名)  # 列表追加



		print('模具重开始定义变量名列表',self.模具重开始定义变量名列表)
		if 等号前加帽号 =='加帽号':
			self.文本内容 = self.文本内容.replace("=", ":=") #替换   , 1) 次数 1

	def 模具一一追加入模具重开始定义变量名列表(self):

		if '//定义//' in self.文本内容 :  # 其它条件.
			if 'var' in self.文本内容:
				定义文本内容 = self.文本内容.replace("var", "")  # 替换   , 1) 次数 1

			定义文本内容 = 定义文本内容.rstrip()  # 指定删除的字符串末尾的字符（默认为空格）
			文本内容列表 = 定义文本内容.split(" ")
			定义变量名 = 文本内容列表[0]
			self.全局定义变量名列表.append(定义变量名)  # 列表追加
			self.模具重开始定义变量名列表.append(定义变量名)  # 列表追加


	def 模具一一符号字典替换清洗(self):
		符号字典 = {}  # 关键词字典['字']='典' 符号字典[] =

		符号字典['='] = '='
		符号字典['；'] = ':'
		符号字典['.'] = '.'
		符号字典['?'] = '?'
		符号字典['{'] = '{'
		符号字典['}'] = '}'
		符号字典['^'] = ','
		符号字典[':'] = ':'
		符号字典['%'] = '%'
		符号字典['('] = '('
		符号字典[')'] = ')'
		符号字典['['] = '['
		符号字典[']'] = ']'
		符号字典['"'] = '"'
		符号字典['''] = '"'
		符号字典['''] = '"'
		符号字典["'"] = '"'
		符号字典['”'] = '"'
		符号字典['“'] = '"'
		符号字典['encoding="UTF-8"'] = 'encoding="UTF-8"'
		符号字典['encoding="gbk"'] = 'encoding="gbk"'
		符号字典['^'] = ','

		if 'for ' in self.文本内容 or '不替换' in self.文本内容:
			return  # 返回

		for 符号键 in 符号字典:
			if 符号键 in self.文本内容:
				self.文本内容 = self.文本内容.replace(符号键, 符号字典[符号键])  # 替换   , 1) 次数 1


	def 模具一一语法关键词替换清洗(self):
		语法关键词字典 = {}  # 语法关键词字典['字']='典' 符号字典[] = """ """
		语法关键词字典['打印'] = 'fmt.Printfln("hello",变量)// 打印'
		语法关键词字典['常量'] = 'const '
		语法关键词字典['关系'] = '// 非 !(!T )、并 &&(T && T)、或 ||(T || T)'
		语法关键词字典['对比'] = '// 对比==、!= 、<、<=、>、>='
		语法关键词字典['运算'] = """/* +、-、* 和 /、%
						/ 对于整数运算而言,结果依旧为整数,例如:9 / 4 -> 2.
						取余运算符只能作用于整数:9 % 4 -> 1.
						*/"""
		语法关键词字典['格式化'] = '%d 用于格式化整数,%g 用于格式化浮点型 %数字.mg  %s用于字符串, %c格式化2字节位字符'
		语法关键词字典['判断文本'] = """/*判断是否为字母:unicode.IsLetter(文本字符串)
		判断是否为数字:unicode.IsDigit(文本字符串)
		判断是否为空白符号:unicode.IsSpace(文本字符串)*/"""
		语法关键词字典['其它条件'] = '} else if 逻辑型条件 == 2 { //其它条件'
		语法关键词字典['否则'] = '} else { // 否则'
		语法关键词字典['否'] = 'false//否'

		语法关键词字典['文本'] = 'string'
		语法关键词字典['点数'] = 'float32'
		语法关键词字典['字典传递'] = """func 模具一传递(字典 map[string]string) {//int Go 中不存在引用传递,所有的参数传递都是值传递'
				fmt.Printf("字典:值: %d \n", 字典)
	}"""

		语法关键词字典['列表传递'] = """func 模具一一列表传递(列表 []string) {//int Go 中不存在引用传递,所有的参数传递都是值传递'
	
		fmt.Printf("列表:值: %d \n", 列表[0])
	}"""
		语法关键词字典['传递指针'] = """	初数 := 0
		初数的指针 := &初数 // 赋予指针 变更为 指针类型
		模具一运算(10, 5, 初数的指针)//传递三个值
		fmt.Printfln("两数相乘:", *初数的指针) // *指针的变量
	
		func 模具一运算(值一, 值二 int, 初数的指针 *int) {// *int 整数指针类型
		*初数的指针 = 值一 * 值二
	}"""
		语法关键词字典['数组传递'] = """	浮点数数组 := [3]float64{7.0, 8.5, 9.1}
		相加数 := 模具一一数组相加(&浮点数数组) // 必设为 & 传递列表指针 
	
		fmt.Println("列表数相加为: %f \n", 相加数)
	
		func 模具一一数组相加(a *[3]float64) (相加数 float64) {//数组必设为 *[3]
			for _, 数组值 := range a { // for 循环 列表 范围
				相加数 = 相加数 + 数组值
			}
			return
	} """
		语法关键词字典['列表追加'] = """列表三 = append(列表三,4,)   //追加  追加的元素必须和原切片的元素同类型 """
		语法关键词字典['列表复制'] = """复制列表个数 := copy(主体列表, 复制的列表) // 合并复制入主体列表"""
		语法关键词字典['等待'] = """time.Sleep(10 * time.Second)// 等待秒数 """
		try:
			self.文本内容 = self.文本内容.replace(self.无空格文本内容, 语法关键词字典[self.无空格文本内容])  # 替换   , 1) 次数 1
		except KeyError:  # 异常处理
			return  # 返回
		else:
			return  # 返回


	def 模具一一文本关键词替换清洗(self):
		文本关键词字典 = {}  # 语法关键词字典['字']='典' 符号字典[] = """ """
		文本关键词字典['替换二'] = """	re, _ = regexp.Compile(".{0,}?") //re规则
				替换后文本 = re.ReplaceAllString(原文本, "替换字符") """  # re正则式
		文本关键词字典['提取'] = """ """  # re正则式
 
		文本关键词字典['替换'] = """清洗后文本 := strings.Replace(原文本, 规则字符, "b25", -1)// 替换次数 -1 则替换所有 """
		文本关键词字典['空格'] = """清洗空格后文本 = strings.TrimSpace(原文本)//剔除字符串开头和结尾的空白(空格)符号 """
		文本关键词字典['空格二'] = """剔除字符后文本 = strings.Trim(原文本, "a")//开头和结尾的 字符 除掉. 剔除开头 TrimLeft,剔除结尾 TrimRight"""
		文本关键词字典['文本包含'] = """对否 = strings.Contains(原文本, "a")//判断 原文本 是否包含 规则字符串 """
		文本关键词字典['文本转列表'] = """分割的列表 = strings.Split(原文本, "a") // 以 分割符号 分割成列表"""
		文本关键词字典['列表转文本'] = """文本 = strings.Join(原列表, "") //列表 拼接为文本, ""为空白的 连接符号,可以是其它 字符 """
		文本关键词字典['数字转文本'] = """数字文本= strconv.Itoa(数字)// 数字转 文本  """
		文本关键词字典['文本转数字'] = """文本换数字, _ = strconv.Atoi(原文本)// 文本换数字 """
		文本关键词字典['判断开头'] = """对否 = strings.HasPrefix(原文本, 规则字符)//判断 原文本 是否以 规则字符串 开头 前缀 """
		文本关键词字典['出现次数'] = """次数 = strings.Count(原文本, 规则字符) //次数 整数 .//规则字符串 出现的非重叠次数 """

		try:
			self.文本内容 = str(self.文本内容).replace(self.无空格文本内容, 文本关键词字典[self.无空格文本内容])  # 替换   , 1) 次数 1
		
		
		except KeyError as 异常:  # 异常处理
			
			return  # 返回
		else:
			return  # 返回


	def 模具一一导入模具替换清洗(self):
		导入模具字典 = {}  # 导入模具字典['字典遍历'] = """"""
		导入模具字典['字典遍历'] = """for 键 := range 文本字典 {.
			fmt.Println("文本字典%s: ", 键, "值为%s \n", 文本字典[键])
		}"""
		导入模具字典['列表遍历'] = """for _, 值 := range 列表 { //  _, 忽略
	
			fmt.Println("%s \n", 值) //%c 格式化2字节位 %d 整数 %f 点数
		}"""
		导入模具字典['文本遍历'] = """for 计数器 := 0; 计数器 < len(文本); 计数器 = 计数器 + 1 {
			fmt.fmt.fmt.Printfff("遍历%d 字符串%c\n", 计数器, 范围[计数器])//%c 两字节
		}"""
		导入模具字典['如果'] = """if 逻辑型条件 == 0 { /* break//结束循环、continue//跳过本次循环、goto//跳转到 或者 return//返回 对否=false//否 
					 非 !(!T )、并 &&(T && T)、或 ||(T || T)
					 ==、!= 、<、<=、>、>=*/
		fmt.Println("相等\n")
	} else if 逻辑型条件 == 2 { //其它条件
		fmt.Println("其它条件相等\n")
	
	} else { // 否则
		fmt.Println("不相等\n")"""
		导入模具字典['如果对否'] = """if 对否 { // !(对否) 相反结果
		if 条件 == 0 { /* break//结束循环、continue//跳过本次循环、goto//跳转到 或者 return//返回 对否=false//否 
					 非 !(!T )、并 &&(T && T)、或 ||(T || T)
					 ==、!= 、<、<=、>、>=*/
			对否=false//否 
	}
		fmt.Println("对\n")
	} else {
		fmt.Println("否\n")
	}"""
		导入模具字典['多项条件'] = """	switch 比较数值 { //多项条件 比较数值= 98
		/* break//结束循环、continue//跳过本次循环、goto//跳转到 或者 return//返回 对否=false//否 
					 非 !(!T )、并 &&(T && T)、或 ||(T || T)
					 ==、!= 、<、<=、>、>=*/
		case 98: //条件一
			fmt.fmt.fmt.Printffln("大于 98")
		case 100: //条件二
			fmt.fmt.Printfln("等于 100")
		default: //否则
			fmt.fmt.Printfln("不存在于 98 或 100")
		}"""
		导入模具字典['整数模具'] = """func 模具一一整数模具(传入, x2 int) (返回值 int) {//string
		//defer 模具一untrace("a")//在return返回 后, 最终 执行的 命令	
		// return x2, x3
		return // 返回"""
		导入模具字典['文本模具'] = """func 模具一一文本模具(传入, x2 string)(返回值 string) {//int
		//defer 模具一untrace("a")//在return返回 后, 最终 执行的 命令	
		// return x2, x3
		return // 返回"""
		导入模具字典['执行时间'] = """	开始时间 := time.Now()
		
		结束时间 := time.Now()
		执行时间 := 结束时间.Sub(开始时间)
		fmt.Println("计算模具 执行时间: %s\n", 执行时间)"""
		导入模具字典['获取时间'] = """	
		时间 := time.Now()//获取当前时间
		fmt.Println("%s\n", 时间)
		fmt.Println("%02d.%02d.%4d\n", 时间.Day(), 时间.Month(), 时间.Year())"""

		导入模具字典['错误数'] = """	if 错误数 != nil { //非零
			fmt.Println("错误原因 : ", 错误数)
			
			//  break//结束循环、continue//跳过本次循环、goto//跳转到 或者 return//返回
		}"""
		导入模具字典['每行读取文件'] = """	文件路径 = "F:\\影视发帖推广\\可以注册手机号码.txt"
		文件缓存, 错误数 = os.Open(文件路径)
		if 错误数 != nil { //非零
			fmt.Printf("打开输入文件时发生错误\n" +
				"文件是否存在?\n" +
				"你有没有权限访问它?\n")
			return // 返回
		}
		defer 文件缓存.Close()//关闭
	
		文件内容 = bufio.NewReader(文件缓存)
	
		for {
			每行内容, 错误数 = 文件内容.ReadString('\n') //Windows的行结束符是 \r\n.在使用 ReadString 和 ReadBytes ,直接使用 \n 就可以了
			fmt.Printf("每行内容: %s", 每行内容)
			if 错误数 == io.EOF { // true
				fmt.Printf("每行内容错误:\n",错误数)
				return // 返回
			}
		}"""
		导入模具字典['读取文件'] = """	/*导入库
		"ioutil"
		*/
			文件路径 = "F:\\影视发帖推广\\可以注册手机号码.txt"
		文件内容, 错误数 = ioutil.ReadFile(文件路径)
		if 错误数 != nil {
			fmt.Fprintf(os.Stderr, "读取文件异常原因: %s\n", 错误数)
			// panic(读取文件异常原因.读取文件异常原因or())
		}
		fmt.Printf("文件内容 :\n%s\n", string(文件内容))"""
		导入模具字典['写入文件'] = """	/*导入库
		"bufio"
		*/
		文件路径 = "F:\\影视发帖推广\\临时文本.txt"
		文件缓存, 错误数 = os.OpenFile(文件路径, os.O_WRONLY|os.O_CREATE, 0666)
		/*常会用到以下标志:
			  os.O_RDONLY:只读
			  os.O_WRONLY:只写(部分修改)
			  os.O_CREATE:创建:如果指定文件不存在,就创建该文件.
			  os.O_TRUNC:(全部重写)截断:如果指定文件已存在,就将该文件的长度截为0.
		  写文件时,不管是 Unix 还是 Windows,文件的权限都需要使用 0666.
		*/
		if 错误数 != nil {//非零
			fmt.Printf("文件打开或创建时出错\n")
			return //返回
		}
		defer 文件缓存.Close() //缓存关闭
	
		文件写入 = bufio.NewWriter(文件缓存)
		写入内容 = "开或\r\n" // WIN系统 换行为 \r\n
		文件写入.WriteString(写入内容)
		文件写入.Flush() // 文件写入完成
		fmt.Printf("文件写入完成\n")"""
		导入模具字典['输入'] = """	/*导入库
		"bufio"
		*/
		等待输入 = bufio.NewReader(os.Stdin)
		fmt.Println("请等待输入内容 ,回车 确认键结束: ")
		输入的内容, 输入错误数 = 等待输入.ReadString('\n') // 输入以  \n 回车 确认键结束
		if 输入错误数 != nil {
			fmt.Printf("错误原因: %s\n", 错误数)
	
		}
		fmt.Printf("输入的内容: %s\n", 输入的内容)"""
		导入模具字典['文件复制'] = """	/*导入库
		"io"
		*/
		//设定 文件复制(目标文件, 源文件)
		文件缓存, 错误数 = os.Open(源文件) //打开文件
		if 错误数 != nil {// 非零
			fmt.Printf("打开文件错误\n",错误数)
			return
		}
		defer 文件缓存.Close()
		文件写入, 错误数 := os.OpenFile(目标文件, os.O_WRONLY|os.O_CREATE, 0644) //写入文件
		if 错误数 != nil {// 非零
			fmt.Printf("文件写入错误\n",错误数)
			return
		}
		defer 文件写入.Close()//关闭
		return io.Copy(文件写入, 文件缓存) //核心在这里,io.Copy 一行代码搞定"""

		导入模具字典['模板'] = """"""
		导入模具字典['模板'] = """"""

		try:
			self.文本内容 = self.文本内容.replace(self.无空格文本内容, 导入模具字典[self.无空格文本内容])  # 替换   , 1) 次数 1
		except KeyError:  # 异常处理
			return  # 返回
		else:
			return  # 返回


	def 模具一一模板(self):
		pass

if __name__ == '__main__':
	GO语言一字符替换 = 类一一GO语言一字符替换()
