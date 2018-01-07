#coding: utf8
from django.contrib import admin
from shuang.src.formula.formula_controller import formula_test
from shuang.src.formula.formula_model import ssq_formula,ssq_formula_fact
from shuang.src.basic.basic_model import  TSsqShishibiao,TSsqShishibiao_ext
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

__author__ = 'zr'


@admin.register(ssq_formula)
class re_formula (admin.ModelAdmin):  ##公式的 admin

    actions = ['make_formula_cal']#最开始的时候我不是写字符串，而是通过import 了之后写进去的。方法写在里面后就变了

    list_display=('formula_id','formula_name','formula_type',) #显示列表

    search_fields = ('formula_id','formula_name','formula_type',)  #搜索列表

    list_editable=('formula_name','formula_type',) #就地编辑

    fieldsets=(  #编辑列表
        ['基本信息',
         {'fields':('formula_id','formula_name','formula_type')

          }
        ],
        ['详细信息',
         {'classes': ('collapse',), # CSS
          'fields':('formula_express','formula_note')
          }
        ]

    )

    def make_formula_cal(slef, request, queryset):
        '''按输入的 formula_list计算所有的结果,如果开始位置找不到则计算所有结果'''

        #print '由于要指定开始的位置，所以不能直接把输入的 queryset 直接传进去，使用了[obj]'
        message='返回信息    '
        for obj in queryset:
            message=message+'公式'+str(obj.formula_name)+'：'
            batch='初始化'
            if obj.ssq_formula_fact_set.all().exists():
                max_ssq=obj.ssq_formula_fact_set.latest('target_periods')
                batch=formula_test(max_ssq.target_periods,0,[obj]) ##从指定的某个地方开始计算
                message =message+'从'+str(max_ssq.target_periods) +'期开始计算，'+' batch='+batch+'；'
            else:
                batch=formula_test('', -1, [obj])
                message=message+ '该公式不存在任何计算结果，重新开始计算的batch=' +batch+'；'


        slef.message_user(request, message)##最后输出一个信息
    make_formula_cal.short_description = '计算公式的结果'#给下拉操作定义个中文名称

@admin.register(ssq_formula_fact)
class re_formula_fact (admin.ModelAdmin):##公式的计算结果展示

    list_display=('batch','now_periods','target_periods','result','formula_value','formula_type','right_nums','formula','attribute1') #显示列表

    search_fields = ('batch','now_periods','result','right_nums','formula')  #搜索列表

    #list_editable=('formula_name','formula_type',) #就地编辑

    fieldsets=(  #编辑列表
        ['基本信息',
         {'fields':('batch','now_periods','target_periods','result')

          }
        ],
        ['详细信息',
         {'classes': ('collapse',), # CSS
          'fields':('formula_value','formula_type','right_nums')
          }
        ]

    )
