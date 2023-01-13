import requests
import pandas as pd
import tabulate
from nsepython import *
from stocks.Ohlc_check import Ohlc_check
from stocks.CheckYestHighLow import CheckYestHighLow
from stocks.SuperTrendInd import SuperTrendInd

# mystocks = ['PNB', 'MCX', 'SAIL', 'TCS', 'BSOFT', 'BEL', 'BALRAMCHIN', 'OFSS', 'VEDL', 'HAVELLS', 'DELTACORP', 'TECHM', 'BATAINDIA', 'SBIN', 'RAIN', 'WIPRO', 'CANBK', 'GMRINFRA', 'INFY', 'MARUTI', 'INDHOTEL', 'CHOLAFIN', 'JUBLFOOD', 'LTIM', 'TATASTEEL', 'SHREECEM', 'TVSMOTOR', 'M&M', 'ADANIPORTS', 'FSL', 'HCLTECH', 'FEDERALBNK', 'LTTS', 'WHIRLPOOL', 'MGL', 'AUROPHARMA', 'AARTIIND', 'PERSISTENT', 'EICHERMOT', 'ASTRAL', 'ICICIPRULI', 'NESTLEIND', 'DABUR', 'TITAN', 'GUJGASLTD']
mystocks =['JSWSTEEL','HINDALCO','JINDALSTEL','CANBK','MAXHEALTH','APLAPOLLO','HCLTECH','DABUR','TATACONSUM','AXISBANK','ITC','BHARTIARTL']
############### CHECK YESTERTDAY HIGH - BUY##################
chkHighLow = CheckYestHighLow()
breaks1dayhigh = chkHighLow.checkYestHigh(mystocks)
print("")
print("*********** Breaks yesterday HIGH - BUYSIDE ********")
print(breaks1dayhigh)
print("")
############### CHECK YESTERTDAY LOW ##################
breaks1daylow = chkHighLow.checkYestLow(mystocks)
print("*********** Breaks yesterday LOW - SELLSIDE*********")
print(breaks1daylow)
print("")

############### SUPERTREND #############################
print("*********** SuperTrend ********")
stObj = SuperTrendInd()
allPSuperTrendStks = []
allNSuperTrendStks = []
allStocks = breaks1daylow + breaks1dayhigh
for i in allStocks:
    st = stObj.allSuperTrends(i)
    if st == "allPositive":
        allPSuperTrendStks.append(i)
    elif st == "allNegative":
        allNSuperTrendStks.append(i)
    else:
        pass


print("*********** Positive all-15,D SuperTrend ********")
print(allPSuperTrendStks)
print("*********** Negative all-15,D SuperTrend ********")
print(allNSuperTrendStks)
