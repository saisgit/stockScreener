import numpy as np
import datetime
from datetime import datetime, timedelta
import urllib
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import concurrent.futures
from timeit import default_timer as timer
import time
import sys
# Keep module imports prior to classes

def get920data1(fno):
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
        tickers=fno,  # start=startDay, end=tday,
        period=period,
        interval=duration,
        proxy=proxyServer, #group_by='ticker',
        progress=False,
        timeout=10
    )
    pd.set_option('display.max_columns', None)
    # df.sort_values(by=['Date'],ascending=False,inplace = True)
    df = round(df, 2)
    # df['symbol'] = stock
    df_inside = df.reset_index(inplace=False)
    res = df_inside[df_inside['Datetime'].astype(str).str.contains('09:15:00')][
        ['Open','High','Low','Close']] # 'Datetime'
    # result1.append(res)
    print(res.columns)
    # res=res.reset_index()
    # res.columns = ['_'.join(col).strip() for col in res.columns.values]
    # res.rename(columns={'a Unnamed: 0_level_1': 'a', 'b Unnamed: 1_level_1': 'b'}, inplace=True)
    # print(res.columns)
    res1=res
    id_vars = [idv for idv in res1.columns if 'Unnamed' in idv[1]]
    value_vars = [valv for valv in res1.columns if 'Unnamed' not in valv[1]]
    df_multiidx = res1.melt(id_vars=id_vars, value_vars=value_vars, var_name=['ohlc', 'stock'])
    df_multiidx.rename(columns={col_ren: col_ren[0] for col_ren in id_vars})
    # df2 = df_multiidx.reset_index()
    reslt = df_multiidx.pivot_table('value', ['stock'], 'ohlc')
    return reslt.reset_index()



fno1 = ['TATACOMM', 'NMDC', 'IOC', 'INDIGO', 'MFSL', 'HINDPETRO', 'HINDALCO', 'IDEA', 'SIEMENS', 'ABCAPITAL', 'IBULHSGFIN', 'PNB', 'ABB', 'MPHASIS', 'PVR', 'MCX', 'HINDCOPPER', 'PEL', 'SYNGENE', 'NATIONALUM', 'BPCL', 'LICHSGFIN', 'IDFCFIRSTB', 'SUNPHARMA', 'BHEL', 'ULTRACEMCO', 'SAIL', 'HDFCBANK', 'TCS', 'LT', 'JSWSTEEL', 'IDFC', 'BSOFT', 'EXIDEIND', 'METROPOLIS', 'BEL', 'TATAMOTORS', 'RAMCOCEM', 'M&MFIN', 'INDIAMART', 'MANAPPURAM', 'BALRAMCHIN', 'OFSS', 'JINDALSTEL', 'HDFC', 'VEDL', 'IRCTC', 'TORNTPOWER', 'HAVELLS', 'GNFC', 'GODREJPROP', 'BANKBARODA', 'MCDOWELL-N', 'GRANULES', 'DELTACORP', 'VOLTAS', 'ABBOTINDIA', 'ICICIBANK', 'INDUSTOWER', 'TECHM', 'L&TFH', 'BATAINDIA', 'SBIN', 'PETRONET', 'RAIN', 'UBL', 'RBLBANK', 'KOTAKBANK', 'TATACHEM', 'CUB', 'PAGEIND', 'CANFINHOME', 'WIPRO', 'CANBK', 'GMRINFRA', 'INFY', 'HDFCAMC', 'ATUL', 'MARUTI', 'INDHOTEL', 'BAJFINANCE', 'INTELLECT', 'POWERGRID', 'BOSCHLTD', 'CONCOR', 'IEX', 'BALKRISIND', 'HDFCLIFE', 'TATAPOWER', 'CROMPTON', 'CHOLAFIN', 'JUBLFOOD', 'BRITANNIA', 'SHRIRAMFIN', 'CHAMBLFERT', 'LTIM', 'TATASTEEL', 'SHREECEM', 'TVSMOTOR', 'M&M', 'DEEPAKNTR', 'DLF', 'CUMMINSIND', 'AXISBANK', 'ADANIPORTS', 'MUTHOOTFIN', 'ADANIENT', 'FSL', 'ICICIGI', 'ITC', 'DRREDDY', 'AUBANK', 'POLYCAB', 'INDIACEM', 'HAL', 'HCLTECH', 'NAVINFLUOR', 'PIIND', 'FEDERALBNK', 'DIXON', 'DALBHARAT', 'LTTS', 'ABFRL', 'ALKEM', 'JKCEMENT', 'COLPAL', 'OBEROIRLTY', 'SBICARD', 'GAIL', 'BANDHANBNK', 'TORNTPHARM', 'WHIRLPOOL', 'BAJAJ-AUTO', 'ACC', 'BERGEPAINT', 'ASIANPAINT', 'NAUKRI', 'HEROMOTOCO', 'HONAUT', 'MGL', 'AUROPHARMA', 'ZEEL', 'LUPIN', 'AARTIIND', 'UPL', 'GODREJCP', 'ZYDUSLIFE', 'TRENT', 'PERSISTENT', 'SUNTV', 'EICHERMOT', 'BAJAJFINSV', 'COFORGE', 'ASTRAL', 'GRASIM', 'ICICIPRULI', 'RECLTD', 'INDUSINDBK', 'NTPC', 'SBILIFE', 'NESTLEIND', 'DABUR', 'GLENMARK', 'RELIANCE', 'AMBUJACEM', 'TATACONSUM', 'TITAN', 'IGL', 'ASHOKLEY', 'IPCALAB', 'COALINDIA', 'ONGC', 'PFC', 'COROMANDEL', 'BHARATFORG', 'MARICO', 'HINDUNILVR', 'PIDILITIND', 'APOLLOTYRE', 'GUJGASLTD', 'MOTHERSON', 'LALPATHLAB', 'ESCORTS', 'BIOCON', 'APOLLOHOSP', 'DIVISLAB', 'CIPLA', 'MRF', 'LAURUSLABS', 'SRF', 'BHARTIARTL']

fno = list(map(lambda x: x+".NS",fno1))

start = timer()

print(get920data1(fno))
end = timer()
print("Time taken with parallel execution is ",end-start)
