from datetime import date
from nsepy import get_history
import pandas as pd
import yfinance as yf
from nsepython import *

class NoOfContracts():
    # Stock futures (Similarly for index futures, set index = True)
    def checkContract(self,symbol):
        stock_fut = get_history(symbol=symbol,
                                start=date(2023, 1, 10),
                                end=date(2023, 1, 30),
                                # index=True,
                                futures=True,
                                expiry_date=date(2023, 1, 25)
                                )
        # stock_fut = get_history(symbol="ZYDUSLIFE", start=date(2023,1,1), end=date(2023,1,10))
        stock_fut.reset_index(inplace=True)
        # pd.set_option('display.max_columns', None)
        # stock_fut.set_index(['Date', 'Symbol', 'Close', 'Number of Contracts','Change in OI'], inplace=True)
        stock_fut = stock_fut[['Date', 'Symbol', 'Close', 'Number of Contracts']]
        stock_fut.sort_values(by=['Date'], ascending=False, inplace=True)
        stock_fut = stock_fut.reset_index()
        if stock_fut.empty:
            pass
        else:
            stock_fut['contracts_1day_ago'] = stock_fut['Number of Contracts'].shift(-1)
            # print(stock_fut)
            contracts = round(stock_fut['Number of Contracts'][0], 0)
            contracts1dayago = round(stock_fut['contracts_1day_ago'][0], 0)
            print("contracts:"+str(contracts), " | contracts1dayago:"+str(contracts1dayago)," | contracts1dayago * 1.5:"+ str(1.5 * contracts1dayago))
            if (contracts >= 1.5 * contracts1dayago):
                return True
            else:
                return False
    # ss = stock_fut[stock_fut.columns[0:4]]

    # print(checkContract("ABFRL"))

    # fno = fnolist()
fno = ['TATACOMM', 'NMDC', 'IOC', 'INDIGO', 'MFSL', 'HINDPETRO', 'HINDALCO', 'IDEA', 'SIEMENS', 'ABCAPITAL', 'IBULHSGFIN', 'PNB', 'ABB', 'MPHASIS', 'PVR', 'MCX', 'HINDCOPPER', 'PEL', 'SYNGENE', 'NATIONALUM', 'BPCL', 'LICHSGFIN', 'IDFCFIRSTB', 'SUNPHARMA', 'BHEL', 'ULTRACEMCO', 'SAIL', 'HDFCBANK', 'TCS', 'LT', 'JSWSTEEL', 'IDFC', 'BSOFT', 'EXIDEIND', 'METROPOLIS', 'BEL', 'TATAMOTORS', 'RAMCOCEM', 'M&MFIN', 'INDIAMART', 'MANAPPURAM', 'BALRAMCHIN', 'OFSS', 'JINDALSTEL', 'HDFC', 'VEDL', 'IRCTC', 'TORNTPOWER', 'HAVELLS', 'GNFC', 'GODREJPROP', 'BANKBARODA', 'MCDOWELL-N', 'GRANULES', 'DELTACORP', 'VOLTAS', 'ABBOTINDIA', 'ICICIBANK', 'INDUSTOWER', 'TECHM', 'L&TFH', 'BATAINDIA', 'SBIN', 'PETRONET', 'RAIN', 'UBL', 'RBLBANK', 'KOTAKBANK', 'TATACHEM', 'CUB', 'PAGEIND', 'CANFINHOME', 'WIPRO', 'CANBK', 'GMRINFRA', 'INFY', 'HDFCAMC', 'ATUL', 'MARUTI', 'INDHOTEL', 'BAJFINANCE', 'INTELLECT', 'POWERGRID', 'BOSCHLTD', 'CONCOR', 'IEX', 'BALKRISIND', 'HDFCLIFE', 'TATAPOWER', 'CROMPTON', 'CHOLAFIN', 'JUBLFOOD', 'BRITANNIA', 'SHRIRAMFIN', 'CHAMBLFERT', 'LTIM', 'TATASTEEL', 'SHREECEM', 'TVSMOTOR', 'M&M', 'DEEPAKNTR', 'DLF', 'CUMMINSIND', 'AXISBANK', 'ADANIPORTS', 'MUTHOOTFIN', 'ADANIENT', 'FSL', 'ICICIGI', 'ITC', 'DRREDDY', 'AUBANK', 'POLYCAB', 'INDIACEM', 'HAL', 'HCLTECH', 'NAVINFLUOR', 'PIIND', 'FEDERALBNK', 'DIXON', 'DALBHARAT', 'LTTS', 'ABFRL', 'ALKEM', 'JKCEMENT', 'COLPAL', 'OBEROIRLTY', 'SBICARD', 'GAIL', 'BANDHANBNK', 'TORNTPHARM', 'WHIRLPOOL', 'BAJAJ-AUTO', 'ACC', 'BERGEPAINT', 'ASIANPAINT', 'NAUKRI', 'HEROMOTOCO', 'HONAUT', 'MGL', 'AUROPHARMA', 'ZEEL', 'LUPIN', 'AARTIIND', 'UPL', 'GODREJCP', 'ZYDUSLIFE', 'TRENT', 'PERSISTENT', 'SUNTV', 'EICHERMOT', 'BAJAJFINSV', 'COFORGE', 'ASTRAL', 'GRASIM', 'ICICIPRULI', 'RECLTD', 'INDUSINDBK', 'NTPC', 'SBILIFE', 'NESTLEIND', 'DABUR', 'GLENMARK', 'RELIANCE', 'AMBUJACEM', 'TATACONSUM', 'TITAN', 'IGL', 'ASHOKLEY', 'IPCALAB', 'COALINDIA', 'ONGC', 'PFC', 'COROMANDEL', 'BHARATFORG', 'MARICO', 'HINDUNILVR', 'PIDILITIND', 'APOLLOTYRE', 'GUJGASLTD', 'MOTHERSON', 'LALPATHLAB', 'ESCORTS', 'BIOCON', 'APOLLOHOSP', 'DIVISLAB', 'CIPLA', 'MRF', 'LAURUSLABS', 'SRF', 'BHARTIARTL']

    # futureContracts = []
    # for i in fno:
    #     if(checkContract(i) == True):
    #         futureContracts.append(i)
    #

print("*********** Contracts greater than 1.5 times of previous ********")
# fno = ['SUNTV', 'ABFRL']
allstks = fno
futureContracts = []
cons = NoOfContracts()

for i in allstks:
    if(cons.checkContract(i) == True):
        futureContracts.append(i)

print(futureContracts)
