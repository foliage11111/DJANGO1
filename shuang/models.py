#coding: utf8
from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here. 测试一下
class ssq_formula(models.Model):

    formula_id = models.IntegerField(primary_key=True,db_tablespace='USERS')
    formula_name = models.CharField(null=False,max_length=100)
    formula_express= models.CharField(null=False,max_length=100)
    formula_note= models.CharField(null=False,max_length=200)
    attribute1= models.CharField(null=True,max_length=100)
    attribute2= models.CharField(null=True,max_length=100)
    attribute3= models.CharField(null=True,max_length=100)
    attribute4= models.CharField(null=True,max_length=100)
    attribute5= models.CharField(null=True,max_length=100)

    class Meta:
        managed = True
        db_table = 'ssq_formula'

class ssq_formula_fact(models.Model):
    fact_id= models.IntegerField(primary_key=True,db_tablespace='USERS')
    periods= models.IntegerField(null=False)
    result =models.BooleanField(null=False)
    formula_value=models.CharField(null=False,max_length=100)
    attribute1 =models.CharField(null=True,max_length=100)
    attribute2 =models.CharField(null=True,max_length=100)
    attribute3 =models.CharField(null=True,max_length=100)
    attribute4 =models.CharField(null=True,max_length=100)
    attribute5 =models.CharField(null=True,max_length=100)

    class Meta:
        managed = True
        db_table = 'ssq_formula_fact'

class formula_fact_per(models.Model):
    per_id =  models.IntegerField(primary_key=True,db_tablespace='USERS')
    periods = models.IntegerField(null=False)
    fact_id = models.IntegerField(null=False)
    result = models.BooleanField(null=False)
    formula_id = models.IntegerField(null=False)
    formula_in5 = models.FloatField(null=False)
    formula_in10 = models.FloatField(null=False)
    formula_in30 = models.FloatField(null=False)
    formula_in50 = models.FloatField(null=False)
    formula_in100 = models.FloatField(null=False)
    formula_total = models.FloatField(null=False)

    class Meta:
        managed = True
        db_table = 'formula_fact_per'

class FoliageSsq(models.Model):
    ####总表
    num = models.IntegerField(primary_key=True)
    r1 = models.IntegerField(blank=True, null=True)
    r2 = models.IntegerField(blank=True, null=True)
    r3 = models.IntegerField(blank=True, null=True)
    r4 = models.IntegerField(blank=True, null=True)
    r5 = models.IntegerField(blank=True, null=True)
    r6 = models.IntegerField(blank=True, null=True)
    b1 = models.IntegerField(blank=True, null=True)
    sum1 = models.IntegerField(blank=True, null=True)
    sum2 = models.IntegerField(blank=True, null=True)

    def chushihua(self,num_list):
        if  num_list:
            self.r1=num_list[0]
            self.r2=num_list[1]
            self.r3=num_list[2]
            self.r4=num_list[3]
            self.r5=num_list[4]
            self.r6=num_list[5]
            self.b1=num_list[6]

    def list_all_balls(self):
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.b1]

    def list_red_balls(self):
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6]

    class Meta:
        managed = False
        db_table = 'foliage_ssq'

class FoliageSsq_ext(models.Model):
    ##总表的扩展表
    id=models.AutoField(primary_key=True,db_tablespace='USERS')
    num=models.IntegerField(blank=True, null=True)#外键，关联事实表的foliage_ssq的num
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

    class Meta:
        managed = True
        db_table = 'foliagessq_ext'


class TSsqShishibiao(models.Model):
    ##事实表的扩展表
    num = models.IntegerField(primary_key=True,db_tablespace='USERS')
    waijian = models.IntegerField(blank=True, null=True) ##关联总表的num
    taoshu = models.IntegerField(blank=True, null=True)
    r1 = models.IntegerField(blank=True, null=True)
    r2 = models.IntegerField(blank=True, null=True)
    r3 = models.IntegerField(blank=True, null=True)
    r4 = models.IntegerField(blank=True, null=True)
    r5 = models.IntegerField(blank=True, null=True)
    r6 = models.IntegerField(blank=True, null=True)
    b1 = models.IntegerField(blank=True, null=True)
    sum1 = models.IntegerField(blank=True, null=True)
    sum2 = models.IntegerField(blank=True, null=True)
    time = models.DateField( blank=True, null=True)

    def chushihua(self,num_list):
        print num_list
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
                self.waijian=num_all.all()[0].num

    def list_all_balls(self):
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6,self.b1]

    def list_red_balls(self):
        return [self.r1,self.r2,self.r3,self.r4,self.r5,self.r6]

    class Meta:
        managed = True
        db_table = 't_ssq_shishibiao'


class TSsqShishibiao_ext(models.Model):
    id=models.AutoField(primary_key=True,db_tablespace='USERS')
    num=models.IntegerField(blank=True, null=True)#外键，关联事实表的t_ssq_shishibiao的num
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

    class Meta:
        managed = True
        db_table = 'tssqshishibiao_ext'