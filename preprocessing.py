# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 00:45:48 2020

@author: sabab
"""


import pandas as pd 
import seaborn as sns


df = pd.read_csv('test.csv')

print(df.columns)

print(df.dtypes)

df = df[['text']]

df.to_csv (r'data_test.csv', index = None, header=True)