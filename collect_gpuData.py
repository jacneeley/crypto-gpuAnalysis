# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:44:50 2022

@author: Jacne
"""

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import csv 
import time

url = 'https://www.tomshardware.com/news/gpu-pricing-index'

#Parse data from html website
page = requests.get(url)
soup1 = bs(page.content,"html.parser")
soup1.title.text

#code to grab header data from tables
table = soup1.find('table',{'class':'table__wrapper table__wrapper--inbodyContent table__wrapper--sticky table__wrapper--divider'})
headers =[]
for i in table.find_all('th'):
    col = i.text.strip()
    headers.append(col)
headers

df = pd.DataFrame(columns = headers)


max_pages = 12
current_page = 1
    
while current_page <= max_pages:
    current_url= f'{url}/{current_page}'
    print(current_url)
    
    html = requests.get(current_url)
    soup = bs(html.content,'html.parser')
    
    for row in table.find_all('tr')[1:]: #exclude header
        data = row.find_all('td')
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
        
    time.sleep(5) #sleep for 5 seconds to prevent sending too many requests
    current_page+=1
    
#data, starting at index[0], is September 2022 <- October 2021

df.rename(columns = {'Sept eBay Price':'eBay Price'},inplace = True)
df=df.replace('N/A','nan')

#optionally, if we want to start from 1 year ago(october21), reverse the df
df = df.iloc[::-1]

export_csv = df.to_csv(r'averageMonthlyGPUPrice_ebay.csv',index = None, header = True)

    