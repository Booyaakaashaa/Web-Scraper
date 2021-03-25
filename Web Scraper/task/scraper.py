import requests
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
article_data = soup.find_all("span", string="News")
for article in article_data:
    source = article.parent.parent.parent.parent.parent
    link = "https://www.nature.com" + str(source.find('a', {"data-track-action": "view article"})["href"])
    link_data = requests.get(link)
    new_soup = BeautifulSoup(link_data.content, 'html.parser')
    file_name = new_soup.title.string
    underscore = file_name.maketrans(" ", "_")
    file_name = file_name.translate(underscore)
    with open(f"{file_name}.txt", "wb") as output:
        output.write(bytes(new_soup.get_text(), encoding="utf-8"))





