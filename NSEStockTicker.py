import requests
from time import sleep

url = "https://latest-stock-price.p.rapidapi.com/price"

querystring = {"Indices":"NIFTY 500","Identifier":"SBINEQN,TRIDENTEQN,ALOKINDSBEN,TATACHEMEQN,TATAPOWEREQN,STLTECHEQN,VEDLEQN,DEEPAKNTREQN,RELIANCEEQN ,INFYEQN ,IEXEQN ,UNOMINDAEQN ,IRCTCEQN,CDSLEQN"}

headers = {
    "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
}
while True:
 response = requests.request("GET", url, headers=headers, params=querystring)
 data = response.json()   #Storing the api data 
 dataSize = len(data)     #How big is json data
 
 if(0 < dataSize):    # only printing if we have any data
  print("*********Ambani Portfolio*********")
  print("")
 
  for i in range(0 , dataSize):    #loop through every stock
   string = [data[i]['symbol'],str(data[i]['lastPrice'])]
   print(': '.join(string) + " Rupees")
 
  print("")
  print("Last Updated- " + data[0]['lastUpdateTime'])
 else:
  print("Data is being Updating.....")
 
 sleep(20)  #sleep for 20 sec
