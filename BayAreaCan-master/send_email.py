#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
import time
today = str(date.today())
news = f'Local_News_{today}'

report_names = ["Alameda","Santa Clara","Contra Costa","San Francisco","San Mateo","Marin","Solano","Sonoma","Napa", news]

email_dict = {
	"Alameda": "ktai0417@gmail.com",
	"Marin": "atendo@ucsd.edu",
	"Solano": "anikabhattacharjya1@gmail.com",
	"San Mateo": "trentonbirch17@gmail.com",
	"Napa": "k5le@ucsd.edu",
	"Sonoma": "khc059@ucsd.edu",
	"Contra Costa": "jaidachan1888@gmail.com",
	"San Francisco": "henryleedavis3@gmail.com",
	"Santa Clara": "pranav650@gmail.com"
}

# email_dict = {
# 	"Alameda": "shivaum1@gmail.com",
# 	"Marin": "shivaumkumar1@gmail.com",
# 	"Solano": "kumars7@uw.edu",
# 	"San Mateo": "shiv.2k.yt@gmail.com",
# 	"Napa": "shivaum1@gmail.com",
# 	"Sonoma": "shivaumkumar1@gmail.com",
# 	"Contra Costa": "kumars7@uw.edu",
# 	"San Francisco": "shiv.2k.yt@gmail.com",
# 	"Santa Clara": "shivaumkumar2018@gmail.com"
# }

email_dict[news] = "pranav650@gmail.com"

# open the file to be sent
rootdir = os.getcwd()
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		filepath = subdir + os.sep + file
		name = file.split(".txt")[0]
		if file.endswith(".txt") and name in report_names:
			fromaddr = "gauravmohan00@gmail.com"
			for county in email_dict:
				if (county == name):
					toaddr = email_dict[county]
			print(name)
			print(toaddr)

			# instance of MIMEMultipart
			msg = MIMEMultipart()

			# storing the senders email address
			msg['From'] = fromaddr

			# storing the receivers email address
			msg['To'] = toaddr

			if (name in news):
				# storing the subject
				msg['Subject'] = "Local News Reports " + today

				# string to store the body of the mail
				body = "Here are the local news reports for " + today
			else:
				# storing the subject
				msg['Subject'] = "COVID-19 Reports " + name + " County " + today

				# string to store the body of the mail
				body = "Here are the daily reports for " + name + " County " + today

			# attach the body with the msg instance
			msg.attach(MIMEText(body, 'plain'))

			filename = file
			attachment = open(filepath, "rb")
			p = MIMEBase('application', 'octet-stream')
			p.set_payload((attachment).read())
			encoders.encode_base64(p)
			p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
			msg.attach(p)
			if (name not in news):
				filename = "Bay Area.txt"
				filepath = subdir + os.sep + filename
				attachment = open(filepath, "rb")
				ba = MIMEBase('application', 'octet-stream')
				ba.set_payload((attachment).read())
				encoders.encode_base64(ba)
				ba.add_header('Content-Disposition', "attachment; filename= %s" % filename)
				msg.attach(ba)
			# creates SMTP session
			s = smtplib.SMTP('smtp.gmail.com', 587)

			# start TLS for security
			s.starttls()
			# Authentication
			s.login(fromaddr, "Gaurav2468")

			# Converts the Multipart msg into a string
			text = msg.as_string()

			s.sendmail(fromaddr, toaddr, text)

			# terminating the session
			s.quit()
