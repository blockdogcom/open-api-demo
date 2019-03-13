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
