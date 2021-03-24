import requests
import bs4 as Beautifulsoup

url = "https://www.nature.com/nature/articles"
response = requests.get(url)
scrape = Beautifulsoup(response.content)
