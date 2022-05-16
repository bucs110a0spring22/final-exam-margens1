import requests
import random


class OwenWilsonAPI:

    def __init__(self):
        self.url = f'https://owen-wilson-wow-api.herokuapp.com/wows/random'


    def get(self):
      r = requests.get(self.url)
      data_extracted = r.json()
      return data_extracted

 

