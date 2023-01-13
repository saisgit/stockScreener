# https://www1.nseindia.com/content/fo/fo_underlyinglist.htm
import requests
import pandas as pd
import tabulate
from nsepython import *

# positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
# print(fnolist())
# def __init__(self):
#     positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
#     endp = len(positions['data'])
class Ohlc_check():
    def openLowBuy(self,endp,positions):
        buy = []
        buytable = []
        for x in range(0, endp):
            if(positions['data'][x]['open']==positions['data'][x]['dayLow']):
                buy.append(positions['data'][x]['symbol'])
                ts = []
                #print(positions['data'][x]['symbol'] + "-->" + positions['data'][x]['open'] + "-->" + str(positions['data'][x]['change']) + "-->" + str(positions['data'][x]['pChange']))
                ts.append(positions['data'][x]['symbol'])
                ts.append(str(positions['data'][x]['open']))
                ts.append(str(positions['data'][x]['change']))
                ts.append(str(positions['data'][x]['pChange']))
                buytable.append(ts)
        return buy,buytable

    def openHighSell(self,endp,positions):
        selltable = []
        sell = []
        for x in range(0, endp):
            if(positions['data'][x]['open']==positions['data'][x]['dayHigh']):
                sell.append(positions['data'][x]['symbol'])
                ts = []
                #print(positions['data'][x]['symbol'] + "-->" + positions['data'][x]['open'] + "-->" + str(positions['data'][x]['change']) + "-->" + str(positions['data'][x]['pChange']))
                ts.append(positions['data'][x]['symbol'])
                ts.append(str(positions['data'][x]['open']))
                ts.append(str(positions['data'][x]['change']))
                ts.append(str(positions['data'][x]['pChange']))
                selltable.append(ts)
        return sell,selltable
