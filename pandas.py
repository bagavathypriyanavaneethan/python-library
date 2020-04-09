# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:03:44 2020

@author: Bagavathi Priya
"""

import pandas as pd
a=pd.Series(list('abcdef'))
print(a) 

b=pd.Series([1,2,3,4,5],index=[11,12,34,55,77])
print(b)

c=pd.Series(range(5),index=list('abcde'))
print(c)
print(c['c'])

d={'a':100,'b':200}
a=pd.Series(d)
print(a)
b=pd.Series(d,list('abc'))
print(b)

a={'One': pd.Series([1,2,3,4],index=['a','b','c','d']),'Two':pd.Series([9,2,8,5],index=['a','b','c','d'])}
b=pd.DataFrame(a)
print(b)
print(a['One'])
b['new']=b['One']*2
print(b)


b=pd.Series(['green','red','yellow'],index=[0,2,1])
a=b.reindex(range(5),fill_value='black')
print(a)
a[4]='pink'
print(a)


a=pd.Series([1,2,3,4])
print(a.mean())
print(a.describe())


data={'india':50,'us':70}
d=pd.DataFrame(data)
print(d)

