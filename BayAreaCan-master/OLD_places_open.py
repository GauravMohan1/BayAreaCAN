from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

opts = Options()
opts.headless = True
driver = webdriver.Firefox(options=opts)

driver.get("https://www.nbcbayarea.com/news/coronavirus/reopening-the-bay-area-full-list-of-counties-easing-coronavirus-restrictions/2290710/")
time.sleep(5)

driver.switch_to.frame(driver.find_element_by_id('datawrapper-chart-7fff7'))
rows = driver.find_elements_by_class_name("css-kfswhc.svelte-fugjkr")

my_dict = {}

for item in rows:
    places = item.find_elements_by_css_selector("td")
    my_dict[places[0].text] = {
    	"Bars": places[1].text,
    	"Indoor Dining": places[2].text,
    	"Outdoor Dining": places[3].text,
    	"Places of Worship": places[4].text,
    	"Gyms": places[5].text,
    	"Personal Care": places[6].text
    }
    del places[0:6]

print(my_dict)

counties = [
"Alameda",
"Santa Clara",
"Contra Costa",
"San Francisco",
"San Mateo",
"Marin",
"Solano",
"Sonoma",
"Napa"
]

for county in counties:
	output_text = ""
	output_text += "Bars: " + str(my_dict[county]["Bars"]) + "\n"
	output_text += "Indoor Dining: " + str(my_dict[county]["Indoor Dining"]) + "\n"
	output_text += "Outdoor Dining: " + str(my_dict[county]["Outdoor Dining"]) + "\n"
	output_text += "Places of Worship: " + str(my_dict[county]["Places of Worship"]) + "\n"
	output_text += "Gyms: " + str(my_dict[county]["Gyms"]) + "\n"
	output_text += "Personal Care: " + str(my_dict[county]["Personal Care"]) + "\n"
	with open(f'{county}.txt', 'a') as data:
		data.write(output_text+'\n')
		data.close()
