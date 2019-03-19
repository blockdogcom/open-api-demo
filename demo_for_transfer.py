import datetime as dt
import time

import pytz
import requests
from eospy.keys import EOSKey

from eos.cleos import MyCleos

APIKEY = '5b4added-e80c-41fb-b5a9-16269d2de79b'
ENDPOINT = 'https://open-api.eos.blockdog.com'
PRIVATE_KEY = '5JWSqcrgN3ScgrF1t1Jz4wrm4BJA39wzY3K6gBU8h4JXdBnX5CP'

ce = MyCleos(ENDPOINT, APIKEY)

_from = 'sssss5555555'
_to = 'sssss5555551'
arguments = {
    "from": _from,  # sender
    "to": _to,  # receiver
    "quantity": '0.0001 EOS',  # In EOS
    "memo": "EOS to the moon",
}

payload = {
    "account": "eosio.token",
    "name": "transfer",
    "authorization": [{
        "actor": _from,  # sender
        "permission": "active",
    }],
}

# Converting payload to binary
data = ce.abi_json_to_bin(payload['account'], payload['name'], arguments)
# Inserting payload binary form as "data" field in original payload
payload['data'] = data['binargs']

trx = {
    "actions": [payload],
    'expiration': str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))
}

resp = ce.push_transaction(trx, EOSKey(PRIVATE_KEY), broadcast=True)
transaction_id = resp['transaction_id']
print('trx_id:', resp['transaction_id'])

# waiting for transaction excueting
while True:
    try:
        result = ce.third_get_transaction(transaction_id)
        print(result)
        break
    except requests.exceptions.HTTPError as e:
        if e.response['error'] == 'transaction not found':
            time.sleep(1)
