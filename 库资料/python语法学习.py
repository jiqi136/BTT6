语法
	基础
		基础语法
			编码
				默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
				在 Windows 下可以不写第一行注释:
					#!/usr/bin/python3
					第一行注释标的是指向 python 的路径，告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
					此外还有以下形式（推荐写法）：
					#!/usr/bin/env python3
				如下实例：
			
				这种用法先在 env（环境变量）设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。
			标识符
							
				第一个字符必须是字母表中字母或下划线'_'。
				标识符的其他的部分有字母、数字和下划线组成。
				标识符对大小写敏感。
				在Python 3中，非-ASCII 标识符也是允许的了。
            
			python保留字
				保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
				>>> import keyword
				>>> keyword.kwlist
				['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
			
			注释
				Python中单行注释以 # 开头，实例如下：
					#!/usr/bin/python3
					# 第一个注释
					print ("Hello, Python!") # 第二个注释
				多行注释可以用多个 # 号：
					#!/usr/bin/python3
					# 第一个注释
					# 第二个注释
			
			行与缩进
				 python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
				缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
					if True:
						print ("True")
					else:
						print ("False")
				以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
					if True:
						print ("Answer")
						print ("True")
					else:
						print ("Answer")
					  print ("False")    # 缩进不一致，会导致运行错误
				以上程序由于缩进不一致，执行后会出现类似以下错误：
					 File "test.py", line 6
						print ("False")    # 缩进不一致，会导致运行错误
														  ^
					IndentationError: unindent does not match any outer indentation level
			
			多行语句
				Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
					total = item_one + \
							item_two + \
							item_three
				在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
					total = ['item_one', 'item_two', 'item_three',
                            'item_four', 'item_five']
			
			数据类型
				python中数有四种类型：整数、长整数、浮点数和复数。
				    整数， 如 1
					长整数 是比较大的整数
					浮点数 如 1.23、3E-2
					复数 如 1 + 2j、 1.1 + 2.2j
			
			字符串
				python中单引号和双引号使用完全相同。
				使用三引号(三引号括号内合并括号外)(''或"")'")可以指定一个多行字符串。
				 转义符 '\'
				自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
				python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
				字符串是不可变的。
				按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。 
					word = '字符串'
					sentence = "这是一个句子。"
					paragraph = """这是一个段落，
					可以由多行组成"""
			
			空行
				函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
				空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
				记住：空行也是程序代码的一部分。
			
			等待用户输入
				执行下面的程序在按回车键后就会等待用户输入：
					#!/usr/bin/python3
                    input("\n\n按下 enter 键后退出。")
				以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下键时，程序将退出。
				
			同一行显示多条语句
				Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
					#!/usr/bin/python3
					import sys; x = 'runoob'; sys.stdout.write(x + '\n')
				执行以上代码，输入结果为：
					$ python3 test.py
					runoob
			
			多个语句构成代码组
				缩进相同的一组语句构成一个代码块，我们称之代码组。
				像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
				我们将首行及后面的代码组称为一个子句(clause)。
					if expression : 
					   suite
					elif expression : 
					   suite 
					else : 
					   suite
			Print 输出
				rint 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
					#!/usr/bin/python3
					x="a"
					y="b"
					# 换行输出
					print( x )
					print( y )
					print('---------')
					# 不换行输出
					print( x, end=" " )
					print( y, end=" " )
					print()
				以上实例执行结果为：
					a
					b
					---------
					a b
			import 与 from...import
				在 python 用 import 或者 from...import 来导入相应的模块。
				将整个模块(somemodule)导入，格式为： import somemodule
				从某个模块中导入某个函数,格式为： from somemodule import somefunction
				从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
				将某个模块中的全部函数导入，格式为： from somemodule import *
					导入 sys 模块
					
						import sys
						print('================Python import mode==========================');
						print ('命令行参数为:')
						for i in sys.argv:
							print (i)
						print ('\n python 路径为',sys.path)
					
					导入 sys 模块的 argv,path 成员
						
						from sys import argv,path  #  导入特定的成员
						 
						print('================python from import===================================')
						print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
			命令行参数
				很多程序可以执行一些操作来查看一些基本信，Python可以使用-h参数查看各参数帮助信息：
					$ python -h
					usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
					Options and arguments (and corresponding environment variables):
					-c cmd : program passed in as string (terminates option list)
					-d     : debug output from parser (also PYTHONDEBUG=x)
					-E     : ignore environment variables (such as PYTHONPATH)
					-h     : print this help message and exit
					[ etc. ]
				我们在使用脚本形式执行 Python 时，可以接收命令行输入的参数，具体使用可以参照 Python 3 命令行参数
		基本数据类型
			等号（=）用来给变量赋值
				 Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
				在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
				等号（=）用来给变量赋值。
				等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。
			多个变量赋值						
				 Python允许你同时为多个变量赋值。例如：
				    a = b = c = 1
				以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
				您也可以为多个对象指定多个变量。例如：
				    a, b, c = 1, 2, "runoob"
				以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。	
			标准数据类型						
				Python3 中有六个标准的数据类型：
				
				Number（数字）
				
				String（字符串）（文本）
				List（列表）（文本集合表）
				
				Tuple（元组）
				Sets（集合）
				Dictionary（字典）
					
					
	网页
		调用模块
			
		Http网页请求
					接收网页
						请求的网址
						浏览器头部
							浏览器类型
							本地系统类型
							COOKIE
							源码保存至变量
					发送网页
						发送的网址
						浏览器头部
							浏览器类型
							本地系统类型
							COOKIE
							变量内容源码
					发送网页
		逻辑运算
				变量比较  （根据结果得出 对 与 否则  ）
						字符变量A包含字符变量B
						列表变量A包含字符变量B
						字符变量A等于字符字符变量B
						字符变量A长度比较计数变量B
							变量A和变量B比较结果
							大于
							小于
							等于
						计数器变量A比较计数器变量B
							变量A和变量B比较结果
							大于
							小于
							等于
						列表变量A元素个数比较计数器变量B
							变量A和变量B比较结果
							大于
							小于
							等于
						字符变量A以字符变量B开头
							变量A和变量B比较结果
							大于
							小于
							等于
				循环操作
					无限循环
					指定循环次数
					使用计数器变量
					循环指定列表
						保存每个循环变量至 文本A
					从数据库中查询数据
						查询语句
				跳出本次循环
				结束当前循环
				暂停等待
					等待指定的时间
						使用计数器变量的值
					随机时间
						从 A  到  B
					等待指定的元素出现
					等待指定的字符出现
					超过时间  A  秒
				跳转
					跳转到步骤
				结束流程
					成功，完成预期的整个流程
					失败，数据提取和预期不符
					失败，被目标服务器封IP
					失败，目标服务器内部异常
					失败，HTTP请求返回异常
					失败，用户没有登录
					失败，用户名或密码错误
					失败，登录帐号被禁用
					失败，当前数据已删除
					失败，未知异常
					其它提示信息
				引用脚本
				
				
					
		变量处理
			变量处理
				要处理的变量 A  保存至新变量 B
				数据处理
					内容截取
					内容替换
						可用标签 （*）（参数）
						替换为标签 （参数1）（参数2）（参数N） 变量A和变量B
					HTML标签过滤
						链接<a
						表格<table
						表格行<tr
						单元<td
						段落<p
						......
					纯正则替换
					数据转换
						将结果转换为简体
						将结果转换为繁体
						自动转换为拼音
						时间修正转换
						论坛UBB转换
						大小写转换
					智能提取
						提取第一张图片
						提取邮箱
						提取手机号码
					高级功能
						自动摘要
						字符编码转换
						随机插入
							从一个文本文件 中随机读取N行，随机插入到标签内容里
						空内容缺省
							如果标签的值的空，用以下的字符串作为缺省值
						
						内容添加前后缀
							前字符串
							后字符串  可加变量A
						同义词替换
			变量重置
				字符变量
				列表变量
				计数器变量
				使用随机数填充字符变量
					随机3位数字
					随机5位字母
					随机3位汉字
					随机字母+数字
			清空变量
				操作对象  列表变量
				操作方式
					清空整个变量
					去掉为空的记录
					移除最后一条记录
					移除重复记录
					移除第一条记录
				内容必须包含  并  或
				内容不得包含
				排序
					升序
					降序
			循环提取 文本变量
				提取数据方式
				前后截取
				正则提取
				保存至列表变量
			提取网址
				必须包含
				不得包含
				网址补全  以当前网址作为标准补全相对网址，如果源码中是完整链接则不需要
			计数处理
				操作类型
					增加
					减少
					乘以
					除以（进一法）
					除以（四舍五入）
					重置
				操作数值 
					原始数值
					使用变量 A
			变量转化
				文本变量转化为计数器变量
				文本变量添加到列表变量
				列表变量合并为文本变量
				原列表变量合并到新列表变量
				列表变量个数转化为计数器变量
				文本变量长度转化为计数器变量
				合并字条串   【换行】
				字符转化为数字失败后返回0
			提取列表
				字符串分割
				使用正则表达式
				正则循环提取
				楼层类型分割
				保存至列表变量
			时间处理
				指定时间
				时间格式
				时间差转换
				时间差转换参考格式
				时间戳转换
				保存至变量
			随机取值
				从列表变量 取值到 文本变量
				第一
				最后
				随机
				指定
				取值后删除
			提取XML
					xmlpath
			提取JSON
					jsonpath
			提取浏览器缓存
					获取所有文件到时列表变量
					按查询获取文件地址列表到列表变量
					按查询结果获取单个 文件地址到字符变量
					获取所有网址到时列表变量
					按查询获取网址列表到列表变量
					按查询结果获取单个网址到字符变量
					查询条件    
					正则表达式
					获取数据后删除对应记录
		文件下载
			HTTP下载
			    载入Cookie
				下载文件网址
				保存文件夹
				文件名格式
				后缀名
				下载超时  秒
					自动跳转
				文件地址必含
			图文下载
				载入Cookie
				下载文件网址
				保存文件夹
				文件名格式
				后缀名
				下载超时  秒
					自动跳转
				文件地址必含
			文件下载
				载入Cookie
				下载文件网址
				保存文件夹
				文件名格式
				后缀名
				下载超时  秒
					自动跳转
				文件地址必含
		数据库操作
			执行SQL操作
		本地文件操作
			保存文本
				变量类型
					文本类型
					列表类型
				写入方式
					追加
					覆盖
				内容格式模式
					【换行】
				保存路径
				文件编码
			读取本地文本
				读取文本（全部读取，结果存入文本变量）
				读取文本（对读取内容进行分割，结果存入列表变量）
				分隔方式
					【换行】
					正则
				读取后删除文本（成功返回1，失败返回0，为文本变量）
				文本是否存在（存在返回1，不存在返回0，为文本变量）
				文件编码
				本地文本路径
				存入变量
			目录操作
				创建目录
				读取目录
				删除目录
				目录路径
			导出excel
				数据库查询语句
			配置文件INI读写
				保存配置
				读取配置
				节点名称
				文件路径
		其它操作
			邮件
				接收邮件
					登陆协议  
						POP3
						IMAP
					服务地址
						端口
						SSL
					邮箱帐号
					邮箱密码
				    邮件收取设置
						收取邮件数量
							全部
							第一封
						邮件内容存入变量
						发件人邮箱
						邮件标题包含字符
				发送邮件
					接收邮件
					登陆协议  
						POP3
						IMAP
					服务地址
						端口
						SSL
					邮箱帐号
					邮箱密码
				    邮件发送设置
						邮件收件人
						邮件标题
						邮件内容
			FTP上传
				主机
				端口
				用户名
				密码
				本地文件地址
				上传至FTP的目录
				被动模式
				执行命令
					删除文件
					列出文件
					创建目录
			拨号换IP
				ADSL拨号
				VPN拨号
				拨号前断开所有活动链接
				帐号设置
					用户名
					密码
					拨号结果保存至变量 （拨号成功返回0，拨号异常失败返回-1）
			调用外部程序
				程序文件路径
				启动参数
					等待进程完成
					隐藏窗口
			验证码配置
				本地图片识别
					下载图片
						通过HTTP文件下载
						或者网页截图所得
					图片所在路径
					验证码识别配置
					保存结果至变量
					超时时间  
				打码平台
					模板名称
				打码方式
		自定义代码
			运行C#代码
			外部插件
				C#
				PHP
				PYTHON
		多线程						
					
					
					
	网页
		调用模块
			
		Http网页请求
					接收网页
						请求的网址
						浏览器头部
							浏览器类型
							本地系统类型
							COOKIE
							源码保存至变量
					发送网页
						发送的网址
						浏览器头部
							浏览器类型
							本地系统类型
							COOKIE
							变量内容源码
					发送网页
		逻辑运算
				变量比较  （根据结果得出 对 与 否则  ）
						字符变量A包含字符变量B
						列表变量A包含字符变量B
						字符变量A等于字符字符变量B
						字符变量A长度比较计数变量B
							变量A和变量B比较结果
							大于
							小于
							等于
						计数器变量A比较计数器变量B
							变量A和变量B比较结果
							大于
							小于
							等于
						列表变量A元素个数比较计数器变量B
							变量A和变量B比较结果
							大于
							小于
							等于
						字符变量A以字符变量B开头
							变量A和变量B比较结果
							大于
							小于
							等于
				循环操作
					无限循环
					指定循环次数
					使用计数器变量
					循环指定列表
						保存每个循环变量至 文本A
					从数据库中查询数据
						查询语句
				跳出本次循环
				结束当前循环
				暂停等待
					等待指定的时间
						使用计数器变量的值
					随机时间
						从 A  到  B
					等待指定的元素出现
					等待指定的字符出现
					超过时间  A  秒
				跳转
					跳转到步骤
				结束流程
					成功，完成预期的整个流程
					失败，数据提取和预期不符
					失败，被目标服务器封IP
					失败，目标服务器内部异常
					失败，HTTP请求返回异常
					失败，用户没有登录
					失败，用户名或密码错误
					失败，登录帐号被禁用
					失败，当前数据已删除
					失败，未知异常
					其它提示信息
				引用脚本
				
				
					
		变量处理
			变量处理
				要处理的变量 A  保存至新变量 B
				数据处理
					内容截取
					内容替换
						可用标签 （*）（参数）
						替换为标签 （参数1）（参数2）（参数N） 变量A和变量B
					HTML标签过滤
						链接<a
						表格<table
						表格行<tr
						单元<td
						段落<p
						......
					纯正则替换
					数据转换
						将结果转换为简体
						将结果转换为繁体
						自动转换为拼音
						时间修正转换
						论坛UBB转换
						大小写转换
					智能提取
						提取第一张图片
						提取邮箱
						提取手机号码
					高级功能
						自动摘要
						字符编码转换
						随机插入
							从一个文本文件 中随机读取N行，随机插入到标签内容里
						空内容缺省
							如果标签的值的空，用以下的字符串作为缺省值
						
						内容添加前后缀
							前字符串
							后字符串  可加变量A
						同义词替换
			变量重置
				字符变量
				列表变量
				计数器变量
				使用随机数填充字符变量
					随机3位数字
					随机5位字母
					随机3位汉字
					随机字母+数字
			清空变量
				操作对象  列表变量
				操作方式
					清空整个变量
					去掉为空的记录
					移除最后一条记录
					移除重复记录
					移除第一条记录
				内容必须包含  并  或
				内容不得包含
				排序
					升序
					降序
			循环提取 文本变量
				提取数据方式
				前后截取
				正则提取
				保存至列表变量
			提取网址
				必须包含
				不得包含
				网址补全  以当前网址作为标准补全相对网址，如果源码中是完整链接则不需要
			计数处理
				操作类型
					增加
					减少
					乘以
					除以（进一法）
					除以（四舍五入）
					重置
				操作数值 
					原始数值
					使用变量 A
			变量转化
				文本变量转化为计数器变量
				文本变量添加到列表变量
				列表变量合并为文本变量
				原列表变量合并到新列表变量
				列表变量个数转化为计数器变量
				文本变量长度转化为计数器变量
				合并字条串   【换行】
				字符转化为数字失败后返回0
			提取列表
				字符串分割
				使用正则表达式
				正则循环提取
				楼层类型分割
				保存至列表变量
			时间处理
				指定时间
				时间格式
				时间差转换
				时间差转换参考格式
				时间戳转换
				保存至变量
			随机取值
				从列表变量 取值到 文本变量
				第一
				最后
				随机
				指定
				取值后删除
			提取XML
					xmlpath
			提取JSON
					jsonpath
			提取浏览器缓存
					获取所有文件到时列表变量
					按查询获取文件地址列表到列表变量
					按查询结果获取单个 文件地址到字符变量
					获取所有网址到时列表变量
					按查询获取网址列表到列表变量
					按查询结果获取单个网址到字符变量
					查询条件    
					正则表达式
					获取数据后删除对应记录
		文件下载
			HTTP下载
			    载入Cookie
				下载文件网址
				保存文件夹
				文件名格式
				后缀名
				下载超时  秒
					自动跳转
				文件地址必含
			图文下载
				载入Cookie
				下载文件网址
				保存文件夹
				文件名格式
				后缀名
				下载超时  秒
					自动跳转
				文件地址必含
			文件下载
				载入Cookie
				下载文件网址
				保存文件夹
				文件名格式
				后缀名
				下载超时  秒
					自动跳转
				文件地址必含
		数据库操作
			执行SQL操作
		本地文件操作
			保存文本
				变量类型
					文本类型
					列表类型
				写入方式
					追加
					覆盖
				内容格式模式
					【换行】
				保存路径
				文件编码
			读取本地文本
				读取文本（全部读取，结果存入文本变量）
				读取文本（对读取内容进行分割，结果存入列表变量）
				分隔方式
					【换行】
					正则
				读取后删除文本（成功返回1，失败返回0，为文本变量）
				文本是否存在（存在返回1，不存在返回0，为文本变量）
				文件编码
				本地文本路径
				存入变量
			目录操作
				创建目录
				读取目录
				删除目录
				目录路径
			导出excel
				数据库查询语句
			配置文件INI读写
				保存配置
				读取配置
				节点名称
				文件路径
		其它操作
			邮件
				接收邮件
					登陆协议  
						POP3
						IMAP
					服务地址
						端口
						SSL
					邮箱帐号
					邮箱密码
				    邮件收取设置
						收取邮件数量
							全部
							第一封
						邮件内容存入变量
						发件人邮箱
						邮件标题包含字符
				发送邮件
					接收邮件
					登陆协议  
						POP3
						IMAP
					服务地址
						端口
						SSL
					邮箱帐号
					邮箱密码
				    邮件发送设置
						邮件收件人
						邮件标题
						邮件内容
			FTP上传
				主机
				端口
				用户名
				密码
				本地文件地址
				上传至FTP的目录
				被动模式
				执行命令
					删除文件
					列出文件
					创建目录
			拨号换IP
				ADSL拨号
				VPN拨号
				拨号前断开所有活动链接
				帐号设置
					用户名
					密码
					拨号结果保存至变量 （拨号成功返回0，拨号异常失败返回-1）
			调用外部程序
				程序文件路径
				启动参数
					等待进程完成
					隐藏窗口
			验证码配置
				本地图片识别
					下载图片
						通过HTTP文件下载
						或者网页截图所得
					图片所在路径
					验证码识别配置
					保存结果至变量
					超时时间  
				打码平台
					模板名称
				打码方式
		自定义代码
			运行C#代码
			外部插件
				C#
				PHP
				PYTHON
		多线程	
实例
		导入模块库
								导入模块库 网页请求库
					导入模块库 网页分析库
					导入模块库 网页错误库
					导入模块库 http甜点库
					
					
					
										import urllib.request
					import urllib.parse
					import urllib.error
					import http.cookiejar
		

		浏览器 http访问头 user agent 字段大全 
								淘宝浏览器2.0 on Windows 7 x64：

					Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11

					猎豹浏览器2.0.10.3198 急速模式on Windows 7 x64：

					Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER

					猎豹浏览器2.0.10.3198 兼容模式on Windows 7 x64：

					Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)

					猎豹浏览器2.0.10.3198 兼容模式on Windows XP x86 IE6：

					Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"

					 

					 

					猎豹浏览器1.5.9.2888 急速模式on Windows 7 x64：

					Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER

					猎豹浏览器1.5.9.2888 兼容模式 on Windows 7 x64：

					Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

					QQ浏览器7.0 on Windows 7 x64 IE9：

					Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)

					QQ浏览器7.0 on Windows XP x86 IE6：

					Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)

					360安全浏览器5.0自带IE8内核版 on Windows XP x86 IE6：

					Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)

					 

					360安全浏览器5.0 on Windows XP x86 IE6：

					Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)

					360安全浏览器5.0 on Windows 7 x64 IE9：

					Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

					360急速浏览器6.0 急速模式 on Windows XP x86：

					Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1

					360急速浏览器6.0 急速模式 on Windows 7 x64：

					Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1

					360急速浏览器6.0 兼容模式 on Windows XP x86 IE6：

					Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)

					360急速浏览器6.0 兼容模式 on Windows 7 x64 IE9：

					Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

					360急速浏览器6.0 IE9/IE10模式 on Windows 7 x64 IE9：

					Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)

					搜狗浏览器4.0 高速模式 on Windows XP x86：

					Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0

					搜狗浏览器4.0 兼容模式 on Windows XP x86 IE6：

					Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)

					 

					Waterfox 16.0 on Windows 7 x64：

					Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0

					Ipad：

						Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5

					 

					Firefox x64 4.0b13pre on Windows 7 x64：

						Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre

					 

					Firefox x64 on Ubuntu 12.04.1 x64：

					Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0

					Firefox x86 3.6.15 on Windows 7 x64：

						[HTTP_USER_AGENT] => Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15

					 

					Chrome x64 on Ubuntu 12.04.1 x64：

					Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11

					Chrome x86 23.0.1271.64 on Windows 7 x64：

					Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11

					Chrome x86 10.0.648.133 on Windows 7 x64：

						Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16

					 

					IE9 x64 9.0.8112.16421 on Windows 7 x64：

						Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)

					 

					IE9 x86 9.0.8112.16421 on Windows 7 x64：

						Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)

					 

					Firefox x64 3.6.10 on ubuntu 10.10 x64：

						Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10

					 

					andorid 2.2自带浏览器，不支持HTML5视频

					  Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
		拨号重连换IP
						import os
			import time

			os.system(r"rasphone -h 宽带连接") #xxx0是你的拨号名称，xp下默认是“宽带连接”。
			os.system(r"rasdial 宽带连接 02007044432@163.gd  77341859") #xxx0同上，xxx1 拨号用户名 ，xxx2拨号密码。

			time.sleep(3) 
			 


			input("\n\n按下 确认键enter 键后退出.")
		网页文件下载
			详解
								import urllib.request  
				#首先需要导入用到的模块：urllib.request
				hearder={
				   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
				}
				#设置一些Headers信息,让爬虫模拟成浏览器访问页面
				headers = {  
						'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
					}
				url="https://www.zhihu.com"  
				#变量的url网址
				提交数据集=urllib.request.Request(网址,headers=头部)
				请求的答复=urllib.request.urlopen(提交数据集).read()
				#保存时的“w”可写.decode('utf-8')看情况添加，“WB”可写不添加
				#urllib.request.urlopen(url)，打开并爬取变量(url)的网页
				#read()读取全部，
				#读取内容常见的有3种方式，其用法是：
				#1. read()读取文件的全部内容，与readlines()不同的是，read()会把读取到的内容赋给一个字符串变量。
				#2. readlines()读取文件的全部内容，readlines()会把读取到的内容赋值给一个列表变量。
				#3. readline()读取文件的一行内容。
				#decode网站的编码。互联网上使用最广的UTF-8编码，Windows系统则是gbk, gb2312
				#写入文件中
				#我们已经成功实现了一个网页的爬取，那么我们如何将爬取的网页以网页的形式保存在本地呢？
				#思路如下：
				#1. 爬取一个网页并将爬取到的内容读取出来赋给一个变量。
				#2. 以写入的方式打开一个本地文件，命名为*.html等网页格式。
				#3. 将步骤1中的变量写入该文件中。
				#4. 关闭该文件
				#我们刚才已经成功获取到了百度首页的内容并读取赋给了变量data，接下来，可以通过以下代码实现将爬取到的网页保存在本地。
				fh=open("c://baidu2.html","w")# r只读，w可写，a追加
				#open读取内容，"c://baidu2.html"保存文件的本地位置与名称
				fh.write(get)
				#写入变量(get)至文件 
				#读取  A=fh.read()
				fh.close()
				#关闭文件
				print(get)  
				#
				input("\n\n按下 确认键enter 键后退出。")
			短例
					import urllib.request
					import urllib.parse
					网址='http://3e38.com'
					头部={
					   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
					}
					发送=urllib.request.Request(网址,headers=头部)
					读取=urllib.request.urlopen(发送).read()
					fhandle=open("./1.html","wb")
					fhandle.write(读取)
					fhandle.close()
					input("\n\n按下 确认键enter 键后退出。")
					
					
		提交数据
			详解
									导入、 网页请求库、
					导入、 网页分析库、
					
					
					#为了整齐，开始处设定“头部信息”
					网址=‘http://www.iqianyue.com/mypost’
					数据=｛"name"：‘fengxin’，"pass"：‘123’｝#必须是中括号｛
					#查看网页的源代码，查找form，必要是<>内的内容关键字，一项一项复制，切勿复制表外的项内容
					数据编码=网页分析库、。网页进行编码、（数据）。进行编码、（‘UTF8’）#UTF8能转换为小写
					提交数据集=网页请求库、。请求、（网址，数据编码）# 请求Request须是开头字母大写
					#提交数据集=网页请求库、。请求、（网址，数据编码，头部属性、=头部信息）另一种方式“头部属性”放在最后
					请求的答复=网页请求库、。打开网页、（提交数据集）
					文件、打开、（“。/提交数据4.HTML”，二进制写入、）# 符号/无法写入只能是复制，或者直接删除。/也能创建于同级目录里。HTML能转换为小写
					文件、。写入、(请求的答复。读取全部、)
					文件、。关闭、
					退出、
			简例
									import urllib.request
					import urllib.parse
					网址='http://www.iqianyue.com/mypost'
					数据={"name":'fengxin',"pass":'123'}
					数据编码=urllib.parse.urlencode(数据).encode('utf8')
					提交数据集=urllib.request.Request(网址,数据编码)# 请求Request须是开头字母大写
					请求的答复=urllib.request.urlopen(提交数据集)
					fhandle=open("./提交数据4.html","wb")
					fhandle.write(请求答复.read())
					fhandle.close()
					input("\n\n按下 确认键enter 键2后退出.")
		甜点的全局安装与保存于文件
			详解
									#设置保存甜点信息的文件，同级目录下的甜点信息.txt
					文件名 = '甜点信息.txt'
					#使用http甜点库.甜点器()创建甜点器对象
					甜点信息=http甜点库.甜点器(文件名)
					#使用HTTP甜点处理器创建甜点信息处理器，并以其为参数构建开启器对象
					处理者=网页请求库.HTTP甜点处理器(甜点信息)
					安装者=网页请求库.构建_开启器(处理者)
					#将开启器安装为全局
					网页请求库.安装_开启器(安装者)
			简例
									#设置保存甜点信息的文件,同级目录下的甜点信息.txt
					文件名 = '甜点信息.txt'
					#使用http甜点库.甜点器()创建甜点器对象
					甜点信息=http.cookiejar.CookieJar(文件名)
					#使用HTTP甜点处理器创建甜点信息处理器,并以其为参数构建开启器对象
					处理者=urllib.request.HTTPCookieProcessor(甜点信息)
					安装者=urllib.request.build__opener(处理者)
					#将开启器安装为全局
					urllib.request.install__opener(安装者)
		异常错误
			详解
									尝试:
						答复=网页请求库.打开网页(请求)
					异常 网页错误库.HTTP错误 as e:
						｛显示｝(e.编码)
						｛显示｝(e.原因)
						#					try语句按照如下方式工作；
						#首先，执行try子句（在关键字try和关键字except之间的语句）
						#如果没有异常发生，忽略except子句，try子句执行后结束。
						#如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
						#如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
					#一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
					#处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
					#一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
					#except (RuntimeError, TypeError, NameError):
					#pass
				简例
										try:
						reponse=urllib.request.urlopen(request)
					except urllib.error.HTTPError as e:
						print(e.code)
						print(e.reason)
		第二次网页文件下载
			详解
									网页2='http://bbs.chinaunix.net/forum-327-1.html'
					请求的答复2=网页请求库.打开网页(网页)
					文件2=打开('./test2.html','wb')
					文件2.写入(请求的答复2.读取全部())
					文件2.关闭()
			简例
									网页2='http://bbs.chinaunix.net/forum-327-1.html'
					请求的答复2=urllib.request.urlopen(网页2)
					文件2=open('./test2.html','wb')
					文件2.write(请求的答复2.read())
					文件2.close()
		函数（变数）
								def 函数名（参数列表）:
					函数体
					def #定义变数 变数名（被代替的变数）
					函数体
					return;
					
					函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
					任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
					函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
					函数内容以冒号起始，并且缩进。
					return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。		
		表达式
			匹配范围
					match 从字符串的开头开始匹配
					。#匹配成功，返回Match对象，失败则返回None，若要完全匹配，子字符串要以$结尾。
					search 是从字符串任意位置开始匹配
					，#成功返回Match对象，否则返回None，注意，如果中存在多个子串，只返回第一个。
					上面两个都是匹配上一个就停止。
					findall 是返回所有能匹配上的字符串列表。
			group()
			·						group()：母串中与模式pattern匹配的子串；
					group(0)：结果与group()一样；
					groups()：所有group组成的一个元组，group(1)是与patttern中第一个group匹配成功的子串，group(2)是第二个，依次类推，如果index超了边界，抛出IndexError；
					findall()：返回的就是所有groups的数组，就是group组成的元组的数组，母串中的这一撮组成一个元组，那一措组成一个元组，这些元组共同构成一个list，就是findall()的返回结果。另，如果groups是只有一个元素的元组，findall的返回结果是子串的list，而不是元组的list了。
					http://blog.csdn.net/djskl/article/details/44357389
			元字符
									"^" ：^会匹配行或者字符串的起始位置，有时还会匹配整个文档的起始位置。 
					"$"  ：$会匹配行或字符串的结尾。
					"\w"：匹配字母，数字，下划线。
					"\b" :不会消耗任何字符只匹配一个位置，常用于匹配单词边界。
					单词边界符能够匹配中文符号、英文符号、空格、制表符、回车符号，以及各种边界，比如单词在开头，单词在结尾。
					例如，想从字符串中"This is Regex"匹配单独的单词 "is" 正则就要写成 "\bis\b" 。
					\b 不会匹配is 两边的字符，但它会识别is 两边是否为单词的边界。
					"\s"：匹配空格 。
					"\d"：匹配一个数字。
					"."：匹配除了换行符以外的任何字符。"\w"不能匹配空格，而"."可以。
					"[abc]":字符组，匹配包含括号内元素的字符。
					"|":或。A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
			元字符(举例)
									举例：
					在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，.可以匹配任意字符，所以：
						'00\d'可以匹配'007'，但无法匹配'00A'
						'\d\d\d'可以匹配'010'
						'\w\w\d'可以匹配'py3'
						'py.'可以匹配'pyc'、'pyo'、'py!'等等。
						\s可以匹配一个空格（也包括Tab等空白符）。
						py也可以匹配'python‘，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
					几种反义
					写法很简单改成大写就行了，意思与原来的相反，这里就不举例子了。
					"\W" 匹配任意不是字母，数字，下划线 的字符
					"\S" 匹配任意不是空白符的字符
					"\D" 匹配任意非数字的字符
					"\B" 匹配不是单词开头或结束的位置
					"[^abc]" 匹配除了abc以外的任意字符
			量词
									 "*"(贪婪) ：重复零次或更多
					例如"aaaaaaaa" 匹配字符串中所有的a。正则："a*"会出到所有的字符"a"
					"+"(懒惰) ：重复一次或更多次
					例如"aaaaaaaa" 匹配字符串中所有的a。正则"a+"会取到字符中所有的a字符，"a+"与"a*"不同在于"+"至少是一次而"*" 可以是0次。
					"?"(占有) ：重复零次或一次
					例如"aaaaaaaa" 匹配字符串中的a。正则："a?" 只会匹配一次，也就是结果只是单个字符a。
					"{n}" ：重复n次
					例如从"aaaaaaaa" 匹配字符串的a 并重复3次。正则："a{3}"结果就是取到3个a字符  "aaa"。
					"{n,m}" ：重复n到m次
					例如正则 "a{3,4}" 将a重复匹配3次或者4次 所以供匹配的字符可以是三个"aaa"也可以是四个"aaaa"，正则都可以匹配到。
					"{n,}" ：重复n次或更多次
					与{n,m}不同之处就在于匹配的次数将没有上限，但至少要重复n次。正则"a{3,}"，a至少要重复3次。
					
			量词例子
									.匹配除换行符外的单个字符
					+匹配前一个表达式一次或多次
					？匹配前面一个表达式0次或多次，如果紧跟在量词 * + {} ?后 量词为非贪婪，匹配尽量少的字符
					例如，对 "123abc" 应用 /\d+/ 将会返回 "123"，如果使用 /\d+?/,那么就只会匹配到 "1"。
			实例
				src="//(.+?\.jpg)"#src="//  "相同项的范围截取 。 (**) 括号内容是截取后保留的内容。.jpg相同项的范围截取。
				同上#  .+?\  .表示任意字符。 +表示匹配一次或多次  ?表示匹配尽量少的字符  \匹配完成
		
		图片下载
										
										import urllib.request
					import urllib.parse
					import re
					总数=(1,2)
					for 页数 in 总数:
						网页= urllib.request.urlopen('http://www.meizitu.com/a/more_'+str(页数)+'.html').read()
						网页2=网页.decode('gbk')#经常出现的是 UTF-8
						图片列表= re.findall(r'src="(http://mm.chinasareview.com/.+?\.jpg)" alt=', 网页2)
						名序列=1
						
						for 图片地址 in 图片列表:
							
							f= open('t5b'+str(页数)+str(名序列)+'.jpg','wb')
							图片内容=urllib.request.urlopen(图片地址)#后面的是urlopen
							f.write(图片内容.read())
							f.close()
							名序列+=1
							print('成功保存第%d页第%d张图片'%(page,x))
					input("\n\n按下 确认键enter 键后退出.")
		存放指定目录
			例
									import os#导入文件夹操作的模块
					new=5855
					名序列=758
					名=str('名序gregerge587837列')
					fpath = 'C:\\'+'n'+'/'+ str(new)# 指定放在C盘 目录下
					if not os.path.exists(fpath):#必有条件选择，否则出错
						os.makedirs(fpath) # makedirs 创建多级目录文件夹，mkdir创建一个文件夹
					f= open(fpath + '/' +'mrb'+str(名序列)+'.txt','w')# 'w'测试是在WIN系统下，网页应是'wb'
					f.write(名)
					f.close()
					input("\n\n按下 确认键enter 键后退出.")
		异常处理
			例
						
									try:#定义 判断。包纳可能产生错误的 语句前 导入模块库 import urllib.error
						图片内容=urllib.request.urlopen(图片地址集)#后面的是urlopen
					
							
						f= open(新目录+ '/' +str(名序列)+'.jpg','wb')# 
						f.write(图片内容.read())
						f.close()
					except urllib.error.URLError as e:#显示错误。urllib.error.URLError错误的审查器
						print('网址404')
					finally:#处理异常，忽略错误，继续运行执行
						名序列+=1
		启动火狐
			例
			 1#aboutabout:support打开的firefox浏览器配置文件  D:\消息\火狐\FF
		总页数、链接页、内容下载
			例
									import urllib.request
					import urllib.parse
					import urllib.error
					import re
					import os
					#总页数
					for 页数 in range(3,10):
						头部= {  
						'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20161201 Firefox/35.6'  
					}
						页数数据集=urllib.request.Request('http://www.meizitu.com/a/more_'+str(页数)+'.html',headers=头部)
						网页= urllib.request.urlopen(页数数据集).read()
						网页2=网页.decode('gbk')#经常出现的是 UTF-8
						#链接单页
						链接列表= re.findall(r'<a target=.+?href="(http:/.+?\.html)', 网页2)
						#内容页下载
						图集=0
						for 内容页链接 in 链接列表:
							内容页数据集=urllib.request.Request(内容页链接,headers=头部)
							try:
								#处理异常
								内容网页= urllib.request.urlopen(内容页数据集).read()
							except urllib.error.URLError as e:
								print('网址404')
							finally:
							   
								内容网页2=内容网页.decode('gbk')#经常出现的是 UTF-8
							图片列表= re.findall(r'" src="(http://mm.chinasareview.com/.+?\.jpg)',内容网页2)
							图集+=1
							名序列=00
							for 图片地址 in 图片列表:
								图片地址集=urllib.request.Request(图片地址,headers=头部)
								新目录= 'C:\\'+'下载图'+'/'+str(页数)+'页'+'/'+ str(图集)# 指定放在C盘 目录下
								if not os.path.exists(新目录):#必有条件选择，否则出错
									os.makedirs(新目录) # makedirs 创建多级目录文件夹，mkdir创建一个文件夹
								
								try:
									#处理异常
									图片内容=urllib.request.urlopen(图片地址集)#后面的是urlopen
								
										
									f= open(新目录+ '/' +str(名序列)+'.jpg','wb')# 
									f.write(图片内容.read())
									f.close()
								except urllib.error.URLError as e:
									print('网址404')
								finally:
									名序列+=1
							print('成功保存第%d页第%d图集'%(页数,图集))
					input("\n\n按下 确认键enter 键后退出.")
		1
		2
		3
		4
		6
		6
启动浏览器
		可视化操作
		导入的模块库
			from selenium import webdriver# 浏览的驱动
			import time# 时间
		
		Chrome正在受到自动软件的控制
								# 加启动配置
					option = webdriver.ChromeOptions()
					option.add_argument('disable-infobars')
					driver = webdriver.Chrome(chrome_options=option)
					
		
		Chrome浏览器静默模式启动（headless）
								from selenium import webdriver
					option = webdriver.ChromeOptions()# 加启动配置
					option.add_argument('headless')  # 静默模式
					# 打开chrome浏览器
					driver = webdriver.Chrome( chrome_options=option)
		一：selenium设置phantomjs请求头：
			# 进入浏览器设置
			options = webdriver.ChromeOptions()
			# 设置中文
			options.add_argument('lang=zh_CN.UTF-8')
			# 更换头部
			options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
			browser = webdriver.Chrome(chrome_options=options)

			
		chrome配置不加载图片
							# coding:utf-8
				from selenium import webdriver

				# 加启动配置
				option = webdriver.ChromeOptions()


				# 打开chrome浏览器
				chrome_options = webdriver.ChromeOptions()
				prefs = {"profile.managed_default_content_settings.images":2}
				chrome_options.add_experimental_option("prefs",prefs)
							
				driver = webdriver.Chrome(chrome_options=chrome_options)

















				driver.get("http://www.bubuko.com/infodetail-2100670.html")
				print(driver.title)
		操作浏览器基本方法
								from selenium import webdriver
					import time
					driver = webdriver.Chrome()  #Firefox  Ie
					driver.get(r"http://www.baidu.com/")  
					  
					#参数是像素点宽，高  
					driver.set_window_size(800,800)
					#driver.maximize_window() 浏览器全屏显示，不带参数
					print("浏览器大小是800px，800px")
					time.sleep(3)#设置暂停等待.单位是秒（s）,时间值可以是小数也可以是整数
					  
					driver.find_element_by_link_text("新闻").click()  
					time.sleep(3)#设置暂停等待
					driver.back()     #返回前一个页面
					time.sleep(10)
					driver.forward()  #前进前一个页面  
					driver.refresh()  #刷新当前页面  
					driver.find_element_by_css_selector("#ww").send_keys("python3")
					time.sleep(3)
					driver.find_element_by_xpath("//*[@class='btn']").click()
					time.sleep(3)
					driver.refresh()  #刷新当前页面
					time.sleep(3)
					driver.quit()#1.退出有两种方式，一种是close;另外一种是quit.2.close用于关闭当前窗口，当打开的窗口较多时，就可以用close关闭部分窗口
					#3.quit用于结束进程，关闭所有的窗口.4.最后结束测试，要用quit。quit可以回收c盘的临时文件
					input("\n\n按下 确认键enter 键后退出.")
		打开本地的文件
			driver.get("file:///C:/下载中转站/Untitled-1.html")
		元素定位
			<input id="kw" class="s_ipt" type="text" autocomplete="off" maxlength="100" name="wd">
						1.通过id定位：driver.find_element_by_id()
							1.#从上面定位到的元素属性中，可以看到有个id属性：id="search-key"，这里可以通过它的id属性单位到这个元素。
							2.#定位到搜索框后，用send_keys()方法
			2.通过name（有多项不准确）定位：find_element_by_name()
				1.#从上面定位到的元素属性中，可以看到有个name属性：name="wd"，这里可以通过它的name属性单位到这个元素。
				说#明：这里运行后会报错，说明这个搜索框的name属性不是唯一的，无法通过name属性直接定位到输入框			
			3.通过class定位：driver.find_element_by_class_name()
				1.#从上面定位到的元素属性中，可以看到有个class属性：class="s_ipt"，这里可以通过它的class属性定位到这个元素。
			4.通过tag（标签,有多项不准确）定位：find_element_by_tag_name().
				1.#从上面定位到的元素属性中，可以看到每个元素都有tag（标签）属性，如搜索框的标签属性，就是最前面的input
				2.#很明显，在一个页面中，相同的标签有很多，所以一般不用标签来定位。以下例子，仅供参考和理解，运行肯定报错
			5.通过link（文本）定位：driver.find_element_by_link_text()
				
			6.通过partial_link（模糊长文本）定位：driver.find_element_by_partial_link_text()
				1.#有时候一个超链接它的字符串可能比较长，如果输入全称的话，会显示很长，这时候可以用一模糊匹配方式，截取其中一部分字符串就可以了
				2.#如“hao123”,只需输入“ao123”也可以定位到
			7.通过xpath（层次结构）定位：driver.find_element_by_xpath()
				1.#以上定位方式都是通过元素的某个属性来定位的，如果一个元素它既没有id、name、class属性也不是超链接，这么办呢？或者说它的属性很多重复的。这个时候就可以用xpath解决
				2.#xpath是一种路径语言，跟上面的定位原理不太一样，首先第一步要先学会用工具查看一个元素的xpath
				3.#安装上图的步骤，在FriePath插件里copy对应的xpath地址
			8.通过css定位：driver.find_element_by_css_selector()
				1.#css是另外一种语法，比xpath更为简洁，但是不太好理解。这里先学会如何用工具查看，后续的教程再深入讲解
				2.#打开FirePath插件选择css
				3.#定位到后如下图红色区域显示
				
			定位后#点击.click() 或  输入.send_keys("python3")  请空输入框：clear()
			#time.sleep(5)
		组元素定位
			xpath
									1.#属性及属性值
					在XPath中可以利用属性及属性值来匹配元素，要注意的是，元素的属性名前要有"@"前缀。例如：
					//B[@id]表示所有具有属性id的B元素，结果为id值为b1和b2的两个B元素
					//B[@*]表示所有具有属性的B元素，结果为两个具有id属性的B元素和一个具有name属性B元素
					//B[not(@*)]表示所有不具有属性的B元素，结果为A元素→C元素下的B元素
					//B[@id="b1"] id值为b1的B元素，结果为A元素下的B元素
					2.#位置匹配
					对于每一个元素，它的各个子元素是有序的。
					如：/A/B/C[1]表示A元素→B元素→C元素的第一个子元素，得到name值为b的B元素
					/A/B/C[last()]表示A元素→B元素→C元素的最后一个子元素，得到id值为e2的E元素
					/A/B/C[position()>1]表示A元素→B元素→C元素之下的位置号大于1的元素，得到id值为d1的D元素和两个具有id值的E元素
					代码
												# coding:utf-8
						from selenium import webdriver
						import random
						import time
						driver = webdriver.Chrome()
						time.sleep(2)
						driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E6%B5%8B%E8%AF%95%E9%83%A8%E8%90%BD&rsv_pq=b0c246650000b933&rsv_t=3841AI9YNsV6tj2e4K78rMrhvADvE2AqPBs1%2FfYKm7qVFv1zbU9asIdwmGA&rqlang=cn&rsv_enter=1&rsv_sug3=4&rsv_sug1=1&rsv_sug7=100&inputT=2474&rsv_sug4=2475")
						driver.implicitly_wait(10)
						s = driver.find_elements_by_xpath(".//*[@id]/h3/a")
						time.sleep(2)
						# 设置随机值
						t = random.randint(0, 9)
						# 随机取一个结果点击鼠标
						s[t].click()
						time.sleep(2)
						input("\n\n按下 确认键enter 键后退出.")
		
		隐式等待
			.#implicitly_wait()默认参数单位是秒，这里的5秒并不是一个固定的等待时间，它不影响脚本的执行速度。
			.#implicitly_wait()并不针对页面上的某一元素进行等待，当脚本执行到某个元素定位时，若元素可以定位，则继续执行；
			.#若元素定位不到，则它将以轮询的方式不断判断元素是否被定位到，直到超出设置时长还没有定位到元素，则抛出异常。
								隐式等待是通过一定的时长等待页面上某元素加载完成。如果超出了设置的时长元素还没有加载，会抛出NoSuchElementException异常。
					webdriver的implicitly_wait()方法来实现隐式等待，默认设置为0。
					这个等待函数是针对整个driver的，只需要设置一个函数就行。也就是说，使用driver去获取一个元素或对象，当找不到这个元素时，它就会自动根据设置的时间去等待，超过设置的时长才会抛出错误。
					隐式等待使用到抛出异常，NoSuchElementException异常需要先导入：
					from selenium .common.exceptions import NoSuchElementException
					implicitly_wait()方法由webdriver提供。
		操作元素（键盘和鼠标事件）
			一、简单操作
									1.点击（鼠标左键）页面按钮：click()
					2.请空输入框：clear()
					3.输入字符串：send_keys()
					4.打开测试部落论坛后，点击放大镜搜索图标，一般为了保证输入的正确性，可以先清空下输入框，然后输入搜索关键字
			二.submit()一般用于模拟回车键
				1.在前面百度搜索案例中，输入关键字后，可以直接按回车键搜索，也可以点搜索按钮搜索。
			三、键盘操作
									1.selenium提供了一整套的模拟键盘操作事件，前面submit()方法如果不行的话，可以试试模拟键盘事件
					2.模拟键盘的操作需要先导入键盘模块：from selenium.webdriver.common.keys import Keys
					3.模拟enter键，可以用send_keys(Keys.ENTER)
			四.其它常见的键盘操作：
									1.鼠标不仅仅可以点击(click),鼠标还有其它的操作，如：鼠标悬停在某个元素上，鼠标右击，鼠标按住某个按钮拖到
					2.鼠标事件需要先导入模块：from selenium.webdriver.common.action_chains import ActionChains
					perform() 执行所有ActionChains中的行为
					move_to_element() 鼠标悬停
					3.双击鼠标：double_click()
					4.右击鼠标：context_click()
			五、其它常见的键盘操作：
									键盘F1到F12：send_keys(Keys.F1) 把F1改成对应的快捷键
					复制Ctrl+C：send_keys(Keys.CONTROL,'c') 
					粘贴Ctrl+V：send_keys(Keys.CONTROL,'v') 
					 全选Ctrl+A：send_keys(Keys.CONTROL,'a') 
					剪切Ctrl+X：send_keys(Keys.CONTROL,'x') 
					制表键Tab:  send_keys(Keys.TAB) 
					删除键send_keys(Keys.BACK_SPACE)
					空格键send_keys(Keys.SPACE)
					enter回车键send_keys(Keys.ENTER) 
		窗口截图
			webdriver提供了截图函数get_screenshot_as_file('保存文件的路径')来截取当前窗口。
			例# driver.get_screenshot_as_file('E:\\screenshot\\baidu.jpg')  
		获取（文本）元素属性
			一、获取title页面标题# 	title = driver.title
			二、获取标签对之间的文本信息 driver.text #text = driver.find_element_by_xpath(".//*[@id='crumb']/div/span").text
			获取当前页面的URL网址 #now_url = driver.current_url 
			获取浏览器名称 driver.name
			获取元素的其它属性
				1.获取其它属性方法:get_attribute("属性")，这里的参数可以是class、name等任意属性
				2.如获取百度输入框的class属性
				
			七、参考代码
									# coding:utf-8
					from selenium import webdriver
					import time
					driver = webdriver.Firefox()
					driver.implicitly_wait(10)
					driver.get("http://www.baidu.com")
					time.sleep(2)
					
					# 获取title页面标题
					title = driver.title
					print title
					
					二、获取获取标签对之间的文本信息
					text = driver.find_element_by_id("setf").text
					print text
					
					# 获取元素的标签
					tag = driver.find_element_by_id("kw").tag_name
					print tag
					
					# 获取元素的其它属性
					name = driver.find_element_by_id("kw").get_attribute("class")
					print name
					
					# 获取输入框的内容
					driver.find_element_by_id("kw").send_keys("yoyoketang")
					value = driver.find_element_by_id("kw").get_attribute("value")
					print value
					
					# 获取浏览器名称
					print driver.name
		断言，验证信息
			没有好的学习讲解
		多表单切换
			webdriver只能在一个页面上定位和识别元素，对于iframe或frame不能直接定位。
			通过switch_to.frame()方法将当前的主体切换为frame或iframe表单的内嵌页面中。
			参考代码
									# coding:utf-8
				from selenium import webdriver
				 
				driver = webdriver.Firefox()
				driver.get("http://mail.163.com/")
				driver.implicitly_wait(30)
				# 切换iframe
				# iframe = driver.find_element_by_tag_name("iframe")
				# driver.switch_to_frame(iframe)
				# driver.switch_to_frame("x-URS-iframe")
				driver.switch_to.frame("x-URS-iframe")
				driver.find_element_by_name("email").send_keys("123")
				driver.find_element_by_name("password").send_keys("456")
				# 释放iframe，重新回到主页面上
				driver.switch_to.default_content()
			参考代码2
									from selenium import webdriver  
				from time import sleep  
				from selenium.common.exceptions import NoSuchElementException  
				  
				driver =webdriver.Firefox()  
				driver.get(r"http://192.168.225.137/html5/myframe.html")  
				driver.set_window_size(2000,2000)  
				  
				#切换到iframe里面，iframe（name='myframe'）  
				driver.switch_to.frame("myframe")  
				  
				#下面就是正常操作  
				#隐式等待10s  
				driver.implicitly_wait(10)  
				try:  
					el = driver.find_element_by_xpath("//*[@id='kw']")  
					el1 = driver.find_element_by_id("su")  
					sleep(2)  
				except NoSuchElementException as e:  
					print(e)  
				else:  
					el.send_keys("python")  
					el1.click()  
				finally:  
					driver.quit() 
		多窗口切换
			在页面操作过程中有时候点击某个链接会弹出新的窗口
			，#webdriver的switch_to.window()方法，可以实现在不同窗口之间的切换。
			获取当前页面的句柄：driver.current_window_handle
			获取所有窗口的句柄：window_handles
			switch_to.window():切换到相应的窗口。用于不同窗口的切换；switch_to.frame()用于不同表单的切换。
			切换句柄
				方法1
										1.循环判断是否与首页句柄相等
					2.如果不等，说明是新页面的句柄
					3.获取的新页面句柄后，可以切换到新打开的页面上
					4.打印新页面的title,看是否切换成功
				方法二：
					1.直接获取all_h这个list数据里面第二个hand的值：all_h[1]
			参考代码
									# coding:utf-8
				from selenium import webdriver
				driver = webdriver.Firefox()
				driver.get("http://bj.ganji.com/")
				h = driver.current_window_handle
				print h  # 打印首页句柄
				driver.find_element_by_link_text("招聘求职").click()
				all_h = driver.window_handles
				print all_h     # 打印所有的句柄
				# 方法一：判断句柄，不等于首页就切换
				# for i in all_h:                       # 这里不建议用for循环了，很多小伙伴懵的
				#     if i != h:
				#         driver.switch_to.window(i)
				#         print driver.title
				# 方法二：获取list里面第二个直接切换
				driver.switch_to.window(all_h[1])
				print driver.title
				# 关闭新窗口
				driver.close()
				# 切换到首页句柄
				driver.switch_to.window(h)
				# 打印当前的title
				print driver.title
		单选框和复选框的操作
				单选框是圆的；下图复选框是方的，这个是业界的标准，要是开发小伙伴把图标弄错了，可以先抽他了。
				二、radio和checkbox源码
					1.上图的html源码如下，把下面这段复杂下来，写到文本里，后缀改成.html就可以了。
										<html>  
					<head>  
					<meta http-equiv="content-type" content="text/html;charset=utf-8" />  
					<title>单选和复选</title>  
					</head>  
					<body>  
					</form>  
					<h4>单选：性别</h4>   
					<form>  
					<label value="radio">男</label>   
					<input name="sex" value="male" id="boy" type="radio"><br>  
					<label value="radio1">女</label>  
					<input name="sex" value="female" id="girl" type="radio">  
					</form>  
					<h4>微信公众号：从零开始学自动化测试</h4>  
					<form>  
					<!-- <label for="c1">checkbox1</label> -->  
					<input id="c1" type="checkbox">selenium<br>  
					<!-- <label for="c2">checkbox2</label> -->  
					<input id="c2" type="checkbox">python<br>  
					<!-- <label for="c3">checkbox3</label> -->  
					<input id="c3" type="checkbox">appium<br>  
					<!-- <form>  
					<input type="radio" name="sex" value="male" /> Male  
					<br />  
					<input type="radio" name="sex" value="female" /> Female  
					</form> -->  
					  
					</body>  
					</html>  
				三、单选：radio
					定位id，点击图标就可以了，代码如下
					（获取url地址方法：把上面源码粘贴到文本保存为.html后缀后用浏览器打开，
					在浏览器url地址栏复制出地址就可以了）
				四、复选框：checkbox
					勾选单个框，比如勾选selenium这个，可以根据它的id=c1直接定位到点击就可以了
					1.全部勾选，可以用到定位一组元素，从上面源码可以看出，复选框的type=checkbox,
					这里可以用xpath语法：.//*[@type='checkbox']
					2.这里注意，敲黑板做笔记了：find_elements是不能直接点击的，它是复数的，
					所以只能先获取到所有的checkbox对象，然后通过for循环去一个个点击操作
					选择所有的复选框后取消第二个和最后一个：
						len()方法可以计算定位到的元素个数；
						pop()方法获取列表中某个元素，pop().click()定位到某个checkbox后取消勾选；
						pop()\pop(-1)都表示最后一个checkbox；
						pop(0)第一个checkbox；
						代码
														#通过xpath定位  
							inputs = driver.find_elements_by_xpath("//*[@type='checkbox']")  
							#通过以上两种方式定位就不需要判断定位的标签是否是复选框的了  
							for i in checkboxs:  
								i.click()  
								sleep(1)  
								  
							#打印当前页面上input="checkbox" 的个数  
							print(len(inputs))  
							  
							#把页面上第二个checkbox取到勾选  
							inputs.pop(1).click()  
							sleep(2)  
							driver.find_elements_by_xpath("//*[@type='checkbox']").pop(-1).click()  
							#前面已经把所有checkbox勾上了，通过pop().click()对某个checkbox再勾选，即是取消勾选。  
				五、判断是否选中：is_selected()
					1.有时候这个选项框，本身就是选中状态，如果我再点击一下，它就反选了，
					这可不是我期望的结果，那么可不可以当它是没选中的时候，我去点击下；
					当它已经是选中状态，我就不点击呢？那么问题来了：
					如何判断选项框是选中状态？
					2.判断元素是否选中这一步才是本文的核心内容，点击选项框对于大家来说没什么难度。
					获取元素是否为选中状态，打印结果如下图。
					3.返回结果为bool类型，没点击时候返回False,点击后返回True，
					接下来就很容易判断了，既可以作为操作前的判断，也可以作为测试结果的判断
				参考代码：
											# coding:utf-8
						from selenium import webdriver
						driver = webdriver.Firefox()
						driver.get("file:///C:/Users/Gloria/Desktop/checkbox.html")
						# 没点击操作前，判断选项框状态
						s = driver.find_element_by_id("boy").is_selected()
						print s
						driver.find_element_by_id("boy").click()
						# 点击后，判断元素是否为选中状态
						r = driver.find_element_by_id("boy").is_selected()
						print r
						# 复选框单选
						driver.find_element_by_id("c1").click()
						# 复选框全选
						checkboxs = driver.find_elements_by_xpath(".//*[@type='checkbox']")
						for i in checkboxs:
							i.click()
		随机数
							1.搜索结果有10条，从这10条中随机取一个就ok了
				2.先导入随机函数：import random
				3.设置随机值范围为0~9：a=random.randint(0~9) #s[a随机数].click(点击)
		处理浏览器弹窗
			一、最简单的alert弹窗 
								这种弹窗是最简单的一种，Selenium里有自带的方法来处理它，
								用switch_to.alert先定位到弹窗，然后使用一系列方法来操作：
				accept - 点击【确认】按钮
				dismiss - 点击【取消】按钮（如有按钮）,相当于点右上角x，取消弹出框
				send_keys - 输入内容（如有输入框）
				我们用以下代码就能实现切换至弹窗并点击【确定】按钮的效果：
				al = driver.switch_to_alert()
				al.accept()
				这里这个switch_to_alert()其实是旧写法，照理应该是用switch_to.alert()，但是新写法却会报错，目前猜测是版本问题，可能不支持新写法，这里就先用旧写法。
				以下是完整代码，为了运行的时候看得清楚，我加了两处等待：
					# encoding:utf-8
					from selenium import webdriver
					import time
					driver = webdriver.Firefox()
					driver.get("http://www.runoob.com/try/try.php?filename=tryjs_alert")
					driver.switch_to.frame("iframeResult")
					driver.find_element_by_xpath("html/body/input").click()
					time.sleep(1)
					al = driver.switch_to_alert()
					time.sleep(1)
					al.accept()
					
					12
			二、自定义弹窗
								由于alert弹窗不美观，现在大多数网站都会使用自定义弹窗，
								使用Selenium自带的方法就驾驭不了了，此时就要搬出JS大法。
								这里举一个新世界教育官网首页的例子：
				新世界教育官网首页
				大家能看到，图中的这种弹窗就是现在主流的表现形式，处理这种弹窗可以利用HTML DOM Style 对象，
				有一个display属性，可以设置元素如何被显示，
				详细解释可以参考http://www.w3school.com.cn/jsref/prop_style_display.asp。
				将display的值设置成none就可以去除这个弹窗了：
				js = 'document.getElementById("doyoo_monitor").style.display="none";'
				完整代码如下：
					# encoding:utf-8
					from selenium import webdriver
					import time
					driver = webdriver.Firefox()
					driver.get("http://sh.xsjedu.org/")
					time.sleep(1)
					js = 'document.getElementById("doyoo_monitor").style.display="none";'
					driver.execute_script(js)
		JS处理滚动条
			selenium并不是万能的，有时候页面上操作无法实现的，这时候就需要借助JS来完成了。
								常见场景：
				当页面上的元素超过一屏后，想操作屏幕下方的元素，是不能直接定位到，会报元素不可见的。
				这时候需要借助滚动条来拖动屏幕，使被操作的元素显示在当前的屏幕上。
				滚动条是无法直接用定位工具来定位的。selenium里面也没有直接的方法去控制滚动条，
				这时候只能借助J了，还好selenium提供了一个操作js的方法:
				execute_script()，可以直接执行js的脚本。
				一、JavaScript简介
				1.JavaScript是世界上最流行的脚本语言，因为你在电脑、手机、平板上浏览的所有的网页，
				以及无数基于HTML5的手机App，交互逻辑都是由JavaScript驱动的。简单地说，
				JavaScript是一种运行在浏览器中的解释型的编程语言。
				那么问题来了，为什么我们要学JavaScript？
				2.有些特殊的操作selenium2+python无法直接完成的，JS刚好是这方面的强项，所以算是一个很
				好的补充。对js不太熟悉的，可以网上找下教程，简单了解些即可。
				http://www.w3school.com.cn/js/index.asp4
			控制滚动条高度
							1.滚动条回到顶部：
				js="var q=document.getElementById('id').scrollTop=0"
				driver.execute_script(js）
				2.滚动条拉到底部
				js="var q=document.documentElement.scrollTop=10000"
				driver.execute_script(js)
				3.这里可以修改scrollTop 的值，来定位右侧滚动条的位置，0是最上面，10000是最底部。	
			三、横向滚动条
				1.有时候浏览器页面需要左右滚动（一般屏幕最大化后，左右滚动的情况已经很少见了）。
				2.通过左边控制横向和纵向滚动条scrollTo(x, y）js = "window.scrollTo(100,400);"
				driver.execute_script(js)
				3.第一个参数x是横向距离，第二个参数y是纵向距离
				
			四、Chrome浏览器
							1.以上方法在Firefox上是可以的，但是用Chrome浏览器，发现不管用。
				谷歌浏览器就是这么任性，不听话，于是用以下方法解决谷歌浏览器滚动条的问题。
				2.Chrome浏览器解决办法：
				js = "var q=document.body.scrollTop=0"
				driver.execute_script(js)
		cookie相关操作
			cookie操作的几个方法
							1.获取所有cookies： get_cookies()
				2.获取指定name的cookie:  driver.get_cookie（name）
				3.清除指定cookie：delete_cookie()
				4.清除所有cookies： delete_all_cookies()
				5.添加cookie的值: add_cookie(cookie_dict)
				（第五个方法可以用于绕过验证码登录，下篇详细介绍）
			参考代码
				# coding:utf-8
				from selenium import webdriver
				import time
				driver = webdriver.Firefox()
				# 启动浏览器后获取cookies
				print driver.get_cookies()
				driver.get("http://www.cnblogs.com/yoyoketang/")
				# 打开主页后获取cookies
				print driver.get_cookies()
				# 登录后获取cookies
				url = "https://passport.cnblogs.com/user/signin"
				driver.get(url)
				driver.implicitly_wait(30)
				driver.find_element_by_id("input1").send_keys(u"上海-悠悠")
				driver.find_element_by_id("input2").send_keys(u"xxx")
				driver.find_element_by_id("signin").click()
				time.sleep(3)
				print driver.get_cookies()
				# 获取指定name的cookie
				print driver.get_cookie(name=".CNBlogsCookie")
				# 清除指定name的cookie
				driver.delete_cookie(name=".CNBlogsCookie")
				print driver.get_cookies()
				# 为了验证此cookie是登录的，可以删除后刷新页面
				driver.refresh()#刷新页面
				# 清除所有的cookie
				driver.delete_all_cookies()
				print driver.get_cookies()
			添加cookie方法：driver.add_cookie（）
				1.add_cookie(cookie_dict)方法里面参数是cookie_dict，说明里面参数是字典类型。
				cookie组成结构
							cookie ={u'domain': u'.cnblogs.com',
					u'name': u'.CNBlogsCookie',
					u'value': u'xxxx',
					u'expiry': 1491887887,
					u'path': u'/',
					u'httpOnly': True,
					u'secure': False}
					domain：服务器域名
					name：cookie的名称
					value：cookie对应的值，动态生成的
					expiry：Cookie有效终止日期
					path：Path属性定义了Web服务器上哪些路径下的页面可获取服务器设置的Cookie
					httpOnly：防脚本攻击
					secure:在Cookie中标记该变量，表明只有当浏览器和Web Server之间的通信协议为加密认证协议时，
					浏览器才向服务器提交相应的Cookie。当前这种协议只有一种，即为HTTPS。
				添加cookie
					1.这里需要添加两个cookie，一个是.CNBlogsCookie，另外一个是.Cnblogs.AspNetCore.Cookies。
					2.我这里打开的网页是博客的主页：http://www.cnblogs.com/yoyoketang，没进入登录页。
					3.添加cookie后刷新页面,接下来就是见证奇迹的时刻了。
					五、参考代码：
					 
					
						# coding:utf-8
						from selenium import webdriver
						import time
						driver = webdriver.Firefox()
						driver.get("http://www.cnblogs.com/yoyoketang")
						# # 添加cookie
						c1 = {u'domain': u'.cnblogs.com',
							  u'name': u'.CNBlogsCookie',
							  u'value': u'xxxx',
							  u'expiry': 1491887887,
							  u'path': u'/',
							  u'httpOnly': True,
							  u'secure': False}
						c2 = {u'domain': u'.cnblogs.com',
							  u'name': u'.Cnblogs.AspNetCore.Cookies',
							  u'value': u'xxxx',
							  u'expiry': 1491887887,
							  u'path': u'/',
							  u'httpOnly': True,
							  u'secure': False}
						driver.add_cookie(c1)  # 添加2个值
						driver.add_cookie(c2)
					有几点需要注意：
						1.登录时候要勾选下次自动登录按钮。
						2.add_cookie（）只添加name和value，对于博客园的登录是不成功。
						3.本方法并不适合所有的网站，一般像博客园这种记住登录状态的才会适合。
			 # 清除所有的cookie
            self.driver.delete_all_cookies()
            print('清除所有的cookie')
		判断标题title
			1.首先导入expected_conditions模块
			2.由于这个模块名称比较长，所以为了后续的调用方便，重新命名为EC了（有点像数据库里面多表查询时候重命名）
			3.打开博客首页后判断title,返回结果是True或False
			判断完全等于:title_is
			判断包含:title_contains
			代码
				# coding:utf-8
				from selenium import webdriver
				from selenium.webdriver.support import expected_conditions as EC
				driver = webdriver.Firefox()
				driver.get("http://www.cnblogs.com/yoyoketang")
				# 判断title完全等于
				title = EC.title_is(u'上海-悠悠 - 博客园')
				print title(driver)
				# 判断title包含
				title1 = EC.title_contains(u'上海-悠悠')
				print title1(driver)
				# 另外一种写法,交流QQ群：232607095
				r1 = EC.title_is(u'上海-悠悠 - 博客园')(driver)
				r2 = EC.title_contains(u'上海-悠悠')(driver)
				print r1
				print r2
		判断元素（expected_conditions）
			一、功能介绍和翻译
				text_to_be_present_in_element : #判断某个元素中的text是否 包含 了预期的字符串
				text_to_be_present_in_element_value : 判断某个元素中的value属性是否 包含 了预期的字符串
				title_is： #判断当前页面的title是否完全等于（==）预期字符串，返回布尔值
				title_contains : 判断当前页面的title是否包含预期字符串，返回布尔值
				presence_of_element_located : 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
				visibility_of_element_located : 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
				visibility_of : 跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
				presence_of_all_elements_located : 判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
				frame_to_be_available_and_switch_to_it : 判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
				invisibility_of_element_located : 判断某个元素中是否不存在于dom树或不可见
				element_to_be_clickable : 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
				staleness_of : 等某个元素从dom树中移除，注意，这个方法也是返回True或False
				element_to_be_selected : 判断某个元素是否被选中了,一般用在下拉列表
				element_selection_state_to_be : 判断某个元素的选中状态是否符合预期
				element_located_selection_state_to_be : 跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
				alert_is_present : 判断页面上是否存在alert
							切记判断条件：
				常用的判断条件：
				title_is 标题是某内容
				title_contains 标题包含某内容
				presence_of_element_located #元素加载出，传入定位元组，如(By.ID, 'p')
				visibility_of_element_located 元素可见，传入定位元组
				visibility_of 可见，传入元素对象
				presence_of_all_elements_located 所有元素加载出
				text_to_be_present_in_element #某个元素文本包含某文字
				text_to_be_present_in_element_value #某个元素值包含某文字
				frame_to_be_available_and_switch_to_it frame加载并切换
				invisibility_of_element_located 元素不可见
				element_to_be_clickable #元素可点击
				staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
				element_to_be_selected 元素可选择，传元素对象
				element_located_to_be_selected 元素可选择，传入定位元组
				element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
				element_located_selection_state_to_be 传入定位元组以及状态，相等返回True，否则返回False
                    alert_is_present #是否出现Alert
			二、查看源码和注释
				1.打开python里这个目录l可以找到：Lib\site-packages\selenium\webdriver\support\expected_conditions.py
		判断文本
			在做结果判断的时候，经常想判断某个元素中是否存在指定的文本，如登录后判断页面中是账号是否是该用户的用户名。

			在前面的登录案例中，写了一个简单的方法，但不是公用的，在EC模块有个方法是可以专门用来判断元素中存在指定文本的：text_to_be_present_in_element。
			一、源码分析
			1.翻译：判断元素中是否存在指定的文本，两个参数：locator, text
			locator参数是定位的方法
			text参数是期望的值
			2.__call__里返回的是布尔值：Ture和False
			参考代码
			

				# coding:utf-8

				import time

				# coding:utf-8
				from selenium import webdriver
				from selenium.webdriver.support import expected_conditions as EC
				driver = webdriver.Chrome()
				url = "https://www.baidu.com"
				driver.get(url)

				locator = ("name", "tj_trxueshu")#("name"表示元素定位的方法, "tj_trxueshu"定位的标记)
				#简单的方法locator = ("xpath", ".//*[@id='u1']/a[6]")
				print(locator )


				text = "学术"
				result = EC.text_to_be_present_in_element(locator, text)(driver)
				print (result)


				# 下面是失败的案例
				text1 = u"学术vd"
				result1 = EC.text_to_be_present_in_element(locator, text1)(driver)
				print (result1)

				locator2 = ("id", "su")
				text2 = "百度一下"
				result2 = EC.text_to_be_present_in_element_value(locator2, text2)(driver)
				print (result2)
				input("\n\n按下 确认键enter 键后退出.")

				
					另外一个差不多复方法判断元素的value值：text_to_be_present_in_element_value。
		上传文件
			文件上传是web页面上很常见的一个功能，自动化成功中操作起来却不是那么简单。
			一般分两个场景：一种是input标签，这种可以用selenium提供的send_keys()方法轻松解决；
			另外一种非input标签实现起来比较困难，可以借助autoit工具或者SendKeys第三方库。
			1.先定位到文件上传按钮，通过input标签实现上传功能的可以通过send_keys("文件地址")上传
				from selenium import webdriver  
  
				driver = webdriver.Firefox()  
				driver.get(r"http://192.168.225.137/html5/file.html")  
				#通过send_keys()上传  
				driver.find_element_by_css_selector("[type='file']").send_keys("C:\\Users\\Administrator\\Desktop\\html5.txt")
		
		下载文件
			Firefox 文件下载
				对于Firefox，需要我们设置其Profile：

				browser.download.dir：#指定下载路径
				browser.download.folderList：#设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
				browser.download.manager.showWhenStarting：#设为false不显示开始，设为true显示开始.在开始下载时是否显示下载管理器
				browser.helperApps.neverAsk.saveToDisk：#对所给出文件类型不再弹出框进行询问

				下面来个示例：
					# -*- coding: utf-8 -*-

					from selenium import webdriver
					from time import sleep

					profile = webdriver.FirefoxProfile()
					
					#指定下载路径
					profile.set_preference('browser.download.dir', 'd:\\')
					
					#设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；
					#设置成 1 表示下载到默认路径
					profile.set_preference('browser.download.folderList', 2)
					
					#设为false不显示开始，
					#设为true显示开始.在开始下载时是否显示下载管理器
					profile.set_preference('browser.download.manager.showWhenStarting', False)
					
					#对所给出文件类型不再弹出框进行询问
					profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')#zip按照文件扩展名排列的 Mime 类型
					
					driver = webdriver.Firefox(firefox_profile=profile)

					driver.get('http://sahitest.com/demo/saveAs.htm')
					driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
					sleep(3)
					driver.quit()
				按照文件扩展名排列的 Mime 类型
										扩展名 	类型/子类型
						application/octet-stream
					323 	text/h323
					acx 	application/internet-property-stream
					ai 	application/postscript
					aif 	audio/x-aiff
					aifc 	audio/x-aiff
					aiff 	audio/x-aiff
					asf 	video/x-ms-asf
					asr 	video/x-ms-asf
					asx 	video/x-ms-asf
					au 	audio/basic
					avi 	video/x-msvideo
					axs 	application/olescript
					bas 	text/plain
					bcpio 	application/x-bcpio
					bin 	application/octet-stream
					bmp 	image/bmp
					c 	text/plain
					cat 	application/vnd.ms-pkiseccat
					cdf 	application/x-cdf
					cer 	application/x-x509-ca-cert
					class 	application/octet-stream
					clp 	application/x-msclip
					cmx 	image/x-cmx
					cod 	image/cis-cod
					cpio 	application/x-cpio
					crd 	application/x-mscardfile
					crl 	application/pkix-crl
					crt 	application/x-x509-ca-cert
					csh 	application/x-csh
					css 	text/css
					dcr 	application/x-director
					der 	application/x-x509-ca-cert
					dir 	application/x-director
					dll 	application/x-msdownload
					dms 	application/octet-stream
					doc 	application/msword
					dot 	application/msword
					dvi 	application/x-dvi
					dxr 	application/x-director
					eps 	application/postscript
					etx 	text/x-setext
					evy 	application/envoy
					exe 	application/octet-stream
					fif 	application/fractals
					flr 	x-world/x-vrml
					gif 	image/gif
					gtar 	application/x-gtar
					gz 	application/x-gzip
					h 	text/plain
					hdf 	application/x-hdf
					hlp 	application/winhlp
					hqx 	application/mac-binhex40
					hta 	application/hta
					htc 	text/x-component
					htm 	text/html
					html 	text/html
					htt 	text/webviewhtml
					ico 	image/x-icon
					ief 	image/ief
					iii 	application/x-iphone
					ins 	application/x-internet-signup
					isp 	application/x-internet-signup
					jfif 	image/pipeg
					jpe 	image/jpeg
					jpeg 	image/jpeg
					jpg 	image/jpeg
					js 	application/x-javascript
					latex 	application/x-latex
					lha 	application/octet-stream
					lsf 	video/x-la-asf
					lsx 	video/x-la-asf
					lzh 	application/octet-stream
					m13 	application/x-msmediaview
					m14 	application/x-msmediaview
					m3u 	audio/x-mpegurl
					man 	application/x-troff-man
					mdb 	application/x-msaccess
					me 	application/x-troff-me
					mht 	message/rfc822
					mhtml 	message/rfc822
					mid 	audio/mid
					mny 	application/x-msmoney
					mov 	video/quicktime
					movie 	video/x-sgi-movie
					mp2 	video/mpeg
					mp3 	audio/mpeg
					mpa 	video/mpeg
					mpe 	video/mpeg
					mpeg 	video/mpeg
					mpg 	video/mpeg
					mpp 	application/vnd.ms-project
					mpv2 	video/mpeg
					ms 	application/x-troff-ms
					mvb 	application/x-msmediaview
					nws 	message/rfc822
					oda 	application/oda
					p10 	application/pkcs10
					p12 	application/x-pkcs12
					p7b 	application/x-pkcs7-certificates
					p7c 	application/x-pkcs7-mime
					p7m 	application/x-pkcs7-mime
					p7r 	application/x-pkcs7-certreqresp
					p7s 	application/x-pkcs7-signature
					pbm 	image/x-portable-bitmap
					pdf 	application/pdf
					pfx 	application/x-pkcs12
					pgm 	image/x-portable-graymap
					pko 	application/ynd.ms-pkipko
					pma 	application/x-perfmon
					pmc 	application/x-perfmon
					pml 	application/x-perfmon
					pmr 	application/x-perfmon
					pmw 	application/x-perfmon
					pnm 	image/x-portable-anymap
					pot, 	application/vnd.ms-powerpoint
					ppm 	image/x-portable-pixmap
					pps 	application/vnd.ms-powerpoint
					ppt 	application/vnd.ms-powerpoint
					prf 	application/pics-rules
					ps 	application/postscript
					pub 	application/x-mspublisher
					qt 	video/quicktime
					ra 	audio/x-pn-realaudio
					ram 	audio/x-pn-realaudio
					ras 	image/x-cmu-raster
					rgb 	image/x-rgb
					rmi 	audio/mid
					roff 	application/x-troff
					rtf 	application/rtf
					rtx 	text/richtext
					scd 	application/x-msschedule
					sct 	text/scriptlet
					setpay 	application/set-payment-initiation
					setreg 	application/set-registration-initiation
					sh 	application/x-sh
					shar 	application/x-shar
					sit 	application/x-stuffit
					snd 	audio/basic
					spc 	application/x-pkcs7-certificates
					spl 	application/futuresplash
					src 	application/x-wais-source
					sst 	application/vnd.ms-pkicertstore
					stl 	application/vnd.ms-pkistl
					stm 	text/html
					svg 	image/svg+xml
					sv4cpio 	application/x-sv4cpio
					sv4crc 	application/x-sv4crc
					swf 	application/x-shockwave-flash
					t 	application/x-troff
					tar 	application/x-tar
					tcl 	application/x-tcl
					tex 	application/x-tex
					texi 	application/x-texinfo
					texinfo 	application/x-texinfo
					tgz 	application/x-compressed
					tif 	image/tiff
					tiff 	image/tiff
					tr 	application/x-troff
					trm 	application/x-msterminal
					tsv 	text/tab-separated-values
					txt 	text/plain
					uls 	text/iuls
					ustar 	application/x-ustar
					vcf 	text/x-vcard
					vrml 	x-world/x-vrml
					wav 	audio/x-wav
					wcm 	application/vnd.ms-works
					wdb 	application/vnd.ms-works
					wks 	application/vnd.ms-works
					wmf 	application/x-msmetafile
					wps 	application/vnd.ms-works
					wri 	application/x-mswrite
					wrl 	x-world/x-vrml
					wrz 	x-world/x-vrml
					xaf 	x-world/x-vrml
					xbm 	image/x-xbitmap
					xla 	application/vnd.ms-excel
					xlc 	application/vnd.ms-excel
					xlm 	application/vnd.ms-excel
					xls 	application/vnd.ms-excel
					xlt 	application/vnd.ms-excel
					xlw 	application/vnd.ms-excel
					xof 	x-world/x-vrml
					xpm 	image/x-xpixmap
					xwd 	image/x-xwindowdump
					z 	application/x-compress
					zip 	application/zip
			Chrome 文件下载
				Chrome浏览器类似，设置其options：

				download.default_directory：设置下载路径
				profile.default_content_settings.popups：设置为 0 禁止弹出窗口
				它的设置就简单多了，看个示例：
					# -*- coding: utf-8 -*-

					from selenium import webdriver
					from time import sleep


					options = webdriver.ChromeOptions()
					prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
					options.add_experimental_option('prefs', prefs)

					driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe', chrome_options=options)
					driver.get('http://sahitest.com/demo/saveAs.htm')
					driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
					sleep(3)
					driver.quit()
			按键下载文件
				1.当点到下载按钮时候，会弹出如下页面
				2.如果想点“保存文件”按钮，解决问题思路：

				- 先按TAB键，移动光标聚焦到保存按钮上

				- 再按下ENTER键，这样就能保存了
				二、代码实现
					# coding:utf-8
					from selenium import webdriver
					import SendKeys
					import time

					driver = webdriver.Firefox()
					driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")

					time.sleep(3)
					# 默认在取消按钮上，先切换到保存文件上
					SendKeys.SendKeys("{TAB}")  # 发送TAB键

					time.sleep(3)
					# 火狐上第一次回车没生效，所以多发一次回车
					SendKeys.SendKeys("{ENTER}")   # 发送回车键
					SendKeys.SendKeys("{ENTER}")   # 发送回车键

			实例：下载一个文件（此实例只适合Firefox浏览器）
				    from selenium import webdriver  
					import os  
					import time  
					  
					#为了能够让Firefox()实现下载，需要对FirefoxPile()进行设置  
					fp = webdriver.FirefoxProfile()  
					  
					#browser.download.folderList设置为0，下载到浏览器默认的路径；设置为2则可以设置下载路径  
					fp.set_preference('browser.download.folderList',2)  
					#browser.download.manager.showWhenStarting设为false不显示开始，设为true显示开始  
					fp.set_preference('browser.download.manager.showWhenStarting',False)  
					#browser.download.dir用于指定下载文件的目录，os.getcwd()当前目录  
					fp.set_preference('browser.download.dir',os.getcwd())  
					#browser.helperApps.neverAsk.saveToDisk指定下载页面的Content-type值，“application/octet-stream”是文件的类型  
					fp.set_preference('browser.helperApps.neverAsk.saveToDisk',  
									   'application/octet-stream')  
					#将所有设置的信息在调用webdriver的Firefox时作为参数传递给浏览器，Firefox浏览器就是根据折现设置信息将文件下载到设定的脚本目录下。  
					driver = webdriver.Firefox(firefox_profile = fp)  
					driver.get('https://pypi.python.org/pypi/selenium')  
					driver.find_element_by_partial_link_text("selenium-3.0").click()  
					time.sleep(30)  
					driver.quit() 
					
					
					为了能够让Firefox()实现下载，需要对FirefoxPile()进行设置：

					browser.download.folderList设置为0，下载到浏览器默认的路径；设置为2则可以设置下载路径
					browser.download.manager.showWhenStarting设为false不显示开始，设为true显示开始
					browser.download.dir用于指定下载文件的目录，os.getcwd()当前目录
					browser.helperApps.neverAsk.saveToDisk指定下载页面的Content-type值，“application/octet-stream”是文件的类型

				HTTP Content-type常用的对照表：http://tool.oschina.net/commons
		读取Excel数据（xlrd）
			环境安装
								1.安装xlrd
				pip install xlrd
				2.安装xlwt
				pip install xlwt
			读取excel文件
								#-*- coding:utf-8  -*-
				import xlrd
				import xlwt



				#excel文件全路径
				excelpath = '123.xls'
				#用于读取excel文件
				tableopen = xlrd.open_workbook(excelpath)
				#获取excel工作簿数
				count = len(tableopen.sheets())#获取表单数
				print ("工作簿数为%s"%count)
				#获取表数据的行、列数
				table = tableopen.sheet_by_name('Sheet1')#读取表1
				竖行 = table.nrows
				横列= table.ncols
				print ("表数据的行数为%s,列数为%s"%(竖行,横列))
				# 循环读取数据
				for i in range(0,竖行):
					rowValues = table.row_values(i) #按行读取数据
					# 输出读取的数据
					for data in rowValues:
						print (data,end='   ')#并列行显示

					print ('     ')


				input("\n\n按下 确认键enter 键后退出.")

			写入excel文件
								import xlrd
				import xlwt
				import random
				# 注意这里的 excel 文件的后缀是 xls 如果是 xlsx 打开是会提示无效
				excelpath = 'est2.xls'
				wtbook = xlwt.Workbook()
				#新增一个sheet工作表
				sheet = wtbook.add_sheet('Sheet1',cell_overwrite_ok=True)
				#写入数据头
				headlist = ['学号','姓名','班级']
				竖行= 0
				横列= 0
				#循环写
				for head in headlist:
					sheet.write(竖行,横列,head)
					横列 = 横列+1
				for i in range(1,50):#行数限制，我这里写入4行数据
					for j in range(1,3):#列数限制，因为我的headlist有三个数据，所以这里肯定是3列
						#写入4行0~99的随机数
						data = random.randint(0,999)
						sheet.write(i,0,i)#(i,0,前面表示行与列，后面的i是输入的数字)
						sheet.write(i,j, data)
					print ("写第[%d]行数据"%(i))
				#保存
				wtbook.save(excelpath)

				input("\n\n按下 确认键enter 键后退出.")

		1
		2
		
		
				
				
			