import pandas as pd
import numpy as np
pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_excel("./xlsx/exer.xlsx")
data = df['GatewayID']
dd = pd.DataFrame(data)

testdf = pd.DataFrame(dd.values.T,columns=dd.index,index=dd.columns)
testdf.to_csv("./csv/test6.csv",index=False,header=False)
print(testdf)