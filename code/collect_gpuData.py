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
headpg = bs(page.content,"html.parser")
headpg.title.text

#code to grab header data from tables
headtable = headpg.find('table',{'class':'table__wrapper table__wrapper--inbodyContent table__wrapper--sticky table__wrapper--divider'})
headers =[]
for i in headtable.find_all('th'):
    col = i.text.strip()
    headers.append(col)
headers = headers[:3]

df = pd.DataFrame(columns = headers)


max_pages = 24
current_page = 1
    
while current_page <= max_pages:
    current_url= f'{url}/{current_page}'

    
    html = requests.get(current_url)
    soup = bs(html.text,'html.parser')
    table = soup.find('table',{'class':'table__wrapper table__wrapper--inbodyContent table__wrapper--sticky table__wrapper--divider'})
    tTitle=soup.find('caption',{'class':'table__caption table__caption--top table__caption--left'})
    #print(tTitle.text)
    print(current_url)
    
    for row in table.find_all('tr')[1:]:#exclude header
        data = row.find_all('td')[:3]
        row_data = [td.text.strip() for td in data]
        length = len(df)
        df.loc[length] = row_data
        
    #time.sleep(1) #sleep for 5 seconds to prevent sending too many requests
    current_page+=1


df.rename(columns = {'Oct eBay Price':'eBay Price'},inplace = True)
df=df.replace('N/A','nan')

#optionally, if we want to start from 1 year ago(october21), reverse the df
df = df.iloc[::-1]

export_csv = df.to_csv(r'averageMonthlyGPUPrice_ebay.csv',index = None, header = True)

    