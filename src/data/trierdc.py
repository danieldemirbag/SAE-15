import pandas as pd
import csv
import numpy as np
ls=[]
with open('U:\Documents\wifi-uha\data\-raw\masterlistrdc.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter="'")
    for row in spamreader:
        df=('; '.join(row))
        ls.append(df)
np.savetxt('listerdctrier.csv',ls,delimiter=';',fmt ='% s')
