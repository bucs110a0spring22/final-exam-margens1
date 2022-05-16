import requests


class BreakingBadAPI:

    def __init__(self):
        '''
        initializes Breaking Bad API class
        args: self
        return: nothing
        '''
        self.url = f'https://breaking-bad-quotes.herokuapp.com/v1/quotes'


    def get(self):
      '''
      gets the information and sets it to a variable
      args: self
      return: the extracted information
      '''
      r = requests.get(self.url)
      data_extracted = r.json()
      return data_extracted