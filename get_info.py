from eos.cleos import MyCleos

APIKEY = '5b4added-e80c-41fb-b5a9-16269d2de79b'
ENDPOINT = 'https://open-api.eos.blockdog.com'

ce = MyCleos(ENDPOINT, APIKEY)

# 获取区块信息
result = ce.get_info()
print('链ID', result['chain_id'])
print('最新区块高度', result['head_block_num'])
print('最新区块时间', result['head_block_time'])

print('最新不可逆区块高度', result['last_irreversible_block_num'])
