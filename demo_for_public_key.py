from eos.cleos import MyCleos

APIKEY = '5b4added-e80c-41fb-b5a9-16269d2de79b'
ENDPOINT = 'https://open-api.eos.blockdog.com'

ce = MyCleos(ENDPOINT, APIKEY)

# 通过public_key获取相应的EOS账户
public_key = 'EOS8Bt5QkEqmvatosB8Jn86RiCGAXw8zSPCdVdm2NkjbEaEG2nP8J'
accounts = ce.get_accounts(public_key)
print(accounts)
