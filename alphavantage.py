import time

import bs4
import json
import pandas as pd
import requests
from datetime import datetime
import csv
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

def datetotimestamp(date):
    time_tuple = date.timetuple()
    timestamp = round(time.mktime(time_tuple))
    return timestamp

def timestamptodate(timestamp):
    return datetime.fromtimestamp(timestamp)

date = datetime.today()
print(datetotimestamp(date))

start = datetotimestamp(datetime(2023,2,9)) #'1673936985'
end = datetotimestamp(datetime.today())#'1673939985'
# url = 'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol=HCLTECH&resolution=5&from='+start+'&to='+end+'&countback=2&currencyCode=INR'
url = 'https://priceapi.moneycontrol.com/techCharts/techChartController/history?symbol=HCLTECH&resolution=5&from='+str(start)+'&to='+str(end)
# url = 'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol=HCLTECH&resolution=5&from='+str(start)+'&to='+str(end)+'&countback=50&currencyCode=INR'
#'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol=HCLTECH&resolution=5&from=1673574880&to=1673940419&countback=330&currencyCode=INR'
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=HCLTECH.NS&interval=5min&apikey=IQAJNL9I9621LDNL&datatype=csv'
url2 ="https://priceapi.moneycontrol.com/techCharts/techChartController/history?symbol=HCLTECH&resolution=5&from=1673936985&to=1673939985"
dayurl = 'https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol=HCLTECH&from=1638156600&to=2114361000&resolution=1D'
import urllib3
tt= "https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol=ADANIENT&resolution=1D&from=1675263062&to=1676127062&countback=2&currencyCode=INR"
try:
    import urllib2 as urlreq # Python 2.x
except:
    import urllib.request as urlreq # Python 3.x
req = urlreq.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
data = json.loads(urlreq.urlopen(req).read())
print(data)
date = []
for dt in data['t']:
    date.append({'Date':timestamptodate(dt)})

dt = pd.DataFrame(date)
print(type(dt),type(data['o']))
intraday_data = pd.concat([dt, pd.DataFrame(data['o']), pd.DataFrame(data['h']), pd.DataFrame(data['l']), pd.DataFrame(data['c']), pd.DataFrame(data['v'])], axis=1)\
    .rename(columns={'o':'Open','h':'High','l':'Low','c':'Close','v':'Volume',})
print(intraday_data)
# print(intraday_data)
# with requests.Session() as s:
#     download = s.get(CSV_URL)
#     decoded_content = download.content.decode('utf-8')
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         print(row)

# url = 'https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O'
# # print(fnolist())
# resp = requests.get(url).json()
# print(resp)