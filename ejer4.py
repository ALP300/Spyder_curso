import pandas as pd
import numpy as np
df= pd.read_csv('DatosYT.csv')
print(df.head())
print(df.dtypes)
print(df.sort_values(by=['ys'], ascending=[False]))
df1= pd.DataFrame(np.sort(df.values, axis=0))
print(df1)