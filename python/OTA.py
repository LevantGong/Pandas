import pandas as pd
import time
def get_now_time():

    now = time.localtime()
    # now_time = time.strftime("%Y-%m-%d %H:%M:%S",now)
    now_time = time.strftime("23%m%d-%H",now)
    return now_time
if __name__ == '__main__':
    now_time = get_now_time()
    pd.set_option('display.unicode.east_asian_width',True)
    df1 = pd.read_excel("./xlsx/exer.xlsx")
    dfR = df1[df1['currentAppVersion'].str.contains("R",na=False)]
    dfS = df1[df1['currentAppVersion'].str.contains("S",na=False)]

    dataR = dfR['GatewayID']
    dataS = dfS['GatewayID']

    DR = pd.DataFrame(dataR)
    DS = pd.DataFrame(dataS)
    DFR = pd.DataFrame(DR.values.T,columns=DR.index,index=DR.columns)
    DFS = pd.DataFrame(DS.values.T,columns=DS.index,index=DS.columns)
    DFR_Count = DFR.shape[1]
    DFS_Count = DFS.shape[1]
    print(DFR.shape[1])
    print(DFS.shape[1])
    if DFR.empty == False:
        DFR.to_csv("./OTAGroup/"+now_time+"Gateway_R_"+"%d" %DFR_Count+"unit"+".csv",index=False,header=False)
    if DFS.empty == False:
        DFS.to_csv("./OTAGroup/"+now_time+"Gateway_S_"+"%d" % DFS_Count+"unit"+".csv",index=False,header=False)


