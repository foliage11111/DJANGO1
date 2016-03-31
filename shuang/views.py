#-*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from models import TSsqShishibiao
# Create your views here.测试

def index(request):
    t = loader.get_template('test2.html')
    ssq1= TSsqShishibiao.objects.filter(num=2003001)
    request.get()
    # Context={'期数':str(ssq1[0].num),'红1':str(ssq1[0].r1)
    #     ,'红2':str(ssq1[0].r2)
    #     ,'红3':str(ssq1[0].r3)
    #     ,'红4':str(ssq1[0].r4)
    #     ,'红5':str(ssq1[0].r5)
    #     ,'红6':str(ssq1[0].r6)
    #     ,'蓝1':str(ssq1[0].b1)
    #     ,'和值':str(ssq1[0].sum1)
    #          }
    Context={'ssq1':ssq1}
    return HttpResponse(t.render(Context))
