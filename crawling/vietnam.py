import requests 
from bs4 import BeautifulSoup
import re
from datetime import datetime

key = "covid"
link = "https://tuoitre.vn/tim-kiem.htm?keywords="

key_links = []
key_title = []
key_text = []
key_update = []
key_img = []

def get_news_link(key):
    URL = link + key
    req = requests.get(URL)

    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find('div',{'class' : 'box-news-latest isstream'})

    news_list = soup.find_all('li', {'class' :'news-item'})
    key_links = [li.find("a")["href"] for li in news_list]

    return key_links 


def get_news(links,key_title, key_text, key_update,key_img):
    URL = "https://tuoitre.vn/" + links
    print(URL)
    req = requests.get(URL)

    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find(class_='article-title').text
    key_title.append(title)

    update = soup.find(class_='date-time').text
    update = re.search(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}', update).group()
    update = update.replace(" ", "/")
    update = update.split('/')
    update = update[2] + "-" + update[1] + "-" +  update[0] + " " +  update[3]
    key_update.append(update)

    text_table = soup.find(class_='content fck')
    text_list = text_table.find_all("p")
    text = [li.get_text() for li in text_list]
    text = ' '.join(text)
    key_text.append(text)

    try:
        img = soup.find(class_="VCSortableInPreviewMode")
        img = img.find("img")['src']
        key_img.append(img)
    except:
        key_img.append("no_img")

key_links = get_news_link(key)
# print(key_links[1])
# get_news(key_links[1], key_title, key_text, key_update, key_img)

for i in key_links:
    get_news(i, key_title, key_text, key_update, key_img)

for i in range(len(key_links)):
    print("link = " + key_links[i])
    print("title = " + key_title[i])
    print("update = " + key_update[i])
    print("text = " + key_text[i])
    print("img = " + key_img[i])
    print("\n\n")