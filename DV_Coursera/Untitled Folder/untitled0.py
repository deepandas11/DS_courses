#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 23:43:04 2018

@author: deepan
"""


import numpy as np                               # vectors and matrices
import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots
import seaborn as sns                            # more plots

from dateutil.relativedelta import relativedelta # working with dates with style
from scipy.optimize import minimize              # for function minimization

import statsmodels.formula.api as smf            # statistics and econometrics
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs

from itertools import product                    # some useful functions
from tqdm import tqdm_notebook

import warnings                                  # `do not disturbe` mode
warnings.filterwarnings('ignore')

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_error



temp = pd.read_csv('data-annual.csv', index_col=['Year'], parse_dates=['Year'])

y_global = temp.Glob
y_north = temp.NHem
y_south = temp.SHem

y_globdiff = y_global - y_global.shift()
y_globdiff.dropna(inplace=True)

y_northdiff = y_north - y_north.shift()
y_northdiff.dropna(inplace=True)

y_southdiff = y_south - y_south.shift()
y_southdiff.dropna(inplace=True)

plt.figure(figsize=(20,10))
plt.subplot(211)
plt.plot(y_global, 'r', label = 'Global Data')
plt.plot(y_north, 'y', label = 'NH Data')
plt.plot(y_south, 'b', label = 'SH Data' )
plt.legend(loc = 'best')
plt.title('Temperature Variation through the years')
plt.ylabel('Temp. (F)')
plt.xlabel('Year ')
plt.grid('on')

plt.subplot(212)
plt.plot(y_globdiff, 'r', label = 'Global Data')
plt.plot(y_northdiff, 'y', label = 'NH Data')
plt.plot(y_southdiff, 'b', label = 'SH Data' )
plt.legend(loc = 'best')
plt.title('Yearly change in Temperature')
plt.ylabel('Temp. Diff. (F)')
plt.xlabel('Year ')
plt.grid('on')
plt.subplots_adjust(hspace = 0.4)

plt.show()
