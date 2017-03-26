# -*- coding: utf8 -*-
__author__ = 'zr'
import re
import datetime
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJANGO1.settings")

django.setup()
from shuang.src.basic.basic_model import FoliageSsq
from shuang.src.basic.basic_model import TSsqShishibiao
from shuang.src.formula.formula_model import ssq_formula

# ssq1=map(int,['05', '14', '20', '26', '30', '33', '12'])
# print ssq1
# print ssq1.reverse()
# print ssq1

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

# exec("X1=R1**2;print X1")
# print X1
# exec('X1='+'eval(formula3)')
# print X1
# print f1,f2,f3
# 还需要特殊的函数，来保证值不大于16，或者不超过32？
# formula_list = ssq_formula.objects.filter().order_by('-formula_id')[0:9]
# print formula_list
###第一部分是计算结果出来
###获得需要计算的公式内容
fumual='now.b1*2%10'
formula_type='get_blue_tail_list'
#todo 定义两个方法  #singl 需要传当前期数，batch 则需要另外写一个方法取一个列表来操作，输入选择性范围。




###因为我想做批量校验，减少数据库 io，所以希望输入的就是两个 ssq
### todo 但是还有只做一半的，仅计算结果，这里要拆开
def formula_test(num,formula):
    now = TSsqShishibiao.objects.filter(num=num)[0]  # 取指定的 ssq
    next_ssq = TSsqShishibiao.objects.filter(num=num + 1)[0]  # 获取需要验证的 ssq

    #todo 调用后如何做后续处理


def caculate_result(now,next_ssq):
###计算结果值
    result_value=eval(fumual)
    print 'result_value=',result_value,'now balls:',now.list_all_balls()
    formula_value=[]
    if formula_type=='get_blue_tail_list': #取蓝球尾数的值
        if result_value >10:
            print 'error 余数超过10'#todo 后续需要改成 return
        elif 0<=result_value<=6:
            formula_value=[10+result_value,result_value]
        elif 6<result_value<=9:
            formula_value = [result_value]

    print formula_value,formula_type

##以下为验证
###运行公式计算公式的结果

    ###获得需要验证的下一个 ssq 或 通过快速的上去了验证结果
    if formula_value :
        if formula_type=='get_blue_tail_list': #取蓝球尾数的值
            for i in formula_value:
                if i==next_ssq.b1:
                    print 'i',i
                    print True,next_ssq.list_all_balls()
                    return 'True'
                    # todo insert into result,需要在循环结束以后
        return 'False'
    else :
        return 'Null'

###把公式结果和验证结果插入


