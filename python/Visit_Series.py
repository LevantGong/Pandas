import pandas as pd

s=pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#访问前三个元素
print(s[:3])
#访问后4个元素
print(s[-4:])
#根据索引号访问单个元素
print(s[['a']])
print(s['a']) #不带索引号版
#使用索引标签访问多个元素值
print(s[['a','b','c']])
