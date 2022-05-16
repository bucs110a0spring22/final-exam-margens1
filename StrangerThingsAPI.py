import requests

class StrangerThingsAPI:

    def __init__(self):
        self.url = f'https://strangerthings-quotes.vercel.app/api/quotes'


    def get(self):
      r = requests.get(self.url)
      response = r.json()
      return response