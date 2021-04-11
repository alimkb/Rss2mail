#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  email.py
#  
#  Copyright 2021 Ali Morakabi <alimkb@gmail.com>
#  
#  
#  

import ssl,smtplib
import config as cfg
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def sendEmail(content):
	

	
	message = MIMEMultipart("alternative")
	message["Subject"] = "Daily News Titles"
	message["From"] = cfg.sender_email
	message["To"] = cfg.receiver_email
	# write the plain part
	#text = ""
	# write the HTML part
	html = content
	# convert both parts to MIMEText objects and add them to the MIMEMultipart message
	#part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")
	#message.attach(part1)
	message.attach(part2)

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(cfg.smtp_server, cfg.port, context=context) as server:
	    server.login(cfg.sender_email, cfg.user_password)
	    server.sendmail(cfg.sender_email, cfg.receiver_email, message.as_string())
