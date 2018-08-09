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

    名字年龄组 = 练习a网表(名字=字典['名字'],年龄=字典['年龄'])
    #年龄 = 练习a网表()
    #名字年龄组=[名字,年龄]

    名字年龄组.save()# 保存数据库

    return render(request, '模型数据库模板/页面内容.html', 字典)
