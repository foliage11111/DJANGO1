#-*- coding:utf8 -*-
from shuang.src.basic.basic_model import FoliageSsq, FoliageSsq_ext, TSsqShishibiao, TSsqShishibiao_ext

from django.conf import settings
import os
__author__ = 'zr'
####本方法统一都是输入一个ssq,事实表和基础表都有返回list的功能，然后返回他的某些ext属性

def cal_shishibiao_ext(tss_ball):
    #事实表根据本次球算出扩展属性,返回shishibiao_ext类型对象
    ball_ext=TSsqShishibiao_ext()
    ball_ext.id=tss_ball.num
    ball_ext.num=tss_ball  #启用外键后直接关联对象
    ball_ext.red_sum=tss_ball.sum1
    ball_ext.prime_reds=cal_zhishu(tss_ball)#质数
    ball_ext.odd_reds=cal_odd_reds(tss_ball)#偶数
    ball_ext.red_shouweikuadu=cal_all_kuadu(tss_ball)#红球首尾快读
    ball_ext.red_weihe=cal_weihe(tss_ball)#首尾跨度
    ball_ext.red_lianhaoshu=cal_lianhao(tss_ball)#连号数
    ball_ext.vertical_blue=cal_blue_differ(tss_ball)#蓝球跨度
    ball_ext.span_reds(cal_horizontal_span(tss_ball))#红球横向差
    ball_ext.vertical_reds(cal_vertical_red(tss_ball))#红球纵向差

    return ball_ext

def cal_basic_ext(tss_ball):
    #事实表根据本次球算出扩展属性,返回FoliageSsq_ext类型对象
    ball_ext=FoliageSsq_ext()
    ball_ext.id=tss_ball.num
    ball_ext.num=tss_ball.num
    ball_ext.red_sum=tss_ball.sum1
    ball_ext.prime_reds=cal_zhishu(tss_ball)#质数
    ball_ext.odd_reds=cal_odd_reds(tss_ball)#偶数
    ball_ext.red_shouweikuadu=cal_all_kuadu(tss_ball)#红球首尾快读
    ball_ext.red_weihe=cal_weihe(tss_ball)#首尾跨度
    ball_ext.red_lianhaoshu=cal_lianhao(tss_ball)#连号数

    ball_ext.span_reds(cal_horizontal_span(tss_ball))#红球横向差

    return ball_ext


def cal_horizontal_span(ball):
    '''
    红球差，后一个减前一个，返回一个list，对应5个水平位移
    :param ball:
    :return:
    '''
    ssq=ball.get_list_red_balls_byList()
    return [ssq[1]-ssq[0],ssq[2]-ssq[1],ssq[3]-ssq[2],ssq[4]-ssq[3],ssq[5]-ssq[4]]

def cal_zhishu(ball):
    '''
    计算质数
    :param 输入Foliagessq或者Tssqshishibiao的对象:
    :return:红球质数个数
    '''
    #ssq_property=TSsqShishibiao_ext()
    prime_reds=0
    zhishu=[2,3,5,7,11,13,17,19,23,29,31]
    ssq_red=ball.get_list_red_balls_byList()
    for i in ssq_red:
        if i in zhishu:
            prime_reds+=1
    return prime_reds

def cal_odd_reds(ball):
    '''
    计算偶数
    :param 输入Foliagessq或者Tssqshishibiao的对象:
    :return:红球偶数个数
    '''
    ssq_property=TSsqShishibiao_ext()
    ssq_property.odd_reds=0
    ssq_red=ball.get_list_red_balls_byList()
    for i in ssq_red:
        if (int(i) % 2) == 0:
            # print i
            ssq_property.odd_reds+=1
    return ssq_property.odd_reds

def cal_all_kuadu(ball):
    '''
    计算首尾跨度
    :param 输入Foliagessq或者Tssqshishibiao的对象:
    :return:红球首尾跨度
    '''
    if ball:
        return ball.r6-ball.r1
    else:
        return 0

def cal_weihe(ball):
    '''
    计算尾和
    :param 输入Foliagessq或者Tssqshishibiao的对象:
    :return:红球尾和，不包含蓝球
    '''
    ssq_red=ball.get_list_red_balls_byList()
    #ssq_property=TSsqShishibiao_ext()
    red_weihe=0
    for i in ssq_red:
        # print int(i)%10
        if i >10:
            red_weihe+=int(i)%10
    return red_weihe


def cal_lianhao(ball):
    '''
    计算连号个数
    :param 输入Foliagessq或者Tssqshishibiao的对象:
    :return:红球连号个数
    '''
   # ssq_property=TSsqShishibiao_ext()
    red_lianhaoshu=0
    list=cal_horizontal_span(ball)
    for i in list:
        if i==1:
            red_lianhaoshu+=1
    #红球差，后一个减前一个，返回一个list，对应5个水平位移
    if red_lianhaoshu>1:
        red_lianhaoshu+=1
    return red_lianhaoshu

def cal_blue_differ(now_ball):
 '''
计算蓝球跟上一期的差异
:param 输入Foliagessq或者Tssqshishibiao的对象:
:return:蓝球差异
 '''
 try:
    num=str(now_ball.num)[4:7]
    q=now_ball.num
    if num=='001':
        ex_ball=TSsqShishibiao.objects.filter(num__lt=q,num__gt=q-1001).order_by("-num")[0]
        if ex_ball:
           # print ex_ball.num,ex_ball.b1
            return now_ball.b1-ex_ball.b1
        else:
            return 0
    else:
        ex_ball=TSsqShishibiao.objects.filter(num=now_ball.num-1)[0]
        if ex_ball:
             return now_ball.b1-ex_ball.b1
        else:
            return 0
 except:
     return False

def cal_vertical_red(now_ball):
    '''
    计算红球上下期差异，已考虑红球跨年相减的情况
    :param 输入Foliagessq或者Tssqshishibiao的对象:
    :return:红球跟上一期的差异列表，如果有问题返回[0,0,0,0,0,0]
    '''
    num=str(now_ball.num)[4:7]
    q=now_ball.num
    try:

        print (q)
        if num=='001':
            ex_ball_list=TSsqShishibiao.objects.filter(num__lt=q,num__gt=q-1001).order_by("-num")
            if ex_ball_list:
                ex_ball=ex_ball_list[0]

                return [now_ball.r1-ex_ball.r1,now_ball.r2-ex_ball.r2,now_ball.r3-ex_ball.r3,now_ball.r4-ex_ball.r4,now_ball.r5-ex_ball.r5,now_ball.r6-ex_ball.r6]
            else:
                return [0,0,0,0,0,0]
        else:
            ex_ball_list=TSsqShishibiao.objects.filter(num=now_ball.num-1)
            if ex_ball_list:
                 ex_ball=ex_ball_list[0]
                 return [now_ball.r1-ex_ball.r1,now_ball.r2-ex_ball.r2,now_ball.r3-ex_ball.r3,now_ball.r4-ex_ball.r4,now_ball.r5-ex_ball.r5,now_ball.r6-ex_ball.r6]
            else:
                return [0,0,0,0,0,0]
    except:
        return False