from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import requests

# Purpose of this file:
# 1) Create a link using the search arguments. The link must be for prices low to high.
# 2) Using beautifulsoup, scrape the page and retrieve the product name, price and link to the product page.
# 3) Store the results in their respective variables.

class EaseTec:
	search = ""
	url = ""
	name = []
	price = []
	link = []

	def __init__(self, search):
		self.search = search
		self.generateLink()
		self.generateResult()

	# Generates a link to be opened
	def generateLink(self):
		search = "+".join(self.search)
		self.url = "https://easetec.com.pk/?orderby=price&paged=1&s=" + search + "&product_cat=0&post_type=product"

	# Open the link and use beautifulsoup to scrape it
	def generateResult(self):
		res = Request(self.url, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
		webpage = urlopen(res).read()

		easeSoup = soup(webpage, "html.parser")

		products = easeSoup.findAll('li', {'class': 'product'}) # Contains a list of all the products

		for product in products:
			self.link.append(product.findAll('a', {'class': 'woocommerce-LoopProduct-link woocommerce-loop-product__link'})[0]['href']) # Product link scraped
			self.price.append(float(product.findAll('span', {'class': 'woocommerce-Price-amount amount'})[0].text.strip()[2:].strip().replace(',', ''))) # Product price scraped
			self.name.append(product.findAll('h2', {'class': 'woocommerce-loop-product__title'})[0].text.strip()) # Product Name scraped
			

# easeTechSearch = '+'.join(sys.argv[1:])

# #easeTecUrl = "https://easetec.com.pk/?s=" + easeTechSearch + "&product_cat=0&post_type=product"
# easeTecUrl = "https://easetec.com.pk/?orderby=price&paged=1&s=" + easeTechSearch + "&product_cat=0&post_type=product"

# easeTecRes = Request(easeTecUrl, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
# easeTecWebpage = urlopen(easeTecRes).read()

# easeTecSoup = soup(easeTecWebpage, "html.parser")

# easeTecElems = easeTecSoup.findAll('li', {'class': 'product'})

# for product in easeTecElems:
# 	easeLink = product.findAll('a', {'class': 'woocommerce-LoopProduct-link woocommerce-loop-product__link'})[0]['href']
# 	easePrice = product.findAll('span', {'class': 'woocommerce-Price-amount amount'})[0].text.strip()
# 	easeName = product.findAll('h2', {'class': 'woocommerce-loop-product__title'})[0].text.strip()
# 	print(easeName, easePrice, easeLink)