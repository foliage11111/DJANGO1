#coding: utf8
from django.http import HttpResponse
from django.template import loader
from dataBase.gedata import dict_2_str_orm
from shuang.src.formula.formula_model import ssq_formula
from shuang.src.formula.formula_model import ssq_formula_fact
from shuang.src.basic.basic_model import TSsqShishibiao
from django.contrib import admin
import time
import datetime
__author__ = 'zr'


def formula_query(request):
    """
    查询双色球公式
        主要逻辑1、根据id删除，为空则提示错误；2、根据查询条件查询；3进入的时候全查询
    :param request:
    :return:
    """
    t = loader.get_template('formula/formula.html')
    if request.method=='POST':
        conditions={'formula_id__gte':request.POST['f_id'],'formula_name__contains':request.POST['f_name']}
        sql1 = dict_2_str_orm(conditions)
        limit_batch=request.POST['batch']
        limit_batch=limit_batch if limit_batch.isdigit() and limit_batch>0 else 10
        print limit_batch
        print sql1
        if request.POST['type_btn']=='delete': #删除
            id_list = request.POST.getlist('test','')#只能取得表单里面的数据
            print id_list
            formula_list=ssq_formula.objects.filter()
            if formula_list:
                formula_list[0].delete()
                Context={'fl1':formula_list,'message':'done'}
                return HttpResponse(t.render(Context))
            else:#如果为空
                Context={'fl1':formula_list,'message':'no such formula'}
                return HttpResponse(t.render(Context))

        elif request.POST['type_btn']=='insert':#新增
            print 'insert'
            if sql1:
                formula_list=ssq_formula.objects.filter()
                Context={'f_list':formula_list,'message':'done'}
                return HttpResponse(t.render(Context))

        else:
            #test_str={'formula_name__contains':'g','formula_id__gte':2}
            formula_list = ssq_formula.objects.filter(**sql1).order_by('-formula_id')[0:limit_batch]
            print formula_list
            Context = {'f_list': formula_list, 'message': 'else'}
            return HttpResponse(t.render(Context))

    formula_lista = ssq_formula.objects.filter().order_by('-formula_id')[0:10]  # 取前面10个  减号表示降序
    Context={'f_list':formula_lista,'message':'not post'}
    return HttpResponse(t.render(Context))


def define_formula(request):
    """
    定义双色球公式
    :param request:
    :return:
    """
    t = loader.get_template('formula/def_formula.html')

    if request.method=='POST':# if 'ssq_num' in request.GET:#GET是一个dict，使用文本框的name作为key #在这里需要做一个判断，是否存在提交数据，以免报错




        Context={'ssq1':'','message':'done'}
        return HttpResponse(t.render(Context))
    else:
        #表示空的，需要增加。
        Context={'formula':'','message':'form fail'}
        return HttpResponse(t.render(Context))


###todo 需要新增一个提交 batch 的计算界面。。。。差不多就是计算请求了，然后通过这个来计算请求的计算结果。
###不过这个可以迟一点做，先做计算完才能停的，即计算完就显示计算结果这样。还有好多内容，还要显示计算结果。。。。不过这个似乎那个 django 的前段也可以做。够快速了。



###以下是校验数据的结果是否正确，并不需要写入数据库？还是写以下好吧？按 batch 记录，然后记录 batch 和提交的计算结果？
###todo 增加计算结果的 batch 字段，同时增加了写入数据库的内容  ；其实还是会有只算值，不保存结果的，比如测试一个公式
def caculate_result(now,next_ssq,formula):
    '''根据输入的第一个 ssq 和目标 ssq 以及公式 object 验证是否正确，并写入 batch'''
###计算结果值
    print '开始计算公式', formula.formula_express, formula.formula_name
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


def formula_test(num_start,num_range,formulas_list):
    '''
    num_start 起始期数，num_range 计算期数范围（空则取指定ssq，0取某期以后所有值,-1就重新计算所有，none 取指定某一期的结果），formula_list 公式id列表（空则计算所有公式），返回 batch id
    '''

#根据 range 获取 ssq 列表
    if not num_start and num_range != -1 :
       return 'error'

    ssq_list = []
    if  num_range>1 :
        ssq_list=TSsqShishibiao.objects.filter(num__gte=num_start)[0:num_range-1]  ##ssqlist，效率差点就差点吧
    elif num_range is None :
        ssq_list = TSsqShishibiao.objects.filter(num__exact=num_start)# 为空取指定的 ssq
    elif num_start>0 and num_range==0:
        ssq_list = TSsqShishibiao.objects.filter(num__gte=num_start) #计算某一期后的所有值
    elif num_range==-1:
        ssq_list = TSsqShishibiao.objects.all()  # 取所有的 ssq


# 获取公式列表
    if formulas_list:
        print '传进来的公式：', formulas_list
        # 由于前段直接把所有对象传进来了，这里不再使用原来的计算方式
        # for i in formula_list:
        #     if ssq_formula.objects.filter(formula_id=i).exists():
        #         formulas_list.append(ssq_formula.objects.filter(formula_id=i)[0])
    else:
        formulas_list=ssq_formula.objects.filter(attribute2__exact='Active')
        print '计算所有公式'

    batch=int(time.time())
#开始循环计算最终的校验结果
    print '需要计算的所有 ssq：',ssq_list
    if ssq_list:
        for now_ssq in ssq_list:
            for now_formula in  formulas_list:
                next_ssq=now_ssq.get_next()
                if next_ssq:
                    result,re_value=caculate_result(now_ssq,next_ssq,now_formula)#计算结果

                    fact=ssq_formula_fact()
                    fact.batch='%d' %batch
                    fact.now_periods=now_ssq.num
                    fact.target_periods=next_ssq.num
                    fact.result=result
                    fact.formula = now_formula
                    fact.formula_value=','.join(map(str,re_value))#caculate_result的返回值里面还要增加返回计算的数据
                    fact.formula_type=now_formula.formula_type
                    fact.create_date=datetime.datetime.today()
                    fact.source_ssq=','.join(map(str,now_ssq.get_all_balls_byList()))
                    fact.target_ssq=','.join(map(str,next_ssq.get_all_balls_byList()))
                    fact.save()
                else:
                    return '没有ssq，即已经是最新的了'
    else:
        return '没有ssq，即已经是最新的了'
            # print p.num,p.get_next().num,j.formula_express
    return str(batch)


