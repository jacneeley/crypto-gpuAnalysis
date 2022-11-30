# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:28:47 2022

@author: Jacne
"""

import numpy as np
import pandas as pd
import csv 
import datetime

btc = pd.read_csv(r'C:/Users/Jacne/Documents/python/visualization_and_datamining/data/market-price.csv',sep=',')

date_time = []
for i in btc['x']:
    date_time.append(datetime.datetime.fromtimestamp(i/1000))   
date_time

btc['x'] = btc['x']/1000

btc.rename(columns = {'x':'Unix Epoch Time(Seconds)','y':'Price'},inplace = True)

btc.insert(
    loc = 0,
    column = 'DateTime',
    value = date_time)

btc.to_csv(r'btc_mktPrice.csv',index = None, header = True)