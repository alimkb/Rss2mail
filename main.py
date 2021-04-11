#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2021 Ali Morakabi <alimkb@gmail.com>
#  
# https://news.google.com/news/rss/headlines/section/topic/{topic}

import config as cfg
import requests
from bs4 import BeautifulSoup
import mailSender 


items = []

# Rss reader function
def fetch_rss(addr) :
	try:
		content = ''
		r = requests.get(addr)
		soup = BeautifulSoup(r.content, features='xml')
		items = soup.find_all('item')		
		#content 
		return items

	except Exception as e:
		print('The scraping job failed. See exception: ')
		print(e)



# main
print(' Start scraping ...')
news_items = []
for i in cfg.urls:
	items = fetch_rss(i)
	for item in items: 
		news_item = {}
		news_item['title'] = item.title.text
		news_item['link'] = item.link.text
		news_item['pubDate'] = item.pubDate.text
		news_item['source'] = item.source.text
		news_items.append(news_item)


			

# make html with specific keywords in news titles 
html = ''
if cfg.words :
	for i in news_items:
		if any(word in i['title'] for word in cfg.words):
			html += cfg.news_html.format(i['link'],i['title'],i['source'],i['pubDate'])		
	
# all titles if there is no keywords list
else :
	
	for i in news_items:
		html += cfg.news_html.format(i['link'],i['title'],i['source'],i['pubDate'])



# Write html file

html_file = cfg.html_file.format(html)
with open('lastNews.html','r+') as htmlfile:
    data = htmlfile.read()
    htmlfile.seek(0)
    htmlfile.write(html_file)
    htmlfile.truncate()

# send email 
mailSender.sendEmail(html_file)

print('Process finished.')
