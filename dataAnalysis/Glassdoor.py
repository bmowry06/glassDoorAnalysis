# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:24:02 2017

@author: bmowry
"""

import numpy as np
import pandas as pd
import re

# import csv of glassdoor jobs data and label
labels = ['Company', 'Location', 'Salary', 'Review', 'Recency']
df = pd.read_csv('Glassdoor.csv', skiprows=1, names=labels)

# import csv of state region data and label
labels = ['West', 'Midwest', 'Northeast', 'South']
regions = pd.read_csv('Regions.csv', names=labels)

# convert to string so that nan float values can be filtered out
df.Salary = df.Salary.astype(str)
# filter out nan values
df = df[df.Salary != 'nan']
# reindex
df.index = range(len(df))
num_salaries = range(len(df.Salary[:]))


# extract average of 25th and 75th quartiles. use this to represent salary
for i in num_salaries:
    p = re.compile('\d+')
    sal = p.findall(str(df.Salary[i]))
    salMean = np.divide(int(sal[0]) + int(sal[1]), 2)
    df.iloc[(i, 2)] = salMean
#    df.Salary[i] = salMeann


# create new column for the region that the job belongs to
df['Region'] = 0    

for i in num_salaries:
    state = df.iloc[(i,1)][-2:]
    if (state in regions.West.values):
        df.iloc[(i,5)] = 'West'
    elif (state in regions.Midwest.values):
        df.iloc[(i,5)] = 'Midwest'
    elif (state in regions.Northeast.values):
        df.iloc[(i,5)] = 'Northeast'
    elif (state in regions.South.values):
        df.iloc[(i,5)] = 'South'
        
df = df[df.Region != 0]
df.index = range(len(df))