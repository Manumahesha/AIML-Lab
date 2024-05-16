import pandas as pd
df=pd.read_csv('EnjoySport.csv')
concepts=df.values[:,:-1]
target=df.values[:,-1]
df.head()
