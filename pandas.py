# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 09:27:48 2019

@author: balu
"""

# Pandas - Data creation
# PD SERIES
import pandas as pd
import numpy as np
data = list((10,20,30,40,50))
s = pd.Series(data)
print(s)
s = pd.Series(data,index=['A','B','C','D','E'])
print(s)
print(type(s))
print(s[1])
print(s[1:4])

print(s[-1])

# Panel - Now Deprecated, fot yOur understanding
# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data)
print(type(health_data))

print(health_data['Guido'])

print(health_data['Guido', 'HR'])


# CSV File - Read
df = pd.read_csv('C:\\Users\\admin\\Downloads\\cereals.csv')
#  ,header=None ,skiprows=1 , names=['Cal', 'Pr', 'Fat', 'sod', 'Fib', 'Rting']

print(df.head(5)) 

print(df.ndim)

print(df.shape)

print(df.axes)

print(df.dtypes)

print(df['protein'].head())

print(df.loc[5:10,'protein'].head()) # Better use .loc or .iloc


print(df.loc[:,['protein','calories']])

newdf = df.loc[:,['name','protein','calories']]
print(newdf.head())


print(df.iloc[:,[1,2,3]])

print(df.describe())

print(df.loc[:,['protein','calories','rating']].describe())


# ALternate - Assign
df3 = df.assign(newclmn= df["calories"]/df["protein"])
print(df3.head())
#concatenate between two cloumns
df["mfrname"] = df["mfr"].map(str) +"--"+ df["name"]

print(df.head())
# covariance
df4cov = df['sodium'].corr(df['rating'])
print(df4cov)

newdf=df.loc[:,['protein','calories','fat','sodium','fiber','carbo','sugars','potass','vitamins','rating']]
newdf.corr()




















