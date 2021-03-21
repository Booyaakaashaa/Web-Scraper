import requests

from bs4 import BeautifulSoup

num = int(input())
url = input()
pyg = requests.get(url)

soup = BeautifulSoup(pyg.content, 'html.parser')
print(soup.find_all('a', limit=num)[num - 1].get('href'))
