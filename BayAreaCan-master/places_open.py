from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

opts = Options()
opts.headless = True
driver = webdriver.Firefox(options=opts)

driver.get("https://projects.sfchronicle.com/2020/coronavirus-map/california-reopening/")
driver.find_element_by_class_name("react-select__indicator.react-select__dropdown-indicator.css-tlfecz-indicatorContainer").click()

test = driver.find_element_by_class_name("react-select__menu.css-26l3qy-menu")
test_child = test.find_elements_by_css_selector("*")

my_dict = {}
counties = []

del test_child[0]

count = 0
for item in test_child:
    #print(test_child[count].text)
    counties.append(test_child[count].text)
    test_child[count].click()
    divs = driver.find_elements_by_css_selector("div")
    # print(divs[53].text + '\n')
    # print(divs[54].text + '\n')
    # print(divs[55].text + '\n')
    # print(divs[56].text + '\n')
    my_dict[counties[count]] = {
        "SipExpire": divs[53].text,
        "Masks": divs[54].text,
        "Open": divs[55].text,
        "Closed": divs[56].text
    }
    count += 1
    driver.find_element_by_class_name("react-select__indicator.react-select__dropdown-indicator.css-tlfecz-indicatorContainer").click()
    test = driver.find_element_by_class_name("react-select__menu.css-26l3qy-menu")
    test_child = test.find_elements_by_css_selector("*")
    del test_child[0]

for county in counties:
    output_text = "\n"
    output_text += str(my_dict[county]["SipExpire"]) + "\n\n"
    output_text += str(my_dict[county]["Masks"]) + "\n\n"
    output_text += str(my_dict[county]["Open"]) + "\n\n"
    output_text += str(my_dict[county]["Closed"]) + "\n\n"
    print(output_text)
    name = county.split()
    del name[-1]
    name = ' '.join(name)
    with open(f'{name}.txt', 'a') as data:
        data.write(output_text+'\n')
        data.close()
