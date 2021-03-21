import requests

from bs4 import BeautifulSoup

num = int(input())
link = input()

response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find_all('h2', limit=num + 1)[num].get_text())
