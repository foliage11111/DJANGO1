# -*- coding: utf8 -*-
__author__ = 'zr'
import re
import datetime
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJANGO1.settings")

django.setup()

from shuang.src.formula.formula_model import ssq_formula

ssq1=map(int,['05', '14', '20', '26', '30', '33', '12'])
print ssq1
print ssq1.reverse()
print ssq1

R1=5
R2=14
R3=20
R4=26
R5=30
R6=33
BLUE=12
X1=0
SUM=R1+R2+R3+R4+R5+R6+BLUE
formula1='R5-R2'
formula2='R1*4-2'
formula3='SUM%16-4' # %百分号是取余数
formula4='R6//4' # //取整 33//4=8
formula5='X1 = R1**2' # 幂函数

f1=eval(formula4)
f2=eval(formula1)
f3=eval(formula3)

exec("X1=R1**2;print X1")
print X1
exec('X1='+'eval(formula3)')
print X1
print f1,f2,f3
# 还需要特殊的函数，来保证值不大于16，或者不超过32？
# formula_list = ssq_formula.objects.filter().order_by('-formula_id')[0:9]
# print formula_list


