#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
#  
#  Copyright 2021 Ali Morakabi <alimkb@gmail.com>
# 

# email address to receive news titles
receiver_email = "my@email.com"


# RSS Urls
urls = ['https://news.yahoo.com/rss/',
        'https://news.google.com/news/rss']


# news title list template
news_html = ''' <div>
		<div style="background-color: #fffacc; padding: 5px;">
		<div>
		<h3><a href="{}" > {} </a></h3> 
		</div>
		</div>
		<div style="background-color: #fffded; padding: 5px;">
		 {} : {}  
		</div>
	    </div>'''


# html file 
html_file = ''' 
	<html><head><title>Gathering News by title</title></head>
	<body>
	<div>
	<h2>Latest News Titles</h2>
	</div>
	<br/>
	{}
	<br/>
	<div>
	<p>You receive news title email regarding rss2mail service.If you no longer want to receive this email please remove your
	email address from rss2mail config file or disable cron job.</p>
	</div>
	</body>
	</html>'''

# keyword list
# list can be empty for gathering all titles : words = []
# or with keywords example : words = ['blah','test','explode']
words = []


# SMTP account info
# SMTP account username 
sender_email = "user@email.com"  

# SMTP password
user_password = 'youpassword'

# port number
port = 465  # For SSL

# SMTP address 
smtp_server = "mail.youdomain.com"

