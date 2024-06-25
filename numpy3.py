import pandas as pd
import numpy as np
import matplotlib as mp
ip=pd.read_csv("/content/mypython.csv")
print(ip.head())
print("\n",ip.info)

print(ip.columns,"\n")
print(ip.isnull().sum(),"\n")
print(ip.count())
