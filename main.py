import requests
import random
import OwenWilsonAPI
import StrangerThingsAPI
import BreakingBadAPI


def main():
   #Proxy Class
   
   OWapi = OwenWilsonAPI.OwenWilsonAPI()
   resultsOwen = OWapi.get()
   
  
   STapi = StrangerThingsAPI.StrangerThingsAPI()
   resultsStrangerThings = STapi.get()
   
   BBapi = BreakingBadAPI.BreakingBadAPI()
   resultsBreakingBad = BBapi.get()
  
   print('1) Owen Wilson')
   print('2) Stranger Things')
   print('3) Breaking Bad') 
   answer = int(input("Choose between an Owen Wilson, Stranger Things, or Breaking Bad quote \n"))

   
  
   if answer == 1:
     print(resultsOwen)
   elif answer == 2:
     print(resultsStrangerThings)
   elif answer == 3:
     print(resultsBreakingBad)
   else: 
     print("Please enter a number 1-3")

main()