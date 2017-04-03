# -*- coding: utf8 -*-


__author__ = 'zr'
import re
import datetime
import os
import django
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DJANGO1.settings")

django.setup()
from shuang.src.basic.basic_model import TSsqShishibiao
from shuang.src.formula.formula_model import ssq_formula

# a1=' class="blue">\xe6\x9f\xa5\xe7\x9c\x8b\xe8\xaf\xa6\xe6\x83\x85</a></td></tr><tr><td>2016034</td><td>2016-03-27 21:30(\xe6\x97\xa5)</td><td class="red">03&nbsp;15&nbsp;21&nbsp;22&nbsp;23&nbsp;28</td><td class="blue">15</td><td>112</td><td>4</td><td>4</td><td>2</td><td>2</td><td><a href="/kaijiang/ssq/2016034.html" target="_blank" class="blue">\xe6\x9f\xa5\xe7\x9c\x8b\xe8\xaf\xa6\xe6\x83\x85</a></td></tr><tr><td>2016033</td><td>2016-03-24 21:30(\xe5\x9b\x9b)</td><td class="red">06&nbsp;17&nbsp;18&nbsp;20&nbsp;27&nbsp;29</td><td class="blue">15</td><td>117</td><td>5</td><td>3</td><td>2</td><td>1</td><td><a href="/kaijiang/ssq/2016033.html" target="_blank" class="blue">\xe6\x9f\xa5\xe7\x9c\x8b\xe8\xaf\xa6\xe6\x83\x85</a>'
#
# ssq1=re.findall(r'<td>\d{7}.*?"blue">\d{2}</td>',a1)
# print ssq1
#
#
# print datetime.date.today()
# #    Article.objects.filter(Q(headline__startswith='Hello') | Q(headline__startswith='Goodbye'))   有待测试
#
# ssq1=map(int,['05', '14', '20', '26', '30', '33', '12'])
# print ssq1
# print ssq1.reverse()
# print ssq1
#
#
# def dict_2_str_mysql(dictin):
#     '''
#     将字典变成，key'value' and key'value'的形式
#     '''
#     tmplist = []
#     tmpsql=''
#     tmporder= ''
#     tmplimit= ''
#     print dictin.items()
#     for k, v in dictin.items():
#         if v:  #为空则跳过
#             tmp = "%s%s" % (str(k), str(v))#数字
#             if 'limit' in tmp:
#                 tmplimit=' '+tmp
#             elif 'order' in tmp:
#                 tmporder=' '+tmp
#             else:
#                 tmplist.append(' ' + tmp + ' ')
#                 tmpsql=' and '.join(tmplist)
#            # print ' and '.join(tmplist)
#     if tmplist or tmporder or tmplimit:
#         return tmpsql+ tmporder+tmplimit
#     else:
#         return ''
# s=dict_2_str_mysql({'limit 0,':10,'order by':' ts.num desc'})
# # print dict_2_str_mysql({'id=':1212,'name__contain=':'hongqiu','limit 0,':10,'order by':' ts.num desc'})
# print s
# print 'order' in 'order by'
# print s.startswith(' order')

# ssq_list = TSsqShishibiao.objects.all()
# print ssq_list
#
# for i in ssq_list:
#     print i

print int(time.time())
print datetime.datetime.today()
print datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
# formulas_list=[]
# formulas_list.append(ssq_formula.objects.filter(formula_id=2013001)[0])
# formulas_list.append(ssq_formula.objects.filter(formula_id=2013002)[0])

# print formulas_list
q=TSsqShishibiao.objects.filter(num__gte=2017020).order_by('num')[0:3]
print q
print len(q)
print q[1].num
print q[1].get_next()
q2=TSsqShishibiao.objects.filter(num__gte=q[1].num).order_by('num')[0:3]
print len(q2)
print q2[0].get_all_balls_byList()
