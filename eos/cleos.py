import requests
from eospy.cleos import Cleos
from eospy.dynamic_url import DynamicUrl


class CustomDynamicUrl(DynamicUrl):
    def __init__(self, url='http://localhost:8888', headers=None, version='v1', cache=None):
        super(CustomDynamicUrl, self).__init__(url, version, cache)
        self.headers = headers

    def _(self, name):
        return CustomDynamicUrl(url=self._baseurl, headers=self.headers, version=self._version,
                                cache=self._cache + [name])

    def get_url(self, url, params=None, json=None, timeout=30):
        # get request
        r = requests.get(url, params=params, json=json, headers=self.headers, timeout=timeout)
        r.raise_for_status()
        return r.json()

    def post_url(self, url, params=None, json=None, data=None, timeout=30):
        # post request
        r = requests.post(url, params=params, json=json, headers=self.headers, data=data, timeout=timeout)
        try:
            r.raise_for_status()
        except:
            raise requests.exceptions.HTTPError(response=r.json())
        return r.json()


class MyCleos(Cleos):

    def __init__(self, url='http://localhost:8888', apikey=None, version='v1'):
        ''' '''
        self._prod_url = url
        # self._wallet_url = wallet_url
        self._version = version
        headers = None
        if apikey is not None:
            headers = {"apikey": apikey}
        self._dynurl = CustomDynamicUrl(url=self._prod_url, headers=headers, version=self._version)

    def third_get_transaction(self, trans_id, timeout=30):
        '''
        POST /v1/third/get_transaction
        {"id":"abcd1234"}
        '''
        return self.post('third.get_transaction', params=None, json={'id': trans_id}, timeout=timeout)

    def third_get_account_transfer(self, account_name=None, code=None, symbol=None, _type=3, _from=None, to=None,
                                   start_block_num=None, end_block_num=None, start_block_time=None, end_block_time=None,
                                   sort=1, size=10, page=1):
        '''
        POST v1/third/get_account_transfer
        '''
        data = {
            'account_name': account_name,
            'code': code,
            'symbol': symbol,
            'type': _type,
            'from': _from,
            'to': to,
            'start_block_num': start_block_num,
            'end_block_num': end_block_num,
            'start_block_time': start_block_time,
            'end_block_time': end_block_time,
            'sort': sort,
            'size': size,
            'page': page
        }
        return self.post('third.get_account_transfer', params=None, json=data, timeout=30)

    def third_get_account_tokens(self, account_name):
        '''
        POST v1/third/get_account_tokens
        '''
        data = {
            'account_name': account_name
        }
        return self.post('third.get_account_tokens', params=None, json=data, timeout=30)
