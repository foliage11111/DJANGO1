#-*- coding:utf8 -*-
__author__ = 'zr'
#链接数据库测试用

import cx_Oracle
# conn = cx_Oracle.connect('foliage/foliage@192.168.1.106/orcl')
def get_conn():
    return  cx_Oracle.connect('foliage/foliage@localhost/orcl')

    #获取操作游标
# conn=get_conn()
# cursor=conn.cursor()
# cursor.prepare("select * from T_SSQ_SHISHIBIAO where num = :id and r1 =:r1")
# cursor.execute(None,{'id':2003001,'r1':''})
# ssq1=cursor.fetchall()
# print ssq1

def test1():
    conn = cx_Oracle.connect('foliage/foliage@localhost/orcl')
    #获取操作游标

    cursor = conn.cursor()


    ##第一种方法
    # pr={'id':3,'tel':13888888888}
    #
    # cursor.execute('select * from phone where id=:id or phone=:tel',pr)

    ##第二种方法

    cursor.execute("SELECT * FROM T_SSQ_SHISHIBIAO")

    ##第三种方法
    cursor.prepare("select * from tb_user where id <= :id")

    cursor.execute(None,{'id':5})
    #cursor.execute("""create table tb_user(id number, name varchar2(50),password varchar(50),primary key(id)) """)
    # for row in cursor:
    #          print row
    charn=cursor.fetchone()
    print charn
    #关闭连接，释放资源
    cursor.execute ("INSERT INTO TEST (ID, COL1, COL2, COL3)VALUES(3, 'aaa', 'bbb', 'ccc')")
    conn.commit()

    while (1):
        row = cursor.fetchone()
        if row == None:
            break
        print "%d, %s, %s, %s" % (row[0], row[1], row[2], row[3])


    cursor.close()
    conn.close();
    #执行完成，打印提示信息

    print 'Completed!'