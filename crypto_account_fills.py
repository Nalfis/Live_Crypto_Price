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
ramon = accounts.json()
#print json.dumps(accounts.json(), indent=4, sort_keys=True)

for key in ramon[1]:
    print ramon[0][key][1]

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
