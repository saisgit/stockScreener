
import talib
import numpy as np
import datetime
from stocks.CheckEma import CheckEma
from stocks.SuperTrendInd import SuperTrendInd
from datetime import datetime, timedelta
from stocks.Ohlc_check import Ohlc_check
from stocks.CheckYestHighLow import CheckYestHighLow
from stocks.SuperTrendInd import SuperTrendInd
import urllib
import yfinance as yf
# grp = talib.get_function_groups()['Pattern Recognition']
# print(grp)
import pandas as pd
import pandas_ta as ta
from nsepython import *

print("*************** nifty change  **************")
print(nse_marketStatus()['marketState'][0]['percentChange'])
positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
# positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20100')
endp = len(positions['data'])
print("*************** BUY **************")
Ohlc = Ohlc_check()
buy, buytable = Ohlc.openLowBuy(endp, positions)
print(buy)
print("*************** SELL **************")
sell, selltable = Ohlc.openHighSell(endp, positions)
print(sell)
############### CHECK YESTERTDAY HIGH ##################
chkHighLow = CheckYestHighLow()
breaks1dayhigh = chkHighLow.checkYestHigh(buy)
print("")
print("*********** O=L and Breaks yesterday HIGH ********")
print(breaks1dayhigh)
print("")
############### CHECK YESTERTDAY LOW ##################
breaks1daylow = chkHighLow.checkYestLow(sell)
print("*********** O=H and Breaks yesterday LOW *********")
print(breaks1daylow)
print("")
chkemaobj = CheckEma()
stObj = SuperTrendInd()
# chkemaobj.addEmaInsideCandle()
# sellStock = addEmaInsideCandle('NESTLEIND')
# sellStock = sellStock[sellStock['ema_21_Signal'] == 'Sell']
# sellStock = sellStock[sellStock['ohlc_sell'] == True]
# sellStock = sellStock[sellStock['Inside_bar'] == True]
# print(sellStock)
# buyStocks = ['AMBUJACEM', 'HEROMOTOCO', 'ICICIPRULI']
# sellStocks = ['ASTRAL', 'PAGEIND', 'TITAN', 'UBL', 'ZYDUSLIFE']
print(datetime.datetime.now())
buy = []
sell = []
inside_bar_ema_21_signal_buy = []
inside_bar_ema_21_signal_sell = []
for i in breaks1dayhigh:#breaks1dayhigh
    buyStock = chkemaobj.addEmaInsideCandle(i)
    st = stObj.superTrendDay(i)
    print("allTrend-", st)
    # buyStock = buyStock[buyStock['ema_21_Signal'] == 'Buy']
    # buyStock = buyStock[buyStock['Inside_bar'] == True]
    print("buy-",i)
    print(buyStock.tail(1))
    tmp = buyStock.iloc[-1]
    if st == 'Positive' and tmp['ema_21_Signal'] == 'Buy':
        buy.append(i)
    if tmp['Inside_bar'] == True and tmp['ema_21_Signal'] == 'Buy':
        inside_bar_ema_21_signal_buy.append(i)
    print("__________________________")
    # buyStock = buyStock[buyStock['Datetime'].astype(str).str.contains(str(tday)+" 09:20:00")]
    # if not buyStock.isempty:
    #     if buyStock['ema_21_Signal'] == 'Buy' and buyStock['Inside_bar'] == True:
    #         buy.append(i)


for i in breaks1daylow:#breaks1daylow
    sellStock = chkemaobj.addEmaInsideCandle(i)
    st = stObj.superTrendDay(i)
    # sellStock = sellStock[sellStock['ema_21_Signal'] == 'Sell']
    # sellStock = sellStock[sellStock['Inside_bar'] == True]
    print("sell-", i)
    print("allTrend-",st)
    print(sellStock.tail(1))
    tmp = sellStock.iloc[-1]
    if st == 'Negative' and tmp['ema_21_Signal'] == 'Sell':
        sell.append(i)
    if tmp['Inside_bar'] == True and tmp['ema_21_Signal'] == 'Sell':
        inside_bar_ema_21_signal_sell.append(i)
    print("__________________________")
#     sellStock = sellStock[sellStock['Datetime'].astype(str).str.contains(str(tday+" 09:20:00"))]
#     if not sellStock.isempty:
#         if sellStock['ema_21_Signal'] == 'Sell' and sellStock['Inside_bar'] == True:
#             sell.append(i)

print("Buy these - ",buy)
print("Sell these - ",sell)
print("")
print('Check Secondary options - below')
print("inside_bar_ema_21_signal_buy--")
print(inside_bar_ema_21_signal_buy)
print("inside_bar_ema_21_signal_sell--")
print(inside_bar_ema_21_signal_sell)