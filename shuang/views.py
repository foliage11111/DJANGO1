#-*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from dataBase.gedata import dict_2_str_orm



# Create your views here.测试

def test(request):
    '''
    测试bootstrap 页面
    :param request:
    :return:
    '''
    t = loader.get_template('base.html')
