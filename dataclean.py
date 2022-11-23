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


#need prices from 10/1/2021 : 09/30/2022 only
btc = btc.drop(btc[btc['Unix Epoch Time(Seconds)'] < 1633132800].index)
btc = btc.drop(btc[btc['Unix Epoch Time(Seconds)'] > 1664582400].index)
btc = btc.reset_index(drop=True)


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


#collect monthly average from btc
#list of prices by month
blst = []
for i in btc['DateTime'].unique():
    blst.append(pd.DataFrame(btc[btc['DateTime']== i]))
    
#avg bitcoin price per month & epoch time
btcp = []
btct = []
for i in blst:
    btcp.append(round(i['Price'].mean(),2))
    btct.append(round(i['Unix Epoch Time(Seconds)'].mean(),2))
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

#drop cards that have a frequency less than 12
gpu = gpu[gpu.groupby('GPU').GPU.transform('count')>11]#transform function is goofy, i goes by index.


#create a dataframe for each card
clst=[]
for i in gpu['GPU'].unique():
    clst.append(pd.DataFrame(gpu[gpu['GPU']==i]))

#build some arrays
p = []
for i in clst:
    i.drop(['QTY Sold'],axis=1,inplace=True)
    for c in i['eBay Price']:
        p.append(c)  
priceAr = np.array(p).reshape(12,12)
priceAr = priceAr.T

monthly_btc = np.array(btcp).reshape(12,1)
epoch_month = np.array(btct).reshape(12,1)
##################################################################################
#building new dataframes from old ones

headers = []    
for g in gpu['GPU'].unique():  
    headers.append(g)
gpudf = pd.DataFrame(priceAr)
gpudf.columns = headers
gpudf = gpudf.astype(float)

btcar = np.concatenate((epoch_month,monthly_btc),axis =1)
btcdf = pd.DataFrame(btcar)
months = list(OrderedDict.fromkeys(months)) #remove duplicates from months list
btcdf.insert(0,'month',months )
btcdf.rename(columns = {0:'Unix Epoch Time',1:'btc_Price'},inplace=True)


# using dictionary to convert specific columns
convert_dict = {'Unix Epoch Time': int,'btc_Price': float}
btcdf = btcdf.astype(convert_dict)

btc_gpu = pd.concat([btcdf,gpudf],axis = 1, join='inner')
export_csv = btc_gpu.to_csv(r'btc_gpu_mktData.csv',index = None, header = True)  
    

