#-*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from models import TSsqShishibiao
from models import FoliageSsq
from shuang.pachong import get_web
from dataBase.gedata import SqlConn
from calculate_property import cal_shishibiao_ext
from calculate_property import cal_basic_ext

# Create your views here.测试

def test(request):
    t = loader.get_template('sepcial_search.html')

    return HttpResponse(t.render(Context))

def index(request):
    t = loader.get_template('normal_search.html')
    ssq1= TSsqShishibiao.objects.filter(num__gte=2015001)
    ##ssq1=FoliageSsq.objects.filter(num__lt=2003001,num__gt=2003001-1001).order_by("-num")
    # cc= cal_shishibiao_ext(ssq1[0])
    # itemDir = cc.__dict__
    # for i in itemDir:
    #     print '{0} : {1}'.format(i, itemDir[i])
    Context={'ssq1':ssq1}
    return HttpResponse(t.render(Context))

def search_basic(request):
    t = loader.get_template('normal_search.html')

    if request.method=='POST':# if 'ssq_num' in request.GET:#GET是一个dict，使用文本框的name作为key #在这里需要做一个判断，是否存在提交数据，以免报错
        ssq_num= int(request.POST['ssq_num'])
        #多表查询，要么我自己写死，就查某个日期范围内的值
        sql_context='select * from tssqshishibiao_ext te and t_ssq_shishibiao t where t.'
        sql=SqlConn()
        ssq1=sql.execute(sql_context)
        sql.close()

        Context={'ssq1':ssq1,'message':'done'}
        return HttpResponse(t.render(Context))
    Context={'ssq1':'','message':'form fail'}
    return HttpResponse(t.render(Context))

def spdier_search(request):
    t = loader.get_template('spider_search.html')
    return_list=[]
    if request.method=='POST':# if 'ssq_num' in request.GET:#GET是一个dict，使用文本框的name作为key #在这里需要做一个判断，是否存在提交数据，以免报错
        num= request.POST['batch']
        batch=get_web(num)
        for i in batch:
            ssq_list= TSsqShishibiao.objects.filter(num=i[0])
            if not ssq_list : #如果是空的说明不存在
                ssq_tmp=TSsqShishibiao()
                ssq_tmp.chushihua(i) #列表初始化事实表，并关联总表外键
                ssq_tmp.save()
                return_list.append(i[0])
    Context={'ssq1':return_list,'message':'Done'}
    return HttpResponse(t.render(Context))


def all_basic_ext1(request):
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