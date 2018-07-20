#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 01:46:58 2018

@author: deepan
"""

import pandas as pd
import numpy as np
import scipy as sp
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


boston_df = pd.read_csv("Boston.csv")


boston_df.head()


#LSTAT - Percentage of population with low status
#MEDV - median Value of home

#ax = boston_df.plot(x = "lstat", y= "medv", style="o")
#ax.set_ylabel("medv")

x = boston_df[["lstat"]].values
y = boston_df[["medv"]].values

x1 = x[:,0]

x2 = x1.astype(np.int64)



plt.figure(1)
plt.scatter(x,y)
plt.grid('on')
plt.xlabel('Lower Status as Percentage of Population')
plt.ylabel('Median Value')


reg = LinearRegression()
reg.fit(x,y)
[intercept, coeff] = (reg.intercept_, reg.coef_)
plt.figure(2)
plt.scatter(x,y)
xs = range(np.min(x2), np.max(x2))
ys = [reg.predict([x]) for x in xs]
y1 = np.asarray(ys)
y2 = y1[:,0]
plt.plot(xs,y2, 'r', linewidth=2.5)
plt.grid('on')
plt.xlabel('Lower Status as Percentage of Population')
plt.ylabel('Median Value')