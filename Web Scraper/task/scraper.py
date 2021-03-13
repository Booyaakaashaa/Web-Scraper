import requests
import json

url = input("Input the URL:\n")
req = requests.get(url)

if req.status_code != 200:
    print("Invalid quote resource!")
