# -*- coding: utf8 -*-
__author__ = 'zr'

import urllib
import re
from shuang.src.basic.basic_model import TSsqShishibiao
from django.db.models import Max
import json
import time
# from urllib import urlopen
# from urllib2 import request_host

def get_web(num):
    '''
    最开始的从woying.com获取数据
    [[T返回期数,红球,蓝球],]
    :param num:
    :return:T返回期数,红球,蓝球
    '''
    url3 = 'http://www.woying.com/kaijiang/ssqls/'+num+'.html'

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

    req1 = urllib.Request(url3)   ##req1 = urllib2.Request(urll,'',header1)
    req1.add_header('User-Agent',header1['User-Agent']) ##需要区别上面加header的方法，这里需要指定header里面某个关键字，然后增加字符串内容
    # req1.set_proxy('27.38.152.195:9797','http') #设置代理
    response=urllib.urlopen(req1)
    #print html1.read()
    # print html1.read().decode("gbk").encode("utf-8")

     # print response.info()  #返回映射对象，该对象带有与url关联的信息，对HTTP来说，返回的服务器响应包含HTTP包头。
            # 对于FTP来说，返回的报头包含'content-length'。对于本地文件，返回的报头包含‘content-length’和'content-type'字段。
            #要注意的是，类文件对象u以二进制模式操作。如果需要以文本形式处理响应数据，则需要使用codecs模块或类似方式解码数据。

    #print  response.getcode()
    if response.getcode() == 200:  #返回200，表示正常？  3打头的一般是重定向，301是永久重定向，302是临时重定向,404表示网页不存在，403禁止访问.500系列是响应过长
        print (response.info())
        print (req1.headers)
    else:
        print ('web is down！')
        return [],'web is down'
    cont=response.read()
    # print cont
    # ssq_list=re.subn(r'(\r\n)+|\s+','',cont)
    ssq_list=re.subn(r'(\r+|\n+)+\s+','',cont) ##去除重复的内容
    # print ssq_list
    table1=re.findall(r'tbody.*?tbody',ssq_list[0]) ##找出主table
    ssq_list=re.findall(r'<td>\d{7}.*?"blue">\d{2}</td>',table1[0]) ##找出每一期的记录分段
    ssq1 =[]
    for char in ssq_list:#制作成为list然后塞入一个list#
       test1=char[4:11]+','+char[char.find('\"red\">')+6:char.find('</td><td class=\"blue\">')].replace('&nbsp;',',')+','+char[char.find('\"blue\">')+7:len(char)-5]
       ssq1.append(map(int,(test1.split(','))))
    ssq1.reverse()
    return ssq1,response.getcode()

     #   time.sleep(5)#休息时间
    #print response.read()
    #urllib.urlretrieve(url3,"c:\\Users\\zr\\Desktop\\ssq_test1.txt")  ###上面抓取网页，抓取以后要下载网页



def get_web_datachart_last():
    '''
    从datachart.500.com网站获取最近一个最大的值
    :return:字符串的 list,比如 [2017117]
    '''
    url3 = 'http://datachart.500.com/ssq/zoushi/newinc/jbzs_redblue.php?expect=' + '30'
    header1 = {}
    header1[
        'User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"

    req1 = urllib.Request(url3)  ##req1 = urllib2.Request(urll,'',header1)
    req1.add_header('User-Agent', header1['User-Agent'])  ##需要区别上面加header的方法，这里需要指定header里面某个关键字，然后增加字符串内容
    # req1.set_proxy('27.38.152.195:9797','http') #设置代理
    response = urllib.urlopen(req1)
    print ("get response")
    if response.getcode() == 200:  #返回200，表示正常？  3打头的一般是重定向，301是永久重定向，302是临时重定向,404表示网页不存在，403禁止访问.500系列是响应过长
        print (response.info())
        print (req1.headers)
    else:
        print ('web is down！')
        return ['web is down']
    print ("relaseing response")
    cont=response.read()
    #print 'cont    '+cont
    ssq_main=re.subn(r'(\r+|\n+)+\s+','',cont) ##去除重复的内容
    print ("reticting trash")
    table1=re.findall(r'tbody.*?tbody',ssq_main[0]) ##找出主table
    print ("get main table")
    print (table1)
    ssq_list=re.findall(r'<td align="center">.*?</tr>',table1[0]) ##找出每一期的记录分段
    print (ssq_list)
    ssq_num = re.findall(r'<td align="center">(.*?)</td>',ssq_list[-1])#期数

    ssq=['20'+ssq_num[0].strip()]#期数里面不知道为啥就是有空格，去不掉，肯定是我对正则的理解不够
    ssq = map(int, ssq)  # 字符串转数字
    print (ssq)
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

    last_ball=[2018052]
    #get_web_datachart_last()
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

    req1 = urllib.Request(url3)   ##req1 = urllib2.Request(urll,'',header1)
    req1.add_header('User-Agent',header1['User-Agent']) ##需要区别上面加header的方法，这里需要指定header里面某个关键字，然后增加字符串内容
    # req1.set_proxy('27.38.152.195:9797','http') #设置代理
    response=urllib.urlopen(req1)
    #print html1.read()
    # print html1.read().decode("gbk").encode("utf-8")

     # print response.info()  #返回映射对象，该对象带有与url关联的信息，对HTTP来说，返回的服务器响应包含HTTP包头。
            # 对于FTP来说，返回的报头包含'content-length'。对于本地文件，返回的报头包含‘content-length’和'content-type'字段。
            #要注意的是，类文件对象u以二进制模式操作。如果需要以文本形式处理响应数据，则需要使用codecs模块或类似方式解码数据。

    #print  response.getcode()
    print ("reponse geted")
    if response.getcode() == 200:  #返回200，表示正常？  3打头的一般是重定向，301是永久重定向，302是临时重定向,404表示网页不存在，403禁止访问.500系列是响应过长
        print (response.info())
       # print req1.headers
    else:
        print ('web is down！')
        return [],'web is down'
    cont=response.read()
    print ("relase main reponse :")
    print (cont)
    ssq_list=re.subn(r'(\r+|\n+)+\s+','',cont) ##去除重复的内容
    # print ssq_list
    table1=re.findall(r'tbody.*?tbody',ssq_list[0]) ##找出主table
    ssq_list=re.findall(r'<td align="center">.*?</tr>',table1[0]) ##找出每一期的记录分段
    #print ssq_list
    ssq1 =[]
    # print ssq_list
    for char in ssq_list:#制作成为list然后塞入一个list#
        test2 = re.findall(r'<td align="center">(.*?)</td>',char)#期数
        test3 =re.findall(r'<td class="chartBall01">(.*?)</td>',char)#红球
        test4 =re.findall(r'<td class="chartBall02">(.*?)</td>',char)#蓝球
        ssq=['20'+test2[0].strip()]+test3+test4#期数里面不知道为啥就是有空格，去不掉，肯定是我对正则的理解不够
        ssq = map(int, ssq)  # 字符串转数字
        print (ssq)
        ssq1.append(ssq)

    return ssq1,response.getcode()