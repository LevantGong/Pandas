import pandas as pd
#整齐
pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('test1.csv')
#将UnitNumber设置为索引列
df.set_index('UnitNumber',inplace=True)

"""
#替换字符串
df.loc[:,"PID"] = df["PID"].str.replace("GW","").astype('object')
print(df)
print(df.dtypes)
 """

"""
#使用值列表进行查询(得到Series)
#df.loc[['F8S09A05','F8N97P27','F8N96X49'],'lastActivityTime']
print(df.loc[['F8S09A05','F8N97P27','F8N96X49'],'lastActivityTime'])
#使用值列表进行查询(得到DataFrame)
print(df.loc[['F8S09A05','F8N97P27','F8N96X49'],['lastActivityTime','firmwareVersion']])
"""
#使用数值区间进行范围查询
    #行index按区间
print(df.loc['F8S09A05':'F8N94Z10','lastActivityTime'])
    #列index按区间
print(df.loc['F8S09A05','appVersion_x':'commission_status_sum'])
    #行列都按区间查询
print(df.loc['F8S09A05':'F8N94Z10','appVersion_x':'commission_status_sum'])
