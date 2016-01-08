#-*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from models import TSsqShishibiao
# Create your views here.测试

def index(req):
    t = loader.get_template('test2.html')
    ssq1= TSsqShishibiao.objects.filter(num=2003001)
    Context={'user':str(ssq1[0].num),'title':'test2'}
    return HttpResponse(t.render(Context))
