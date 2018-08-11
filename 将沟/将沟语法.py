


class 类一一公共库:  # 调用 类的模具 self.模具一一数据库()
    def __init__(self):

        self.模具一一换头部信息()

        变量名="""
            
            """

    def 创建Django项目与运行(self):
        创建Django项目的目录='django-admin startproject 将沟项目名'
        项目根目录下一启动开发服务器='Python manage.py runserver'# runserver 负载压力低 指定端口
        高级命令="""python manage.py runserver 0.0.0.0:8000
        0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000。
        指定端口 python manage.py runserver 8080
                    """
        浏览器地址='127.0.0.1:8000'



        各文件和目录解释="""
        外层的  将沟项目名/目录与将沟无关，只是你项目的容器，可以任意命名。
            manage.py：一个命令行工具，用于与将沟进行不同方式的交互脚本，非常重要！
            内层的  将沟项目名/目录是真正的项目文件包裹目录，它的名字是你引用内部文件的包名，例如：将沟项目名.urls。
                    将沟项目名/__init__.py:一个定义包的空文件。
                    将沟项目名/settings.py:项目的主配置文件，非常重要！
                    将沟项目名/urls.py:路由文件，所有的任务都是从这里开始分配，相当于将沟驱动站点的内容表格，非常重要！
                    将沟项目名/wsgi.py:一个基于WSGI的web服务器进入点，提供底层的网络通信功能，增大网站访问的压力。
                                    上线后，与WEB服务如（apeche,wsgi）配合使用的配置文件
                    
                  """
        def settings项目的主配置文件():
            LANGUAGE_CODE = 'zh_Hans'# 简体汉字
            TIME_ZONE = 'Asia/Shanghai' # 上海时区


            DATABASES =' 数据库默认sqlite3 ，要更改为 MYSQL'#
            INSTALLED_APPS = '频道app管理'#
            STATIC_URL = '静态资源文件路径'
            TEMPLATES ='模板页面文件路径,html'
            MIDDLEWARE = '中间件，添加功能'
            ALLOWED_HOSTS =  '访问服务的IP地址'

            ROOT_URLCONF = 'py网站.urls  路由配置的文件名'
            WSGI_APPLICATION = 'py网站.wsgi.application 增大网站访问的配置文件名'

    def 简单视图(self):
        变量名 = """
                   """
        创建Django项目的目录 = 'django-admin startproject 将沟项目名'
        #  将沟项目名 / settings.py: 项目的主配置文件
        LANGUAGE_CODE = 'zh_Hans'  # 简体汉字
        TIME_ZONE = 'Asia/Shanghai'  # 上海时区
        项目根目录下一创建应用app = 'python manage.py startapp 频道名'  # 确保与manage.py文件处于同一级
        自定义的频道app绑定 = """频道app名 追加在 项目名settings文件中顶部的INSTALLED_APPS设置项。"""

        编写视图页面内容= """打开 频道名/views.py 
                            # coding:utf-8
                        from django.http import HttpResponse
                        #HttpResponse 取代了 Python语句中 print,打印显示出 文件的字符串
                         
                        def index(request):
                            return HttpResponse(r"欢迎光临 自强学堂!")
                   """
        绑定视图函数到对应的URL网址= """打开 将沟项目名/将沟项目名/urls.py 这个文件
                               from django.contrib import admin
                                from django.urls import path
                                from 频道名 import views as 频道名_views  # new
                                 
                                 
                                urlpatterns = [
                                    path('', 频道名_views.index),  # new
                                    path('admin/', admin.site.urls),
                                ]
                           """

    def 模板视图(self):
        变量名 = """
                      """
        创建Django项目的目录 = 'django-admin startproject 将沟项目名'
        #  将沟项目名 / settings.py: 项目的主配置文件
        LANGUAGE_CODE = 'zh_Hans'  # 简体汉字
        TIME_ZONE = 'Asia/Shanghai'  # 上海时区
        项目根目录下一创建应用app = 'python manage.py startapp 频道名'  # 确保与manage.py文件处于同一级
        自定义的频道app绑定 = """频道app名 追加在 项目名settings文件中顶部的INSTALLED_APPS设置项。"""

        def 数据与视图不分离():
            编写视图页面内容 = """打开 频道名/views.py 
                                        # coding:utf-8
                                   from django.shortcuts import render
        
        
                                def home(request):
                                    return render(request, '频道名+模板/home.html')
                               """
            建立模板目录与文件 = """在 频道名 目录下新建一个 templates（模板） 文件夹 再建 频道名同名的目录+模板（避免py程序搜索错误）
                                新建一个 home.html，html代码如下
                                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                                <!DOCTYPE html>
                                <html>
                                <head>
                                    <title>欢迎光临</title>
                                </head>
                                <body>
                                欢迎光临自强学堂
                                </body>
                                </html>
            
                                  """

        def 数据与视图分离():

            编写视图页面内容 = """频道名 目录view.py 文件代码：
            
               # -*- coding: utf-8 -*-

                # from django.http import HttpResponse
                from django.shortcuts import render
                
                def 主页内容(request):
                    字典 = {}
                    字典['标题'] = '欢迎光临3e'
                    字典['内容'] = '一站式掌握必知必会全部技能'
                    return render(request, '频道名模板/home.html', 字典)


                                  """

            模板内网页文件 = """  templates（模板） 文件夹 再建 频道名同名的目录 home.html  文件
                        文件代码：
                                      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                                    <!DOCTYPE html>
                                    <html>
                                    <head>
                                        <title>
                                           提交表单
                                        </title>
                                    </head>
                                    <body>
                                    <form method='post'>
                                    {% csrf_token %}  <!-- 防止伪装提交请求的功能 --> 
                                    <p>
                                    {{ form }}
                                    <input type="submit" value="提交">
                                    
                                    </form>
                                    </p>
                                    <p>{{ rlt }}</p>  <!--为表格处理结果预留位置--> 
                                    <br />
                                    </body>
                                    </html>

                                              """

        绑定视图函数到对应的URL网址 = """打开 将沟项目名/将沟项目名/urls.py 这个文件
                                 from django.contrib import admin
                                from django.urls import path
                                from 频道名 import views as 频道名_视图  # new
                                
                                
                                urlpatterns = [
                                    path('', 频道名_视图.主页内容, name='home'),  # new
                                    path('admin/', admin.site.urls),
                                ]
                                
                                 """


    def Django模板标签(self):
        变量名 = """
                         """
        理解 = """ 视图文件 views.py把数据 传递给 templates（模板）目录下的 home.html文件
                 html文件内的 html语句负责网页格式，而Python语句 解析数据，并渲染到html，两者是分开的
                 简单总结⼀下：⼀般的变量之类的⽤ {{ }}（变量）；
                 功能类的，⽐如循环，条件判断是⽤ {% %}（标签），功能类内 传递的变量 不用再添加 {{ }}
                 views.py 传递多个参数，打包成一个字典形式
                                 """

        def 条件判断if一else标签():
            变量名 = """
                      """
            基本语法格式如下 = """{% if condition %}
                             ... display
                        {% endif %}
                                     """
            或者 = """{% if condition1 %}
                       ... display 1
                    {% elif condition2 %}
                       ... display 2
                    {% else %}
                       ... display 3
                    {% endif %}
                        """
            多个变量做判断 = """根据条件判断是否输出。if/else 支持嵌套。
                    {% if %} 标签接受 and ， or 或者 not 关键字来对多个变量做判断 ，或者对变量取反（ not )，例如：
                    {% if athlete_list and coach_list %}
                         athletes 和 coaches 变量都是可用的。
                    {% endif %}
                                     """
        def 遍历循环for标签():
            变量名 = """
                                  """
            每一次循环 = """ 每一次循环中，模板系统会渲染在 {% for %} 和 {% endfor %} 之间的所有内容。
                    例如，给定一个运动员列表 athlete_list 变量，我们可以使用下面的代码来显示这个列表：
                    
                    <ul>
                    {% for 运动员 in 运动员列表 %}
                        <li>{{ 运动员.name }}</li>
                    {% endfor %}
                    </ul>
                      """
            列表被反向迭代 = """ 给标签增加一个 reversed 使得该列表被反向迭代：
                        {% for 运动员 in 运动员列表 reversed %}
                        ...
                        {% endfor %}
                                  """
            嵌套使用for标签 = """ 可以嵌套使用 {% for %} 标签：
                            
                            {% for athlete in athlete_list %}
                                <h1>{{ athlete.name }}</h1>
                                <ul>
                                {% for sport in athlete.sports_played %}
                                    <li>{{ sport }}</li>
                                {% endfor %}
                                </ul>
                            {% endfor %}
                                                   """
            for循环中还有很多有用的东西 = """变量	描述
                                    列表.counter	索引从 1 开始算
                                    列表.counter0	索引从 0 开始算
                                    列表.revcounter	索引从最大长度到 1
                                    列表.revcounter0	索引从最大长度到 0
                                    列表.first	当遍历的元素为第一项时为真
                                    列表.last	当遍历的元素为最后一项时为真
                                    列表.parentloop	用在嵌套的 for 循环中，获取上一层 for 循环的 列表
                                                  """
            列表中可能为空值时用for一empty = """<ul>
                                        {% for athlete in athlete_list %}
                                            <li>{{ athlete.name }}</li>
                                        {% empty %}
                                            <li>抱歉，列表为空</li>
                                        {% endfor %}
                                        </ul>
                                              """

            def 遍历循环for标签():
                变量名 = """
                                      """
                判断相等标签 = """ifequal（条件相等）/ifnotequal（条件不相等） 标签
                            {% ifequal %} 标签比较两个值，当他们相等时，显示在 {% ifequal %} （条件相等）和 {% endifequal %} （结束条件相等）之中所有的值。
                          
                            下面的例子比较两个模板变量 user 和 currentuser :
                            
                            {% ifequal user currentuser %}
                                <h1>Welcome!</h1>
                            {% endifequal %}
                                                  """
                判断相等标签的否则 = """和 {% if %} 类似， {% ifequal %} 支持可选的 {% else%} 标签：8
                                    
                                    {% ifequal section 'sitenews' %}
                                        <h1>Site News</h1>
                                    {% else %}
                                        <h1>No News Here</h1>
                                    {% endifequal %}
                                      """

                逻辑操作 = """==, !=, >=, <=, >, < 这些比较都可以在模板中使用，比如：
                （注意：比较符号前后必须有至少一个空格！）
                        {% if var >= 90 %}
                        成绩优秀，自强学堂你没少去吧！学得不错
                        {% elif var >= 80 %}
                        成绩良好
                        {% elif var >= 70 %}
                        成绩一般
                        {% elif var >= 60 %}
                        需要努力
                        {% else %}
                        不及格啊，大哥！多去自强学堂学习啊！
                        {% endif %}
                                                                          """
                逻辑操作 = """and, or, not, in, not in 也可以在模板中使用

                        假如我们判断 num 是不是在 0 到 100 之间：
                        {% if num <= 100 and num >= 0 %}
                        num在0到100之间
                        {% else %}
                        数值不在范围之内！
                        {% endif %}
                        
                        假如我们判断 'ziqiangxuetang' 在不在一个列表变量 List 中：
                        {% if 'ziqiangxuetang' in List %}
                        自强学堂在名单中
                        {% endif %}
                 """
                注释标签 = """Django 注释使用 {# #}。
                    {# 这是一个注释 #}
                      """
                过滤器 = """模板过滤器可以在变量被显示前修改它，过滤器使用管道字符，如下所示：
                        {{ name|lower }}
                                      """
                include标签 = """ {% include %} 标签允许在模板中包含其它的模板的内容。
                            下面这个例子都包含了 nav.html 模板：
                            {% include "nav.html" %}
                              """

    def 模型数据库(self):
        变量名 = """
                      """
        创建Django项目的目录 = 'django-admin startproject 将沟项目名'
        #  将沟项目名 / settings.py: 项目的主配置文件
        LANGUAGE_CODE = 'zh_Hans'  # 简体汉字
        TIME_ZONE = 'Asia/Shanghai'  # 上海时区
        项目根目录下一创建应用app = 'python manage.py startapp 频道名'  # 确保与manage.py文件处于同一级
        自定义的频道app绑定 = """频道app名 追加在 项目名settings文件中顶部的INSTALLED_APPS设置项。"""

        安装mysql驱动 = """pip install mysqlclient
                              """
        数据库配置 = """在项目的 settings.py 文件中找到 DATABASES 配置项，将其代码修改为：
           
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
                    'NAME': 'wan', # 不明原因出错,1049，疑似不接受中文，保险先建立 数据库名 	排序规则为utf8_croatian_ci	
                    'USER': 'root',
                    'PASSWORD': '',
                    'HOST':'localhost',
                    'PORT':'3306',
                        }
                    }

                              """
        制定数据库 = """修改 TestModel/models.py 文件，
                    类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，
                    数据类型则由CharField（相当于varchar）、DateField（相当于datetime），
                     max_length 参数限定长度。
                     代码如下：  
        
                    from django.db import models
 
 
                    class 练习a网表(models.Model):
                        名字 = models.CharField(max_length=30)
                        年龄 = models.IntegerField() #年龄与之后的字段 在数据库里再设置 为 允许 空值

                              """
        创建表结构 = """Django 1.7 及以上的版本需要用以下命令
                python manage.py makemigrations
                python manage.py migrate
                              """
        绑定视图函数到对应的URL网址 = """打开 将沟项目名/将沟项目名/urls.py 这个文件
                                       from 模型数据库 import tests as 模型数据库_视图  # 修改以往的 views为tests

                                       urlpatterns = [
                                       
                                                path('模型数据库/', 模型数据库_视图.数据库操作, name='数据库操作'),  # new
                                         """

        def 数据库操作():
            打开文件 = """打开 频道名/testdb.py
                          """

            def 数据库增删改查():


                添加数据 = """
                       from django.test import TestCase
    
                        # Create your tests here.
                        # -*- coding: utf-8 -*-
                        
                        from django.http import HttpResponse
                        
                        from 模型数据库.models import 练习a网表
                        
                        
                        # 数据库操作
                        def 数据库操作(request):
                            test1 = 练习a网表(名字='张三')
                            test1.save()
                            return HttpResponse("<p>数据添加成功！</p>")
                            
                            #总之，一共有四种方法
                            # 方法 1
                            Author.objects.create(name="WeizhongTu", email="tuweizhong@163.com")
                             
                            # 方法 2
                            twz = Author(name="WeizhongTu", email="tuweizhong@163.com")
                            twz.save()
                             
                            # 方法 3
                            twz = Author()
                            twz.name="WeizhongTu"
                            twz.email="tuweizhong@163.com"
                            twz.save()
                             
                            # 方法 4，首先尝试获取，不存在就创建，可以防止重复
                            Author.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")
                            # 返回值(object, True/False)
                                
                                          """

                获取数据 = """from django.test import TestCase
    
                        # Create your tests here.
                        # -*- coding: utf-8 -*-
                        
                        from django.http import HttpResponse
                        
                        from 模型数据库.models import 练习a网表
                        
                        
                        # 数据库操作  一
                        def 数据库操作(request):
                             # 初始化
                            response = ""
                            response1 = ""
                            
                            
                            # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
                            list = 练习a网表.objects.all()
                                
                            # filter相当于SQL中的WHERE，可设置条件过滤结果
                            response2 = 练习a网表.objects.filter(id=1) 
                            
                            # 获取单个对象
                            response3 = 练习a网表.objects.get(id=1) 
                            
                            # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
                            练习a网表.objects.order_by('名字')[0:2]
                            
                            #数据排序
                            练习a网表.objects.order_by("id")
                            
                            # 上面的方法可以连锁使用
                            练习a网表.objects.filter(名字="runoob").order_by("id")
                            
                            # 输出所有数据
                            for var in list:
                                response1 += var.name + " "
                            response = response1
                            return HttpResponse("<p>" + response + "</p>")
                        
                                          """
                更改数据 = """ 修改数据可以使用 save() 或 update():
                    # -*- coding: utf-8 -*-
                     
                    from django.http import HttpResponse
                     
                    from TestModel.models import Test
                     
                    # 数据库操作.
                    def 数据库操作(request):
                        # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
                        test1 = Test.objects.get(id=1)
                        test1.名字 = 'Google'
                        test1.save()
                        
                        # 另外一种方式
                        #Test.objects.filter(id=1).update(name='Google')
                        
                        # 修改所有的列
                        # Test.objects.all().update(name='Google')
                        
                        return HttpResponse("<p>修改成功</p>")

                                          """
                删除数据 = """删除数据库中的对象只需调用该对象的delete()方法即可：
                    # -*- coding: utf-8 -*-
                     
                    from django.http import HttpResponse
                     
                    from 练习a网表Model.models import 练习a网表
                     
                    # 数据库操作
                    def 数据库操作(request):
                        # 删除id=1的数据
                        练习a网表1 = 练习a网表.objects.get(id=1)
                        练习a网表1.delete()
                        
                        # 另外一种方式
                        # 练习a网表.objects.filter(id=1).delete()
                        
                        # 删除所有数据
                        # 练习a网表.objects.all().delete()
                        
                        return HttpResponse("<p>删除成功</p>")

                                          """

            def 分离的保存数据():
                保存数据视图 = """打开 频道名/testdb.py
                from django.test import TestCase

                # Create your tests here.
                # -*- coding: utf-8 -*-
                
                from django.http import HttpResponse
                
                from 模型数据库.models import 练习a网表
                from django.shortcuts import render
                
                
                # 数据库操作
                def 数据库操作(request):
                    字典 = {}
                    字典['标题'] = '3e数据库'
                    字典['名字'] = '处所出'
                    字典['年龄'] = 26
                    字典['添加成功'] = '数据添加成功！'
                
                    名字年龄组 = 练习a网表(名字=字典['名字'],年龄=字典['年龄'])# 多组数据 的保存
                    #年龄 = 练习a网表()
                    #名字年龄组=[名字,年龄]
                
                    名字年龄组.save()# 保存数据库
                
                    return render(request, '模型数据库模板/页面内容.html', 字典)

                                                      """
                页面模板 = """templates（模板） 文件夹 再建 频道名同名的目录 home.html  文件
                  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <!DOCTYPE html>
                    
                    <html>
                    <head>
                        <title>
                            {{标题}}
                        </title>
                    </head>
                    <body>
                    
                    <h3>
                        {{名字}}:{{年龄}}
                        <p>{{添加成功}}</p>
                    
                    </h3>
                    <br />
                    
                    
                    </body>
                    </html>
                                                      """

    def 提交表单(self):
        变量名 = """
                              """
        项目根目录下一创建应用app = 'python manage.py startapp 频道名'  # 确保与manage.py文件处于同一级
        自定义的频道app绑定 = """频道app名 追加在 项目名settings文件中顶部的INSTALLED_APPS设置项。"""
        新建文件 = """频道名  文件夹中新建一个 forms.py 文件
                from django import forms
                 
                class AddForm(forms.Form):
                    a = forms.IntegerField()
                    b = forms.IntegerField()
                              """
        编辑视图文件 = """视图函数 views.py 中
                    # coding:utf-8
                    from django.shortcuts import render
                    from django.http import HttpResponse
                     
                    # 引入我们创建的表单类
                    from .forms import AddForm
                     
                    def index(request):
                        if request.method == 'POST':# 当提交表单时
                         
                            form = AddForm(request.POST) # form 包含提交的数据
                             
                            if form.is_valid():# 如果提交的数据合法
                                a = form.cleaned_data['a']
                                b = form.cleaned_data['b']
                                return HttpResponse(str(int(a) + int(b)))
                         
                        else:# 当正常访问时
                            form = AddForm()
                        return render(request, '频道名+模板/index.html', {'form': form})
                                      """
        绑定视图函数到对应的URL网址 = """打开 将沟项目名/将沟项目名/urls.py 这个文件
                                         from django.contrib import admin
                                        from django.urls import path
                                        from 频道名 import views as 频道名_视图  # new


                                        urlpatterns = [
                                            path('', 频道名_视图.主页内容, name='home'),  # new
                                            path('admin/', admin.site.urls),
                                        ]

                                         """

    def admin后台管理站点(self):
        变量名 = """

                      """
        首先使用命令行创建默认库 = """python manage.py migrate """
        创建管理员用户 = """python manage.py createsuperuser  """
        创建管理员密码为 = """至少 8 个字符 qq962962 """

        为了站点的安全性 = """在实际环境中，为了站点的安全性，我们不能将管理后台的url随便暴露给他人，不能用/admin/这么简单的路径。

                    打开根url路由文件mysite/urls.py，修改其中admin.site.urls对应的正则表达式，换成你想要的，比如：
                    
                    from django.conf.urls import url
                    from django.contrib import admin
                    
                    urlpatterns = [
                        url(r'^my/set/', admin.site.urls),
                    ]

                    这样，我们必须访问http://127.0.0.1:8000/my/set/才能进入admin界面。
                    
                                          """
    def 创建频道功能应用app(self):
        app ="""一个项目由多个频道组成"""
        项目根目录下一创建应用app = 'python manage.py startapp 频道名' # 确保与manage.py文件处于同一级
        系统会自动生成应用的目录="""polls/
                                    __init__.py
                                    admin.py   把数据库绑定到这个文件后,可以在admin网站后台管理  界面下使用并管理该 频道 
                                    apps.py
                                    migrations/
                                        __init__.py
                                    models.py  数据库文件,ORM映射关系,python的数据库创建语句
                                    tests.py
                                    views.py   具体功能文件，由一个又一个函数模具组成
                                     urls.py  该频道 的路由配置文件
                                        """
        自定义的频道app绑定= """
        请注意settings文件中顶部的INSTALLED_APPS设置项。它列出了所有的项目中被激活的Django应用（app）。你必须将你自定义的app绑定在这里。每个应用可以被多个项目使用，并且可以打包和分发给其他人在他们的项目中使用。
        
        默认情况，INSTALLED_APPS中会自动包含下列条目，它们都是Django自动生成的：
        
            django.contrib.admin：admin管理后台站点
            django.contrib.auth：身份认证系统
            django.contrib.contenttypes：内容类型框架
            django.contrib.sessions：会话框架
            django.contrib.messages：消息框架
            django.contrib.staticfiles：静态文件管理框架

                   """
        在admin站点后台管理绑定频道app="""现在还无法看到应用，必须先在admin站点后台管理 中进行绑定，告诉admin站点，
                            请将  频道名 的模型加入站点内，接受站点的管理。

                        打开 频道名/admin.py文件，加入下面的内容：
                        
                        from django.contrib import admin
                        from .models import Question
                        
                        admin.site.register(Question)
                        """

    def 编写频道app视图(self):
        变量名 = """

                   """
        编写代码="""在  频道目录/views.py文件中，编写代码："""
        代码="""from django.http import HttpResponse
                    
                    def index(request):
                        return HttpResponse("Hello, world. You're at the polls index.")
            
                   """

        调用该视图= """为了调用该视图，我们还需要编写urlconf，也就是路由路径。现在，
                在  频道名目录中新建一个文件，名字为urls.py，在其中输入代码如下："""
        如下 = """from django.conf.urls import url
                from . import views
                app_name = '频道名' #如果要使用数据库表，添加这行
                
                urlpatterns = [
                    url(r'^$', views.index, name='index'),
                ]
                   """
        项目的主urls文件= """接下来，在项目的主urls文件中添加urlpattern条目，指向我们刚才建立的polls这个app独有的urls文件，
                   这里需要导入include模块。打开mysite/urls.py文件，代码如下："""
        代码如下= """from django.conf.urls import include, url
                    from django.contrib import admin
                    
                    
                    
                    urlpatterns = [
                        url(r'^频道名/', include('频道名.urls')),
                        url(r'^admin/', admin.site.urls),
                    ]

                   """#include语法相当于多级路由，它把接收到的url地址去除前面的正则表达式，将剩下的字符串传递给下一级路由进行判断。

        def url函数可以接收四个参数(self):
            变量名 = """ Django url() 可以接收四个参数，分别是两个必选参数：regex、view 和两个可选参数：kwargs、name，
            接下来详细介绍这四个参数。

                regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。
            
                view: 用于执行与正则表达式匹配的 URL 请求。
            
                kwargs: 视图使用的字典类型的参数。
            
                name: 用来反向获取 URL。
            

                       """
            Django2以上的版本 = """其中最大的几个改变如下：

                            import url 变成了 import path
                            如果是路径，则须在路径后加个 /
                            
                            旧版 django 的用法：
                            
                            from django.conf.urls import url
                             
                            from . import view
                             
                            urlpatterns = [
                                url(r'^hello$', view.hello),
                            ]
                            
                            新版的参考写法：
                            
                            from django.urls import path
                            from . import view
                            
                            urlpatterns = [
                                path('hello/', view.hello),
                            ]

                               """

    def 数据库安装(self):
        变量名 = """
                   
                   """
        想使用其他的数据库 = """
        如果你想使用其他的数据库，请先安装相应的数据库操作模块，并将settings文件中DATABASES位置的’default’的键值进行相应的修改，
        用于连接你的数据库。其中：
        ENGINE（引擎）：可以是django.db.backends.sqlite3、django.db.backends.postgresql、django.db.backends.mysql、
        django.db.backends.oracle，当然其它的也行。
        NAME（名称）：类似Mysql数据库管理系统中用于保存项目内容的数据库的名字。如果你使用的是默认的SQLite，
        那么数据库将作为一个文件将存放在你的本地机器内，此时的NAME应该是这个文件的完整绝对路径包括文件名，
        默认值os.path.join(BASE_DIR, ’db.sqlite3’)，将把该文件储存在你的项目目录下。
                   """
        操作Mysql数据库的例子= """
        import pymysql         # 一定要添加这两行！通过pip install pymysql！
                        pymysql.install_as_MySQLdb()
                        
                        DATABASES = {
                            'default': {
                                'ENGINE': 'django.db.backends.mysql',
                                'NAME': 'mysite',
                                'HOST': '192.168.1.1',
                                'USER': 'root',
                                'PASSWORD': 'pwd',
                                'PORT': '3306',
                                        }
                                    }
                                                       """

    def 创建模型(self):
        变量名 = """

                   """
        定义模型model = """模型本质上就是数据库表的布局，再附加一些元数据。
                           """
        简单的投票应用= """在这个简单的投票应用中，我们将创建两个模型：Question和Choice。Question包含一个问题和一个发布日期。
        Choice包含两个字段：该选项的文本描述和该选项的投票数。每一条Choice都关联到一个Question。这些都是由Python的类来体现，
        编写的全是Python的代码，不接触任何SQL语句。现在，编辑  频道名/models.py文件，具体代码如下：

                   """
        代码如下= """from django.db import models
                    
                    class Question(models.Model):
                        question_text = models.CharField(max_length=200)
                        pub_date = models.DateTimeField('date published')
                    
                    class Choice(models.Model):
                        question = models.ForeignKey(Question, on_delete=models.CASCADE)
                        choice_text = models.CharField(max_length=200)
                        votes = models.IntegerField(default=0)

                   """

        def 启用模型():
            变量名 = """

                          """
            代码看着有点少= """
                    其实包含了大量的信息，据此，Django会做下面两件事：
            
                创建该app对应的数据库表结构
                为Question和Choice对象创建基于Python的数据库访问API
            
            但是，首先我们得先告诉Django项目，我们要使用投票app。
            要将应用添加到项目中，需要在INSTALLED_APPS设置中增加指向该应用的配置文件的链接。对于本例的投票应用，
            它的配置类文件是  频道名/apps.py，路径格式为  频道名.apps.PollsConfig。我们需要在INSTALLED_APPS中，将该路径添加进去：
            实际上，在多数情况下，我们简写成‘频道名’就可以了：
              """
            运行启用模型命令 = """python manage.py makemigrations 频道名

                          """
            你会看到类似下面的提示= """Migrations for 'polls':
                          polls/migrations/0001_initial.py:
                            - Create model Choice
                            - Create model Question
                            - Add field question to choice
                            通过运行makemigrations命令，相当于告诉Django你对模型有改动，并且你想把这些改动保存为一个“迁移(migration)”。
                            migrations是Django保存模型修改记录的文件，这些文件保存在磁盘上。在例子中，
                            它就是  频道名/migrations/0001_initial.py，你可以打开它看看，
                            里面保存的都是人类可读并且可编辑的内容，方便你随时手动修改。
                          """
            对数据库执行真正的迁移动作= """接下来有一个叫做migrate的命令将对数据库执行真正的迁移动作。但是在此之前，让我们先看看在migration的时候实际执行的SQL语句是什么。
                                有一个叫做sqlmigrate的命令可以展示SQL语句，例如：

                                        $ python manage.py sqlmigrate 频道名 0001


                          """









