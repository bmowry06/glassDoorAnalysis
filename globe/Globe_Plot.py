from datetime import datetime, timedelta
from urllib import urlretrieve
import sys
import os
from globeplot.plotting import GlobePlot
import numpy as np
import pandas as pd
import re
import codecs, json
import itertools

labels = ['Company', 'Location', 'Salary', 'Review', 'Recency']
df_glass = pd.read_csv('Glassdoor.csv', skiprows=1, names=labels)

df_globe1 = df_glass[['Location', 'Salary']]

df_globe1_drop = df_globe1.dropna(how='any')
df_globe1_drop.index = range(len(df_globe1_drop))

df_globe1_drop.Location = df_globe1_drop.Location[:][df_globe1_drop.Location[:] != 'United States']

df_globe1_drop = df_globe1_drop.dropna(how='any')
df_globe1_drop.index = range(len(df_globe1_drop))

df_globe1_drop_cities = []

for i in range(len(df_globe1_drop.Location[:])):
    df_globe1_drop_cities.append(df_globe1_drop.Location[:][i].rsplit(',', 1)[0])

df_globe1_drop_states = []

for i in range(len(df_globe1_drop.Location[:])):
    df_globe1_drop_states.append(df_globe1_drop.Location[:][i].rsplit(',', 1)[1])

df_globe1_drop_sals = []

for i in range(len(df_globe1_drop.Salary[:])):
   p = re.compile('\d+')
   salnums = p.findall(df_globe1_drop.Salary[:][i])
   salnumsmean = np.divide(int(salnums[0]) + int(salnums[1]), 2)
   df_globe1_drop_sals.append(salnumsmean)

df_globe_all = []

for i in range(len(df_globe1_drop_sals)):
    df_globe_all.append([df_globe1_drop_sals[i], df_globe1_drop_cities[i], df_globe1_drop_states[i]])

labels = ['zip_code', 'latitude', 'longitude', 'city', 'state', "county"]
df_geo = pd.read_csv('zip_codes_states.csv', skiprows=1, names=labels)

df_globe4 = df_geo[['latitude', 'longitude', 'city', 'state']]

df_globe_lat = df_geo[['latitude']]

df_globe_lon = df_geo[['longitude']]

# "94085",,,"Sunnyvale","CA","Santa Clara" for Sunnyvale, CA (result is nan value for lat/long): Throw out
# Crystal City, VA not in geo data file: Throw out

lats1 = []

for i in range(len([item[1] for item in df_globe_all])):
    if not any((df_globe4['city'] == [item[1] for item in df_globe_all][i].strip()) & (df_globe4['state'] == [item[2] for item in df_globe_all][i].strip())) == False:
        lats11 = df_globe_lat[(df_globe4['city'] == [item[1] for item in df_globe_all][i].strip()) & (df_globe4['state'] == [item[2] for item in df_globe_all][i].strip())].values[0][0]
        lats1.append(lats11)
    else:
        lats11 = 'NA'
        lats1.append(lats11)
lats12 = [x for x in lats1 if x != 'NA']
lats13 = [x for x in lats12 if str(x) != 'nan']
#print(len(lats1), len(lats12), len(lats13))
latsf = np.array(lats13)

lons1 = []

for i in range(len([item[1] for item in df_globe_all])):
    if not any((df_globe4['city'] == [item[1] for item in df_globe_all][i].strip()) & (df_globe4['state'] == [item[2] for item in df_globe_all][i].strip())) == False:
        lons11 = df_globe_lon[(df_globe4['city'] == [item[1] for item in df_globe_all][i].strip()) & (df_globe4['state'] == [item[2] for item in df_globe_all][i].strip())].values[0][0]
        lons1.append(lons11)
    else:
        lons11 = 'NA'
        lons1.append(lons11)
lons12 = [x for x in lons1 if x != 'NA']
lons13 = [x for x in lons12 if str(x) != 'nan']
#print(len(lons1), len(lons12), len(lons13))
lonsf = np.array(lons13)

sals1 = []

for i in range(len([item[1] for item in df_globe_all])):
    if not any((df_globe4['city'] == [item[1] for item in df_globe_all][i].strip()) & (df_globe4['state'] == [item[2] for item in df_globe_all][i].strip())) == False:
        sals11 = df_globe1_drop_sals[i]
        sals1.append(sals11)
    else:
        sals11 = 'NA'
        sals1.append(sals11)
sals12 = [x for x in sals1 if x != 'NA']

sals13 = []

for i in range(len(lons12)):
    if (str(lons12[i]) == 'nan') == False:
        sals113 = sals12[i]
        sals13.append(sals113)
    else:
        sals113 = 'NA'
        sals13.append(sals113)
sals14 = [x for x in sals13 if x != 'NA']
# sals15 =  [x / 100 for x in sals14]

salsf1 = np.array(sals14)

salsf = np.divide(salsf1, float(np.max(salsf1)))

lats = latsf
lons = lonsf
values = salsf

all_np = []

for i in range(len(latsf)):
    all_np.append([latsf[i], lonsf[i], salsf[i]])

all_npf = [list(itertools.chain.from_iterable(all_np))]
all_npf.insert(0, "2017")
all_npf2 = [all_npf]
print(all_npf2)

file_path = "path_to_directory/filename.json"
json.dump(all_npf2, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
