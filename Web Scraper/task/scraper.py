import requests
from bs4 import BeautifulSoup

output = {}
url = input("Input the URL:\n")
req = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
if req.status_code != 200 or "imdb" not in url or "name" in url:
    print("Invalid movie page!")
else:
    soup = BeautifulSoup(req.content, 'html.parser')
    title = soup.find('meta', property='og:title')
    desc = soup.find('meta', property="og:description")
    output["title"] = title["content"]
    output["description"] = desc["content"]
    print(output)
