from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/MLC_data/data/dataset.txt', delimiter = ",")

df.head()

df2 = df.drop(df.columns[[0, 1, 2]], axis = 1)


df2.head()
# 	0.00031913807189542484	Airplane	612.0	512.0
# 0	0.000319	Airplane	612.0	512.0
# 1	0.000319	Airplane	612.0	512.0
# 2	0.000319	Airplane	612.0	512.0
# 3	0.000319	Airplane	612.0	512.0
# 4	0.000319	Airplane	612.0	512.0

df2.columns = ['ratio', 'object', 'width', 'height']


df2.head()
# ratio	object	width	height
# 0	0.000319	Airplane	612.0	512.0
# 1	0.000319	Airplane	612.0	512.0
# 2	0.000319	Airplane	612.0	512.0
# 3	0.000319	Airplane	612.0	512.0
# 4	0.000319	Airplane	612.0	512.0

df2.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2891886 entries, 0 to 2891885
# Data columns (total 4 columns):
#  #   Column  Dtype  
# ---  ------  -----  
#  0   ratio   float64
#  1   object  object 
#  2   width   float64
#  3   height  float64
# dtypes: float64(3), object(1)
# memory usage: 88.3+ MB

df2['ratio'].value_counts().sort_index()
# 0.000000         768
# 0.000319     1414714
# 0.000638         139
# 0.000957        1968
# 0.001277       16427
#               ...   
# 55.129187          1
# 55.164292          1
# 55.287480          1
# 55.707465          1
# 55.732996          1
Name: ratio, Length: 4575, dtype: int64

df2[df2['ratio'] > 0.5].value_counts().sum()
#9941
