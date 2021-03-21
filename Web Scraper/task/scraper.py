import requests
from bs4 import BeautifulSoup

import json

output = {}
url = input("Input the URL:\n")
req = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
if req.status_code != 200 or "imdb" not in url:
    print("Invalid movie page!")
else:
    soup = BeautifulSoup(req.content, 'html.parser')
    json_data = soup.find('script', type="application/ld+json")
    movie = json.loads(json_data.contents[0])
    output['title'] = movie["name"]
    output["description"] = movie["description"]
    #print(quote.get("content", "Invalid quote resource!"))
    print(output)



