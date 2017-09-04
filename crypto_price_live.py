import requests
import time
from sys import stdout

# put the number of coins and the price based on the date as below
LTC_holdings = {"2014-03-22": 2.4994, "2017-09-01": 2.5}
LTC_price = {"2014-03-22": 15.81, "2017-09-01": 79.24}

sum_holdings = 0
sum_price = 0

# print a summary of what you have before you calculate current market value
print "*" * 80
for item in LTC_holdings.iterkeys():
    print "Bought or Mined: %s LTC's on %s @ %s for a total of: %s" \
          % (LTC_holdings[item], item,
             '${:0,.2f}'.format(LTC_price[item]),
             '${:0,.2f}'.format(LTC_holdings[item] * LTC_price[item]))
    sum_holdings += LTC_holdings[item]
    sum_price += LTC_price[item] * LTC_holdings[item]
print "Total Number of LTC's: %s" % sum_holdings
print "Total Value of LTC's: %s" % '${:0,.2f}'.format(sum_price)

print "*" * 80
# getting realtime price of litecoin and display
while True:
    get_LTC_price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD')
    if get_LTC_price.status_code != 200:
        print "Something is wrong with the URL or the API-Get request"
    else:
        live_LTC = get_LTC_price.json()
        stdout.write("\rLive Price: %s -:- Current Value of Total LTC holdings: %s" %
                     ('${:0,.2f}'.format(live_LTC['USD']), '${:0,.2f}'.format(live_LTC['USD']*sum_holdings)))
        stdout.flush()
        time.sleep(3)
