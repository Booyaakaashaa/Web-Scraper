import requests
import json

url = input("Input the URL:\n")
req = requests.get(url)

if req.status_code != 200:
    print("Invalid quote resource!")
else:
    json_data = req.text
    quote = json.loads(json_data)
    print(quote.get("content", "Invalid quote resource!"))
    """
    try:
        json_data = req.text
        quote = json.loads(json_data)
        print(quote["content"])
    except KeyError:
        print("Invalid quote resource!")"""
