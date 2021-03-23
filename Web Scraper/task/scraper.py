import requests
from bs4 import BeautifulSoup

url = input("Input the URL:\n")
req = requests.get(url)
if req.status_code != 200:
    print(f"The URL returned {req.status_code}")
else:
    with open('source.html', 'wb') as scraped:
        scraped.write(req.content)
    print("\nContent saved.")
"""    soup = BeautifulSoup(req.content, 'html.parser')
    title = soup.find('meta', property='og:title')
    desc = soup.find('meta', property="og:description")
    output["title"] = title["content"]
    output["description"] = desc["content"]"""
