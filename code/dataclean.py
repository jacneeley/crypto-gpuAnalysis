# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:44:20 2022
@author: Jacne
"""

import numpy as np
import pandas as pd
from collections import OrderedDict
import csv
import datetime

btc = pd.read_csv(r'C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_mktPrice.csv',sep=',')
gpu = pd.read_csv(r'C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/averageMonthlyGPUPrice_ebay.csv',sep=',')

btc = btc.drop(btc[btc['Unix Epoch Time(Seconds)'] <= 1616198400].index)

#not very efficient, works for now. Needs to be dynamic in the future.
#switch statement would be great, but python 3.9 does not have that...
months = []
for i in btc['DateTime']:
    if i.startswith('10/'):
        i = 'October'
        months.append(i)
    if i.startswith('11/'):
        i='November'
        months.append(i)
    if i.startswith('12/'):
        i='December'
        months.append(i)
    if i.startswith('1/'):
        i='January'
        months.append(i)
    if i.startswith('2/'):
        i='Febuary'
        months.append(i)
    if i.startswith('3/'):
        i='March'
        months.append(i)
    if i.startswith('4/'):
        i='April'
        months.append(i)
    if i.startswith('5/'):
        i='May'
        months.append(i)
    if i.startswith('6/'):
        i='June'
        months.append(i)
    if i.startswith('7/'):
        i='July'
        months.append(i)
    if i.startswith('8/'):
        i='August'
        months.append(i)
    if i.startswith('9/'):
        i='September'
        months.append(i)        
btc['DateTime'] = months


#list of prices by month
bdf = pd.DataFrame(btc['Price'])
bdf = bdf.astype(float)

#grab a sample of prices
bsamp = bdf.sample(n=362)
bsamp = bsamp.reset_index(drop=True)

bsamples = pd.DataFrame(bsamp)
bsamples.rename(columns = {'Price':'btc_Prices'},inplace=True)


#conversions
prices = []
gpu['eBay Price'] = gpu['eBay Price'].astype(str)
for i in gpu['eBay Price']:
    prices.append(float(i.strip('$').replace(',','')))
gpu['eBay Price']= prices

gpus = []
for i in gpu['GPU']:
    gpus.append(i.strip('(opens in new tab) '))
gpu['GPU'] = gpus
gpu['QTY Sold'] = gpu['QTY Sold'].astype(float)

#values that need to be dropped
gpu = gpu.dropna()
#Drop Values that appear only once, b/c we can't predict them in our model.
gpu = gpu[gpu.groupby('GPU').GPU.transform(len) > 1]
gpu = gpu.reset_index(drop=True)


bsamples = bsamples.sort_values(by='btc_Prices',ascending = False)
bsamples = bsamples.reset_index(drop=True)

#mkt samples
btc_gpu_samples = pd.concat([gpu,bsamples],axis = 1,join='inner')
export_csv = btc_gpu_samples.to_csv(r'btc_gpu_mktSamples.csv',index = None, header = True)  