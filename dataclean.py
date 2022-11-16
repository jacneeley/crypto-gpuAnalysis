# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:44:20 2022

@author: Jacne
"""

import numpy as np
import pandas as pd
import csv
import datetime

btc = pd.read_csv(r'C:/Users/Jacne/Documents/python/visualization_and_datamining/data/btc_mktPrice.csv',sep=',')
gpu = pd.read_csv(r'C:/Users/Jacne/Documents/python/visualization_and_datamining/data/averageMonthlyGPUPrice_ebay.csv',sep=',')


#need prices from 10/1/2021 : 09/30/2022 only
btc = btc.drop(btc[btc['Unix Epoch Time(Seconds)'] < 1633132800].index)
btc = btc.drop(btc[btc['Unix Epoch Time(Seconds)'] > 1664582400].index)

