
# -*- coding:utf-8

import tkinter as tk


"""

"""


class 类一一组件参数:  # 调用 类的模具  self.模具一一查看变量输出文本值('变量名', self.测试打印, 8)
    def __init__(self):
        self.测试打印 = 'ew'

        self.模具一一换手机头部信息()

    def 模具一一示例(self):
        pass
        """
        """

    def 模具一一生成主窗口(self):
        pass
        """
        window = tkinter.Tk()：
        window.title('标题名')    　　　        修改框体的名字, 也可在创建时使用className参数来命名；
        window.resizable(0, 0)
        框体大小可调性，分别表示x, y方向的可变性；1
        表示可变，0
        表示不可变；
        window.geometry('250x150')
        指定主框体大小；
        window.quit()
        退出；（配合响应事件使用）
        window.update_idletasks()
        window.update()
        刷新页面；
        window.mainloop（）    进入消息循环（必需组件）
        """

    def 模具一一15种核心组件(self):
        pass
        """    
        2、tkinter中的15种核心组件：
        Button        　　    按钮；
        Canvas  绘图形组件，可以在其中绘制图形；
        Checkbutton   复选框；
        Entry       文本框（单行）；
        Text          文本框（多行）；
        Frame    框架，将几个组件组成一组
        Label        　　    标签，可以显示文字或图片；
        Listbox      　　    列表框；
        Menu     　　        菜单；
        Menubutton   它的功能完全可以使用Menu替代；
        Message     与Label组件类似，但是可以根据自身大小将文本换行；
        Radiobutton     单选框；
        Scale      　　    滑块；允许通过滑块来设置一数字值
        Scrollbar     滚动条；配合使用canvas, entry, listbox, and text窗口部件的标准滚动条；
        Toplevel   用来创建子窗口窗口组件。
        
        （在Tkinter中窗口部件类没有分级；所有的窗口部件类在树中都是兄弟。）
        """

    def 模具一一组件的放置和排版(self):
        pass
        """
        3、组件的放置和排版（pack, grid, place)
        
        pack组件设置位置属性参数：
        after: 将组件置于其他组件之后；
        before: 将组件置于其他组件之前；
        anchor: 组件的对齐方式，顶对齐
        'n', 底对齐
        's', 左
        'w', 右
        'e'
        side: 组件在主窗口的位置，可以为
        'top', 'bottom', 'left', 'right'（使用时tkinter.TOP, tkinter.LEFT）；
        fill：    填充方式(Y, 垂直，X，水平，BOTH，水平 + 垂直），是否在某个方向充满窗口
        expand
        1
        可扩展，0
        不可扩展，代表控件是否会随窗口缩放
        
        grid组件使用行列的方法放置组件的位置，参数有：
        column:
        组件所在的列起始位置；
        columnspan:
        组件的列宽；跨列数
        row：
        组件所在的行起始位置；
        rowspan：
        
        
        组件的行宽；rowspam = 3
        跨3行
        
        sticky
        对齐方式：NSEW（北南东西）上下左右
        
        padx、pady
        x方向间距、y方向间距（padx = 5）
        place组件可以直接使用坐标来放置组件，参数有：
        anchor: 组件对齐方式；n, ne, e, se, s, sw, w, nw, or center; （'n' == N）
        x: 组件左上角的x坐标；
        y: 组件左上角的y坐标；
        relx: 组件左上角相对于窗口的x坐标，应为0 - 1
        之间的小数；图形位置相对窗口变化
        rely: 组件左上角相对于窗口的y坐标，应为0 - 1
        之间的小数；
        width: 组件的宽度；
        heitht: 组件的高度；
        relwidth: 组件相对于窗口的宽度，0 - 1
        之间的小数，图形宽度相对窗口变化；
        relheight:　    组件相对于窗口的高度，0 - 1
        之间的小数；
        """

    def 模具一一按钮Button时控制按钮的参数(self):
        pass
        """
        4、使用tkinter.Button时控制按钮的参数：
        anchor: 指定按钮上文本的位置；
        background(bg)
        指定按钮的背景色；
        bitmap: 指定按钮上显示的位图；
        borderwidth(bd)
        指定按钮边框的宽度；
        command: 指定按钮消息的回调函数；
        cursor: 指定鼠标移动到按钮上的指针样式；
        font: 指定按钮上文本的字体；
        foreground(fg)
        指定按钮的前景色；
        height: 指定按钮的高度；
        image: 指定按钮上显示的图片；
        state: 指定按钮的状态（disabled）；
        text: 指定按钮上显示的文本；
        width: 指定按钮的宽度
        padx
        设置文本与按钮边框x的距离，还有pady;
        activeforeground
        按下时前景色
        textvariable
        可变文本，与StringVar等配合着用"""

    def 模具一一文本框控制参数(self):
        pass
        """
           
        5、文本框tkinter.Entry, tkinter.Text控制参数：
        
        background(bg)   　　 文本框背景色；
        
        foreground(fg)
        前景色；
        
        selectbackground　　  选定文本背景色；
        
        selectforeground　　  选定文本前景色；
        
        borderwidth(bd)    　 文本框边框宽度；
        
        font                　字体；
        
        show          　　    文本框显示的字符，若为 *，表示文本框为密码框；
        
        state            　　 状态；
        
        width        　　　　  文本框宽度
        
        textvariable    　　  可变文本，与StringVar等配合着用
        """

    def 模具一一标签Label组件控制参数(self):
        pass
        """
      
        6、标签tkinter.Label组件控制参数：
        
        Anchor
        标签中文本的位置；    background(bg)
        foreground(fg)
        背景色；前景色；
        borderwidth(bd)
        边框宽度；    width  、height
        标签宽度；标签高度；
        bitmap
        标签中的位图；    font
        字体；
        image
        标签中的图片；     justify
        多行文本的对齐方式；
        text    　　    标签中的文本，可以使用
        '\n'
        表示换行
        textvariable  　　　    显示文本自动更新，与StringVar等配合着用
        
        """

    def 模具一一单选框和复选框(self):
        pass
        """
          
        7、单选框和复选框Radiobutton, Checkbutton控制参数：
        
        anchor
        文本位置；    background(bg)
        背景色；
        foreground(fg)
        前景色；    borderwidth
        边框宽度；
        width
        组件的宽度；     height     　    组件高度；
        bitmap
        组件中的位图；    image
        组件中的图片；
        font
        字体；    justify
        组件中多行文本的对齐方式；
        text
        指定组件的文本；    value
        指定组件被选中中关联变量的值；
        variable
        指定组件所关联的变量；    indicatoron
        特殊控制参数，当为0时，组件会被绘制成按钮形式;
        textvariable
        可变文本显示，与StringVar等配合着用
          """

    def 模具一一组图组件Canvas控制参数(self):
        pass
        """
        
        8、组图组件Canvas控制参数
        background(bg)
        背景色;
        foreground(fg)
        前景色;
        borderwidth
        组件边框宽度；        width
        组件宽度；
        height
        高度;
        bitmap
        位图;
        image
        图片;
        
        绘图的方法主要以下几种：
        create_arc
        
        椭圆圆弧;
        create_arc(x1, y1, x2, y2, start=0, extent=120, tag='1')
        
        # x1,y1和x2,y2分别为椭圆圆弧外接矩形的左上角和右下角坐标；
        
        从0度，扩充到120度；圆弧别名为:‘1’;
        create_bitmap
        绘制位图，支持XBM;
        create_image
        绘制图片，支持GIF(x, y, image, anchor);
        create_line
        绘制直线；（坐标罗列）
        create_oval;
        绘制椭圆；
        create_polygon
        绘制多边形(坐标依次罗列，不用加括号，还有参数，fill, outline)；
        create_rectangle
        绘制矩形((a, b, c, d), 值为左上角和右下角的坐标)；
        create_text
        绘制文字(字体参数font, )；
        create_window
        绘制窗口；
        delete
        删除绘制的图形；delete('all')
        清除所有图形;
        或清除指定别名的图形；
        itemconfig
        修改图形属性，第一个参数为图形的ID，后边为想修改的参数；
        move          　　
        
        移动图像（1，4，0），1
        为图像对象，4
        为横移4像素，0
        为纵移像素，然后用root.update()
        刷新即可看到图像的移动，
        
        为了使多次移动变得可视，最好加上time.sleep()
        函数或canvas.after()
        函数；
        coords(ID)
        
        返回对象的位置的两个坐标（4
        个数字元组）；只要用create_方法画了一个图形，就会自动返回一个ID,
        
        创建一个图形时将它赋值给一个变量，需要ID时就可以使用这个变量名。
        after（100）    程序在这里暂停100毫秒
        
        对于按钮组件、菜单组件等可以在创建组件时通过command参数指定其事件处理函数。方法为bind;
        或者用bind_class方法进行类绑定，bind_all方法将所有组件事件绑定到事件响应函数上。
        """

    def 模具一一菜单Men(self):

        pass
        """
        
        9、菜单Menu
        参数：
        tearoff
        分窗，0
        为在原窗，1
        为点击分为两个窗口
        bg, fg
        背景，前景
        borderwidth
        边框宽度
        font
        字体
        activebackgound
        鼠标划过时背景，同样有activeforeground，activeborderwidth，disabledforeground
        cursor
        
        当子菜单分离原窗时，鼠标在子菜单栏上的形状cursor = "arrow""circle""clock""cross""dotbox"
        
        "exchange""fleur""heart""heart""man""mouse""pirate""plus"
        等图形
        postcommand
        点击菜单的回调函数
        selectcolor    　    选中时背景色，add_checkbutton控件选中时，√的颜色
        takefocus
        title
        当子菜单分离原窗时的标题
        type
        relief
        当子菜单分离原窗时的3D效果，relief = RAISED, SUNKEN, FLAT, RIDGE, SOLID, GROOVE
        方法：
        menu.add_cascade
        添加子菜单（menu参数为子菜单对象）
        menu.add_command
        添加命令（label参数为显示内容，command参数为响应函数）
        menu.add_separator
        添加分隔线
        menu.add_checkbutton
        添加确认按钮，与add_radiobutton用法相同，效果为：点击时打钩（variable参数决定绑定变量）
        delete
        删除
            """

    def 模具一一弹窗(self):
        pass
        """
      
        12、弹窗
        
        messagebox的方法：
        
        showerror
        错误提示对话框
        showinfo
        信息提示对话框
        showwarning
        警告对话框
        askokcansel
        确认或取消；有返回值True、False
        askquestion
        回答问题；有返回值yes、no
        askretrycansel
        重试或取消；有返回值True、False
        askyesno
        回答是非题；有返回值True、False
        askyesnocancel
        是、否或取消，有返回值True、False、None
        
        messagebox._show函数的控制参数：
        
        default
        指定消息框按钮；
        
        icon
        指定消息框图标；
        
        message     　 　指定消息框所显示的消息；
        
        parent
        指定消息框的父组件；
        
        title
        标题；
        
        type
        类型；
        
        simpledialog模块参数：
        
        title
        指定对话框的标题；
        
        prompt        　显示的文字；
        
        initialvalue
        指定输入框的初始值；
        
        filedialog　　　　模块参数：
        
        filetype   　　  指定文件类型；
        
        initialdir 　　  指定默认目录；
        
        initialfile 　　 指定默认文件；
        
        title    　　　  指定对话框标题
        
        colorchooser模块参数：
        
        initialcolor  　 指定初始化颜色；
        
        title          　指定对话框标题；
          """

    def 模具一一滚动条(self):
        pass

        """
        
      13、滚动条（Scrollbar）
      
      与其他控件绑定；
      
      1、将这些控件的yscrollcommand选项设置为scrollbar的set方法。
      
      （Scrollbar使用set方法改变slder滑块的位置）
      
      2、将scrollbar的command选项设置为这些控件的yview方法。（控件使用yview或xview方法改变自身的视图）
      
      （由于控件代码执行的先后性，所以借助config方法实现双向关联）
      
      参数：
      
      orient
      方位：VERTICAL垂直；HORIZONTAL水平
        """

    def 模具一一颜色参数(self):
        pass
        """HTML 颜色名
        http://www.w3school.com.cn/tags/html_ref_colornames.asp
        """
class 类一一相应事件:  # 调用 类的模具  self.模具一一查看变量输出文本值('变量名', self.测试打印, 8)
    def __init__(self):
        self.测试打印 = 'ew'

        self.模具一一换手机头部信息()

    def 模具一一示例(self):
        pass
        """
        """
    def 模具一一字体(self):
        pass
        """
        1、字体（font)
    
        一般格式：（'Times -10 bold')
    
        ('Times', 10, 'bold', 'italic')
        依次表示字体、字号、加粗、倾斜
        """
    def 模具一一使用图片(self):
        pass
        """
        2、使用图片（image）
    
        photo = PhotoImage(file='path.gif')
    
        canvas = Canvas.create_image(image=photo)
    
        Tkinter只支持gif和bmp等少数几种格式，想要插入其他格式图片需要导入PIL；pip
        安装第三方类库pillow
    
        from PIL import Image, ImageTk
    
        source = Image.open('path.jpg')
    
        photo = ImageTk.PhotoImage(source)
        """
    def 模具一一数据容器(self):
        pass
        """
        3、数据容器
    
        使用set和get方法进行传值和取值，
    
        StringVar()        ：字符类型
    
        BooleanVar()       ：布尔类型
    
        IntVar()                ：整数型
    
        DoubleVar()        ：浮点类型
        """
    def 模具一一数据绑定一传值(self):
        pass
        """
        4、数据绑定：（传值）
    
        Entry、Text、Laber、Button、Radiobutton、Checkbutton：使用textvariable接收或显示可变文本
    
        entryValue = StringVar()
    
        entry = Entry(textvariable=entryValue)
        entryValue.get()  # 输出接收的值
        """
    def 模具一一数据绑定一关联(self):
        pass
        """
        5、数据绑定：（关联）
    
        Radiobutton, Checkbutton：使用value（组件关联变量的值）、variable（组件所关联的变量）
    
        rbValue = IntVar()
    
        rb1 = Radiobutton(text="Red", variable=rbValue, value=1, command=func)
        """
    def 模具一一绑定事件(self):
        pass
        """
            6、绑定事件
        
            bind(sequence, func, add)
            bind_class(className, sequence, func, add)
            bind_all(sequence, func, add)
        
            对于按钮组件、菜单组件等可以在创建组件时通过command参数指定其事件处理函数。方法为bind;
            或者用bind_class方法进行类绑定，bind_all方法将所有组件事件绑定到事件响应函数上。
        
            事件参数：　　
            事件参数：    sequence
            所绑定的事件；
            func            　　    所绑定的事件处理函数，即响应事件；
            add
            可选参数，为空字符或‘+’；
            className    　    所绑定的类；
            """
    def 模具一一鼠标键盘事件(self):
        pass
        """
        7、鼠标键盘事件
    
          < Button - 1 >        　  　鼠标左键按下，2
        表示中键，3
        表示右键；
    
        < ButtonPress - 1 >    　   同上；
    
        < ButtonRelease - 1 >　　　 鼠标左键释放；
    
        < B1 - Motion >  　　       按住鼠标左键移动；
    
        < Double - Button - 1 >  　　 双击左键；
    
        < Enter >       　　      鼠标指针进入某一组件区域；
    
        < Leave >    　　         鼠标指针离开某一组件区域；
    
        < MouseWheel >  　   　　 滚动滚轮；
    
        < KeyPress - A > 　　  　　  按下A键，A可用其他键替代；
    
        < Alt - KeyPress - A >　　　   同时按下alt和A；alt可用ctrl和shift替代；
    
        < Double - KeyPress - A >　　  快速按两下A；
    
        < Lock - KeyPress - A >　　　  大写状态下按A；
    
        < Key > 指键盘的任意按键，
         """
    def 模具一一窗口事件(self):
        pass
        """
        8、窗口事件
    
        Activate        　　　　 当组件由不可用转为可用时触发；
    
        Configure      　　　　  当组件大小改变时触发；
    
        Deactivate    　　　　　 当组件由可用转变为不可用时触发；
    
        Destroy        　　　　  当组件被销毁时触发；
    
        Expose         　　　　　当组件从被遮挡状态中暴露出来时触发；
    
        Unmap        　　　　　　当组件由显示状态变为隐藏状态时触发；
    
        Map         　　　　     当组件由隐藏状态变为显示状态时触发；
    
        FocusIn       　　　 　  当组件获得焦点时触发；
    
        FocusOut      　　　　　 当组件失去焦点时触发；
    
        Property     　　　　    当窗体的属性被删除或改变时触发；
    
        Visibility       　　　　当组件变为可视状态时触发；
        """
    def 模具一一响应事件(self):
        pass
        """
        9、响应事件
    
        event对象（
    
        def func(event)）
    
            的API：
    
        char
        返回
        按键字符，仅对键盘事件有效；
        keycode
        返回
        按键编码，仅对键盘事件有效；
        keysym     　　　　　　　    返回
        按键名，仅对键盘事件有效；
        num
        鼠标按键，仅对鼠标事件有效；
        type         　　　　        所触发的事件类型；
        widget
        引起事件的组件；
        width, heigh
        组件改变后的大小，仅Configure有效；
        x, y
        返回
        鼠标当前位置，相对于窗口；
        x_root, y_root　    返回
        鼠标当前位置，相对于整个屏幕"""


class 类一一各控件事例:  # 调用 类的模具  self.模具一一查看变量输出文本值('变量名', self.测试打印, 8)
    def __init__(self):
        self.测试打印 = 'ew'
        self.实例窗口 = tk.Tk()
        self.实例窗口.title('示例窗口')  # 窗口标题
        self.实例窗口.geometry('600x500')  # 窗口 大小尺寸

        self.模具一一画布()


        # 这里是窗口的内容
        self.实例窗口.mainloop()


    def 模具一一示例(self):
        pass
        """
        """

    def 模具一一一个示例窗口(self):
        self.实例窗口 = tk.Tk()
        self.实例窗口.title('示例窗口')#窗口标题
        self.实例窗口.geometry('300x100')#窗口 大小尺寸

        # 这里是窗口的内容

        self.实例窗口.mainloop()

    def 模具一一标签示例(self):
        标签例 = tk.Label(self.实例窗口,
                     text='颜色标签',  # 标签的文字
                     bg='LightPink',  # 背景颜色
                     font=('Arial', 12),  # 字体和字体大小
                     width=15, height=2)  # 标签长宽
        标签例.pack()  # 固定窗口位置

    def 模具一一按钮控制标签的显示(self):
        #global on_hit
        self.on_hit = False  # 默认初始状态为 False

        def 绑定模具一按钮花样():
            #global on_hit

            if self.on_hit == False:  # 从 False 状态变成 True 状态
                self.on_hit = True
                文字变量储存器.set('you hit me')  # 设置标签的文字为 'you hit me'
            else:  # 从 True 状态变成 False 状态
                self.on_hit = False
                文字变量储存器.set('')  # 设置文字为空


        文字变量储存器 = tk.StringVar()  # 这时文字变量储存器
        标签例 = tk.Label(self.实例窗口,
                     textvariable=文字变量储存器,  # 使用 textvariable 替换 text, 因为这个可以变化
                     bg='green', font=('Arial', 12), width=15, height=2)
        标签例.pack()# 固定窗口位置

        按钮例= tk.Button(self.实例窗口,
                      text='点我变花样',  # 显示在按钮上的文字
                      width=15, height=2,
                      command=绑定模具一按钮花样)  # 点击按钮式执行的命令
        按钮例.pack()  # 固定窗口位置


    def 模具一一输入文本框(self):
        输入单行文本框例 = tk.Entry(self.实例窗口, show=None)#  输入密码时 show=‘*’
        输入单行文本框例.pack()# 固定窗口位置

        def 绑定模具一按钮输入():
            内容缓存 = 输入单行文本框例.get()# 发送
            多行文本框.insert('insert', 内容缓存) #插入

        def 绑定模具一按钮输出():
            内容缓存 = 输入单行文本框例.get()# 发送
            多行文本框.insert('end', 内容缓存)#插入 (2.2,内容缓存) 2行2列出插入内容

        输入按钮 = tk.Button(self.实例窗口, text='按钮打印', width=15,
                       height=2, command=绑定模具一按钮输入)
        输入按钮.pack()# 固定窗口位置


        输出按钮= tk.Button(self.实例窗口, text='按钮打印二',
                       command=绑定模具一按钮输出)
        输出按钮.pack()# 固定窗口位置

        多行文本框 = tk.Text(self.实例窗口,height=10)
        多行文本框.pack()# 固定窗口位置

    def 模具一一打印多行文本框(self):
        输入多行文本框例 = tk.Text(self.实例窗口, show=None)  # 输入密码时 show=‘*’
        输入多行文本框例.pack()  # 固定窗口位置

        def 绑定模具一按钮输入():
            多行文本列表=''
            多行文本列表 = 输入多行文本框例#.get()  # 发送
            # 多行文本列表.insert('insert', 内容缓存)  # 插入
            print('多行文本列表',多行文本列表)


        输入按钮 = tk.Button(self.实例窗口, text='按钮打印', width=15,
                         height=2, command=绑定模具一按钮输入)
        输入按钮.pack()  # 固定窗口位置

    def 模具一一列表框(self):
        文字变量储存器1= tk.StringVar()
        标签例 = tk.Label(self.实例窗口, bg='yellow', width=4, textvariable=文字变量储存器1)
        标签例.pack()# 固定窗口位置


        def 绑定模具一显示选择():
            value = 列表框例.get(列表框例.curselection())#curselection选择
            文字变量储存器1.set(value)

        按钮例 = tk.Button(self.实例窗口, text='显示列表框的选择', width=15,
                       height=2, command=绑定模具一显示选择)
        按钮例.pack()# 固定窗口位置


        文字变量储存器2 = tk.StringVar()
        文字变量储存器2.set((11, 22, 33, 44))

        列表框例 = tk.Listbox(self.实例窗口, listvariable=文字变量储存器2)
        list_items = [1, 2, 3, 4]
        for item in list_items:
            列表框例.insert('end', item)#insert 插入
        列表框例.insert(1, 'first')
        列表框例.insert(2, 'second')#insert 插入
        列表框例.delete(2)#  删除
        列表框例.pack()# 固定窗口位置


    def 模具一一单选框按钮(self):
        文字变量储存器 = tk.StringVar()
        标签例 = tk.Label(self.实例窗口, bg='yellow', width=20, text='选择项')
        标签例.pack()# 固定窗口位置


        def 绑定模具一选项输出():
            标签例.config(text='您已选择' + 文字变量储存器.get()) # config配置  get 发送

        单选框1 = tk.Radiobutton(self.实例窗口, text='选项 A',
                        variable=文字变量储存器, value='A',#variable 变量   value值
                        command=绑定模具一选项输出)
        单选框1.pack()# 固定窗口位置

        单选框2 = tk.Radiobutton(self.实例窗口, text='选项 B',
                            variable=文字变量储存器, value='B',#variable 变量   value值
                            command=绑定模具一选项输出)
        单选框2.pack()# 固定窗口位置

        单选框3 = tk.Radiobutton(self.实例窗口, text='选项 C',
                            variable=文字变量储存器, value='C',#variable 变量   value值
                            command=绑定模具一选项输出)
        单选框3.pack()# 固定窗口位置

    def 模具一一滑块例(self):
        标签例 = tk.Label(self.实例窗口, bg='yellow', width=20, text='选择')
        标签例.pack()# 固定窗口位置

        def 绑定模具一滑块选择输出(默认传入值):
            标签例.config(text='您已选择 ' + 默认传入值) # config配置

        滑块例 = tk.Scale(self.实例窗口, label='滑动选择', from_=30, to=300, orient=tk.HORIZONTAL,
                 length=400, showvalue=1, tickinterval=20, resolution=10, command=绑定模具一滑块选择输出)
        """from_=30  起始值
        to=300      终止值
        length=400  滑块框长度 
        showvalue=10 显示值 是否显示所选中的数字，取值为0时不显示，为1时显示。显示的标签单位长度为tickinterval，即显示出的数字的间隔，取值为3时，即显示5，8，11
        tickinterval=20  卡尺步长
        resolution=10  滑块步长
        """
        滑块例.pack()# 固定窗口位置

    def 模具一一勾选项例(self):
        标签例 = tk.Label(self.实例窗口, bg='yellow', width=20, text='勾选的选择')
        标签例.pack()# 固定窗口位置

        def 绑定模具一勾选选择():
            if (整数变量储存1.get() == 1) and (整数变量储存2.get() == 0):
                标签例.config(text='我选 Python')# config配置
            elif (整数变量储存1.get() == 0) and (整数变量储存2.get() == 1):
                标签例.config(text='我选 C++')# config配置
            elif (整数变量储存1.get() == 0) and (整数变量储存2.get() == 0):
                标签例.config(text='我都不选')# config配置
            else:# 否则
                标签例.config(text='我选两个')# config配置

        整数变量储存1 = tk.IntVar()
        整数变量储存2 = tk.IntVar()
        勾选项1 = tk.Checkbutton(self.实例窗口, text='Python', variable=整数变量储存1, onvalue=1, offvalue=0,
                            command=绑定模具一勾选选择)# onvalue 开值 ，offvalue 关值
        勾选项2 = tk.Checkbutton(self.实例窗口, text='C++', variable=整数变量储存2, onvalue=1, offvalue=0,
                            command=绑定模具一勾选选择)# onvalue 开值 ，offvalue 关值
        勾选项1.pack()# 固定窗口位置
        勾选项2.pack()# 固定窗口位置

    def 模具一一画布(self):

        canvas = tk.Canvas(self.实例窗口, bg='blue', height=150, width=200)
        image_file = tk.PhotoImage(file=r'E:\go学习文件\src\测试\ooopic_1542767823.png')
        image = canvas.create_image(10, 10, anchor='nw', image=image_file)
        x0, y0, x1, y1 = 90, 90, 120, 120
        line = canvas.create_line(x0, y0, x1, y1)
        oval = canvas.create_oval(x0, y0, x1, y1, fill='yellow')
        arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180, fill='green')
        rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
        canvas.pack()

        def moveit():
            canvas.move(rect, 0, 2)

        b = tk.Button(self.实例窗口, text='move', command=moveit).pack()

    def 模具一一示例(self):
        pass
        """
        """




if __name__ == '__main__':
    控件事例 = 类一一各控件事例()
