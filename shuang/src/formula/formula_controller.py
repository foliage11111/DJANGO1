#coding: utf8
from django.http import HttpResponse
from django.template import loader
from dataBase.gedata import dict_2_str_orm
from shuang.src.chaxun.front_query import get_all_rows_cond
from shuang.src.formula.formula_model import ssq_formula

__author__ = 'zr'


def formula_query(request):
    """
    查询双色球公式
        主要逻辑1、根据id删除，为空则提示错误；2、根据查询条件查询；3进入的时候全查询
    :param request:
    :return:
    """
    t = loader.get_template('formula.html')
    if request.method=='POST':
        conditions={'id=':request.POST['f_id'],'name__contain=':request.POST['f_name']}
        if request.POST['del_btn']=='delete': #删除

            formula_list=ssq_formula.objects.filter(id=request.POST['formula_id'])
            if formula_list:
                formula_list[0].delete()
                Context={'fl1':formula_list,'message':'done'}
                return HttpResponse(t.render(Context))
            else:#如果为空
                Context={'fl1':formula_list,'message':'no such formula'}
                return HttpResponse(t.render(Context))

        if request.POST['qur_btn']=='query':#查询
            sql1=dict_2_str_orm(conditions)
            if sql1:
                formula_list=ssq_formula.objects.filter()
                Context={'fl1':formula_list,'message':'done'}
                return HttpResponse(t.render(Context))

    formula_list=ssq_formula.objects.filter(create_date__gt='2016-04-21')#为空则返回所有
    Context={'fl1':formula_list,'message':'form fail'}
    return HttpResponse(t.render(Context))


def define_formula(request):
    """
    定义双色球公式
    :param request:
    :return:
    """
    t = loader.get_template('def_formula.html')

    if request.method=='POST':# if 'ssq_num' in request.GET:#GET是一个dict，使用文本框的name作为key #在这里需要做一个判断，是否存在提交数据，以免报错

        conditions={'ts.num=':request.POST['ssq_num'],'ts.num>':request.POST['start_num'],'ts.num<':request.POST['end_num'],'limit 0,':request.POST['batch']}

        if conditions['ts.num=']:
            del conditions['ts.num>']
            del conditions['ts.num<']
            del conditions['limit 0,']
        ssq1=get_all_rows_cond(conditions)
        Context={'ssq1':ssq1,'message':'done'}
        return HttpResponse(t.render(Context))
    else:
        #表示空的，需要增加。
        Context={'formula':'','message':'form fail'}
        return HttpResponse(t.render(Context))