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

from django.conf.urls import url
from django.contrib import admin
from shuang.views import index
from shuang.views import search_basic
from shuang.views import spdier_search
from shuang.views import all_basic_ext
from shuang.views import all_basic_ext1
from shuang.views import test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shuang/index$',index), #基本查询页面
    url(r'^shuang/index$',index), #基本查询页面
    url(r'^shuang/searchforbasic$',search_basic), #基本查询页面的 查询转跳
    url(r'^shuang/spdier$',spdier_search),
    url(r'^shuang/cal_baisc$',all_basic_ext), #基本查询页面#all_basic_ext
    url(r'^shuang/cal_baisc1$',all_basic_ext1),
    url(r'^shuang/test$',test),
    #url(r'shuang/indexs$','shuang.views.indexs'),
]

