import pandas as pd
import numpy as np

data={
    'state':['Ohio','fhaui','dauid','hcaushd','damidja'],
    'year':[2000,2001,2002,2003,2004],
    'pop':[1.3,3.3,3.2,1.6,1.4]
}

df = pd.DataFrame(data)
""" print(df)
print(df.index)

s= type(df[['year','pop']])
print(df[['year','pop']])

print(df.loc[0])

 """
print(df[['pop']])
df.to_csv("out1.csv",index=False)
