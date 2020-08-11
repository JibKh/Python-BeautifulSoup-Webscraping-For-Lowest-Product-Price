from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import requests
import re

# Purpose of this file:
# 1) Create a link using the search arguments. The link must be for prices low to high.
# 2) Using beautifulsoup, scrape the page and retrieve the product name, price and link to the product page.
# 3) Store the results in their respective variables.

class PakDukaan:
	website = 'Pak Dukaan'
	search = ""
	url = ""
	name = []
	price = []
	link = []

	def __init__(self, search):
		print('Searching', self.website + '...')
		self.search = search
		self.generateLink()
		self.generateResult()
		print('Done!')

	# Generates a link to be opened
	def generateLink(self):
		search = "+".join(self.search)
		self.url = "https://pakdukaan.com/?orderby=price&paged=1&s=" + search + "&post_type=product"

	# Open the link and use beautifulsoup to scrape it
	def generateResult(self):
		res = Request(self.url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
		webpage = urlopen(res).read()

		# Get page html
		pakSoup = soup(webpage, "html5lib")

		# Find relevant parts
		pakStuff = pakSoup.findAll('div', {'class': 'product-name'})
		pakPrice = pakSoup.findAll('div', {'class': 'price-box-inner'})
		pakStuff = pakStuff[::2]
		pakPrice = pakPrice[::2]
		
		# Save them in their respective variables
		for i in range(len(pakStuff)):
			nameAndLink = pakStuff[i].findAll('a')[0]
			self.name.append(nameAndLink.text.strip())
			self.link.append(nameAndLink['href'])
			try:
				self.price.append(float(pakPrice[i].ins.span.text.strip()[1:].replace(',', '').split('.')[0]))
			except:
				self.price.append(float(pakPrice[i].span.text.strip()[1:].replace(',', '').split('.')[0]))