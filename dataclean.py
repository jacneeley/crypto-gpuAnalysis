# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:44:20 2022

@author: Jacne
"""

import numpy as np
import pandas as pd
import csv
import datetime

btc = pd.read_csv(r'C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/btc_mktPrice.csv',sep=',')
gpu = pd.read_csv(r'C:/Users/Jacne/Documents/python/visualization_and_datamining/data/dataminingProject/averageMonthlyGPUPrice_ebay.csv',sep=',')


#need prices from 10/1/2021 : 09/30/2022 only
btc = btc.drop(btc[btc['Unix Epoch Time(Seconds)'] < 1633132800].index)
btc = btc.drop(btc[btc['Unix Epoch Time(Seconds)'] > 1664582400].index)
btc = btc.reset_index(drop=True)

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

#inefficient, but works for now. This needs to be dynamic in the Future.
card1 = pd.DataFrame(gpu[gpu['GPU']=='Radeon RX 6600'])
card2 = pd.DataFrame(gpu[gpu['GPU']=='Radeon RX 6600 XT'])
card3 = pd.DataFrame(gpu[gpu['GPU']=='Radeon RX 6700 XT'])
card4 = pd.DataFrame(gpu[gpu['GPU']=='Radeon RX 6800'])
card5 = pd.DataFrame(gpu[gpu['GPU']=='Radeon RX 6800 XT'])
card6 = pd.DataFrame(gpu[gpu['GPU']=='Radeon RX 6900 XT'])
card7 = pd.DataFrame(gpu[gpu['GPU']=='GeForce RTX 3060 T'])
card8 = pd.DataFrame(gpu[gpu['GPU']=='GeForce RTX 3070'])
card9 = pd.DataFrame(gpu[gpu['GPU']=='GeForce RTX 3070 T'])
card10 = pd.DataFrame(gpu[gpu['GPU']=='GeForce RTX 3080'])
card11 = pd.DataFrame(gpu[gpu['GPU']=='GeForce RTX 3080 T'])
card12 = pd.DataFrame(gpu[gpu['GPU']=='GeForce RTX 3090'])
##################################################################################

clst = [card1,card2,card3,card4,card5,card6
        ,card7,card8,card9,card10,card11,card12]
sums = []
for c in clst:
    #c.drop(['QTY Sold'],axis=1, inplace = True)
    sums.append(round((c['eBay Price'].sum()*12)/(365),2))
    
headers = []
itr = 0
for g in gpu['GPU']:  
    headers.append(g)
    itr+=1
    if itr == 12:
        break
    
dailyAvgPrice = pd.DataFrame([sums]*365,columns = headers)
btc_gpu = pd.concat([btc,dailyAvgPrice],axis = 1, join='inner')
export_csv = btc_gpu.to_csv(r'btc_gpu_mktData.csv',index = None, header = True)  
    

