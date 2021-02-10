from selenium.webdriver.firefox.options import Options
from datetime import date
import time
from bs4 import BeautifulSoup, NavigableString, Tag
from datetime import date
from selenium import webdriver

today = str(date.today())
check_month = today.split("-")[1]
check_day = today.split("-")[2]
calander_dict = {"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August", "09":"September","10":"October","11":"November","12":"December"}
month = calander_dict[check_month]

opts = Options()
opts.headless = True
driver = webdriver.Firefox(options=opts)
driver.get("https://www.nbcbayarea.com/news/coronavirus/live-blog-latest-coronavirus-updates/2255826/")
time.sleep(20)

html = driver.page_source

soup = BeautifulSoup(html, features="lxml")
text = ''
for header in soup.find_all("h2",class_="wp-block-nbc-section-heading"):
	headerText = header.text
	#print(headerText)
	if month in headerText and check_day in headerText:
		nextNode = header
		while True:
			nextNode = nextNode.nextSibling
			if isinstance(nextNode, Tag):
				if nextNode.name == "p":
					text += nextNode.get_text()
					my_list = nextNode.find_all('a',href=True)
					for a in my_list:
						text += str(a['href']) + '\n'
				elif nextNode.name == 'h2':
					break
if not text:
	text += "No updated news for today"
with open(f'Local_News_{today}.txt', 'w') as file:
	file.write(text)
	file.close()
