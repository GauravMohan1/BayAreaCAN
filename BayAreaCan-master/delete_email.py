#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import shutil
from datetime import date

today = str(date.today())
news = f'Local_News_{today}'

rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		filepath = subdir + os.sep + file
		name = file.split(".txt")[0]
		if file.endswith(".txt"):
			if name == "Alameda":
				os.remove(file)
			elif name == "Santa Clara":
				os.remove(file)
			elif name == "San Francisco":
				os.remove(file)
			elif name == "Contra Costa":
				os.remove(file)
			elif name == "San Mateo":
				os.remove(file)
			elif name == "Marin":
				os.remove(file)
			elif name == "Solano":
				os.remove(file)
			elif name == "Sonoma":
				os.remove(file)
			elif name == "Napa":
				os.remove(file)
			elif name == "Bay Area":
				os.remove(file)
			elif name == news:
				os.remove(file)
