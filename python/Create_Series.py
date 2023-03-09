import pandas as pd
import numpy as np
s=pd.Series([4,5,6],range(1,4),dtype=np.int32,name='aa')

print(s)

b=pd.Series([1,'x',3.4,np.nan,[1,2]],range(1,6))
print(b)

print('所有元素值：',b.values)
print('所有索引号：',b.keys())
print('所有索引明细：',*b.index)
print('所有键值对明细：',*b.items())

pd.set_option('display.unicode.east_asian_width',True)
d=pd.Series({'考号':'2019070230402','姓名':'龚玉尚','数学':'97'})
print(d)
print(d.values)
print(*d.index)

dates=pd.date_range('20230305','20230308')
print(dates)

c=pd.Series([6,7,8,9],index=dates)
print(c)
print(*c.keys())