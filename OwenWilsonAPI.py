import requests


class OwenWilsonAPI:

    def __init__(self):
        '''
        initializes Owen Wilson API class
        args: self
        return: nothing
        '''
        self.url = f'https://owen-wilson-wow-api.herokuapp.com/wows/random'


    def get(self):
      '''
      gets the information and sets it to a variable
      args: self
      return: the extracted information
      '''
      r = requests.get(self.url)
      response = r.json()
      return response
      '''
      if response.get('movie'):
        return response['movie']
      else:
        return None
      '''
      

 

