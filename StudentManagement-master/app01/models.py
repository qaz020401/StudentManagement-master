from django.db import models

# Create your models here.

class Student(models.Model):
    # 姓名
    name = models.CharField(max_length=32)
    # 学号
    stu_id = models.CharField(max_length=32, unique=True)
    # 班级
    class_id = models.CharField(max_length=32)
    # 语文成绩
    chinese = models.IntegerField(null=True)
    # 数学成绩
    math = models.IntegerField(null=True)
    # 英语成绩
    english = models.IntegerField(null=True)
