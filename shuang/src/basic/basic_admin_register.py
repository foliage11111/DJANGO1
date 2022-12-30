#coding: utf8
from django.contrib import admin
import sys
import shuang
from shuang.src.basic.basic_model import  TSsqShishibiao,TSsqShishibiao_ext,FoliageSsq,FoliageSsq_ext
__author__ = 'zr'

#todo TSsqShishibiao  and TSsqShishibiao_ext

#todo FoliageSsq and FoliageSsq_ext


class basic_model_ext(admin.TabularInline):
    class Meta:
        verbose_name = '历史数据扩展'
        verbose_name_plural = '历史数据扩展'
    model = TSsqShishibiao_ext  #不需要写前面的注册，只需要这么写？
    extra = 1

@admin.register(TSsqShishibiao)
class fact_model (admin.ModelAdmin):


   # actions = ['make_formula_cal']#最开始的时候我不是写字符串，而是通过import 了之后写进去的。方法写在里面后就变了

    list_display=('num','r1','r2','r3','r4','r5','r6','b1','sum1') #显示列表

    search_fields = ('num','sum1','formula_type',)  #搜索列表

   # list_editable=('formula_name','formula_type',) #就地编辑

    inlines = (basic_model_ext,)  #关联事实表

    fieldsets=(  #编辑列表
        ['基本信息',
         {'fields':(('num','waijian','time'),),

          }
        ],
        ['详细信息',
         {'classes': ('wide',), # CSS
          'fields':(('r1','r2','r3','r4','r5','r6','b1','sum1'),),
          }
        ]


    )
    #readonly_fields = ('num', 'waijian','r1','r2','r3','r4','r5','r6','b1','sum1', 'time')

#admin.site.register(TSsqShishibiao, fact_model)
# class basic_model_ext(admin.TabularInline):
#     model = TSsqShishibiao_ext  #不需要写前面的注册，只需要这么写？