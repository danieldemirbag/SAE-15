import pandas as pd
df = pd.read_csv("listerdctrier.csv", encoding='ISO-8859-1', sep=';')
x = pd.isnull(df).sum().sum()
print(x)