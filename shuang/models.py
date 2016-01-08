#coding: utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here. 测试一下

class FoliageSsq(models.Model):
    num = models.FloatField(primary_key=True)
    r1 = models.FloatField(blank=True, null=True)
    r2 = models.FloatField(blank=True, null=True)
    r3 = models.FloatField(blank=True, null=True)
    r4 = models.FloatField(blank=True, null=True)
    r5 = models.FloatField(blank=True, null=True)
    r6 = models.FloatField(blank=True, null=True)
    b1 = models.FloatField(blank=True, null=True)
    sum1 = models.FloatField(blank=True, null=True)
    sum2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foliage_ssq'


class TSsqShishibiao(models.Model):
    num = models.FloatField(primary_key=True)
    waijian = models.FloatField(blank=True, null=True)
    taoshu = models.FloatField(blank=True, null=True)
    r1 = models.FloatField(blank=True, null=True)
    r2 = models.FloatField(blank=True, null=True)
    r3 = models.FloatField(blank=True, null=True)
    r4 = models.FloatField(blank=True, null=True)
    r5 = models.FloatField(blank=True, null=True)
    r6 = models.FloatField(blank=True, null=True)
    b1 = models.FloatField(blank=True, null=True)
    sum1 = models.FloatField(blank=True, null=True)
    sum2 = models.FloatField(blank=True, null=True)
    time = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ssq_shishibiao'
