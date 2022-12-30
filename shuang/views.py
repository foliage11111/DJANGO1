#-*- coding: utf8 -*-
from django.http import HttpResponse
from django.template import loader,Context

# Create your views here.测试

def test(request):
    '''
    测试bootstrap 页面
    :param request:
    :return:
    '''
    t = loader.get_template('base.html')

   ## return HttpResponse(t.render(Context))
    return HttpResponse(t.render({'',''}))

