import requests

from bs4 import BeautifulSoup

response = requests.get(input())
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find('h1').get_text())
