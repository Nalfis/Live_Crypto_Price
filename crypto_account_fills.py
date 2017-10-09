# Requires python-requests. Install with pip:
#
#   pip install requests
#
# or, with easy-install:
#
#   easy_install requests

import json, hmac, hashlib, time, requests, base64, yaml
from requests.auth import AuthBase

# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request


with open("crypto.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


api_url = cfg['url']['gdax']
API_KEY = cfg['auth']['api_key']
API_SECRET = cfg['auth']['api_sec']
API_PASS = cfg['auth']['pass_ph']
auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)

# Get accounts
accounts = requests.get(api_url + 'accounts', auth=auth)
recent_fills = requests.get(api_url + 'fills', auth=auth)
coins = accounts.json()
fills = recent_fills.json()

print json.dumps(fills, indent=4)

def buys_by_date():
    for x, y in groupby(fills, key=lambda v: v['side']):
        for k, v in groupby(y, key=lambda x: x['created_at'][:10]):
            print {'date': k+'', 'fee': sum(float(d['fee'])for d in v), 'side': x}





#print json.dumps(coins, indent=4, sort_keys=True)
#print json.dumps(recent_fills, indent =4, sort_keys=True)

def current_ltc():
    for key, currency in enumerate((c['currency'], c['balance']) for c in coins):
        if currency[0] == 'LTC':
            global current_ltc_quant
            current_ltc_quant = currency[1]
        if currency[0] == 'USD':
            current_usd = currency[1]


def current_price():
    while True:
        get_LTC_price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD')
        if get_LTC_price.status_code != 200:
            print "Something is wrong with the URL or the API-Get request"
        else:
            current_ltc()
            live_LTC = get_LTC_price.json()
            stdout.write("\rLive Price: %s Current Value of Total LTC holdings: %s" %
                         ('${:0,.2f}'.format(live_LTC['USD']), '${:0,.2f}'.format(live_LTC['USD'] *
                                                                                  (float(current_ltc_quant)))))
            stdout.flush()
            time.sleep(2)


if __name__ == "__main__":
    print json.dumps(recent_fills, indent=4, sort_keys=True)
    #buys_by_date()
    #current_price()
    
    
# Place an order
# order = {
#     'size': 1.0,
#     'price': 1.0,
#     'side': 'buy',
#     'product_id': 'BTC-USD',
# }
# r = requests.post(api_url + 'orders', json=order, auth=auth)
# print r.json()
# {"id": "0428b97b-bec1-429e-a94c-59992926778d"}
