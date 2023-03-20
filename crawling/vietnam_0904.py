import requests 
from bs4 import BeautifulSoup
import re
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

key_links = []
key_title = []
key_text = []
key_update = []
key_img = []
trans_text = []
num_news = 0

def get_news_link():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    URL = "https://tuoitre.vn/tin-moi-nhat.htm"
    req = requests.get(URL)

    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    driver.get(URL)

    xpath = '//*[@id="content"]/div/div[3]/div/div[1]/div/div/div/a'

    soup = BeautifulSoup(req.text, 'html.parser')
    while len(key_links) < 40:
        table = soup.find('div',{'class' : 'box-news-latest isstream'})

        news_list = soup.find_all('li', {'class' :'news-item'})
        for li in news_list:
            key_links.append(li.find("a")["href"])
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
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



key_links = get_news_link()

print(len(key_links))

# for i in key_links:
#     num_news =get_news(num_news,i, key_title, key_text, key_update, key_img)



# for i in range(num_news):
#     print("link = " + key_links[i])
#     print("title = " + key_title[i])
#     print("update = " + key_update[i])
#     print("text = " + key_text[i])
#     print("img = " + key_img[i])
#     print("\n\n")

