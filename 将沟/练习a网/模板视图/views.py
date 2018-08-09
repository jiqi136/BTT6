

# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render

def 主页内容(request):
    字典 = {}
    字典['标题'] = '欢迎光临3e'
    字典['内容'] = '一站式掌握必知必会全部技能'
    return render(request, '模板视图模板/home.html', 字典)
