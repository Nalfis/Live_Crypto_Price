import requests
import time
from sys import stdout
import yaml

# put the number of coins and the price based on the date as below

# LTC_holdings = {"2014-03-22": 2.4994, "2017-09-01": 2.5}
# LTC_price = {"2014-03-22": 15.81, "2017-09-01": 79.24}
LTC_holdings = {"2017-09-10": 5.5005116}
LTC_price = {"2017-09-10": 70.60}

# read from yaml file config settings

with open("crypto_price_live.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

sum_holdings = 0
sum_price = 0
url = cfg['url']['gdax']

# # print a summary of what you have before you calculate current market value

print "*" * 80
for item in sorted(LTC_holdings.iterkeys()):
    print "Bought or Mined: %s LTC's on %s @ %s for a total of: %s" \
          % (LTC_holdings[item], item,
             '${:0,.2f}'.format(LTC_price[item]),
             '${:0,.2f}'.format(LTC_holdings[item] * LTC_price[item]))
    sum_holdings += LTC_holdings[item]
    sum_price += LTC_price[item] * LTC_holdings[item]
print "Total Number of LTC's: %s" % sum_holdings
print "Average Price of LTC's %s" % '${:0,.2f}'.format(sum_price/sum_holdings)
print "Total Price of LTC's: %s" % '${:0,.2f}'.format(sum_price)
print "*" * 80

# getting realtime price of LTC-USD from gdax

while True:

    get_LTC_price = requests.get(url)

    if get_LTC_price.status_code != 200:
        print "Something is wrong with the URL or the API-Get request"
        break
    else:
        live_LTC = get_LTC_price.json()
        stdout.write("\rLive Price: %s -:- Current Value of Total LTC holdings: %s -:- Net Gain/Loss: %s" %
                     ('${:0,.2f}'.format(float(live_LTC['price'])),
                      '${:0,.2f}'.format(float(live_LTC['price'])*sum_holdings),
                      '${:0,.2f}'.format((float(live_LTC['price']) * sum_holdings) - sum_price)
                      )
                     )
        stdout.flush()
        time.sleep(cfg['sleeptime'])