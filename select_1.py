import pandas as pd

df = pd.read_csv('test1.csv')
df.set_index('UnitNumber',inplace=True)

print(data)
data = df[df["firmwareVersion"]=='30.08.08']
print(data.shape[0])


