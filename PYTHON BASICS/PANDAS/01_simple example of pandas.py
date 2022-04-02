# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:55:51 2022

@author: fitsum
"""

import pandas as pd
list_01 = ['seble','helen','fitsum','fasil','mehari']
print("Original data")
print(list_01)

series_01 = pd.Series(list_01)
print("Newly generated data:")
print(series_01)

dictionary_01 = {'name':'fitsum',
                 'age':24,
                 'gender':'male'}
print("Original data: ")
print(dictionary_01)

print("Newly generated data:")
series_02 = pd.Series(dictionary_01)
print(series_02)

print("\n\n\n\n")
print("selecting only name and gender")
# selecting specified data from the dictionary
# example: select the name and gender data from the dictionary
series_03 = pd.Series(dictionary_01, index = ["name", "gender"])
print(series_03)








print("\n\n\n\n")
print("Handling data frame in pandas")
data = {'name':['fitsum','misrak','solomon'],
        'age': [24,24,24],
        'gender':['male','female','male']}
dataframe_01 = pd.DataFrame(data, index = ["name","age"])
print(dataframe_01)

"""loc: used to locate one or more rows in the pandas dataframe"""
print("\n\n\n\n")
print(dataframe_01.iloc[0:,0:])