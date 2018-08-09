# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render


def 分页内容(request):
    字典 = {}
    字典['标题'] = '3e'
    字典['内容'] = '模板过滤器可以在变量被显示前修改它'
    字典['列表'] = ['第一','第二','第三','第八','第五']
    return render(request, '新模板页模板/分页内容.html',字典)
