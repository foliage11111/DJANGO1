# -*- coding: utf8 -*-
__author__ = 'zr'
import re
import datetime

# a1=' class="blue">\xe6\x9f\xa5\xe7\x9c\x8b\xe8\xaf\xa6\xe6\x83\x85</a></td></tr><tr><td>2016034</td><td>2016-03-27 21:30(\xe6\x97\xa5)</td><td class="red">03&nbsp;15&nbsp;21&nbsp;22&nbsp;23&nbsp;28</td><td class="blue">15</td><td>112</td><td>4</td><td>4</td><td>2</td><td>2</td><td><a href="/kaijiang/ssq/2016034.html" target="_blank" class="blue">\xe6\x9f\xa5\xe7\x9c\x8b\xe8\xaf\xa6\xe6\x83\x85</a></td></tr><tr><td>2016033</td><td>2016-03-24 21:30(\xe5\x9b\x9b)</td><td class="red">06&nbsp;17&nbsp;18&nbsp;20&nbsp;27&nbsp;29</td><td class="blue">15</td><td>117</td><td>5</td><td>3</td><td>2</td><td>1</td><td><a href="/kaijiang/ssq/2016033.html" target="_blank" class="blue">\xe6\x9f\xa5\xe7\x9c\x8b\xe8\xaf\xa6\xe6\x83\x85</a>'
#
# ssq1=re.findall(r'<td>\d{7}.*?"blue">\d{2}</td>',a1)
# print ssq1


print datetime.date.today()
#    Article.objects.filter(Q(headline__startswith='Hello') | Q(headline__startswith='Goodbye'))   有待测试

ssq1=map(int,['05', '14', '20', '26', '30', '33', '12'])
print ssq1
print ssq1.reverse()
print ssq1

def dict_2_str_orm(dictin):
    '''
    将字典变成，key'value' , key'value'的形式
    '''
    tmplist = []
    for k, v in dictin.items():
        if v:  #为空则跳过
            tmp = "%s%s" % (str(k), str(v))#数字
            tmplist.append(' ' + tmp + ' ')
           # print ' and '.join(tmplist)
    if tmplist:
        return ' , '.join(tmplist)
    else:
        return ''

print dict_2_str_orm({'id=':1212,'name__contain=':'hongqiu'})