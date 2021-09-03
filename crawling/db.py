import pymysql

from russia import get_news, get_news_link

key_title = []; key_text = []; key_update = []; key_img = []

links = get_news_link()

# for i in key_links:
get_news(links[0], key_title, key_text, key_update, key_img)
print(links[0], key_title[0], key_text[0], key_update[0], key_img[0])

conn = pymysql.connect(
	host='113.198.137.163',
	port=3306,
	user='pnadm',
	passwd='picknews1',
	db='picknews'
)

c_code=643
curs = conn.cursor()

russia = "INSERT ignore INTO article_ledger (country_code, title, article_link, main_text, image_link, article_reg_dtime) VALUES (%s, %s, %s,%s,%s, %s)"

val = (c_code, key_title[0], links[0], key_text[0],  key_img[0], key_update[0] )
Clear = "TRUNCATE TABLE article_ledger"

curs.execute(russia, val)

print("AAA")