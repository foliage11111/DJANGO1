#coding: utf8
import datetime
from django.db import models

__author__ = 'zr'


class FoliageSsq(models.Model):
    ####总表
    class Meta:
        verbose_name='基础组合'
        verbose_name_plural='基础组合们'
    num = models.IntegerField(primary_key=True,verbose_name='序号')
    r1 = models.IntegerField(blank=True, null=True,verbose_name='红1')
    r2 = models.IntegerField(blank=True, null=True,verbose_name='红2')
    r3 = models.IntegerField(blank=True, null=True,verbose_name='红3')
    r4 = models.IntegerField(blank=True, null=True,verbose_name='红4')
    r5 = models.IntegerField(blank=True, null=True,verbose_name='红5')
    r6 = models.IntegerField(blank=True, null=True,verbose_name='红6')
    b1 = models.IntegerField(blank=True, null=True,verbose_name='蓝球')
    sum1 = models.IntegerField(blank=True, null=True,verbose_name='红球和')
    sum2 = models.IntegerField(blank=True, null=True,verbose_name='总和')

    ###通过一个列表初始化数据
    def chushihua(self,num_list):
        if  num_list:
            self.r1=num_list[0]
            self.r2=num_list[1]
            self.r3=num_list[2]
            self.r4=num_list[3]
            self.r5=num_list[4]
            self.r6=num_list[5]
            self.b1=num_list[6]

    def get_all_balls_byList(self):
        '''
                所有红球加蓝球
                :return: [r1,r2,r3,r4,r5,r6]
                '''
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.b1]

    def get_red_balls_by_list(self):
        '''
                所有红球
                :return: [r1,r2,r3,r4,r5,r6]
                '''
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6]

    class Meta:
        managed = True
        db_table = 'foliage_ssq'


class FoliageSsq_ext(models.Model):
    ##总表的扩展表
    class Meta:
        verbose_name = '基础扩展'
        verbose_name_plural = '基础扩展们'
    id=models.AutoField(primary_key=True,db_tablespace='USERS')
    num=models.ForeignKey(FoliageSsq,null=True,on_delete=models.CASCADE)#外键，关联事实表的foliage_ssq的num
    horizontal_span1=models.IntegerField(blank=True, null=True)
    horizontal_span2=models.IntegerField(blank=True, null=True)
    horizontal_span3=models.IntegerField(blank=True, null=True)
    horizontal_span4=models.IntegerField(blank=True, null=True)
    horizontal_span5=models.IntegerField(blank=True, null=True)#红球之间的差
    # vertical_blue=models.IntegerField(blank=True, null=True)#蓝球的差
    # vertical_red1=models.IntegerField(blank=True, null=True)#纵向变化
    # vertical_red2=models.IntegerField(blank=True, null=True)#总表是不会有纵向变化的
    # vertical_red3=models.IntegerField(blank=True, null=True)
    # vertical_red4=models.IntegerField(blank=True, null=True)
    # vertical_red5=models.IntegerField(blank=True, null=True)
    # vertical_red6=models.IntegerField(blank=True, null=True)
    red_sum=models.IntegerField(blank=True, null=True)
    prime_reds=models.IntegerField(blank=True, null=True)#质数
    odd_reds=models.IntegerField(blank=True, null=True)#奇数
   # red_zhishu=models.IntegerField(blank=True, null=True)
    red_weihe=models.IntegerField(blank=True, null=True)#尾和
    red_lianhaoshu=models.IntegerField(blank=True, null=True)#连号个数
    red_shouweikuadu=models.IntegerField(blank=True, null=True)#首尾跨度
    attribute1=models.IntegerField(blank=True, null=True)
    attribute2=models.IntegerField(blank=True, null=True)
    attribute3=models.IntegerField(blank=True, null=True)
    attribute4=models.IntegerField(blank=True, null=True)
    attribute5=models.IntegerField(blank=True, null=True)


    def span_reds(self,slist):
        self.horizontal_span1=slist[0]
        self.horizontal_span2=slist[1]
        self.horizontal_span3=slist[2]
        self.horizontal_span4=slist[3]
        self.horizontal_span5=slist[4]

    def chushihua(self):
        #todo 需要增加一个通过 ssqlist 初始化各个值的方法
        return ''

    class Meta:
        managed = True
        db_table = 'foliagessq_ext'


class TSsqShishibiao(models.Model):

    num = models.IntegerField(primary_key=True,db_tablespace='USERS',verbose_name='期数')
    waijian = models.IntegerField(blank=True, null=True,verbose_name='总表') ##关联总表的num
    taoshu = models.IntegerField(blank=True, null=True,verbose_name='套数（停用）')
    r1 = models.IntegerField(blank=True, null=True,verbose_name='红1')
    r2 = models.IntegerField(blank=True, null=True,verbose_name='红2')
    r3 = models.IntegerField(blank=True, null=True,verbose_name='红3')
    r4 = models.IntegerField(blank=True, null=True,verbose_name='红4')
    r5 = models.IntegerField(blank=True, null=True,verbose_name='红5')
    r6 = models.IntegerField(blank=True, null=True,verbose_name='红6')
    b1 = models.IntegerField(blank=True, null=True,verbose_name='蓝球')
    sum1 = models.IntegerField(blank=True, null=True,verbose_name='红和')
    sum2 = models.IntegerField(blank=True, null=True,verbose_name='总和')
    time = models.DateField( blank=True, null=True,verbose_name='创建时间')

    def get_next(self):
        '''返回下一个ssq 查询集'''
        q=TSsqShishibiao.objects.filter(num__gte=self.num).order_by('num')[0:3]
        if len(q)>1:
            return q[1]
        else:
            return None

    def get_privous(self):
        '''返回上一个 ssq 查询集'''
        q = TSsqShishibiao.objects.filter(num__lte=self.num).order_by('num')[0:3]
        if len(q)>1:
            return q[1]
        else:
            return None

    def chushihua(self,num_list):
        '''
        初始化这个事实发生的期数，并关联总表
        :param num_list: 输入[num,r1,r2,r3,r4,r5,r6,b1]
        :return: 对象
        '''
        if  num_list:
            self.num=num_list[0]
            self.r1=num_list[1]
            self.r2=num_list[2]
            self.r3=num_list[3]
            self.r4=num_list[4]
            self.r5=num_list[5]
            self.r6=num_list[6]
            self.b1=num_list[7]
            self.sum1=self.r1+self.r2+self.r3+self.r4+self.r5+self.r6
            self.sum2=self.sum1+self.b1
            self.time=datetime.date.today()

            num_all=FoliageSsq.objects.filter(r1=self.r1,r2=self.r2,r3=self.r3,r4=self.r4,r5=self.r5,r6=self.r6,b1=self.b1)
            if  num_all:
                ssq_w=num_all.all()[0]
                self.waijian=ssq_w.num
             #   print 'waijian: ',self.waijian,' ssq: ',ssq_w.list_all_balls()
            else:
                self.waijian=1
          #  print self.num,self.list_all_balls()


    def get_all_balls_byList(self):
        '''
                所有红球加蓝球
                :return: [r1,r2,r3,r4,r5,r6]
                '''
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.b1]

    def get_list_red_balls_byList(self):
        '''
                所有红球
                :return: [r1,r2,r3,r4,r5,r6]
                '''
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6]

    class Meta:
        verbose_name = "历史数据"
        verbose_name_plural = "历史数据"
        managed = True
        db_table = 't_ssq_shishibiao'



class TSsqShishibiao_ext(models.Model):
    class Meta:
        verbose_name = '历史扩展'
        verbose_name_plural = '历史扩展'
    id=models.AutoField(primary_key=True,db_tablespace='USERS')
    num=models.ForeignKey(TSsqShishibiao,null=True,on_delete=models.CASCADE)#外键，关联事实表的t_ssq_shishibiao的num
    horizontal_span1=models.IntegerField(blank=True, null=True)
    horizontal_span2=models.IntegerField(blank=True, null=True)
    horizontal_span3=models.IntegerField(blank=True, null=True)
    horizontal_span4=models.IntegerField(blank=True, null=True)
    horizontal_span5=models.IntegerField(blank=True, null=True)#红球之间的差
    vertical_blue=models.IntegerField(blank=True, null=True)#蓝球的差
    vertical_red1=models.IntegerField(blank=True, null=True)#纵向变化
    vertical_red2=models.IntegerField(blank=True, null=True)
    vertical_red3=models.IntegerField(blank=True, null=True)
    vertical_red4=models.IntegerField(blank=True, null=True)
    vertical_red5=models.IntegerField(blank=True, null=True)
    vertical_red6=models.IntegerField(blank=True, null=True)
    red_sum=models.IntegerField(blank=True, null=True)
    prime_reds=models.IntegerField(blank=True, null=True)#质数
    odd_reds=models.IntegerField(blank=True, null=True)#奇数
   # red_zhishu=models.IntegerField(blank=True, null=True)
    red_weihe=models.IntegerField(blank=True, null=True)#尾和
    red_lianhaoshu=models.IntegerField(blank=True, null=True)#连号个数
    red_shouweikuadu=models.IntegerField(blank=True, null=True)#首尾跨度
    attribute1=models.IntegerField(blank=True, null=True)
    attribute2=models.IntegerField(blank=True, null=True)
    attribute3=models.IntegerField(blank=True, null=True)
    attribute4=models.IntegerField(blank=True, null=True)
    attribute5=models.IntegerField(blank=True, null=True)

    def vertical_reds(self,vlist):
        self.vertical_red1=vlist[0]
        self.vertical_red2=vlist[1]
        self.vertical_red3=vlist[2]
        self.vertical_red4=vlist[3]
        self.vertical_red5=vlist[4]
        self.vertical_red6=vlist[5]

    def span_reds(self,slist):
        self.horizontal_span1=slist[0]
        self.horizontal_span2=slist[1]
        self.horizontal_span3=slist[2]
        self.horizontal_span4=slist[3]
        self.horizontal_span5=slist[4]

    def get_all_balls_byList(self):
        '''
        红球加蓝球
        :return: [r1,r2,r3,r4,r5,r6,b1]
        '''
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.b1]

    def get_list_red_balls_byList(self):
        '''
        所有红球
        :return: [r1,r2,r3,r4,r5,r6]
        '''
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6]

    class Meta:
        managed = True
        db_table = 'tssqshishibiao_ext'