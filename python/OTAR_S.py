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
    df1 = pd.read_excel("./xlsx/推送计划23-03-20.xlsx")
    # df2 = pd.read_excel("./xlsx/推送计划23-03-16.xlsx",sheet_name='OE')
    data1 =df1['GW Id']
    # data2 =df2['GW Id']
    DF1 = pd.DataFrame(data1)
    # DF2 = pd.DataFrame(data2)
    # print(DF)
    DF_OCL = DF1.drop_duplicates(subset='GW Id')  #删除重复值
    # DF_OE = DF2.drop_duplicates(subset='GW Id')
    # print(DF1)
    DF_OCL_D = pd.DataFrame(DF_OCL.values.T,columns=DF_OCL.index,index=DF_OCL.columns)
    # DF_OE_D = pd.DataFrame(DF_OE.values.T,columns=DF_OE.index,index=DF_OE.columns)
    DF_OCL_D_Count = DF_OCL_D.shape[1]
    # DF_OE_D_Count = DF_OE_D.shape[1]
    print(DF_OCL_D_Count)
    # print(DF_OE_D_Count)
    DF_OCL_D.to_csv("./OTAGroup/"+now_time+"Gateway_R_"+"%d" %DF_OCL_D_Count+"unit"+".csv",index=False,header=False)
    # DF_OE_D.to_csv("./OTAGroup/"+now_time+"Gateway_OE_"+"%d" %DF_OE_D_Count+"unit"+".csv",index=False,header=False)