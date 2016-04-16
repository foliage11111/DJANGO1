#-*- coding:utf8 -*-
__author__ = 'zr'
#这是一个人自己写的封装sql的方式，好处还是有的，如果不是jango自带了数据库操作方法，models有orm的话，这种封装方式估计就是我简易操作数据库的方式了。
import cx_Oracle

# conn= getdata.SqlConn()
# key_list=['num','r1','r2','r3','r4','r5','r6','b1','sum1']
# sql=getdata.get_s_sql('T_SSQ_SHISHIBIAO',key_list,{'num':ssq_num})
# r=conn.execute(sql)  #结果[(2003001.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 16.0, 21.0)]
# data=getdata.fSqlResult(r,key_list)#字典，符合orm获取的值[{'r4': '4.0', 'r5': '5.0', 'r6': '6.0', 'r1': '1.0', 'r2': '2.0', 'r3': '3.0', 'sum1': '21.0', 'num': '2003001.0', 'b1': '16.0'}]
#
# conn.close()

class SqlConn():
    def __init__(self):
        self.conn= cx_Oracle.connect('foliage/foliage@localhost/orcl')#DBpool.pool.connection()
        self.cur=self.conn.cursor()
    def cur(self):
        return self.cur()
    def commit(self):
        self.conn.commit()
    def execute(self,sql,fetchone=0):
        self.cur.execute(sql)
        return self.cur.fetchone() if fetchone else self.cur.fetchall()
    # def last_id(self,table):
    #     sql='SELECT LAST_INSERT_ID() from %s'%table
    #     return self.execute(sql,1)[0]
    def close(self):
        self.cur.close()
        self.conn.close()

# def safe(s):
#     return cx_Oracle.escape_string(s)


def get_i_sql(table, dict):
    '''
    生成insert的sql语句
    @table，插入记录的表名
    @dict,插入的数据，字典
    '''
    sql = 'insert into %s set ' % table
    sql += dict_2_str(dict)
    return sql


def get_s_sql(table, keys, conditions, isdistinct=0):
    '''
        生成select的sql语句
    @table，查询记录的表名
    @key，需要查询的字段
    @conditions,插入的数据，字典
    @isdistinct,查询的数据是否不重复
    '''
    if isdistinct:
        sql = 'select distinct %s ' % ",".join(keys)
    else:
        sql = 'select  %s ' % ",".join(keys)
    sql += ' from %s ' % table
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql


def get_u_sql(table, value, conditions):
    '''
        生成update的sql语句
    @table，查询记录的表名
    @value，dict,需要更新的字段
    @conditions,插入的数据，字典
    '''
    sql = 'update %s set ' %table
    sql += dict_2_str(value)
    if conditions:
        sql += ' where %s ' %dict_2_str_and(conditions)
    return sql


def get_d_sql(table, conditions):
    '''
    生成detele的sql语句
    @table，查询记录的表名
    @conditions,插入的数据，字典
    '''
    sql = 'delete from  %s  ' %table
    if conditions:
        sql += ' where %s ' %dict_2_str_and(conditions)
    return sql


def dict_2_str(dictin):
    '''
    将字典变成，key='value',key='value' 的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), str(v))
        tmplist.append(' ' + tmp + ' ')
    return ','.join(tmplist)


def dict_2_str_and(dictin):
    '''
    将字典变成，key='value' and key='value'的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        #需要增加判断区分字符串，日期，数字
        tmp = "%s=%s" % (str(k), str(v))#数字
        #tmp = "%s='%s'" % (str(k), str(v)) #字符串
        tmplist.append(' ' + tmp + ' ')
    return ' and '.join(tmplist)

def fSqlResult(r,key_list):
 #r @tuple 数据库fetchall的结果
 # #key_list @list 查询字段的keys
 #  format SQL Result 格式化数据库查询的结果，转化成包含多个字典的列表格式，即((1,2),(3,4))->[{"key1":1,"key2":2},{"key1":3,"key2":4}]
 # #返回 @dict 查询结果
 mlist=[]
 l=len(key_list)
 if r:
     for item in r:
         tmp={}
         for i in range(l):
             tmp[key_list[i]]=str(item[i])
         mlist.append(tmp)
 return mlist