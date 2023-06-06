"""
URL configuration for StudentManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app01 import views


urlpatterns = [
    # 主页
    path('index/', views.index),
    # 查看学生信息
    path('student/', views.show_student),
    # 添加学生信息
    path('add/', views.add_student),
    # 删除学生信息
    path('del/', views.del_student),
    # 修改学生信息
    path('edit/', views.edit_student),
    # 提交修改
    path('edit_submit/', views.edit_submit),
    # 查找学生
    path('search/', views.search_student),
]