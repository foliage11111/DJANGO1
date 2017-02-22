#-*- coding: utf8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from shuang.src.front_query.front_query import get_all_rows_cond
from shuang.src.calculater.calculate_property import cal_shishibiao_ext, cal_basic_ext

from shuang.src.basic.basic_model import FoliageSsq, TSsqShishibiao

__author__ = 'zr'


def index(request):
    '''
    导航主页
    :param request:
    :return:
    '''
    t = loader.get_template("basic/mainFrame.html")

    return HttpResponse(t.render(Context))


def normal(request):
    """
    普通的查询双色球
    仅返回编号，红，蓝
    :param request:
    :return:
    """
    t = loader.get_template('basic/normal_search.html')
    ssq1= TSsqShishibiao.objects.filter(num__gte=2017001)
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
    t = loader.get_template('basic/sepcial_search.html')

    if request.method=='POST':# if 'ssq_num' in request.GET:#GET是一个dict，使用文本框的name作为key #在这里需要做一个判断，是否存在提交数据，以免报错

        conditions={'ts.num=':request.POST['ssq_num'],'ts.num>':request.POST['start_num'],'ts.num<':request.POST['end_num'],'limit 0,':request.POST['batch'],'order by':' ts.num desc'}

        if conditions['ts.num=']:
            del conditions['ts.num>']
            del conditions['ts.num<']
        if conditions['limit 0,']:
            print conditions
        else:
            del conditions['limit 0,']

        ssq1=get_all_rows_cond(conditions)
        Context={'ssq1':ssq1,'message':'done'}
        return HttpResponse(t.render(Context))

    Context={'ssq1':'','message':'form fail'}
    return HttpResponse(t.render(Context))


def all_fact_ext(request):
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


    t = loader.get_template('basic/normal_search.html')
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


    t = loader.get_template('basic/normal_search.html')
    ssq1= TSsqShishibiao.objects.filter(num=2013001)
    ##ssq1=FoliageSsq.objects.filter(num__lt=2003001,num__gt=2003001-1001).order_by("-num")
    # cc= cal_shishibiao_ext(ssq1[0])

    Context={'ssq1':ssq1}
    return HttpResponse(t.render(Context))