#-*- coding: utf8 -*-
from django.http import HttpResponse
from django.template import loader
import sys
from shuang.src.basic.basic_model import TSsqShishibiao
from shuang.src.basic.basic_controller import cal_shishibiao_ext
from shuang.src.spider.pachong import get_web,get_web_datachart_ajax

__author__ = 'zr'


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
            print (num)
            batch,return_code[0]=get_web_datachart_ajax(num) #按个抓取双色球，并返回列表和查询网页状态

            if batch:
                for i in batch:
                    print('新 ssq 是否存在？', i)
                    ssq_list= TSsqShishibiao.objects.filter(num=i[0])#确实事实表里面是否已近各有了这个期数

                    if not ssq_list.exists() : #如果是空的说明不存在,我之前还判断里面的[0]，其实一点都没有，所以报错了
                        print ('插入新 ssq', i[0])
                        ssq_tmp=TSsqShishibiao()
                        ssq_tmp.chushihua_easy(i) #列表初始化事实表，并关联总表外键
                        ssq_tmp.save()
                        print('事实表插入完成')
                        ssq_ext=cal_shishibiao_ext(ssq_tmp)
                        #ssq_ext.num=ssq_tmp
                        ssq_ext.save()
                        print('ext插入完成')
                        return_list.append(i)
                if return_list:
                    print ('全部插入完成',return_list)
                    return_code[0] = '全部插入完成'
                else:
                    return_code[0] = '没有更新的数据，未发生数据写入'
            else:
                print ('web get nothing')
                return_code[0] = 'form fail !!!!!!!!!!!!!!!!!!!'
            # print '为什么不插入 ext 表？'
            # for j in return_list:#先全部插入事实表，再把插入成功的数据生成对应的事实表
            #     ssq_tmp2=TSsqShishibiao()
            #     ssq_tmp2.chushihua(j)
            #     ssq_ext=cal_shishibiao_ext(ssq_tmp2)
            #     ssq_ext.save()
            #     print  '插入外键表',j

    except Exception as e:
        print (e)
        print(sys._getframe().f_code.co_name)
        return_code[0]='form fail !!!!!!!!!!!!!!!!!!!'

    t = loader.get_template('basic/spider_search.html')
    Context={'ssq1':return_list,'message':return_code[0],'batch':num,'ssq_len':len(return_list)}
    return HttpResponse(t.render(Context))