import urllib.request
import json
import time
import winsound

url = "https://ddda.lennardf1989.com/api/v2/grace/Steam"

while True:
    data = json.load(urllib.request.urlopen(url))
    print(data, "\n")
    if data['grace'] in ("yes", "maybe"):
        for i in range(8):
            print("Grace Period!")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        time.sleep(1200)
    else:
        print("Not Grace Period!")
    time.sleep(120)
