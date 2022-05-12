#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 18:02:26 2022

@author: stephaniehull
"""

import geopandas as gpd
import pandas as pd
import numpy as np 
import requests


censustract= gpd.read_file('Census Tracts 2020', dtype={'geoid20':str})
demographic = pd.read_csv('Census Demographic Data.csv', dtype={'GEO.id2.Id2':str})

censustract = censustract.merge(demographic, left_on='geoid20', right_on ='GEO.id2.Id2',
                          how='outer', validate='1:1',indicator=True)

print(censustract['_merge'].value_counts())
censustract = censustract.drop(columns='_merge')
#%%
variables = {'B02003_003E':'HC01_VC54.Estimate..RACE...One.race...White',
            'B02003_004E':'HC01_VC55.Estimate..RACE...One.race...Black.or.African.American'
            }
var_list = variables.keys()
var_string = ','.join(var_list)


api = "http://api.census.gov/data/2019/acs/acs1"

for_clause = 'county:*'
in_clause = 'state:36'

payload = {"get":var_string,'for':for_clause,'in':in_clause}



#%%
response = requests.get(api, payload)
print(response)

 
row_list = response.json()
colnames = row_list[0]
datarows = row_list[1:]

race = pd.DataFrame(columns=colnames, data=datarows)
race = race.replace('-666666666', np.nan)
race = race.rename(columns=variables)

race = race.rename(columns={ 'county': 'geoid20'})
race = race.astype(str)
race.to_csv('Race_by_County.csv')

#%%Merging rental registry onto Specific Neighborhoods through a query. I will then merge it with
#the race variable so that I can get demographic data to analyze in my other .py file. 


rentreg = pd.read_csv('Rental_Registry.csv', dtype=str)
rentreg = rentreg.query("Neighborhood == 'Fruit Belt' or Neighborhood == 'Pratt-Willert'")
print(rentreg)
merged = censustract.merge(race, on='geoid20', how='outer', indicator=True)
print(merged['_merge'].value_counts())
merged = merged.drop(columns='_merge')

            
