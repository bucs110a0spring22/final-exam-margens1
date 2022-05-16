import requests
import OwenWilsonAPI
import StrangerThingsAPI
import BreakingBadAPI


def main():
   '''
   Asks the user to choose between three options and returns a quote from one of the three
   args: None
   return: None
   '''
   
   OWapi = OwenWilsonAPI.OwenWilsonAPI()
   resultsOwen = OWapi.get()
   resultsOwen = resultsOwen[0]
  
   STapi = StrangerThingsAPI.StrangerThingsAPI()
   resultsStrangerThings = STapi.get()
   resultsStrangerThings = resultsStrangerThings[0]
   
   BBapi = BreakingBadAPI.BreakingBadAPI()
   resultsBreakingBad = BBapi.get()
   resultsBreakingBad = resultsBreakingBad[0]

   
   print('1) Owen Wilson')
   print('2) Stranger Things')
   print('3) Breaking Bad') 
   answer = int(input("Choose between an Owen Wilson, Stranger Things, or Breaking Bad quote \n"))


   if answer == 1:
     for q in resultsOwen:
        print(q, ':', resultsOwen.get(q))
   elif answer == 2:
     for q in resultsStrangerThings:
        print(q, ':', resultsStrangerThings.get(q)) 
   elif answer == 3:
     for q in resultsBreakingBad:
        print(q, ':', resultsBreakingBad.get(q))
   else: 
     print("Please enter a number 1-3")

main()
