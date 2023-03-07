import pandas as pd

fpath = "test1.csv"
ratings = pd.read_csv(fpath)

ratings.head()
ratings.info()
print(ratings.head())

