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




urls = ['https://news.yahoo.com/rss/',
        'https://news.google.com/news/rss']

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

html_file = ''' 
	<html><head><title>Gathering News by title</title></head>
	<body>
	{}
	</body>
	</html>'''

words = ['against']

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
print(' Starting scraping :')
news_items = []
for i in urls:
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
if words :
	for i in news_items:
		if any(word in i['title'] for word in words):
			html += news_html.format(i['link'],i['title'],i['source'],i['pubDate'])		
	
# all titles if there is no keywords list
else :
	
	for i in news_items:
		html += news_html.format(i['link'],i['title'],i['source'],i['pubDate'])



# Write html file

html_file = html_file.format(html)
with open('lastNews.html','r+') as htmlfile:
    data = htmlfile.read()
    htmlfile.seek(0)
    htmlfile.write(html_file)
    htmlfile.truncate()
