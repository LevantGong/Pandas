import csv

file = open('./csv/test6.csv')
fileReader = csv.reader(file)
data = list(fileReader)
print(data)