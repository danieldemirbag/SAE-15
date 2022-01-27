import pandas as pd
df = pd.read_csv("liste1ertrier.csv", encoding='ISO-8859-1', sep=';')
x = pd.isnull(df).sum().sum()
print(x)