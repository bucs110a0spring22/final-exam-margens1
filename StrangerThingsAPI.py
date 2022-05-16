import requests

class StrangerThingsAPI:

    def __init__(self):
        '''
        initializes Stranger Things API class
        args: self
        return: nothing
        '''
        self.url = f'https://strangerthings-quotes.vercel.app/api/quotes'


    def get(self):
      '''
      gets the information and sets it to a variable
      args: self
      return: the extracted information
      '''
      r = requests.get(self.url)
      response = r.json()
      return response