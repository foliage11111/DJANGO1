#-*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from dataBase.gedata import dict_2_str_orm
from models import TSsqShishibiao
from models import FoliageSsq
from shuang.pachong.pachong import get_web
from shuang.chaxun.front_query import get_all_rows_cond
from shuang.jisuanqi.calculate_property import cal_shishibiao_ext
from shuang.jisuanqi.calculate_property import cal_basic_ext
from models import ssq_formula


# Create your views here.测试

def test(request):
    '''
    测试bootstrap 页面
    :param request:
    :return:
    '''
    t = loader.get_template('base.html')

    return HttpResponse(t.render(Context))


def index(request):
    '''
    导航主页
    :param request:
    :return:
    '''
    t = loader.get_template('test3.html')

    return HttpResponse(t.render(Context))

def normal(request):
    """
    普通的查询双色球
    仅返回编号，红，蓝
    :param request:
    :return:
    """
    t = loader.get_template('normal_search.html')
    ssq1= TSsqShishibiao.objects.filter(num__gte=2015001)
    ##ssq1=FoliageSsq.objects.filter(num__lt=2003001,num__gt=2003001-1001).order_by("-num")
    # cc= cal_shishibiao_ext(ssq1[0])
    # itemDir = cc.__dict__
    # for i in itemDir:
    #     print '{0} : {1}'.format(i, itemDir[i])
    Context={'ssq1':ssq1}
    return HttpResponse(t.render(Context))

def search_allrows(request):
    """
    带条件查询包含所有扩展数据的双色球
    :param request:
    :return:
    """
    t = loader.get_template('sepcial_search.html')

    if request.method=='POST':# if 'ssq_num' in request.GET:#GET是一个dict，使用文本框的name作为key #在这里需要做一个判断，是否存在提交数据，以免报错

        conditions={'ts.num=':request.POST['ssq_num'],'ts.num>':request.POST['start_num'],'ts.num<':request.POST['end_num'],'rownum<=':request.POST['batch']}

        if conditions['ts.num=']:
            del conditions['ts.num>']
            del conditions['ts.num<']
            del conditions['rownum<=']
        ssq1=get_all_rows_cond(conditions)
        Context={'ssq1':ssq1,'message':'done'}
        return HttpResponse(t.render(Context))

    Context={'ssq1':'','message':'form fail'}
    return HttpResponse(t.render(Context))

def spider_search(request):
    """
    爬虫的查询主程序
    :param request:
    :return:
    """
    return_list=[]
    return_code=['']
    num=50
    try:
        if request.method=='POST':# if 'ssq_num' in request.GET:#GET是一个dict，使用文本框的name作为key #在这里需要做一个判断，是否存在提交数据，以免报错
            num= request.POST['batch']
            batch,return_code[0]=get_web(num) #按个抓取双色球，并返回列表和查询网页状态
            for i in batch:
                ssq_list= TSsqShishibiao.objects.filter(num=i[0])#确实事实表里面是否已近各有了这个期数
                print 'if filter goes wrong',ssq_list,'0'
                if not ssq_list : #如果是空的说明不存在,我之前还判断里面的[0]，其实一点都没有，所以报错了
                    ssq_tmp=TSsqShishibiao()
                    ssq_tmp.chushihua(i) #列表初始化事实表，并关联总表外键
                    ssq_tmp.save()
                    return_list.append(i)
            print 'cross ssb'
            for j in return_list:#先全部插入事实表，再把插入成功的数据生成对应的事实表
                ssq_tmp2=TSsqShishibiao()
                ssq_tmp2.chushihua(j)
                ssq_ext=cal_shishibiao_ext(ssq_tmp2)
                ssq_ext.save()
    except Exception:
        return_code[0]='form fail'

    t = loader.get_template('spider_search.html')
    Context={'ssq1':return_list,'message':return_code[0],'batch':num,'ssq_len':len(return_list)}
    return HttpResponse(t.render(Context))


def all_basic_ext1(request):
    """
    事实表的外置扩展表的一键生成
    :param request:
    :return:
    """
    basic_list=TSsqShishibiao.objects.all()
    for i in basic_list:
        ext=cal_shishibiao_ext(i)
        # itemDir = ext.__dict__
        # for i in itemDir:
        #     print '{0} : {1}'.format(i, itemDir[i])
        ext.save()


    t = loader.get_template('normal_search.html')
    ssq1= TSsqShishibiao.objects.filter(num=2013001)
    ##ssq1=FoliageSsq.objects.filter(num__lt=2003001,num__gt=2003001-1001).order_by("-num")
    # cc= cal_shishibiao_ext(ssq1[0])

    Context={'ssq1':ssq1}
    return HttpResponse(t.render(Context))

def all_basic_ext(request):
    """
    基础表的外置扩展表一键生成
    :param request:
    :return:
    """
    vmin=0
    tmp=20000
    vmax=8861
    for i in range(vmax):

        basic_list=FoliageSsq.objects.filter(num__gt=vmin,num__lte=vmin+tmp)
        print vmin,vmin+tmp
        vmin=vmin+tmp

        for i in basic_list:
            ext=cal_basic_ext(i)
            # itemDir = ext.__dict__
            # for i in itemDir:
            #     print '{0} : {1}'.format(i, itemDir[i])
            ext.save()


    t = loader.get_template('normal_search.html')
    ssq1= TSsqShishibiao.objects.filter(num=2013001)
    ##ssq1=FoliageSsq.objects.filter(num__lt=2003001,num__gt=2003001-1001).order_by("-num")
    # cc= cal_shishibiao_ext(ssq1[0])

    Context={'ssq1':ssq1}
    return HttpResponse(t.render(Context))

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

    formula_list=ssq_formula.objects.filter(create_date__gt='2016/4/21')#为空则返回所有
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

        conditions={'ts.num=':request.POST['ssq_num'],'ts.num>':request.POST['start_num'],'ts.num<':request.POST['end_num'],'rownum<=':request.POST['batch']}

        if conditions['ts.num=']:
            del conditions['ts.num>']
            del conditions['ts.num<']
            del conditions['rownum<=']
        ssq1=get_all_rows_cond(conditions)
        Context={'ssq1':ssq1,'message':'done'}
        return HttpResponse(t.render(Context))
    else:
        #表示空的，需要增加。
        Context={'formula':'','message':'form fail'}
        return HttpResponse(t.render(Context))