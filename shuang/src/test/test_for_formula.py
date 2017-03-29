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



###因为我想做批量校验，减少数据库 io，所以希望输入的就是两个 ssq，但是在批量验证的时候，我可以通过批量输入公式，然后来进行校验。先循环 ssq，再循环 formula
##如果输入的是ssq 范围和公式列表，则按一个一个 ssq 和公式列表来计算，todo num_range 要默认1，如何默认1？要校验 formula list 是否有效

###需要新增一个提交 batch 的计算界面。。。。差不多就是计算请求了，然后通过这个来计算请求的计算结果。
###不过这个可以迟一点做，先做计算完才能停的，即计算完就显示计算结果这样。还有好多内容，还要显示计算结果。。。。不过这个似乎那个 django 的前段也可以做。够快速了。



###以下是校验数据的结果是否正确，并不需要写入数据库？还是写以下好吧？按 batch 记录，然后记录 batch 和提交的计算结果？
###todo 增加计算结果的 batch 字段，同时增加了写入数据库的内容  ；其实还是会有只算值，不保存结果的，比如测试一个公式
def caculate_result(now,next_ssq,formula):
###计算结果值
    result_value=eval(formula.formula_express)
    print 'result_value=',result_value,'now balls:',now.list_all_balls()
    formula_value=[result_value]
    if formula.formula_type=='get_blue_tail_list': #取蓝球尾数的值
        if result_value >10:
            print 'error 余数超过10'#todo 后续需要改成 return
        elif 0<=result_value<=6:
            formula_value=[10+result_value,result_value]
        elif 6<result_value<=9:
            formula_value = [result_value]

    print formula_value,formula.formula_type

##以下为验证
###运行公式计算公式的结果

    ###获得需要验证的下一个 ssq 或 通过快速的上去了验证结果
    if formula_value :
        if formula.formula_type=='get_blue_tail_list': #取蓝球尾数的值
            for i in formula_value:
                if i==next_ssq.b1:
                    print 'i',i
                    print True,next_ssq.list_all_balls()
                    return 'True'
                    # todo insert into result,需要在循环结束以后

        elif formula.formula_type=='kill red':
            for i in formula_value:
                if i==next_ssq.r1 or i==next_ssq.r2 or i==next_ssq.r3 or i==next_ssq.r4 or i==next_ssq.r5 or i==next_ssq.r6:
                    print i,'Ture'
                    return  'Ture'
        return 'False'
    else :
        return 'Null'

###把公式结果和验证结果插入


def formula_test(num_start,num_range,formula_list):#
    '''输入起始期数，和范围（空则取指定ssq，0取所有值），以及公式id列表（空则计算所有公式）'''
#获取 ssq 列表
    ssq_list = []
    if  num_range>1 :
        #todo 根据 numstart 和 range 获得需要计算的，排好序的 ssq 序列，下面的取 ssq 要改，单纯的加一不靠谱。需要做好列表穿进去
                    #todo 增加 formulalist 的取值，前端传进来的估计只有 formula 的 id 不一定能传值进来。
        ssq_list=TSsqShishibiao.objects.filter(num__gte=num_start)[0:num_range-1]  ##ssqlist，效率差点就差点吧
    elif num_range is None :
        ssq_list = TSsqShishibiao.objects.filter(num__exact=num_start)# 为空取指定的 ssq

    elif num_range==0:
        ssq_list = TSsqShishibiao.objects.all()  # 取所有的 ssq


# 获取公式列表
    formulas_list=[]
    if formula_list:
        for i in formula_list:
            if ssq_formula.objects.filter(formula_id=i).exists():
                formulas_list.append(ssq_formula.objects.filter(formula_id=i)[0])
    else:
        formulas_list=ssq_formula.objects.filter(attribute2__exact='Active')

#开始循环计算最终的校验结果
    print ssq_list
    print formulas_list
    for p in ssq_list:
        for j in  formulas_list:
            result=caculate_result(p,p.get_next(),j)
            # print p.num,p.get_next().num,j.formula_express
#
formula_test(2003033,None,'')
