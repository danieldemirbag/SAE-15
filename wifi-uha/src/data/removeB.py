import pandas as pds
df = pds.read_csv("liste1ertrier.csv", encoding='ISO-8859-1', sep=';')
for i in range(len(df)):
df1 = df.iloc[:,0] # accès de la première colonne
df.iloc[0,:] # accès au premier enregistrement*
