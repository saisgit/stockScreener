# try:
    # import requests
# except (ModuleNotFoundError, ImportError):
    # print("requests module not found")
    # os.system(f"{sys.executable} -m pip install -U requests")
# finally:
    # import requests

# try:
    # import pandas as pd
# except (ModuleNotFoundError, ImportError):
    # print("pandas module not found")
    # os.system(f"{sys.executable} -m pip install -U pandas")
# finally:
    # import pandas as pd
	
# try:
    # from bs4 import BeautifulSoup
# except (ModuleNotFoundError, ImportError):
    # print("BeautifulSoup module not found")
    # os.system(f"{sys.executable} -m pip install -U beautifulsoup4")
# finally:
    # from bs4 import BeautifulSoup
import sys
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
# Keep module imports prior to classes
#colA = sys.argv[1]
#colB = sys.argv[2]
#colC = sys.argv[3]
#colD = sys.argv[4]

Charting_Link = "https://chartink.com/screener/"
Charting_url = 'https://chartink.com/screener/process'

#You need to copy paste condition in below mentioned Condition variable

#Condition = "( {57960} ( [0] 15 minute close > [-1] 15 minute max ( 20 , [0] 15 minute close ) and [0] 15 minute volume > [0] 15 minute sma ( volume,20 ) ) ) "


# Condition = "( {33489} ( latest volume > latest sma( latest volume , 10 ) * 2 ) )" 
NR7Condition = "( {33489} ( 1 day ago high - 1 day ago low < 2 days ago high - 2 days ago low and 1 day ago high - 1 day ago low < 3 days ago high - 3 days ago low and 1 day ago high - 1 day ago low < 4 days ago high - 4 days ago low and 1 day ago high - 1 day ago low < 5 days ago high - 5 days ago low and 1 day ago high - 1 day ago low < 6 days ago high - 6 days ago low and 1 day ago high - 1 day ago low < 7 days ago high - 7 days ago low ) )" 

NR7Condition_not = "( {33489} ( ( {33489} not ( 1 day ago high - 1 day ago low < 2 days ago high - 2 days ago low and 1 day ago high - 1 day ago low < 3 days ago high - 3 days ago low and 1 day ago high - 1 day ago low < 4 days ago high - 4 days ago low and 1 day ago high - 1 day ago low < 5 days ago high - 5 days ago low and 1 day ago high - 1 day ago low < 6 days ago high - 6 days ago low and 1 day ago high - 1 day ago low < 7 days ago high - 7 days ago low ) ) ) )"

NegativeST = "({33489}(latest close<latest supertrend(7,3)))"
NSma = "({33489}(latest close<latest sma(latest close,55)))"
PositiveST = "({33489}(latest close>latest supertrend(7,3)))"
PSma = "({33489}(latest close>latest sma(latest close,55)))"

#def GetDataFromChartink(payload):
#    payload = {'scan_clause': payload}
#    
#    with requests.Session() as s:
#        r = s.get(Charting_Link)
#        soup = BeautifulSoup(r.text, "html.parser")
#        csrf = soup.select_one("[name='csrf-token']")['content']
#        s.headers['x-csrf-token'] = csrf
#        r = s.post(Charting_url, data=payload)
#        df = pd.DataFrame()
#        for item in r.json()['data']:
#            #print(item['nsecode'])
#            df = df.append(item, ignore_index=True)
#            #df2 = pd.concat([df, pd.DataFrame.from_records([item])])
#            #df = pd.concat([df, df2])
#    return df


#data = GetDataFromChartink(Condition)

#data = data.sort_values(by='per_chg', ascending=False)

#print(data['nsecode'])
#fno = data['nsecode'].values.tolist()
def GetDataFromChartink(Condition):
    Condition = {'scan_clause': Condition}
    #flist = []
    with requests.Session() as s:
        r = s.get(Charting_Link)
        soup = BeautifulSoup(r.text, "html.parser")
        csrf = soup.select_one("[name='csrf-token']")['content']
        s.headers['x-csrf-token'] = csrf
        r = s.post(Charting_url, data=Condition)
        #print(r.json()['data'])
        # df = pd.DataFrame()
        df = pd.DataFrame(r.json()['data'])
        # for item in r.json()['data']:
            # df2 = pd.DataFrame(item)
            # #df = df.append(item, ignore_index=True)
            # df = pd.concat([df,df2], axis= 1)
            # flist.append(item['nsecode'])
    return df


NR7df = GetDataFromChartink(NR7Condition)
NR7df['nr7_data'] = 'NR7'
nr7df2 = NR7df[['nsecode','nr7_data']]

N_NR7df = GetDataFromChartink(NR7Condition_not)
N_NR7df['nr7_data'] = ' '
n_nr7df2 = N_NR7df[['nsecode','nr7_data']]

finalNR7Df = pd.concat([nr7df2,n_nr7df2])

ndf = GetDataFromChartink(NegativeST)
ndf['strend'] = 'Negative'
ndf2 = ndf[['nsecode','strend']]

pdf = GetDataFromChartink(PositiveST)
pdf['strend'] = 'Positive'
pdf2 = pdf[['nsecode','strend']]

finalTrendDf = pd.concat([ndf2,pdf2])

nsma_df = GetDataFromChartink(NSma)
nsma_df['SMA55'] = 'Below'
nsma_df2 = nsma_df[['nsecode','SMA55']]

psma_df = GetDataFromChartink(PSma)
psma_df['SMA55'] = 'Above'
psma_df2 = psma_df[['nsecode','SMA55']]

finalSMADf = pd.concat([nsma_df2,psma_df2])

FDF = pd.merge(finalTrendDf, finalSMADf, how='inner', on = 'nsecode')
finalResult = pd.merge(FDF, finalNR7Df, how='inner', on = 'nsecode')

ff = finalResult#[:4]
colA = 'stock'
colB = 'strend'
colC = 'MA55'
colD = 'NR7_data'

fnolist = ff['nsecode'].values.tolist()
for i in fnolist:
    colA += ","+ff[ff['nsecode']==i].values[0][0]
    colB += ","+ff[ff['nsecode']==i].values[0][1]
    colC += ","+ff[ff['nsecode']==i].values[0][2]
    colD += ","+ff[ff['nsecode']==i].values[0][3]

#print(flist)
#print(len(flist))
#for i in flist:
#	colA += ","+i


print(colA)
print(colB)
print(colC)
print(colD)

#data.to_csv("Chartink_result.csv")