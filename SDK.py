import requests

class Speechly:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://157.245.133.112:500/'
        self.headers = {'Authorization': 'Bearer ' + self.api_key}

    def post(self, url, data):
        return requests.post(self.base_url + url, data=data, headers=self.headers)

    def get(self, url):
        return requests.get(self.base_url + url, headers=self.headers)




