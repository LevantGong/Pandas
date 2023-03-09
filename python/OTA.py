import pandas as pd
import numpy as np
pd.set_option('display.unicode.east_asian_width',True)
df1 = pd.read_excel("./xlsx/exer1.xlsx")
dfR = df1[df1['currentAppVersion'].str.contains("R",na=False)]
dfS = df1[df1['currentAppVersion'].str.contains("S",na=False)]

dataR = dfR['GatewayID']
dataS = dfS['GatewayID']

DR = pd.DataFrame(dataR)
DS = pd.DataFrame(dataS)
DFR = pd.DataFrame(DR.values.T,columns=DR.index,index=DR.columns)
DFS = pd.DataFrame(DS.values.T,columns=DS.index,index=DS.columns)
print(DFR)
print(DFS)
if DFR.empty == False:
    DFR.to_csv("./OTAGroup/Gateway_R.csv",index=False,header=False)
if DFS.empty == False:
    DFS.to_csv("./OTAGroup/Gateway_S.csv",index=False,header=False)


