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
def fetch_rss(addr, word) :
	try:
		r = requests.get(addr)
		soup = BeautifulSoup(r.content, features='xml')
		items = soup.findAll('item')
		return items

	except Exception as e:
		print('The scraping job failed. See exception: ')
		print(e)



print('Starting scraping :')
for i in urls:
	items = fetch_rss(i, words)
	for item in items:
		print(item)
		key = input('Press any key t continue ...')
	
print('--- Finished scraping ---')
	
