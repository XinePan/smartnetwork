# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.

from .models import Tester

class TesterAdmin(admin.ModelAdmin):
    list_display = ('id','name','sex','email','age','phone','image','status','create_time')
    list_filter = ('sex', 'status', 'create_time')
    search_fields = ('name','email','phone')
    fieldsets = (
        (None,{
            'fields':(
                'name',
                ('sex','age','image','Introduction'),
                ('email','phone'),
                'status'
            )
        }
        ),
    )

admin.site.register(Tester,TesterAdmin)