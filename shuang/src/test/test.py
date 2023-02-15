# -*- coding: utf8 -*-


__author__ = 'zr'
import re
import urllib
import datetime

import os
import django
from django.db.models import Max
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
#
# print int(time.time())
# print datetime.datetime.today()
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
# formulas_list=[]
# formulas_list.append(ssq_formula.objects.filter(formula_id=2013001)[0])
# formulas_list.append(ssq_formula.objects.filter(formula_id=2013002)[0])

# print formulas_list
# q=TSsqShishibiao.objects.filter(num__gte=2017020).order_by('num')[0:3]
# print q
# print len(q)
# print q[1].num
# print q[1].get_next()
# q2=TSsqShishibiao.objects.filter(num__gte=q[1].num).order_by('num')[0:3]
# print len(q2)
# print q2[0].get_all_balls_byList()

def rr(r1,r2):
    return r1+r2
a=0
t1=4
t2=3




def blue_format(b):
    '''格式化蓝球，输入一个数字，按16取余数'''
    if  b>16:
        return b%16
    else:
        return b


def red_format(b):
    '''格式化蓝球，输入一个数字，按16取余数'''
    if  b>33:
        return b%33
    else:
        return b

print (red_format(34))

print (blue_format(27))

# ssl=TSsqShishibiao.objects.filter(num__gte=)
# ssq_ext = cal_shishibiao_ext(ssq_tmp2)
# ssq_ext.save()


def get_web_from_data500(num):
    '''
    已停用，考虑不周全，已改用get_web_datachart_ajax
    [[T返回期数,红球1,红球2,红球3,红球4,红球5,红球6,蓝球],]
    :param num:
    :return:[[T返回期数,红球1,红球2,红球3,红球4,红球5,红球6,蓝球],]
    '''
    #url3 = 'http://www.woying.com/kaijiang/ssqls/'+num+'.html'
    url3 = 'http://datachart.500.com/ssq/?expect='+num
    print (url3)

    #f = urllib.urlopen(url='file:/D:\\myapplesapple_id.txt')  打开本地文件
    #f = urllib.urlopen(url='ftp://python:read@www.*****.com/')  打开ftp
    #
    # r.add_data(data) 向请求添加数据。如果请求是HTTP请求，则方法改为‘POST’。data是向指定url提交的数据，要注意该方法不会将data追教导之前已经设置的任何数据上，而是使用现在的data替换之前的。
    # r.add_header(key, val) 向请求添加header信息，key是报头名，val是报头值，两个参数都是字符串。
    # r.addunredirectedheader(key, val) 作用基本同上，但不会添加到重定向请求中。
    # r.set_proxy(host, type) 准备请求到服务器。使用host替换原来的主机，使用type替换原来的请求类型。

    ###以上是使用urlopen直接打开的方法，下面说的是使用request对象的方法，主要目的是为了增加header，标准的urlopen也支持data和proxy，

    response = urllib.request.urlopen(url3)
    #print html1.read()
    # print html1.read().decode("gbk").encode("utf-8")

     # print response.info()  #返回映射对象，该对象带有与url关联的信息，对HTTP来说，返回的服务器响应包含HTTP包头。
            # 对于FTP来说，返回的报头包含'content-length'。对于本地文件，返回的报头包含‘content-length’和'content-type'字段。
            #要注意的是，类文件对象u以二进制模式操作。如果需要以文本形式处理响应数据，则需要使用codecs模块或类似方式解码数据。

    #print  response.getcode()
    if response.getcode() == 200:  #返回200，表示正常？  3打头的一般是重定向，301是永久重定向，302是临时重定向,404表示网页不存在，403禁止访问.500系列是响应过长
        print (response.info())

    else:
        print ('web is down！')
        return [],'web is down'
    cont=response.read()
    print (cont)
    ssq_list=re.subn(r'(\r+|\n+)+\s+','',cont) ##去除重复的内容
    # print ssq_list
    table1=re.findall(r'tbody.*?tbody',ssq_list[0]) ##找出主table
    ssq_list=re.findall(r'<td align="center">.*?</tr>',table1[0]) ##找出每一期的记录分段
    #print ssq_list
    ssq1 =[]

    for char in ssq_list:#制作成为list然后塞入一个list#
        test2 = re.findall(r'<td align="center">(.*?)</td>',char)#期数
        test3 =re.findall(r'<td class="chartBall01">(.*?)</td>',char)#红球
        test4 =re.findall(r'<td class="chartBall02">(.*?)</td>',char)#蓝球
        ssq=[test2[0].strip()]+test3+test4#期数里面不知道为啥就是有空格，去不掉，肯定是我对正则的理解不够
        ssq = map(int, ssq)  # 字符串转数字
        print (ssq)
        ssq1.append(ssq)

    #ssq1.reverse()
    #document.write(ssq_list)
    #document.closed
    return ssq1,response.getcode()

#print get_web_from_data500('100')

def get_web_datachart_last():
    '''
    从datachart.500.com网站获取最近一个最大的值
    :return:字符串的 list,比如 [2017117]
    '''
    url3 = 'http://datachart.500.com/ssq/zoushi/newinc/jbzs_redblue.php?expect=' + '30'
    response = urllib.request.urlopen(url3)
    if response.getcode() == 200:  #返回200，表示正常？  3打头的一般是重定向，301是永久重定向，302是临时重定向,404表示网页不存在，403禁止访问.500系列是响应过长
        print (response.info())

    else:
        print ('(web is down！')
        return ['web is down']
    cont=response.read()
    #print 'cont    '+cont
    ssq_list=re.subn(r'(\r+|\n+)+\s+','',cont) ##去除重复的内容
    # print ssq_list
    table1=re.findall(r'tbody.*?tbody',ssq_list[0]) ##找出主table
    ssq_list=re.findall(r'<td align="center">.*?</tr>',table1[0]) ##找出每一期的记录分段
    #print ssq_list
    test2 = re.findall(r'<td align="center">(.*?)</td>',ssq_list[-1])#期数

    ssq=['20'+test2[0].strip()]#期数里面不知道为啥就是有空格，去不掉，肯定是我对正则的理解不够
    ssq = map(int, ssq)  # 字符串转数字
   # print ssq
    return ssq

def get_web_datachart_ajax(num):
    '''
    考虑了最大期数等问题后，如果输入的批次过大，则从网页取最后一个作为 from to 的内容
    [[T返回期数,红球1,红球2,红球3,红球4,红球5,红球6,蓝球],]
    :param num:
    :return:[[T返回期数,红球1,红球2,红球3,红球4,红球5,红球6,蓝球],]
    '''
    #url3 = 'http://www.woying.com/kaijiang/ssqls/'+num+'.html'

    #first_ball = TSsqShishibiao.objects.last()
    #print 'first_ball.num',first_ball.num,'first_ball.get_all_balls_byList()',first_ball.get_all_balls_byList()
    #其实用这个 last 的方法也可以，他是根据主键后排序的来取值的。其实也很快。
    first_ball =int(TSsqShishibiao.objects.all().aggregate(Max('num')).get('num__max'))

    last_ball=get_web_datachart_last()
    if first_ball and last_ball:#正常情况下应该都是从第一个 url3开始
        print ('first_ball',first_ball)
        print ('last_ball',last_ball[0])
        if first_ball+int(num)>=int(last_ball[0]): #如果自己的最后一个加上批次大于了网页的最大值，则用from 我的第一个 to 网页的最后一个
            url3='http://datachart.500.com/ssq/zoushi/newinc/jbzs_redblue.php?expect=all&from=' + \
                 str(first_ball)[2:] + '&to=' + str(last_ball[0])[2:] + '&jumpsrc=http://datachart.500.com/ssq/'
        else:##如果最后一个加上批次小于网页的最大值,则使用 from 我的最后一个 to 我的最后一个加上+batch
            url3 = 'http://datachart.500.com/ssq/zoushi/newinc/jbzs_redblue.php?expect=all&from=' + \
            str(first_ball)[2:] + '&to=' + str(int(first_ball+ int(100)))[2:] + '&jumpsrc=http://datachart.500.com/ssq/'
    else: #任意一个为空，则默认拿100个
        url3 = 'http://datachart.500.com/ssq/zoushi/newinc/jbzs_redblue.php?expect=' + '100'
    print (url3)

    #f = urllib.urlopen(url='file:/D:\\myapplesapple_id.txt')  打开本地文件
    #f = urllib.urlopen(url='ftp://python:read@www.*****.com/')  打开ftp
    #
    # r.add_data(data) 向请求添加数据。如果请求是HTTP请求，则方法改为‘POST’。data是向指定url提交的数据，要注意该方法不会将data追教导之前已经设置的任何数据上，而是使用现在的data替换之前的。
    # r.add_header(key, val) 向请求添加header信息，key是报头名，val是报头值，两个参数都是字符串。
    # r.addunredirectedheader(key, val) 作用基本同上，但不会添加到重定向请求中。
    # r.set_proxy(host, type) 准备请求到服务器。使用host替换原来的主机，使用type替换原来的请求类型。

    ###以上是使用urlopen直接打开的方法，下面说的是使用request对象的方法，主要目的是为了增加header，标准的urlopen也支持data和proxy，
    header1 = {}
    header1['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"

    response = urllib.request.urlopen(url3)
    #print html1.read()
    # print html1.read().decode("gbk").encode("utf-8")

     # print response.info()  #返回映射对象，该对象带有与url关联的信息，对HTTP来说，返回的服务器响应包含HTTP包头。
            # 对于FTP来说，返回的报头包含'content-length'。对于本地文件，返回的报头包含‘content-length’和'content-type'字段。
            #要注意的是，类文件对象u以二进制模式操作。如果需要以文本形式处理响应数据，则需要使用codecs模块或类似方式解码数据。

    #print  response.getcode()
    if response.getcode() == 200:  #返回200，表示正常？  3打头的一般是重定向，301是永久重定向，302是临时重定向,404表示网页不存在，403禁止访问.500系列是响应过长
        print (response.info())
       # print req1.headers
    else:
        print ('web is down！')
        return [],'web is down'
    cont=response.read()
    #print cont
    ssq_list=re.subn(r'(\r+|\n+)+\s+','',cont) ##去除重复的内容
    # print ssq_list
    table1=re.findall(r'tbody.*?tbody',ssq_list[0]) ##找出主table
    ssq_list=re.findall(r'<td align="center">.*?</tr>',table1[0]) ##找出每一期的记录分段
    #print ssq_list
    ssq1 =[]
    # print ssq_list
    # for char in ssq_list:#制作成为list然后塞入一个list#
    #     test2 = re.findall(r'<td align="center">(.*?)</td>',char)#期数
    #     test3 =re.findall(r'<td class="chartBall01">(.*?)</td>',char)#红球
    #     test4 =re.findall(r'<td class="chartBall02">(.*?)</td>',char)#蓝球
    #     ssq=['20'+test2[0].strip()]+test3+test4#期数里面不知道为啥就是有空格，去不掉，肯定是我对正则的理解不够
    #     ssq = map(int, ssq)  # 字符串转数字
    #     print ssq
    #     ssq1.append(ssq)

    return ssq1,response.getcode()

#print get_web_datachart_ajax('100')
def test():
    last = TSsqShishibiao.objects.last()
    max =TSsqShishibiao.objects.all().aggregate(Max('num'))
    print ('num__max',max.get('num__max'))
    print (last.get_all_balls_byList())
    print (last.num)
    print ('http://datachart.500.com/ssq/zoushi/newinc/jbzs_redblue.php?expect=all&from=' + str(last.num)[2:] + '&to=' + str(last.num + int(100))[2:] + '&jumpsrc=http://datachart.500.com/ssq/')
    return ''

#test()
#get_web_datachart_ajax(100)

print (32%16)