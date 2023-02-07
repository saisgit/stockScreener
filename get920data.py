import talib
import numpy as np
import datetime
from datetime import datetime, timedelta
import urllib
import yfinance as yf
import pandas as pd
import pandas_ta as ta


def get920data(stock):
    tday = datetime.today()
    period = "1d"
    duration = "5m"  # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
    totalStock = []
    # stock ="HINDALCO" #HINDALCO
    try:
        proxyServer = urllib.request.getproxies()['http']
    except KeyError:
        proxyServer = ""
    # _df = pd.DataFrame() # Empty DataFrame
    # df = yf.download(stock+".NS",start=startDay,end=tday)
    df = yf.download(
        tickers=stock + ".NS",  # start=startDay, end=tday,
        period=period,
        interval=duration,
        proxy=proxyServer,
        progress=False,
        timeout=10
    )
    pd.set_option('display.max_columns', None)
    # df.sort_values(by=['Date'],ascending=False,inplace = True)
    df = round(df, 2)
    df_inside = df.reset_index(inplace=False)
    res = df_inside[df_inside['Datetime'].astype(str).str.contains('09:20:00')][
        ['Open','High','Low','Close']] #'Datetime',
    return res.values.tolist()[0]


print(get920data('CHAMBLFERT'))