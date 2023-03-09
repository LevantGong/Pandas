#读取txt文件
import pandas as pd

fpath = './test3.txt'

pvuv = pd.read_csv(
    fpath,
    sep="\t",
    header=None,
    names=['pdate','pv','uv']
)
print(pvuv)