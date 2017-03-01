#-*- coding:utf8 -*-
"""DJANGO1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from shuang.src.basic.basic_controller import index, normal, search_allrows, all_fact_ext, all_basic_ext
from shuang.src.spider.spdier_controller import spider_search
from DJANGO1 import formula_urls

from shuang.views import test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shuang/index$',index), #基本求查询页面
    url(r'^shuang/normal$',normal), #基本查询页面
    url(r'^shuang/searchforbasic$',search_allrows), #查询所有的列 查询转跳
    url(r'^shuang/spider$',spider_search),#爬虫页面
    url(r'^shuang/', include('DJANGO1.formula_urls'))#
    ,
]

urlpatterns.extend(
    [
    url(r'^shuang/cal_baisc_ext$', all_basic_ext),  # 充填全局表的扩展表
    url(r'^shuang/cal_fact_ext$', all_fact_ext),  # 充填事实表的扩展表
    url(r'^shuang/test$', test),  # 测试bootstrap用
    ]
)


