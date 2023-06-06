from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')

def show_student(request):
    date_list = models.Student.objects.all()
    context = {
        'values': date_list,
    }
    return render(request, 'showInformation.html', context)

def add_student(request):
    if request.method == 'GET':
        return render(request, 'addInformation.html')
    # 获取前端传来的数据
    name = request.POST.get('name')
    stu_id = request.POST.get('stu_id')
    class_id = request.POST.get('class_id')
    chinese = request.POST.get('chinese')
    math = request.POST.get('math')
    english = request.POST.get('english')
    # 将数据添加到数据库
    try:
        models.Student.objects.create(name=name, stu_id=stu_id, class_id=class_id, chinese=chinese, math=math, english=english)
    except:
        context = {
            'msg': '信息添加失败,请点击返回主页',
            'title': '添加学生信息'
        }
        return render(request, 'addReturnInfor.html', context)
    else:
        context = {
            'msg': '信息添加成功,请点击返回主页',
            'title': '添加学生信息'
        }
        return render(request, 'addReturnInfor.html',context)


def del_student(request):
    if request.method == 'GET':
        return render(request, 'delInformation.html')
    elif request.method == 'POST':
        # 获取前端传来的数据
        stu_id = request.POST.get('stu_id')
        # 将数据从数据库中删除
        flag = models.Student.objects.filter(stu_id=stu_id).delete()
        if flag[0] == 0:
            context = {
                'msg': '信息删除失败,请检查输入信息后重试!'
            }
            return render(request, 'delInformation.html', context)
        else:
            context = {
                'msg': '信息删除成功,请点击返回主页'
            }
            return render(request, 'addReturnInfor.html', context)
    else:
        context = {
            'msg': '请求方法不正确'
        }
        return render(request, 'delInformation.html', context)

def edit_student(request):
    if request.method == 'GET':
        return render(request, 'editInformation.html')
    # 获取前端传来的数据
    stu_id = request.POST.get('stu_id')
    data_list = models.Student.objects.filter(stu_id=stu_id)
    if not data_list:
        context = {
            'msg': '没有找到相关学生,请检查输入信息后重试!'
        }
        return render(request, 'editInformation.html', context)
    else:
        context = {
            'value': data_list
        }
        return render(request, 'changeInformation.html', context)

def edit_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        stu_id = request.POST.get('stu_id')
        class_id = request.POST.get('class_id')
        chinese = request.POST.get('chinese')
        math = request.POST.get('math')
        english = request.POST.get('english')
        # 将数据添加到数据库
        flag = models.Student.objects.filter(stu_id=stu_id).update(name=name, class_id=class_id, chinese=chinese, math=math,
                                    english=english)
        if not flag:
            context = {
                'msg': '信息修改失败,请点击返回主页',
                'title': '修改学生信息'
            }
            return render(request, 'addReturnInfor.html', context)
        else:
            context = {
                'msg': '信息修改成功,请点击返回主页',
                'title': '修改学生信息'
            }
            return render(request, 'addReturnInfor.html', context)

def search_student(request):
    if request.method == 'GET':
        return render(request, 'searchInformation.html')
    elif request.method == 'POST':
        # 获取前端传来的数据
        stu_id = request.POST.get('stu_id')
        data_list = models.Student.objects.filter(stu_id=stu_id)
        if not data_list:
            context = {
                'msg': '信息查询失败,请检查输入信息后重试!',
                'stu_id':stu_id,
            }
            return render(request, 'searchInformation.html', context)
        else:
            context = {
                'values': data_list,
            }
            return render(request, 'showInformation.html', context)
    else:
        context = {
            'msg': '请求方法不正确!'
        }
        return render(request, 'searchInformation.html', context)