import requests
from bs4 import BeautifulSoup

url = input("Input the URL:\n")
req = requests.get(url)
if req.status_code != 200:
    print(f"The URL returned {req.status_code}")
else:
    with open('file.html', 'wb') as scraped:
        scraped.write(req.content)
        print("Content saved.")
"""    soup = BeautifulSoup(req.content, 'html.parser')
    title = soup.find('meta', property='og:title')
    desc = soup.find('meta', property="og:description")
    output["title"] = title["content"]
    output["description"] = desc["content"]"""
