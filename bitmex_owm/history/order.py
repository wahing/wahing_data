'''
Created on Feb 8, 2020

@author: zero
'''

import pandas as pd
import time
import ccxt

bitmex = ccxt.bitmex()

#一次取500
limit = 500

#分钟级
# current_time = int(time.time() * 1000)
# since_time = current_time - limit * 60 * 1000

#天级
current_time = int(time.time() * 1000)
since_time = current_time - limit * 60 * 1000 * 60 * 24

data  = bitmex.fetch_ohlcv(symbol='BTC/USD', limit=limit , timeframe='1d',since=since_time)
df = pd.DataFrame(data)
df = df.rename(columns={0:'open_time',1:'open',2:'high',3:'low',4:'close',5:'volume'})
df['open_time'] = pd.to_datetime(df['open_time'],unit='ms') + pd.Timedelta(hours=8)
# print(df)
df = df.set_index('open_time',drop=True)
df.to_csv('bitmex_data.csv')
