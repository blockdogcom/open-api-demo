import time

import requests
from eospy.keys import EOSKey

from eos.cleos import MyCleos

APIKEY = '5b4added-e80c-41fb-b5a9-16269d2de79b'
ENDPOINT = 'https://open-api.eos.blockdog.com'
ce = MyCleos(ENDPOINT, APIKEY)

# 创建 EOS 账号需要已有一个 EOS 账号
creator = 'farss5555555'
creator_private_key = '5JWSqcAgN3ScgRF1O1Jz4wrm4BJA39wzB3K6gBU8h4JXdBmX5CP'

# 创建账号首先需要秘钥对, 创建一个秘钥对
# 如果有安装 cleos, 直接用 cleos create key --to-console 创建秘钥对
# 或者使用其他工具生成, 比如 https://github.com/eoscafe/eos-key
# 或者使用代码生成, 如下:
key = EOSKey()
print('public key:', key.to_public())
print('请妥善保管你的 private key:', key.to_wif())

public_key = key.to_public()
new_name = 'farsssssssss'  # 新账户名

# 创建用户并为新用户抵押 net, cpu, 购买内存
try:
    resp = ce.create_account(creator, creator_private_key, new_name, owner_key=public_key, active_key='',
                             stake_net='0.0010 EOS', stake_cpu='0.0010 EOS', ramkb=8)

    print('trx_id:', resp['transaction_id'])

    time.sleep(10)

    # 等交易完成, 查询新账户信息
    account = ce.get_account(new_name)
    print(account)
except requests.exceptions.HTTPError as e:
    print(e.response)
