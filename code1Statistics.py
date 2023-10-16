import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

import statistics
# mean,median,mode
df = sns.load_dataset('tips')
df.head()

np.mean(df['total_bill'])
np.median(df['total_bill'])

statistics.mode(df['total_bill'])
sns.boxplot(['total_bill'])

sns.histplot(df['total_bill'])

# with probability density function
sns.histplot(df['total_bill'],kde=True)

# loading different dataset
df1 = sns.load_dataset('iris')
df1.head()

sns.histplot(df1['sepal_length'],kde=True)
sns.histplot(df1['sepal_width'],kde=True)

# getting barplot
sns.countplot(df1['species'])

#Using Percentile
np.percentile(df1['sepal_length'],[25,75])
