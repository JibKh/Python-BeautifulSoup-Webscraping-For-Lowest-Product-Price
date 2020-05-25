import sys
from Websites.easeTec import EaseTec
from Websites.indusTech import IndusTech
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

# ====== IndusTech ======
print('Searching IndusTech...')
indusTech = IndusTech(search) # Class created which contains the results of the search
print('Done!')


# ====== EaseTec ======
print('Searching EaseTec...')
easeTec = EaseTec(search) # Class created which contains the results of the search
print('Done!')


# ====== EXCEL/CSV ======
print('\nMaking Excel Workbook...')
MakeWorkbook(search, easeTec, indusTech)
print('Done! \n\nOpen:', '_'.join(search) + '.xlsx')

if len(easeTec.name) == 0:
	print('EaseTec found no results..\nTry something else?')

if len(indusTech.name) == 0:
	print('\nIndusTech found no results..\nTry something else?')
