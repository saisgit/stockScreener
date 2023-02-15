import requests
from bs4 import BeautifulSoup
from pandas_market_calendars import get_calendar
import pandas as pd
import urllib
import numpy as np
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta
from datetime import date
import timeit
fno = ['TATACOMM', 'NMDC', 'IOC', 'INDIGO', 'MFSL', 'HINDPETRO', 'HINDALCO', 'IDEA', 'SIEMENS', 'ABCAPITAL',
       'IBULHSGFIN', 'PNB', 'ABB', 'MPHASIS', 'PVR', 'MCX', 'HINDCOPPER', 'PEL', 'SYNGENE', 'NATIONALUM', 'BPCL',
       'LICHSGFIN', 'IDFCFIRSTB', 'SUNPHARMA', 'BHEL', 'ULTRACEMCO', 'SAIL', 'HDFCBANK', 'TCS', 'LT', 'JSWSTEEL',
       'IDFC', 'BSOFT', 'EXIDEIND', 'METROPOLIS', 'BEL', 'TATAMOTORS', 'RAMCOCEM', 'M&MFIN', 'INDIAMART', 'MANAPPURAM',
       'BALRAMCHIN', 'OFSS', 'JINDALSTEL', 'HDFC', 'VEDL', 'IRCTC', 'TORNTPOWER', 'HAVELLS', 'GNFC', 'GODREJPROP',
       'BANKBARODA', 'MCDOWELL-N', 'GRANULES', 'DELTACORP', 'VOLTAS', 'ABBOTINDIA', 'ICICIBANK', 'INDUSTOWER', 'TECHM',
       'L&TFH', 'BATAINDIA', 'SBIN', 'PETRONET', 'RAIN', 'UBL', 'RBLBANK', 'KOTAKBANK', 'TATACHEM', 'CUB', 'PAGEIND',
       'CANFINHOME', 'WIPRO', 'CANBK', 'GMRINFRA', 'INFY', 'HDFCAMC', 'ATUL', 'MARUTI', 'INDHOTEL', 'BAJFINANCE',
       'INTELLECT', 'POWERGRID', 'BOSCHLTD', 'CONCOR', 'IEX', 'BALKRISIND', 'HDFCLIFE', 'TATAPOWER', 'CROMPTON',
       'CHOLAFIN', 'JUBLFOOD', 'BRITANNIA', 'SHRIRAMFIN', 'CHAMBLFERT', 'LTIM', 'TATASTEEL', 'SHREECEM', 'TVSMOTOR',
       'M&M', 'DEEPAKNTR', 'DLF', 'CUMMINSIND', 'AXISBANK', 'ADANIPORTS', 'MUTHOOTFIN', 'ADANIENT', 'FSL', 'ICICIGI',
       'ITC', 'DRREDDY', 'AUBANK', 'POLYCAB', 'INDIACEM', 'HAL', 'HCLTECH', 'NAVINFLUOR', 'PIIND', 'FEDERALBNK',
       'DIXON', 'DALBHARAT', 'LTTS', 'ABFRL', 'ALKEM', 'JKCEMENT', 'COLPAL', 'OBEROIRLTY', 'SBICARD', 'GAIL',
       'BANDHANBNK', 'TORNTPHARM', 'WHIRLPOOL', 'BAJAJ-AUTO', 'ACC', 'BERGEPAINT', 'ASIANPAINT', 'NAUKRI', 'HEROMOTOCO',
       'HONAUT', 'MGL', 'AUROPHARMA', 'ZEEL', 'LUPIN', 'AARTIIND', 'UPL', 'GODREJCP', 'ZYDUSLIFE', 'TRENT',
       'PERSISTENT', 'SUNTV', 'EICHERMOT', 'BAJAJFINSV', 'COFORGE', 'ASTRAL', 'GRASIM', 'ICICIPRULI', 'RECLTD',
       'INDUSINDBK', 'NTPC', 'SBILIFE', 'NESTLEIND', 'DABUR', 'GLENMARK', 'RELIANCE', 'AMBUJACEM', 'TATACONSUM',
       'TITAN', 'IGL', 'ASHOKLEY', 'IPCALAB', 'COALINDIA', 'ONGC', 'PFC', 'COROMANDEL', 'BHARATFORG', 'MARICO',
       'HINDUNILVR', 'PIDILITIND', 'APOLLOTYRE', 'GUJGASLTD', 'MOTHERSON', 'LALPATHLAB', 'ESCORTS', 'BIOCON',
       'APOLLOHOSP', 'DIVISLAB', 'CIPLA', 'MRF', 'LAURUSLABS', 'SRF', 'BHARTIARTL']

nse = get_calendar("NSE")
end_date = pd.Timestamp('2022-12-15 00:00:00', tz='Asia/Kolkata').date()
start_date = end_date - pd.Timedelta(days=10)
schedule = nse.schedule(start_date=start_date, end_date=end_date)
working_days = schedule.index.date
# current_day = working_days[-1]
# current_day_dmy = working_days[-1].strftime("%d%m%Y")
# previous_day_dmy = working_days[-2].strftime("%d%m%Y")
# print(current_day_dmy, previous_day_dmy)


def get_oh_ol_stocks(current_date, ohlc):
    # fnolink_tdy = "https://archives.nseindia.com/products/content/sec_bhavdata_full_07022023.csv"
    fnolink_tdy = "https://archives.nseindia.com/products/content/sec_bhavdata_full_{}.csv".format(
        current_date.strftime("%d%m%Y"))
    tdy = pd.read_csv(fnolink_tdy, skipinitialspace=True)
    pd.set_option('display.max_columns', None)
    tdy.reset_index(inplace=True)
    tdy.columns = tdy.columns.str.replace(' ', '')
    # print(tdy['SERIES'])
    tdy['SERIES'].str.replace(' ', '')
    tdy['OPEN_PRICE'].astype(str).str.replace(' ', '')
    tdy['HIGH_PRICE'].astype(str).str.replace(' ', '')
    tdy = tdy[tdy['SERIES'] == 'EQ']
    tdy = round(tdy, 2)
    # print(tdy)
    tdy = tdy[tdy['SYMBOL'].isin(fno)]
    if ohlc == 'OH':
        tdy['OH'] = np.where(tdy['OPEN_PRICE'] == tdy['HIGH_PRICE'], 'o=h', 'NA')
        res = tdy[tdy['OH'].astype(str).str.contains('o=h')]['SYMBOL']
        oh_stocks = res.values.tolist()
        return oh_stocks
    elif ohlc == 'OL':
        tdy['OL'] = np.where(tdy['OPEN_PRICE'] == tdy['LOW_PRICE'], 'o=l', 'NA')
        res = tdy[tdy['OL'].astype(str).str.contains('o=l')]['SYMBOL']
        ol_stocks = res.values.tolist()
        return ol_stocks
    else:
        pass
    # print(oh_stocks)


def superTrendDay(stock, current):
    # stock = "ULTRACEMCO"
    tday = current  # datetime.today()
    startDay = tday - timedelta(days=45)
    df = ''
    if stock == '^NSEI':
        df = yf.download(stock, start=startDay, end=tday + timedelta(days=1), progress=False)
    else:
        df = yf.download(stock + ".NS", start=startDay, end=tday + timedelta(days=1), progress=False)
    # OR if you want to automatically apply the results to the DataFrame
    strend_value = df.ta.supertrend(period=7, multiplier=3, append=True)['SUPERT_7_3.0'][-1]
    df['temp'] = np.where((df["Close"] >= strend_value), 'Positive', 'Negative')
    trend = df.tail(1)['temp'][0]
    # print(strend_value)
    return trend


# def getallCond(stockCode,current):
#     # stockCode = "DEEPAKNTR"
#     tday = current #datetime.today()
#     startDay = tday - timedelta(days=1)
#     # print(tday.date(),startDay)
#     data = yf.download(stockCode + ".NS", start=startDay, end=tday+timedelta(days=1), progress=False)
#     data.reset_index(inplace=True)
#     # print(data)
#     pd.set_option('display.max_columns', None)
#     # data.sort_values(by=['Datetime'], ascending=False, inplace=True)
#     # data.sort_values('Date', inplace=True)
#     # print(data.columns)
#     # data.set_index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
#     # data.reset_index(inplace=True)
#     data.sort_values(by=['Date'], ascending=False, inplace=True)
#     for i in range(1, 2):
#         data['open_' + str(i) + 'day_ago'] = data['Open'].shift(-i)
#         data['high_' + str(i) + 'day_ago'] = data['High'].shift(-i)
#         data['low_' + str(i) + 'day_ago'] = data['Low'].shift(-i)
#         data['close_' + str(i) + 'day_ago'] = data['Close'].shift(-i)
#
#     data['prevBrk'] = np.where(data['Low'] < data['low_1day_ago'], 'brkPrevlow',
#                                np.where(data['High'] > data['high_1day_ago'], 'brkPrevhigh', 'NA'))
#
#     trend = superTrendDay(stockCode, current)
#     # print(tday.date())
#     data['Supertrend'] = trend
#     data['Symbol'] = stockCode
#     data = round(data, 2)
#     data['pctChg'] = ((data['Open'] - data['Low']) / data['Low']) * 100
#     # print(data)
#     data = data[data['prevBrk'] == 'brkPrevlow']
#     data = data[data['Supertrend'] == 'Negative']
#     #print(data)
#     res = data[data['Date'].astype(str).str.contains(str((tday)))][
#         ['Symbol', 'Open', 'High', 'Low', 'Close', 'prevBrk', 'Supertrend', 'pctChg']]
#     # print(res)
#     if res.empty:
#         pass
#     else:
#         return res


def getallCond(stockCode, current, ohlc):
    # stockCode = "DEEPAKNTR"
    tday = current  # datetime.today()
    startDay = tday - timedelta(days=1)
    # print(tday.date(),startDay)
    data = yf.download(stockCode + ".NS", start=startDay, end=tday + timedelta(days=1), progress=False)
    data_5mins = yf.download(
        tickers=stockCode + ".NS", start=tday, end=tday + timedelta(days=1),
        period='1d',
        interval='5m',
        proxy=None,
        progress=False
    )
    data_5mins.reset_index(inplace=True)
    data.reset_index(inplace=True)
    pd.set_option('display.max_columns', None)
    data_5mins.sort_values(by=['Datetime'], ascending=False, inplace=True)
    data.sort_values(by=['Date'], ascending=False, inplace=True)
    data_5mins = round(data_5mins, 2)
    data = round(data, 2)
    data_5mins_915 = data_5mins[data_5mins['Datetime'].astype(str).str.contains(str(('09:15')))]
    data_5mins_920 = data_5mins[data_5mins['Datetime'].astype(str).str.contains(str(('09:20')))]
    # print(data_5mins_920['Low'].values[0])
    # prevCandleBrk:str = ''
    OHpct = round(
        ((data_5mins_915['Open'].values[0] - data_5mins_915['Low'].values[0]) / data_5mins_915['Open'].values[0]) * 100,
        2)
    OLpct = round(((data_5mins_915['High'].values[0] - data_5mins_915['Open'].values[0]) /
                   data_5mins_915['High'].values[0]) * 100, 2)
    # print(OHpct,OLpct)
    if data_5mins_920['Low'].values[0] < data_5mins_915['Low'].values[0]:
        prevCandleBrk = 'brk5minslow'
    elif data_5mins_920['High'].values[0] > data_5mins_915['High'].values[0]:
        prevCandleBrk = 'brk5minshigh'
    else:
        prevCandleBrk = 'NA'

    data['prevBrk'] = prevCandleBrk
    trend = superTrendDay(stockCode, current)
    # print(tday.date())
    data['Supertrend'] = trend
    data['Symbol'] = stockCode
    if ohlc == 'OH':
        data['pctChg'] = ((data['Open'] - data['Low']) / data['Low']) * 100
        data['first5min'] = OHpct
        data = data[data['prevBrk'] == 'brk5minslow']
        data = data[data['Supertrend'] == 'Negative']
    elif ohlc == 'OL':
        data['pctChg'] = ((data['High'] - data['Open']) / data['Open']) * 100
        data['first5min'] = OLpct
        data = data[data['prevBrk'] == 'brk5minsHigh']
        data = data[data['Supertrend'] == 'Positive']

    # print(data)
    res = data[data['Date'].astype(str).str.contains(str((tday)))][
        ['Symbol', 'Open', 'High', 'Low', 'Close', 'prevBrk', 'Supertrend', 'pctChg', 'first5min']]  # 'High', 'Low', 'Close',
    # print(res)
    if res.empty:
        pass
    else:
        return res


def StartBackTest(current_day):
    # print("Running for - ",current_day)
    # print(datetime.today())
    nifty_st = superTrendDay('^NSEI', current_day)
    # print("Nifty supertrend - ",nifty_st)
    df = pd.DataFrame()
    if nifty_st == 'Negative':
        oh_stocks = get_oh_ol_stocks(current_day, 'OH')
        for i in oh_stocks:
            # print(i)
            df = pd.concat([df, getallCond(i, current_day, 'OH')])
        # print(df)
        # print(df.describe())
        # print("Avg Profit with O=H Strategy")
        #avg = (round(df["pctChg"].mean(), 2))
        df['nifty_st'] = nifty_st
        #df['avgProfit'] = avg
        df['current_day'] = str(current_day.strftime("%d-%m-%Y"))
    elif nifty_st == 'Positive':
        ol_stocks = get_oh_ol_stocks(current_day, 'OL')
        for i in ol_stocks:
            # print(i)
            df = pd.concat([df, getallCond(i, current_day, 'OL')])
        # print(df)
        # print(df.describe())
        # print("Avg Profit with O=L Strategy")
        # print(round(df["pctChg"].mean(), 2))
        #avg = (round(df["pctChg"].mean(), 2))
        df['nifty_st'] = nifty_st
        #df['avgProfit'] = avg
        df['current_day'] = str(current_day.strftime("%d-%m-%Y"))
    return df


print(working_days)
start = timeit.default_timer()
final = pd.DataFrame()
for i in working_days:
    res = StartBackTest(i)
    final = pd.concat([final, res])

print(final)
final.to_csv('logs/backtest_920.csv', index=False)
stop = timeit.default_timer()
execution_time = stop - start

print("Program Executed in "+str(execution_time))

