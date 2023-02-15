import urllib
import numpy as np
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta
from datetime import date

from pandas_market_calendars import get_calendar

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

fnolink_tdy = "https://archives.nseindia.com/products/content/sec_bhavdata_full_07022023.csv"
fnolink_ydy = "https://archives.nseindia.com/products/content/sec_bhavdata_full_06022023.csv"
tdy = pd.read_csv(fnolink_tdy, skipinitialspace=True)
ydy = pd.read_csv(fnolink_ydy, skipinitialspace=True)
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
tdy['OH'] = np.where(tdy['OPEN_PRICE'] == tdy['HIGH_PRICE'], 'o=h', 'NA')
# print(tdy['OH'])
# res1 = tdy[tdy['OH'].astype(str).str.contains('o=h')][[
#     'SYMBOL', 'DATE1', 'OPEN_PRICE', 'HIGH_PRICE', 'LOW_PRICE', 'CLOSE_PRICE']]
res = tdy[tdy['OH'].astype(str).str.contains('o=h')]['SYMBOL']
# res = tdy[tdy['OH'].astype(str).str.contains('o=h')][
#         ['SYMBOL']]
# print(res.values.tolist())
oh_stocks = res.values.tolist()
print(oh_stocks)

def superTrendDay(stock):
    # stock = "ULTRACEMCO"
    tday = datetime.today()
    startDay = tday - timedelta(days=45)
    df = yf.download(stock + ".NS", start=startDay, end=tday, progress=False)
    # OR if you want to automatically apply the results to the DataFrame
    strend_value = df.ta.supertrend(period=7, multiplier=3, append=True)['SUPERT_7_3.0'][-1]
    df['temp'] = np.where((df["Close"] >= strend_value), 'Positive', 'Negative')
    trend = df.tail(1)['temp'][0]
    # print(strend_value)
    return trend


def getallCond(stockCode):
    #stockCode = "DEEPAKNTR"
    tday = datetime.today()
    startDay = tday - timedelta(days=2)
    # print(tday.date(),startDay)
    data = yf.download(stockCode + ".NS", start=startDay, end=tday, progress=False)
    data.reset_index(inplace=True)
    # print(data)
    pd.set_option('display.max_columns', None)
    # data.sort_values(by=['Datetime'], ascending=False, inplace=True)
    # data.sort_values('Date', inplace=True)
    # print(data.columns)
    # data.set_index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
    # data.reset_index(inplace=True)
    data.sort_values(by=['Date'], ascending=False, inplace=True)
    for i in range(1, 2):
        data['open_' + str(i) + 'day_ago'] = data['Open'].shift(-i)
        data['high_' + str(i) + 'day_ago'] = data['High'].shift(-i)
        data['low_' + str(i) + 'day_ago'] = data['Low'].shift(-i)
        data['close_' + str(i) + 'day_ago'] = data['Close'].shift(-i)

    data['prevBrk'] = np.where(data['Low'] < data['low_1day_ago'], 'brkPrevlow',
                      np.where(data['High'] > data['high_1day_ago'], 'brkPrevhigh','NA'))

    trend = superTrendDay(stockCode)
    # print(tday.date())
    data['Supertrend'] = trend
    data['Symbol'] = stockCode
    data = round(data, 2)
    data['pctChg'] = ((data['Open'] - data['Low'])/data['Low']) * 100
    # print(data)
    data = data[data['prevBrk'] == 'brkPrevlow']
    data = data[data['Supertrend'] == 'Negative']
    res = data[data['Date'].astype(str).str.contains(str((tday - timedelta(days=1)).date()))][
            ['Symbol','Open','High','Low','Close','prevBrk','Supertrend','pctChg']]
    # print(res)
    if res.empty:
        pass
    else:
        return res


# df = pd.DataFrame()
# for i in oh_stocks:
#     # print(i)
#     df = pd.concat([df,getallCond(i)])
#
# print(df)
# # print(df.describe())
# print("Avg Profit with O=H Strategy")
# print(round(df["pctChg"].mean(),2))
"""
oh_stocks = []
tday = datetime.today()
for stockCode in fno:
    # stockCode = "DEEPAKNTR"
    # startDay = tday - timedelta(days=1)
    data = yf.download(stockCode + ".NS", start=tday, end=tday, progress=False)
    data.reset_index(inplace=True)
    data = round(data, 2)
    # print(str(data["Open"][0]), str(data["High"][0]))
    if str(data["Open"][0]) == str(data["High"][0]):
        oh_stocks.append(stockCode)

print(oh_stocks) #['NMDC', 'HINDPETRO', 'IDEA', 'SAIL', 'IDFC', 'GNFC', 'WIPRO', 'BOSCHLTD', 'CHAMBLFERT', 'DEEPAKNTR', 'ITC', 'FEDERALBNK', 'DIXON', 'ZEEL', 'APOLLOTYRE', 'GUJGASLTD', 'BIOCON']
"""
nse = get_calendar("NSE")
end_date = pd.Timestamp('2022-12-15 00:00:00', tz='Asia/Kolkata').date()
start_date = end_date - pd.Timedelta(days=10)
schedule = nse.schedule(start_date=start_date, end_date=end_date)
working_days = schedule.index.date
stockCode ="HINDALCO"
tday = working_days[0]
data_5mins = yf.download(
        tickers=stockCode + ".NS", start=tday, end=tday + timedelta(days=1),
        period='90d',
        interval='5m',
        proxy=None,
        progress=False,
        group_by = 'ticker',
        auto_adjust=True,
        prepost=False,
        threads=True
    )
print(data_5mins)