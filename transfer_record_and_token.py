from eos.cleos import MyCleos

APIKEY = '5b4added-e80c-41fb-b5a9-16269d2de79b'
ENDPOINT = 'https://open-api.eos.blockdog.com'

ce = MyCleos(ENDPOINT, APIKEY)

# 获取账户的转账记录
result = ce.third_get_account_transfer(account_name='farss5555555')
print(result)

# 获取账户的所有代币及余额
result = ce.third_get_account_tokens(account_name='farss5555555')
print(result)
