#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2021 Ali Morakabi <alimkb@gmail.com>
#  
# https://news.google.com/news/rss/headlines/section/topic/{topic}

#install lxml : pip3 install lxml

import requests
from bs4 import BeautifulSoup


interval = 360 # in minutes

urls = ['https://news.yahoo.com/rss/',
        'https://news.google.com/news/rss']

words = ['apple','best','stocks']

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
print('------- Starting scraping :')
for i in urls:
	items = fetch_rss(i)
	news_items = []
	for item in items: 
		news_item = {}
		news_item['title'] = item.title.text
		news_item['description'] = item.description
		news_item['link'] = item.link.text
		news_item['pubDate'] = item.pubDate.text
		news_items.append(news_item)
		 
			
for i in news_items:
	if 'Blood' in i['title'] :
		print(i)		
	

	
