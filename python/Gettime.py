import time
import pandas as pd
import os

def get_now_time():

    now = time.localtime()
    # now_time = time.strftime("%Y-%m-%d %H:%M:%S",now)
    now_time = time.strftime("23%m%d-%H",now)
    return now_time

if __name__ == '__main__':
    now_time = get_now_time()
    print(now_time)
    df1 = pd.read_excel("./xlsx/exer.xlsx")
    DR = pd.DataFrame(df1)
    DR.to_csv("./OTAGroup/"+now_time+"Gateway_R.csv",index=False,header=False)