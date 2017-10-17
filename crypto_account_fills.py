# Requires python-requests. Install with pip:
#
#   pip install requests
#
# or, with easy-install:
#
#   easy_install requests

import json, hmac, hashlib, time, requests, base64, yaml, datetime
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


def get_current_fill(days=0):
    # Get accounts
    fills = requests.get(api_url + 'fills', auth=auth)
    list_fills = fills.json()
    LTC = list_fills
    day = days * - 1
    fill_date = (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y-%m-%d')
    buy_sum_size = 0
    sell_sum_size = 0
    buy_fee = 0
    sell_fee = 0
    buy_sum_price = 0
    sell_sum_price = 0

    for k in LTC:
        if k['product_id'] == "LTC-USD" and k['created_at'][:10] == fill_date and k['side'] == 'buy':
            print "side: {} - size: {} * price ${:,.5f} fee: ${:,.5f} - date: {}".format(k['side'],
                                                                                         k['size'],
                                                                                         float(k['price']),
                                                                                         float(k['fee']),
                                                                                         k['created_at'][:10])
            buy_sum_price += (float(k['size']) * (float(k['price']) + float(k['fee'])))
            buy_sum_size += float(k['size'])
            buy_fee += float(k['fee'])
        if k['product_id'] == "LTC-USD" and k['created_at'][:10] == fill_date and k['side'] == 'sell':
            print "side: {} - size: {} * price ${:,.5f} fee: ${:,.5f} - date: {}".format(k['side'],
                                                                                         k['size'],
                                                                                         float(k['price']),
                                                                                         float(k['fee']),
                                                                                         k['created_at'][:10])
            sell_sum_price += (float(k['size']) * (float(k['price']) + float(k['fee'])))
            sell_sum_size += float(k['size'])
            sell_fee += float(k['fee'])

    if buy_sum_size > 0:
        buy_avg_price = buy_sum_price / buy_sum_size
    else:
        buy_avg_price = 0
    if sell_sum_size > 0:
        sell_avg_price = sell_sum_price / sell_sum_size
    else:
        sell_avg_price = 0

    print "\n\n"
    print "Traded on: {}".format(fill_date)
    print "*" * 45
    print "Total LTC Bought: {:,.5f} \nPrice Paid: ${:,.2f} \nAverage Price Paid: ${:,.2f}".format(buy_sum_size,
                                                                                                   buy_avg_price,
                                                                                                   buy_avg_price)
    print "*" * 45
    print "Total LTC Sold: {:,.5f} \nFor a Total Of: ${:,.2f} \nAverage Price Sold: ${:,.2f}".format(sell_sum_size,
                                                                                                     sell_avg_price,
                                                                                                     sell_avg_price)
    print "*" * 45


if __name__ == '__main__':
    get_current_fill(3)

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