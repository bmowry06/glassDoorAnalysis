# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:24:02 2017

@author: bmowry
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import re

# import csv of glassdoor jobs data and label
labels = ['Company', 'Location', 'Salary', 'Review', 'Recency']
df = pd.read_csv('Glassdoor.csv', skiprows=1, names=labels)

# convert to string so that nan float values can be filtered out
df.Salary = df.Salary.astype(str)
# filter out nan float values
df = df[df.Salary != 'nan']
# reindex
df.index = range(len(df))

# extract average of 25th and 75th quartiles. we use this to represent the 
# salary
for i in range(len(df.Salary[:])):
    p = re.compile('\d+')
    sal = p.findall(str(df.Salary[i]))
    salMean = np.divide(int(sal[0]) + int(sal[1]), 2)
    df.iloc[(i, 2)] = salMean
#    df.Salary[i] = salMean
  
# number of bins for hist = sqrt of number of data points
n_data = len(df.Salary)
n_bins = np.sqrt(n_data)
n_bins = int(n_bins)


plt.title('Distribution of Data Science Salaries')
plt.xlabel('Salary Range')
plt.ylabel('Qty')
plt.hist(df.Salary, bins=n_bins, alpha = 0.75, histtype='bar', ec='black')

#sns.set()
#sns.swarmplot(x='Location', y='Salary', data=df)
#plt.xlabel('Location')
#plt.ylabel('Salary')
#plt.show()

