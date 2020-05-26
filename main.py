import sys
from Websites.easeTec import EaseTec
from Websites.indusTech import IndusTech
from Websites.czone import Czone
from Websites.pakDukaan import PakDukaan
from makeExcel import MakeWorkbook

# Purpose of this file:
# 1) Call all the website classes and store their results in their corresponding class names
# 2) Call the class to export the results to an excel workbook

# Ensure search arguments are taken
if len(sys.argv[1]) <= 1:
	print('Please input a search argument. Example: python main.py Power Supply')
	exit()

# Search argument list
search = sys.argv[1:]

# Create a list of all the websites to search
websites = [IndusTech(search), EaseTec(search), Czone(search), PakDukaan(search)]

# Create an Excel Workbook
print('\nMaking Excel Workbook...')
MakeWorkbook(search, websites)
print('Done! \n\nOpen:', '_'.join(search) + '.xlsx\n')

# Print number of results for each page
for site in websites:
	if len(site.name) == 0:
		print(site.website, 'return no results... Try something else?')
	else:
		print(site.website, 'found', len(site.name), 'results')