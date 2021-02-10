#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.options import Options
from datetime import date
import time

from selenium import webdriver

opts = Options()
opts.headless = True
driver = webdriver.Firefox(options=opts)

driver.get("https://www.worldometers.info/coronavirus/usa/california/")

odd_county_cases = driver.find_elements_by_class_name("odd")[0:28]
even_county_cases = driver.find_elements_by_class_name("even")[0:28]

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

my_dict = {}

for item in even_county_cases:
	for county in counties:
		plus_count = 0
		if county in item.text:
			for index in item.text.split(' '):
				if "+" in index:
					plus_count += 1
			count = -9
			if (plus_count == 1):
				count += 1
			if (plus_count == 0):
				count += 2
			total_cases = item.text.split(' ')[count]
			count += 1
			if '+' in item.text.split(' ')[count]:
				new_cases = item.text.split(' ')[count]
				count += 1
			else:
				new_cases = 0
			total_deaths = item.text.split(' ')[count]
			count += 1
			if '+' in item.text.split(' ')[count]:
				new_deaths = item.text.split(' ')[count]
			else:
				new_deaths = 0


			my_dict[county] = {
								"Total Cases": total_cases,
								"Total New Cases": new_cases,
								"Total Deaths": total_deaths,
								"Total New Deaths": new_deaths
							  }

for item in odd_county_cases:
	for county in counties:
		plus_count = 0
		if county in item.text:
			for index in item.text.split(' '):
				if "+" in index:
					plus_count += 1
			count = -9
			if (plus_count == 1):
				count += 1
			if (plus_count == 0):
				count += 2
			total_cases = item.text.split(' ')[count]
			count += 1
			if '+' in item.text.split(' ')[count]:
				new_cases = item.text.split(' ')[count]
				count += 1
			else:
				new_cases = 0
			total_deaths = item.text.split(' ')[count]
			count += 1
			if '+' in item.text.split(' ')[count]:
				new_deaths = item.text.split(' ')[count]
			else:
				new_deaths = 0


			my_dict[county] = {
								"Total Cases": total_cases,
								"Total New Cases": new_cases,
								"Total Deaths": total_deaths,
								"Total New Deaths": new_deaths
							  }

driver.get("https://projects.sfchronicle.com/2020/coronavirus-map/")
total_bay_cases = driver.find_elements_by_class_name("cacounter-module--count--1-ikC")
bay_cases = total_bay_cases[0].text
bay_deaths = total_bay_cases[1].text
daily_bay_cases = driver.find_elements_by_class_name("cacounter-module--plus--6gulP")
today_bay_cases = daily_bay_cases[0].text.split(' ')[0]
today_bay_deaths = daily_bay_cases[1].text.split(' ')[0]

my_dict["Bay Area"] = {
					"Total Cases": bay_cases,
					"Total New Cases": today_bay_cases,
					"Total Deaths": bay_deaths,
					"Total New Deaths": today_bay_deaths
				  }
print(my_dict)
today = date.today()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

with open(f'Bay Area.txt', 'w') as data:
	data.write("(This report was generated at " + str(current_time) + " on " + str(today) + ')\n')
	output_text = ""
	output_text += "Bay Area" + "\n"
	output_text += "Total Cases: " + str(my_dict["Bay Area"]["Total Cases"]) + "\n"
	output_text += "Total New Cases: " + str(my_dict["Bay Area"]["Total New Cases"]) + "\n"
	output_text += "Total Deaths: " + str(my_dict["Bay Area"]["Total Deaths"]) + "\n"
	output_text += "Total New Deaths: " + str(my_dict["Bay Area"]["Total New Deaths"]) + "\n"
	data.write(output_text+'\n')
	data.close()

for county in counties:
	output_text = ""
	output_text += county + " County" + "\n"
	output_text += "Total Cases: " + str(my_dict[county]["Total Cases"]) + "\n"
	output_text += "Total New Cases: " + str(my_dict[county]["Total New Cases"]) + "\n"
	output_text += "Total Deaths: " + str(my_dict[county]["Total Deaths"]) + "\n"
	output_text += "Total New Deaths: " + str(my_dict[county]["Total New Deaths"]) + "\n"
	with open(f'{county}.txt', 'w') as data:
		data.write("(This report was generated at " + str(current_time) + " on " + str(today) + ')\n')
		data.write(output_text+'\n')
		data.close()
