#coding: utf8
from django.contrib import admin
from shuang.src.formula.formula_model import ssq_formula,ssq_formula_fact
from shuang.src.formula.forumla_admin_register import re_formula,re_formula_fact
from shuang.src.basic.basic_admin_register import fact_model,basic_model_ext


# Register your models here.
# Register your models here.

from shuang.src.formula.formula_model import formula_fact_per


admin.site.register([formula_fact_per])

# admin.site.register(ssq_formula_fact,re_formula_fact)
#
# admin.site.register(ssq_formula,re_formula)
admin.site.site_header='双色球系统'

admin.site.site_title='双色球系统'