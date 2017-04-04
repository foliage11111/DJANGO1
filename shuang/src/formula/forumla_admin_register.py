#coding: utf8
from django.contrib import admin
from shuang.src.formula.formula_controller import make_formula_cal
from shuang.src.formula.formula_model import ssq_formula,ssq_formula_fact


__author__ = 'zr'


@admin.register(ssq_formula)
class re_formula (admin.ModelAdmin):

    actions = [make_formula_cal]#只能注册一次，每个方法就用这个 list 写进去吗？

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

@admin.register(ssq_formula_fact)
class re_formula_fact (admin.ModelAdmin):

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

