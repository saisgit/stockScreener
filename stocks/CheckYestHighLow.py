import urllib
from nsetools import Nse
import yfinance as yf

import numpy as np
import pandas as pd
class CheckYestHighLow():
    def checkYesterday(self,stockCode,signal):
        #stockCode = "BSOFT"
        period="3d"
        duration="1d" #Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
        totalStock = []
        try:
            proxyServer = urllib.request.getproxies()['http']
        except KeyError:
            proxyServer = ""

        data = yf.download(
                            tickers=stockCode+".NS",
                            period=period,
                            interval=duration,
                            proxy=proxyServer,
                            progress=False,
                            timeout=10
                        )
        data.reset_index(inplace=True)
        # data.sort_values(by=['Datetime'], ascending=False, inplace=True)
        data.sort_values('Date', inplace=True)
        # print(data.columns)
        data.set_index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
        data.reset_index(inplace=True)
        data.sort_values(by=['Date'],ascending=False,inplace = True)
        for i in range(1,3):
            #data['open_'+str(i)+'day_ago'] = data['Open'].shift(-i)
            data['high_'+str(i)+'day_ago'] = data['High'].shift(-i)
            data['low_'+str(i)+'day_ago'] = data['Low'].shift(-i)
            #data['close_'+str(i)+'day_ago'] = data['Close'].shift(-i)
        pd.set_option('display.max_columns', None)
        ltp = round(data['Close'][2],2)
        low_1day_ago = round(data['low_1day_ago'][2],2)
        low_2day_ago = round(data['low_2day_ago'][2],2)
        high_1day_ago = round(data['high_1day_ago'][2],2)
        high_2day_ago = round(data['high_2day_ago'][2],2)
        if(signal == 'sell'):
            # if ((ltp < low_1day_ago) & (low_1day_ago < low_2day_ago)):
            #     return 'breaks2daylow'
            if(ltp < low_1day_ago):
                return 'breaks1daylow'
            else:
                return 'no'
        else:
            # if ((ltp > high_1day_ago) & (high_1day_ago > high_2day_ago)):
            #     return 'breaks2dayhigh'
            if (ltp > high_1day_ago):
                return 'breaks1dayhigh'
            else:
                return 'no'


    def checkYestHigh(self,buy):
        ############### CHECK YESTERTDAY HIGH ##################
        breaks1dayhigh = []
        for i in buy:
            chk = CheckYestHighLow.checkYesterday(self,i,"buy")
            if (chk == "breaks1dayhigh"):
                breaks1dayhigh.append(i)
        return breaks1dayhigh

    def checkYestLow(self,sell):
    ############### CHECK YESTERTDAY LOW ##################
        breaks1daylow = []
        for i in sell:
            chk = CheckYestHighLow.checkYesterday(self,i, "sell")
            if (chk == "breaks1daylow"):
                breaks1daylow.append(i)
        return breaks1daylow

