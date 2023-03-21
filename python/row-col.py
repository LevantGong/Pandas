import pandas as pd

df = pd.read_csv('./csv/Task_23-03-20.csv')

dfn =  pd.DataFrame(df)

dfns = pd.DataFrame(dfn.values.T,columns=dfn.index,index=dfn.columns)

dfns_Count = dfns.shape[0]

print(dfns)

dfns.to_csv("./OTAGroup/"+"Gateway_"+"%d" %dfns_Count+"unit"+".csv",index=True,header=False)