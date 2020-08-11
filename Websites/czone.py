from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import requests

# Purpose of this file:
# 1) Create a link using the search arguments. The link must be for prices low to high.
# 2) Using beautifulsoup, scrape the page and retrieve the product name, price and link to the product page.
# 3) Store the results in their respective variables.

class Czone:
	website = 'Computer Zone'
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
		search = "%20".join(self.search)
		self.url = "https://www.czone.com.pk/search.aspx?kw=" + search

	# Open the link and use beautifulsoup to scrape it
	def generateResult(self):
		res = Request(self.url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
		webpage = urlopen(res).read()

		# Get page html
		czoneSoup = soup(webpage, "html5lib")

		# Find relevant parts
		czoneStuff = czoneSoup.findAll('div', {'class': 'product'})
		
		# Save them in their respective variables
		for i in range(len(czoneStuff)):
			self.name.append(czoneStuff[i].findAll('h4')[0].text.strip())
			self.price.append(float(czoneStuff[i].findAll('div', {'class': 'price'})[0].text.strip()[3:].replace(',', '')))
			self.link.append("www.czone.com.pk" + czoneStuff[i].findAll('h4')[0].a['href'])