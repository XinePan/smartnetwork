# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Tester(models.Model):
    SEX_ITEMS=[(1,'男'),(2,'女'),(0,'未知')]
    STATUX_ITEMS=[(0,'申请'),(1,'通过'),(2,'拒绝')]
    name = models.CharField(max_length=128,verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS,verbose_name="性别")
    age = models.IntegerField(validators=[MaxValueValidator(200),MinValueValidator(1)],verbose_name="年龄")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20,verbose_name="电话")
    image = models.ImageField(verbose_name="头像")
    Introduction = models.TextField(verbose_name="简介")

    status = models.IntegerField(choices=STATUX_ITEMS,verbose_name='审核状态')

    create_time = models.DateTimeField(auto_now_add=True,editable=False,verbose_name="创建时间")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "人员"



