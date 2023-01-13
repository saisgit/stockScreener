#!/usr/bin/python3

# Pyinstaller compile Windows: pyinstaller --onefile --icon=src\icon.ico src\screenipy.py  --hidden-import cmath --hidden-import talib.stream --hidden-import numpy --hidden-import pandas --hidden-import alive-progress
# Pyinstaller compile Linux  : pyinstaller --onefile --icon=src/icon.ico src/screenipy.py  --hidden-import cmath --hidden-import talib.stream --hidden-import numpy --hidden-import pandas --hidden-import alive-progress

# Keep module imports prior to classes
import os
import urllib

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta
from datetime import date

class SuperTrendInd():
    def superTrendDay(self,stock):
        # stock = "ULTRACEMCO"
        tday = datetime.today()
        startDay = tday - timedelta(days=100)
        # _df = pd.DataFrame() # Empty DataFrame
        df = yf.download(stock + ".NS", start=startDay, end=tday, progress=False)
        # df.ta.supertrend(period=7, multiplier=3)
        # OR if you want to automatically apply the results to the DataFrame
        strend_value = df.ta.supertrend(period=7, multiplier=3, append=True)['SUPERT_7_3.0'][-1]

        df['temp'] = np.where((df["Close"] >= strend_value), 'Positive', 'Negative')
        trend = df.tail(1)['temp'][0]
        # print(stock, "D", round(strend_value, 2), trend)
        return trend


    def superTrend15min(self,stock):
            # stock = "ULTRACEMCO"
            tday = datetime.today()
            startDay = tday - timedelta(days=50)
            period = "1d"
            duration = "15m"  # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
            totalStock = []
            try:
                proxyServer = urllib.request.getproxies()['http']
            except KeyError:
                proxyServer = ""
            # _df = pd.DataFrame() # Empty DataFrame
            # df = yf.download(stock+".NS",start=startDay,end=tday)
            df = yf.download(
                tickers=stock + ".NS", start=startDay, end=tday,
                period=period,
                interval=duration,
                proxy=proxyServer,
                progress=False,
                timeout=10
            )
            # df.ta.supertrend(period=7, multiplier=3)
            # OR if you want to automatically apply the results to the DataFrame
            strend_value = df.ta.supertrend(period=7, multiplier=3, append=True)['SUPERT_7_3.0'][-1]

            df['temp'] = np.where((df["Close"] >= strend_value), 'Positive', 'Negative')
            trend = df.tail(1)['temp'][0]
            # print(stock,"15m", round(strend_value, 2), trend)
            return trend


    def superTrend5min(self,stock):
            # stock = "ULTRACEMCO"
            tday = datetime.today()
            startDay = tday - timedelta(days=50)
            period = "1d"
            duration = "5m"  # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
            totalStock = []
            try:
                proxyServer = urllib.request.getproxies()['http']
            except KeyError:
                proxyServer = ""
            # _df = pd.DataFrame() # Empty DataFrame
            # df = yf.download(stock+".NS",start=startDay,end=tday)
            df = yf.download(
                tickers=stock + ".NS", start=startDay, end=tday,
                period=period,
                interval=duration,
                proxy=proxyServer,
                progress=False,
                timeout=10
            )
            # df.ta.supertrend(period=7, multiplier=3)
            # OR if you want to automatically apply the results to the DataFrame
            strend_value = df.ta.supertrend(period=7, multiplier=3, append=True)['SUPERT_7_3.0'][-1]

            df['temp'] = np.where((df["Close"] >= strend_value), 'Positive', 'Negative')
            trend = df.tail(1)['temp'][0]
            # print(stock,"5m", round(strend_value, 2), trend)
            return trend


    def allSuperTrends(self,stock):
        # print("Day ST")
        # print(superTrendDay('IOC'))
        if (SuperTrendInd.superTrend15min(self,stock) == SuperTrendInd.superTrendDay(self,stock) == "Positive"):
            return "allPositive"
        elif (SuperTrendInd.superTrend15min(self,stock) == SuperTrendInd.superTrendDay(self,stock) == "Negative"):
            return "allNegative"
        else:
            return None
        # print("ST 15 min")
        # print(superTrend15min('IOC'))
        # print("ST 5 min")
        # print(superTrend5min('IOC'))
        # print(stock +" == "+"5m-->"+superTrend5min(stock)+" | "+ "15m-->"+superTrend15min(stock)+" | "+ "D-->"+superTrendDay(stock)+" | ")


    #print(allSuperTrends("ULTRACEMCO"))
    # print(superTrend5min("NAVINFLUOR"))
    # print(superTrend15min("NAVINFLUOR"))
    # print(superTrendDay("NAVINFLUOR"))

    # fno = ['TATACOMM', 'NMDC', 'IOC', 'INDIGO', 'MFSL', 'HINDPETRO', 'HINDALCO', 'IDEA', 'SIEMENS', 'ABCAPITAL', 'IBULHSGFIN', 'PNB', 'ABB', 'MPHASIS', 'PVR', 'MCX', 'HINDCOPPER', 'PEL', 'SYNGENE', 'NATIONALUM', 'BPCL', 'LICHSGFIN', 'IDFCFIRSTB', 'SUNPHARMA', 'BHEL', 'ULTRACEMCO', 'SAIL', 'HDFCBANK', 'TCS', 'LT', 'JSWSTEEL', 'IDFC', 'BSOFT', 'EXIDEIND', 'METROPOLIS', 'BEL', 'TATAMOTORS', 'RAMCOCEM', 'M&MFIN', 'INDIAMART', 'MANAPPURAM', 'BALRAMCHIN', 'OFSS', 'JINDALSTEL', 'HDFC', 'VEDL', 'IRCTC', 'TORNTPOWER', 'HAVELLS', 'GNFC', 'GODREJPROP', 'BANKBARODA', 'MCDOWELL-N', 'GRANULES', 'DELTACORP', 'VOLTAS', 'ABBOTINDIA', 'ICICIBANK', 'INDUSTOWER', 'TECHM', 'L&TFH', 'BATAINDIA', 'SBIN', 'PETRONET', 'RAIN', 'UBL', 'RBLBANK', 'KOTAKBANK', 'TATACHEM', 'CUB', 'PAGEIND', 'CANFINHOME', 'WIPRO', 'CANBK', 'GMRINFRA', 'INFY', 'HDFCAMC', 'ATUL', 'MARUTI', 'INDHOTEL', 'BAJFINANCE', 'INTELLECT', 'POWERGRID', 'BOSCHLTD', 'CONCOR', 'IEX', 'BALKRISIND', 'HDFCLIFE', 'TATAPOWER', 'CROMPTON', 'CHOLAFIN', 'JUBLFOOD', 'BRITANNIA', 'SHRIRAMFIN', 'CHAMBLFERT', 'LTIM', 'TATASTEEL', 'SHREECEM', 'TVSMOTOR', 'M&M', 'DEEPAKNTR', 'DLF', 'CUMMINSIND', 'AXISBANK', 'ADANIPORTS', 'MUTHOOTFIN', 'ADANIENT', 'FSL', 'ICICIGI', 'ITC', 'DRREDDY', 'AUBANK', 'POLYCAB', 'INDIACEM', 'HAL', 'HCLTECH', 'NAVINFLUOR', 'PIIND', 'FEDERALBNK', 'DIXON', 'DALBHARAT', 'LTTS', 'ABFRL', 'ALKEM', 'JKCEMENT', 'COLPAL', 'OBEROIRLTY', 'SBICARD', 'GAIL', 'BANDHANBNK', 'TORNTPHARM', 'WHIRLPOOL', 'BAJAJ-AUTO', 'ACC', 'BERGEPAINT', 'ASIANPAINT', 'NAUKRI', 'HEROMOTOCO', 'HONAUT', 'MGL', 'AUROPHARMA', 'ZEEL', 'LUPIN', 'AARTIIND', 'UPL', 'GODREJCP', 'ZYDUSLIFE', 'TRENT', 'PERSISTENT', 'SUNTV', 'EICHERMOT', 'BAJAJFINSV', 'COFORGE', 'ASTRAL', 'GRASIM', 'ICICIPRULI', 'RECLTD', 'INDUSINDBK', 'NTPC', 'SBILIFE', 'NESTLEIND', 'DABUR', 'GLENMARK', 'RELIANCE', 'AMBUJACEM', 'TATACONSUM', 'TITAN', 'IGL', 'ASHOKLEY', 'IPCALAB', 'COALINDIA', 'ONGC', 'PFC', 'COROMANDEL', 'BHARATFORG', 'MARICO', 'HINDUNILVR', 'PIDILITIND', 'APOLLOTYRE', 'GUJGASLTD', 'MOTHERSON', 'LALPATHLAB', 'ESCORTS', 'BIOCON', 'APOLLOHOSP', 'DIVISLAB', 'CIPLA', 'MRF', 'LAURUSLABS', 'SRF', 'BHARTIARTL']
