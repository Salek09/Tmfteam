RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

banner = f"""
  {GREEN}                    
  
  _____ __  __ ___   _____ ___   _   __  __ 
 |_   _|  \/  | __| |_   _| __| /_\ |  \/  |
   | | | |\/| | _|    | | | _| / _ \| |\/| |
   |_| |_|  |_|_|     |_| |___/_/ \_\_|  |_|
                                            

                                            

  ð˜›ð˜°ð˜°ð˜­ ð˜£ð˜º ð˜šð˜ˆð˜ð˜ˆð˜Žð˜Œ
  ð˜›ð˜Œð˜“ð˜Œð˜Žð˜™ð˜ˆð˜” ð˜Šð˜ð˜ˆð˜•ð˜•ð˜Œð˜“ - @ð—¦ð—®ð˜ƒð—®ð—´ð—²ð˜…25  """

print(banner)

import requests

#Telegram channel :- t.m/savagex25 

url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"
number = input("Enter phone number: ")  # Assuming you get the phone number as input

headers = {
    "X-KM-User-AspId": "100012345612345",
    "X-KM-User-Agent": "ANDROID/1152",
    "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
    "X-KM-Accept-language": "bn",
    "X-KM-AppCode": "01",
}

params = {"msisdn": number}

response = requests.get(url, headers=headers, params=params)

print(response.text)
