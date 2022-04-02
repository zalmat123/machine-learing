# Pandas full tutorials
"""
Created on Fri Mar 25 19:32:29 2022

@author: fitsum
"""

# Now the Pandas package can be referred to as pd instead of pandas.
import pandas as pd 
mydataframe = {
    'name':['fitsum','solomon','chernet'],
    'age':[24,24,24]}
print(mydataframe)

"""Changing the given data frame into the pandas dataframe."""

df = pd.DataFrame(mydataframe)
print(df)#the output is very interesting

print("\n\n\n\n")
"""Print only the first column"""
print("The first column will be displayed hereunder")
print(df.iloc[:,0])
print(pd.__version__)