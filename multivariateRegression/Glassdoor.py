# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:24:02 2017

@author: bmowry
"""
import pandas as pd

labels = ['Company', 'Location', 'Salary', 'Review', 'Recency']
df = pd.read_csv('Glassdoor.csv', skiprows=1, names=labels)

e1 = "$(\d+)k-"
e2 = "-$(\d+)k"
for i in range(len(df.Salary)):
    df.Salary[i] = str(df.Salary[i])[12:]