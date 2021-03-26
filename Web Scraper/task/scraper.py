import requests
import string
import os
from bs4 import BeautifulSoup

page_num = int(input())
content_type = input()
page = 1
cwd = os.getcwd()
while page <= page_num:
    os.mkdir(f"Page_{page}")
    os.chdir((os.path.join(cwd, f"Page_{page}")))
    url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_data = soup.find_all("span", string=content_type)
    for article in article_data:
        source = article.parent.parent.parent.parent.parent
        link = "https://www.nature.com" + str(source.find('a', {"data-track-action": "view article"})["href"])
        link_data = requests.get(link)
        new_soup = BeautifulSoup(link_data.content, 'html.parser')
        file_name = new_soup.find("meta", {"name": "dc.title"})["content"]
        underscore = file_name.maketrans(" ", "_", string.punctuation)
        file_name = file_name.translate(underscore)
        data = bytes("".join(p.get_text() if p != "\n" else p for p in new_soup.find("div", {"class": "article-item__body"}).contents), encoding="utf-8")
        with open(f"{file_name}.txt", "wb") as output:
            output.write(data)
            print(file_name)
    print(f"All files written and saved successfully from Page no. {page}")
    page += 1
    os.chdir(cwd)
