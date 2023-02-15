from nsepython import *
from colorama import Fore, Back, Style
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', 1000)
print(datetime.datetime.now())
# print(nse_index())
# print(nse_get_index_list())--
my_indices = ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY BANK', 'NIFTY METAL', 'NIFTY FIN SERVICE',
              'NIFTY FMCG', 'NIFTY IT','NIFTY AUTO', 'NIFTY OIL AND GAS', 'NIFTY PHARMA']
# print(nse_get_advances_declines())
# print(nse_get_top_gainers())
# print(nse_get_top_losers())
# it = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index={}'.format('SECURITIES%20IN%20F%26O'))['data'][0]
# print(it)
for index in my_indices:
    urlindex = index.replace(' ', '%20')
    data = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index={}'.format(urlindex))['data'][0]
    symbol = data['symbol']
    pchange = data['pChange']
    if pchange > 0:
        print(Fore.GREEN,symbol,'>>>',  str(pchange))
    else:
        print(Fore.RED,symbol, '>>>', str(pchange))
