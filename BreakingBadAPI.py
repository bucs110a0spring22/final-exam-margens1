import requests
import random


class BreakingBadAPI:

    def __init__(self):
        self.url = f'https://breaking-bad-quotes.herokuapp.com/v1/quotes'


    def get(self):
      r = requests.get(self.url)
      data_extracted = r.json()
      return data_extracted