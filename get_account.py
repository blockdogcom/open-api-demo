from eos.cleos import MyCleos

APIKEY = '5b4added-e80c-41fb-b5a9-16269d2de79b'
ENDPOINT = 'https://open-api.eos.blockdog.com'

ce = MyCleos(ENDPOINT, APIKEY)


result = ce.get_account('binancecold1')
print('账户名', result['account_name'])
print('创建时间', result['created'])
print('可流通的EOS数量', result['core_liquid_balance'])
print(f"NET情况: 已用 {result['net_limit']['used']}, 可用 {result['net_limit']['available']}, 最大 {result['net_limit']['max']}")
print(f"CPU情况: 已用 {result['cpu_limit']['used']}, 可用 {result['cpu_limit']['available']}, 最大 {result['cpu_limit']['max']}")

print(f"资源情况: NET {result['total_resources']['net_weight']}, CPU {result['total_resources']['cpu_weight']}, "
      f"RAM {result['total_resources']['ram_bytes']} BYTE")

print(f"自抵押: NET {result['self_delegated_bandwidth']['net_weight']}, CPU {result['self_delegated_bandwidth']['cpu_weight']}")