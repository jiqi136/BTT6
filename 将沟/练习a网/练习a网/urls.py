# -*- coding: utf-8 -*-
"""练习a网 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from 模板视图 import views as 模板视图_视图  # new
from 新模板页 import views as 新模板页_视图  # new
from 模型数据库 import tests as 模型数据库_视图  # new
from 提交表单 import views as 提交表单_视图  # new



urlpatterns = [
    path('', 模板视图_视图.主页内容, name='home'),  # new
    path('admin/', admin.site.urls),


    path('新模板页/', 新模板页_视图.分页内容, name='分页内容'),  # new
    path('模型数据库/', 模型数据库_视图.数据库操作, name='数据库操作'),  #
    path('提交表单/', 提交表单_视图.页面内容, name='提交表单'),  # new


]
