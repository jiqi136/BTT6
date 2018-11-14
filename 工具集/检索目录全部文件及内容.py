# -*- coding:utf-8


import os  # 本地操作



import pyautogui  # 弹窗




class 类一一检索目录全部文件及内容:  # 调用 类的模具 self.模具一一数据库()
	def __init__(self):
		self.循环 = 0
		self.测试打印=''

		self.循环的弹窗内容 = '输入要检索目录路径,\n ⑴ 完成 点"ok”:进入下一步 \n⑵ 点否"Cancel”: 退出检索程序 '

		self.跳过循环 = ''
		self.文本路径 = ''
		self.目标目录= '1'

		while self.循环 == 0:  # 条件循环


			self.文本内容合成 = ''

			if len(self.目标目录)==1:
				self.模具一一弹窗输入目标目录字符串()
				self.循环的弹窗内容 = '输入要要检索文件内容,\n ⑴ 完成 点"ok”:开始检索 \n⑵ 点否"Cancel”: 退出检索程序 '
				if self.循环 == 998:
					break  # 结束循环
				elif '跳过循环 ' in self.跳过循环:
					continue  # 跳过循环

			self.模具一一弹窗输入检索文件内容()
			if self.循环 == 998:
				break  # 结束循环

			elif '跳过循环 ' in self.跳过循环:
				continue  # 跳过循环

			self.模具一一弹窗输入检索类型()
			if self.循环 == 998:
				break  # 结束循环

			elif '跳过循环 ' in self.跳过循环:
				continue  # 跳过循环
			"""
			开始检索
			"""
			self.模具一一查看变量输出文本值("开始检索", "")
			self.模具一一展开目录下全部子目录与子文件()
			self.模具一一检索文件及内容()

	"""          1      """



	def 模具一一弹窗输入目标目录字符串(self):

		self.目标目录 = pyautogui.prompt(self.循环的弹窗内容)

		if 'None' in str(self.目标目录):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
			self.模具一一查看变量输出文本值("目标目录 空值", self.目标目录, 5)
			self.循环 = 998
			return  # 返回

		elif len(self.目标目录) == 0:
			self.目标目录 = "E:\go学习文件\src"
			self.模具一一查看变量输出文本值("默认目录", self.目标目录, 5)

		# self.跳过循环 = '跳过循环 '

		else:  # 否则

			return  # 返回

	def 模具一一弹窗输入检索文件内容(self):
		self.检索文件内容的弹窗内容 = '请输入要检索文件内容,\n ⑴ 完成 点"ok”:开始检索 \n⑵ 点否"Cancel”: 退出检索程序 '

		self.检索文件内容 = pyautogui.prompt(self.检索文件内容的弹窗内容)# 输入字符串

		if 'None' in str(self.检索文件内容):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
			self.模具一一查看变量输出文本值("None", self.检索文件内容,5)
			self.循环 = 998
			return  # 返回

		elif len(self.检索文件内容) == 0:
			self.模具一一查看变量输出文本值("字数为 0", self.检索文件内容, 5)

			self.跳过循环='跳过循环 '

		else:  # 否则
			self.模具一一查看变量输出文本值("完成 输入", self.检索文件内容, 5)
			return  # 返回

	def 模具一一弹窗输入检索类型(self):
		self.检索类型弹窗内容 = '输入文件的检索类型,\n ⑴ 输入一位字符为检索 模具  \n⑵ 输入二位字符为检索 打印文本 '

		self.检索类型 = pyautogui.prompt(self.检索类型弹窗内容)  # 输入字符串

		if 'None' in str(self.检索文件内容):  # break # 结束循环 continue # 跳过当前循环,继续进行下一轮循环
			self.模具一一查看变量输出文本值("None", self.检索类型, 5)
			self.循环 = 998
			return  # 返回

		elif len(self.检索文件内容) == 0:
			self.模具一一查看变量输出文本值("字数为 0", self.检索类型, 5)

			self.跳过循环 = '跳过循环 '

		else:  # 否则
			self.模具一一查看变量输出文本值("完成 输入", self.检索类型, 5)
			return  # 返回
	"""        2     """

	def 模具一一展开目录下全部子目录与子文件(self):

		self.递归子目录列表=[]
		self.递归子文件列表 = []

		self.模具一一递归展开目录与文件(self.目标目录)


	def 模具一一递归展开目录与文件(self,目标目录):

		子目录列表与文件列表 = os.listdir(目标目录)  # 分离出目录列表与文件列表
		for 子目录或文件 in 子目录列表与文件列表:
			根目录的子目录或文件路径 = os.path.join(目标目录, 子目录或文件)
			if os.path.isdir(根目录的子目录或文件路径):  # 判断 是否为 文件夹  判断文件 os.path.isfile
				# os.path.isfile() 函数判断某一路径是否为文件
				子目录 = 根目录的子目录或文件路径
				self.递归子目录列表.append(子目录)  # 列表追加
				self.模具一一查看变量输出文本值("子目录", 子目录, 8)

				self.模具一一递归展开目录与文件(子目录)

			else:  # 否则 为文件
				子文件 = 根目录的子目录或文件路径
				self.模具一一查看变量输出文本值("子文件", 子文件, 8)
				self.递归子文件列表.append(子文件)  # 列表追



	def 模具一一检索文件及内容(self):

		for 递归子文件 in self.递归子文件列表:
			if ".py" in 递归子文件 or  ".go" in 递归子文件 or  ".txt" in 递归子文件 or  ".doc" in 递归子文件:
				if   ".gox" in 递归子文件:
					continue  # 跳过当前循环
				文本内容列表=self.模具一一读取与写入文件(递归子文件, 操作类型="每行读取", 内容='', 写入类='w')  #
				"""操作类型="读取"  or    操作类型="每行读取"  
				操作类型="写入"  or   操作类型="格式写入"
				默认 内容=''
				默认 重写 'w'   or 追加 写入类='a' 
				"""
				行数计数=0
				for 行 in 文本内容列表:
					行数计数 =行数计数+1

					if len(self.检索类型)==1: # 检索模具#  break # 结束循环 continue # 跳过当前循环，继续进行下一轮循环
						if "def " in 行 or "func " in 行:
							if self.检索文件内容 in 行:
								self.模具一一查看变量输出文本值("检索内容: {} 在文件".format(self.检索文件内容), 递归子文件)
								self.模具一一查看变量输出文本值("行数", str(行数计数))
								self.模具一一查看变量输出文本值("内容:", 行)
								self.模具一一查看变量输出文本值("/////////////////////", "")

					else:# 否则  检索打印 文本内容
						if "'" in 行 or '"' in 行:

							if self.检索文件内容 in 行:
								self.模具一一查看变量输出文本值("检索内容: {} 在文件".format(self.检索文件内容), 递归子文件)
								self.模具一一查看变量输出文本值("行数", str(行数计数))
								self.模具一一查看变量输出文本值("内容:", 行)
								self.模具一一查看变量输出文本值("/////////////////////", "")

		self.模具一一查看变量输出文本值("\n\n================检索内容,成功完成======================================================================\n\n\n", "")
		self.循环的弹窗内容 = '检索内容,成功完成.\n ⑴ 继续 :输入要检索文件内容,完成 点"ok”:继续相同目录再检索 \n⑵ 点否"Cancel”: 退出再启动,更换检索目录 \n⑶ 点否"Cancel”: 退出检索程序'

	"""        公共库    """

	def 模具一一查看变量输出文本值(self, 变量名, 变量文本值, 测试输入=0):

		if 测试输入 == 0:
			print(变量名, ': ', 变量文本值)
		elif len(self.测试打印) != 0:
			print(变量名, ': ', 变量文本值)

	def 模具一一读取与写入文件(self, 文件路径, 操作类型, 内容, 写入类='w'):  # 内容='格式写入'  写入类='a'   追加
		pass
		"""self.模具一一读取与写入文件(文件路径, 操作类型="每行读取", 内容='', 写入类='w')  #
				操作类型="读取"  or    操作类型="每行读取"  
				操作类型="写入"  or   操作类型="格式写入"
				默认 内容=''
				默认 重写 'w'   or 追加 写入类='a' 
		"""
		文本内容列表=''
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

	def 模具一一模板(self):
		pass

检索目录全部文件及内容=类一一检索目录全部文件及内容()