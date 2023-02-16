#-*- coding: utf8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from shuang.src.front_query.front_query import get_all_rows_cond
from shuang.src.calculater.calculate_property import cal_shishibiao_ext, cal_basic_ext
from dataBase.gedata import SqlConn
from dataBase.gedata import dict_2_str_mysql
from shuang.src.basic.basic_model import FoliageSsq, TSsqShishibiao

__author__ = 'zr'


def index(request):
    '''
    导航主页
    :param request:
    :return:
    '''
    t = loader.get_template("basic/mainFrame.html")
    html = t.render({'now': ''})
    return HttpResponse(html)


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
            print (conditions)
        else:
            conditions['limit 0,']=50#默认只拿50个，免得崩溃

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
        print (vmin,vmin+tmp)
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

def update_shishibiao_ext():
    """
    由于以前用的方法太慢了，直接在全表查询，r1，r2...r6，b1的匹配方式太慢了
    改为获取了最新的事实表数据以后
    1、生成并插入临时表的最新匹配数据
    2、把临时表的数据匹配写入ext表里面去
    :return:
    成功则为true，失败则返回false
    """
    try:
        #把新生产的快速匹配数据插入临时表数据
        sql_insert = '''INSERT into ssb_ssq_temp  select ssb.num as shishinum ,fss.NUM as basicnum , null as last_update from   ssq.t_ssq_shishibiao ssb ,  foliage_ssq  fss
                        where fss.R1 =ssb.r1  and fss.R2 =ssb.r2  and fss.R3 = ssb.r3  and fss.R4 = ssb.r4 and fss.r5=ssb.r5 and fss.r6= ssb.r6 and fss.b1=ssb.b1 
                        and  ssb.waijian =0 and ssb.taoshu =1  '''
        cur = SqlConn()
        ssq1 = cur.execute(sql_insert )
        print('insert new ssq into table ssb_ssq_temp done：' + str(ssq1))
        cur.commit()

        #吧临时表数据反写回事实表
        sql_update='''update ssq.t_ssq_shishibiao ssb inner join  ssb_ssq_temp  sst  on ssb.num =sst.shishinum set ssb.waijian = sst.basicnum where  ssb.waijian =0 '''
        ssq2 = cur.execute(sql_update)
        print('update waijian colomun in t_ssq_shishibiao done：' + str(ssq2))
        cur.commit()


        sql_update = '''UPDATE ssb_ssq_temp sst set sst.last_update =SYSDATE() where sst.last_update is NULL '''
        ssq3 = cur.execute(sql_update)
        print('update last_update_time colomun in ssb_ssq_temp done：' + str(ssq3))
        cur.commit()

        cur.close()

    except Exception as e:
            print ('更新扩展执行错误，关闭'+e)
            raise e
    finally:

        cur.close()
    return 'true'