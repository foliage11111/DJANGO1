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
from shuang.src.formula.formula_model import  ssq_formula_fact
import time
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
##如果输入的是ssq 范围和公式列表，则按一个一个 ssq 和公式列表来计算，

###todo 需要新增一个提交 batch 的计算界面。。。。差不多就是计算请求了，然后通过这个来计算请求的计算结果。
###不过这个可以迟一点做，先做计算完才能停的，即计算完就显示计算结果这样。还有好多内容，还要显示计算结果。。。。不过这个似乎那个 django 的前段也可以做。够快速了。



###以下是校验数据的结果是否正确，并不需要写入数据库？还是写以下好吧？按 batch 记录，然后记录 batch 和提交的计算结果？
###todo 增加计算结果的 batch 字段，同时增加了写入数据库的内容  ；其实还是会有只算值，不保存结果的，比如测试一个公式
def caculate_result(now,next_ssq,formula):
    '''根据输入的第一个 ssq 和目标 ssq 以及公式 object 验证是否正确，并写入 batch'''
###计算结果值
    print '开始计算公式', formula.formula_express,formula.formula_name
    result_value=eval(formula.formula_express)
    print 'result_value=',result_value,'now balls:',now.get_all_balls_byList()
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
    if formula_value and next_ssq :
        if formula.formula_type=='get_blue_tail_list': #取蓝球尾数的值
            for i in formula_value:
                if i==next_ssq.b1:
                    print 'i',i
                    print True,next_ssq.list_all_balls()
                    return 'True',formula_value
                    # todo insert into result,需要在循环结束以后

        elif formula.formula_type=='kill red':
            for i in formula_value:
                if i==next_ssq.r1 or i==next_ssq.r2 or i==next_ssq.r3 or i==next_ssq.r4 or i==next_ssq.r5 or i==next_ssq.r6:
                    return  'False',formula_value #如果在下一期有就不是错了
                else:
                    return 'True', formula_value
        return 'Null',formula_value ## 不属于任何一种类型，返回 null
    else :
        return 'Null',formula_value

###把公式结果和验证结果插入


def formula_test(num_start,num_range,formula_list):
    '''
    num_start 起始期数， num_range 计算期数范围（空则取指定ssq，0取所有值），formula_list 公式id列表（空则计算所有公式）
    '''

#根据 range 获取 ssq 列表
    ssq_list = []
    if  num_range>1 :
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

    batch=int(time.time())
#开始循环计算最终的校验结果
    print ssq_list
    print formulas_list
    for now_ssq in ssq_list:
        for now_formula in  formulas_list:

            next_ssq=now_ssq.get_next()
            if next_ssq:
                result,re_value=caculate_result(now_ssq,next_ssq,now_formula)#计算结果

                fact=ssq_formula_fact()
                fact.batch='%d' %batch
                fact.now_periods=now_ssq.num
                fact.target_periods=next_ssq.num
                fact.formula=now_formula
                fact.result=result
                fact.formula_value=','.join(map(str,re_value))#caculate_result的返回值里面还要增加返回计算的数据
                fact.formula_type=now_formula.formula_type
                fact.create_date=datetime.datetime.today()
                fact.source_ssq=','.join(map(str,now_ssq.get_all_balls_byList()))
                fact.target_ssq=','.join(map(str,next_ssq.get_all_balls_byList()))
                fact.save()
            # print p.num,p.get_next().num,j.formula_express
    return batch
#
formula_test(2017016,10,'')


##todo 完善所有公式，然后计算
##todo 数据写进 controller 里面去
##