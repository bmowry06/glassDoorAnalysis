#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:38:38 2017

@author: bmowry
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#note: df is defined in Glassdoor.py, where the data is initialized.

# number of bins for hist = sqrt of number of data points
n_data = len(df.Salary)
n_bins = np.sqrt(n_data)
n_bins = int(n_bins)


plt.title('Distribution of Data Science Salaries')
plt.xlabel('Salary Range (thousands of dollars)')
plt.ylabel('Qty')
plt.hist(df.Salary, bins=n_bins, alpha = 0.75, histtype='bar', ec='black')
plt.show()

for i in ['South', 'West', 'Northeast', 'Midwest']:
    plt.title(i)
    plt.xlabel('Salary Range (thousands of dollars')
    plt.ylabel('Qty')
    plt.hist(df.Salary[df.Region==i], bins=int(np.sqrt(len(
        df.Salary[df.Region==i]))), alpha = 0.75, histtype='bar', ec='black')
    plt.show()

plt.title('Overall Salary boxplot')
plt.xlabel('Salary (thousands of dollars)')
sns.boxplot(df.Salary)
plt.show()

print(pd.to_numeric(df.Salary).describe())

sns.boxplot(x='Region', y='Salary', data=df)
plt.title('Boxplot by region')
plt.xlabel('Regions')
plt.ylabel('Salary (thousands of dollars)')
plt.show()

#sns.violinplot(x='Region', y='Salary', data=df, inner=None)
#plt.title('Swarmplot by region')
#plt.xlabel('Regions')
#plt.ylabel('Salary')
#plt.show()

