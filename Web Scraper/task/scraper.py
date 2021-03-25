import requests
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
article_data = soup.find_all("News")



