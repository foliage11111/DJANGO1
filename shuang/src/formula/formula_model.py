#coding: utf8
from django.db import models

__author__ = 'zr'


class ssq_formula(models.Model):
    '''
    双色球公式类
    '''
    formula_id = models.AutoField(primary_key=True,db_tablespace='USERS')
    """zhge kyi ?

    sd
    """
    formula_name = models.CharField(null=False,max_length=100)#公式自定义名称

    formula_express= models.CharField(null=False,max_length=100)#表达式
    formula_note= models.CharField(null=False,max_length=200)#公式备注
    create_date=models.DateField(null=True,)
    update_date=models.DateField(null=True,auto_now = True)
    formula_type=models.CharField(null=True,max_length=100)#针对蓝球还是红球的杀号还是选号
    batch = models.CharField(null=True, max_length=200)  # 公式备注
    status= models.CharField(null=True,max_length=100)# 是否有效
    attribute1= models.CharField(null=True,max_length=100)
    attribute2= models.CharField(null=True,max_length=100)
    attribute3= models.CharField(null=True,max_length=100)
    attribute4= models.CharField(null=True,max_length=100)
    attribute5= models.CharField(null=True,max_length=100)


    class Meta:
        managed = True
        db_table = 'ssq_formula'


class ssq_formula_fact(models.Model):
    """
    双色球公式结果，每一期的结果都要算
    """
    fact_id= models.AutoField(primary_key=True,db_tablespace='USERS')
    batch =models.CharField(null=True,max_length=100)#批次号
    now_periods= models.IntegerField(null=True) #基于计算的期数
    target_periods=models.IntegerField(null=True) #目标核对的期数
    result =models.CharField(null=False,max_length=100) #结果是否正确
    formula_value=models.CharField(null=False,max_length=100)#结果是什么
    formula_type=models.CharField(null=True,max_length=100)#针对蓝球还是红球的杀号还是选号
    create_date=models.DateField(null=True)#创建时间
    update_date = models.DateField(null=True, auto_now=True)
    '''如果公式对了，会涉及多少个可能的组合'''
    right_nums=models.IntegerField(null=True)
    target_ssq=models.CharField(null=True,max_length=100)#源的列表组合
    source_ssq=models.CharField(null=True,max_length=100)#目标的列组合
    attribute1 =models.CharField(null=True,max_length=100)
    attribute2 =models.CharField(null=True,max_length=100)
    attribute3 =models.CharField(null=True,max_length=100)
    attribute4 =models.CharField(null=True,max_length=100)
    attribute5 =models.CharField(null=True,max_length=100)

    class Meta:
        managed = True
        db_table = 'ssq_formula_fact'


class formula_fact_per(models.Model):
    """
    从每一期的角度来看公式的正确率
        1、如果总的正确率一直在下降，这种肯定是不怎么靠谱
        2、找近期正确率非常高的那种
        3、看看哪些公式的波动是否有规律

    """
    per_id =  models.AutoField(primary_key=True,db_tablespace='USERS')
    periods = models.IntegerField(null=False)
    fact_id = models.IntegerField(null=False)
    result = models.BooleanField(null=False)
    create_date=models.DateField(null=True)
    update_date = models.DateField(null=True, auto_now=True)
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