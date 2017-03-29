#coding: utf8
from django.http import HttpResponse
from django.template import loader
from dataBase.gedata import dict_2_str_orm
from shuang.src.front_query.front_query import get_all_rows_cond
from shuang.src.formula.formula_model import ssq_formula

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




        Context={'ssq1':ssq1,'message':'done'}
        return HttpResponse(t.render(Context))
    else:
        #表示空的，需要增加。
        Context={'formula':'','message':'form fail'}
        return HttpResponse(t.render(Context))