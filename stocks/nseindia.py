import requests
import pandas as pd
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',5000)

class NSE:
  pre_market_categories = ['NIFTY 50','Nifty Bank','Emerge','Securities in F&O','Others','All']
  equity_market_categories =
  holidays_categories = ["Clearing","Trading"]
  
  def __init__(self):
    self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    self.session = requests.Session()
    self.session.get("http://nseindia.com",headers=self.headers)
    
  def pre_market_data(self,category):
    pre_market_category = {"NIFTY 50":"NIFTY","Nifty Bank":"BANKNIFTY","Emerge":"SME","Securities in F&O":"FO","Others":"OTHERS","All":"ALL"}
    data = self.session.get(f"https://www.nseindia.com/api/market-data-pre-open?key={pre_market_category[category]}",headers=self.headers).json()["data"]
    new_data = []
    for i in data:
      new_data.append(i["metadata"])
    df = pd.DataFrame(new_data)
    df = df.set_index("symbol", drop=True)
    return df
  
  def equity_market_data(self,category,symbol_list=False):
    category = category.upper().replace(' ','%20').replace('&','%26')
    data = self.session.get(f"https://www.nseindia.com/api/equity-stockIndices?index={category}",headers=self.headers).json()["data"]
    df = pd.DataFrame(data)
    df = df.drop(["meta"],axis=1)
    df = df.set_index("symbol",drop=True)
    if symbol_list:
      return list(df.index)
    else:
      return df
