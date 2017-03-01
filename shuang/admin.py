#coding: utf8
from django.contrib import admin

# Register your models here.
# Register your models here.

from shuang.src.formula.formula_model import formula_fact_per,ssq_formula,ssq_formula_fact

class formula (admin.ModelAdmin):
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

admin.site.register(ssq_formula,formula)
admin.site.register([formula_fact_per,ssq_formula_fact])