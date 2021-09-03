import requests 
from bs4 import BeautifulSoup
import re
from datetime import datetime
from googletrans import Translator

key = "covid"
link = "https://tuoitre.vn/tim-kiem.htm?keywords="

key_links = []
key_title = []
key_text = []
key_update = []
key_img = []
trans_text = []
num_news = 0

def get_news_link():
    URL = "https://tuoitre.vn/tin-moi-nhat.htm"
    req = requests.get(URL)

    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find('div',{'class' : 'box-news-latest isstream'})

    news_list = soup.find_all('li', {'class' :'news-item'})
    key_links = [li.find("a")["href"] for li in news_list]

    return key_links 


def get_news(num_news,links,key_title, key_text, key_update,key_img):
    URL = "https://tuoitre.vn/" + links
    req = requests.get(URL)

    soup = BeautifulSoup(req.text, 'html.parser')

    try:
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
        num_news += 1
    except:
        pass

    try:
        img = soup.find(class_="VCSortableInPreviewMode")
        img = img.find("img")['src']
        key_img.append(img)
    except:
        key_img.append("no_img")
    
    return num_news

def trans(text, transtext):
    translator = Translator()
    #translator = Translator(service_urls=['translate.googleapis.com'])
    for t in text:
        print(len(t))
        if len(t) > 5000:
            a = [t[i:i + 5000] for i in range(0, len(t), 5000)]
            for j in a:
                trans_t += translator.translate(j, src ='vi', dest='ko').text
        else:
            trans_t= translator.translate(t, src ='vi', dest='ko').text
        
        print(trans_t)
        
        #transtext.append(trans_t)


key_links = get_news_link()

for i in key_links:
    num_news =get_news(num_news,i, key_title, key_text, key_update, key_img)



for i in range(num_news):
    print("link = " + key_links[i])
    print("title = " + key_title[i])
    print("update = " + key_update[i])
    print("text = " + key_text[i])
    print("img = " + key_img[i])
    print("\n\n")

