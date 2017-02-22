#-*- coding:utf8 -*-
__author__ = 'zr'
'''
界面的一些常用查询全在这里
'''

from dataBase.gedata import SqlConn
from dataBase.gedata import dict_2_str_mysql

def get_all_rows_cond(conditions):
   '''
   带条件的查询，返回事实表和扩展的的联合查询结果
   :param : conditions={'ts.num=':'总期数','ts.num>':'从哪个起','ts.num<':'到哪个为止',order by ,'limit<=':'总数'}
   :return: 返回cur运行结果
   '''

   sql='''select ts.num,
       ts.r1,
       ts.r2,
       ts.r3,
       ts.r4,
       ts.r5,
       ts.r6,
       ts.b1,
       ts.sum1,
       te.red_lianhaoshu,
       te.red_shouweikuadu,
       te.prime_reds,
       te.odd_reds,
       te.red_weihe,
       te.vertical_blue,
       te.horizontal_span1,
       te.horizontal_span2,
       te.horizontal_span3,
       te.horizontal_span4,
       te.horizontal_span5,
       te.vertical_red1,
       te.vertical_red2,
       te.vertical_red3,
       te.vertical_red4,
       te.vertical_red5,
       te.vertical_red6
  from tssqshishibiao_ext te, t_ssq_shishibiao ts
 where ts.num = te.id '''

   if conditions:
      s=dict_2_str_mysql(conditions)
      if s :
        if s.startswith(' order') or s.startswith(' limit'):
            sql=sql+s
        else:
            sql =sql+ ' and '+s
      else:
        sql+='  order by ts.num desc  limit 0,50'

   else:
      sql+=' order by ts.num desc limit 0,50 '
   print sql
   cur=SqlConn()
   ssq1=cur.execute(sql)
   cur.close()
   return ssq1


def get_all_rows():
    '''
    查询100条事实表和扩展表联合查询的结果
    :return:
    '''
    sql_context='''select ts.num,
       ts.r1,
       ts.r2,
       ts.r3,
       ts.r4,
       ts.r5,
       ts.r6,
       ts.b1,
       ts.sum1,
       te.red_lianhaoshu,
       te.red_shouweikuadu,
       te.prime_reds,
       te.odd_reds,
       te.red_weihe,
       te.vertical_blue,
       te.horizontal_span1,
       te.horizontal_span2,
       te.horizontal_span3,
       te.horizontal_span4,
       te.horizontal_span5,
       te.vertical_red1,
       te.vertical_red2,
       te.vertical_red3,
       te.vertical_red4,
       te.vertical_red5,
       te.vertical_red6
  from tssqshishibiao_ext te, t_ssq_shishibiao ts
 where ts.num = te.id  '''

    vorder=' order by ts.num desc'
    limits=' limit 0,100 '

    print sql_context+vorder+limits
    cur=SqlConn()
    ssq1=cur.execute(sql_context+vorder+limits)
    cur.close()
    return ssq1
