import requests

from bs4 import BeautifulSoup

word = input()
link = input()

response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')

para = soup.find_all('p')
for p in para:
    if word in p.get_text():
        print(p.get_text())
        break
