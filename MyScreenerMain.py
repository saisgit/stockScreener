import requests
import pandas as pd
import tabulate
from nsepython import *
from stocks.Ohlc_check import Ohlc_check
from stocks.CheckYestHighLow import CheckYestHighLow
from stocks.SuperTrendInd import SuperTrendInd

print("*************** nifty change  **************")
print(nse_marketStatus()['marketState'][0]['percentChange'])
positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
endp = len(positions['data'])
print("*************** BUY **************")
Ohlc = Ohlc_check()
buy, buytable = Ohlc.openLowBuy(endp, positions)
print(tabulate.tabulate(buytable, headers=["Symbol", "Open", "ChangePts", "Pcnt"], tablefmt="pretty"))

print("*************** SELL **************")
sell, selltable = Ohlc.openHighSell(endp, positions)
print(tabulate.tabulate(selltable, headers=["Symbol", "Open", "ChangePts", "Pcnt"], tablefmt="pretty"))

print(buy)
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

# allstks = buy + sell
# # PSuperTrendStks = []
# # NSuperTrendStks = []
# # for i in allstks:
# #     st = superTrendDay(i)
# #     if(st == "Positive"):
# #         PSuperTrendStks.append(i)
# #     elif(st == "Negative"):
# #         NSuperTrendStks.append(i)
# #     else:
# #         pass
#
#
# # print("*********** Positive D SuperTrend ********")
# # print(PSuperTrendStks)
# # print("*********** Negative D SuperTrend ********")
# # print(NSuperTrendStks)
#
# # print("*********** Contracts greater than 1.5 times of previous ********")
# # fno = ['SUNTV', 'ABFRL']
# # allstks = buy + sell
# # futureContracts = []
# # for i in allstks:
# #     if(checkContract(i) == True):
# #         futureContracts.append(i)
# #
# # print(futureContracts)
# # ['TATACOMM', 'NMDC', 'IOC', 'HINDPETRO', 'SIEMENS', 'ABCAPITAL', 'MPHASIS', 'MCX', 'PEL', 'BPCL', 'SUNPHARMA', 'METROPOLIS', 'BALRAMCHIN', 'GRANULES', 'GMRINFRA', 'JKCEMENT', 'COALINDIA', 'BHARATFORG', 'ESCORTS', 'BIOCON', 'APOLLOHOSP', 'CIPLA', 'LAURUSLABS', 'SRF', 'BHARTIARTL']
#
