import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import IPython.ipapi



mainDataset = pd.read_csv(r'PATH\finalOutput.csv')
mainDataset.head()
mainDataset.describe
mainDataset.info()
mainDataset.head()

#%matplotlib inline
df_agg = mainDataset.groupby(['Hotel','flablel'])['nflabel'].sum().unstack()
df_agg.plot(kind='bar',stacked=True)

#%matplotlib inline
df_agg = mainDataset.groupby(['Hotel','nflabel'])['flablel'].sum().unstack()
df_agg.plot(kind='bar',stacked=True)
