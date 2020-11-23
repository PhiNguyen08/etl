#Import libary
import requests
import json

class Extract:

    def __init__(self):
        self.data_sources = json.load(open('data_config.json'))
        self.api = self.data_sources['data_sources']["api"]

    def getAPIsData(self, api_name):
        api_url = self.api[api_name]
        response = requests.get(api_url)
        return response.json()
