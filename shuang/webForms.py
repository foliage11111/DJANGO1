#-*- coding: utf8 -*-
__author__ = 'zr'
#统一一个form类处理所有的表单中的FORM
from django import forms

class normalSearchForm(forms.Form):
    ssq_num = forms.CharField()
    batch = forms.CharField()
    start_num = forms.CharField()
    end_num= forms.CharField()
