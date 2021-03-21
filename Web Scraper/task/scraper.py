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
    title = soup.find('meta', property='og:title')
    desc = soup.find('meta', property="og:description")
    print(title['content'], desc['content'])
    """
    movie = json.loads(json_data.contents[0])
    output['title'] = movie["name"]
    output["description"] = movie["trailer"]["description"]
    print(output)



"""
