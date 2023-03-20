import requests 
from bs4 import BeautifulSoup
import re
from datetime import datetime

key = "covid"
link = "https://ria.ru/search/?query="

key_links = []
key_title = []
key_text = []
key_update = []
key_img = []


def get_news_link():
    URL = "https://ria.ru/lenta/"
    req = requests.get(URL)

    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find('div',{'class' : 'list'})
    news_list = table.find_all('a', {'class' :'list-item__title color-font-hover-only'})
    key_links = [li.get('href') for li in news_list]
    return key_links 


def get_news(links,key_title, key_text, key_update,key_img):
    URL = links

    req = requests.get(URL)

    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find(class_='article__title').text
    key_title.append(title)

    update = soup.find('div',{'class' : 'article__info-date'}).get_text()
    update = re.search(r'\d{2}:\d{2} \d{2}.\d{2}.\d{4}', update).group()
    update = update.replace(" ", ".")
    update = update.split('.')
    update = update[3] + "-" + update[2] + "-" +  update[1] + " " +  update[0]
    key_update.append(update)

    text = soup.find('div',{'class' : 'article__body js-mediator-article mia-analytics'}).get_text()
    text = text.replace("\n\n", "")
    key_text.append(text)

    try:
        img = soup.find(class_="photoview__open")
        img = img.find("img")['src']
        key_img.append(img)
    except:
        key_img.append("no_img")

# key_links = get_news_link()
# # print(key_links[1])
# # get_news(key_links[1], key_title, key_text, key_update)

# for i in key_links:
#     get_news(i, key_title, key_text, key_update, key_img)

# for i in range(len(key_links)):
#     print("link = " + key_links[i])
#     print("title = " + key_title[i])
#     print("update = " + key_update[i])
#     print("text = " + key_text[i])
#     print("img = " + key_img[i])
#     print("\n\n")