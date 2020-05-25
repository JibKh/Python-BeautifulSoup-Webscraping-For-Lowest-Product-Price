import pandas as pd

# Purpose of this file:
# 1) Create a sheet for each website containing product price, name and link
# 2) Create a fully compiled sheet in ascending order of price for comparison

class MakeWorkbook:
	filename = ""
	easeTec = None
	indusTec = None


	def __init__(self, search, easeTec, indusTect):
		self.filename = '_'.join(search) + ".xlsx"
		self.easeTec = easeTec
		self.indusTec = indusTect

		# Function to make the pandas dataframe and export to excel
		self.makeDataFrame()

	def makeDataFrame(self):
		# Convert to pandas dataframe
		easeTecData = pd.DataFrame({'Website': ['EaseTec'] * len(self.easeTec.name), 'Name': self.easeTec.name, 'Price': self.easeTec.price, 'Link': self.easeTec.link})
		indusTechData = pd.DataFrame({'Website': ['IndusTech'] * len(self.indusTec.name), 'Name': self.indusTec.name, 'Price': self.indusTec.price, 'Link': self.indusTec.link})
		allSitesData = pd.concat([easeTecData, indusTechData])
		
		# Sort in ascending order of price
		easeTecData.sort_values(by = ['Price'], inplace = True)
		indusTechData.sort_values(by = ['Price'], inplace = True)
		allSitesData.sort_values(by = ['Price'], inplace = True)

		# Sheet labels
		sheets = {'All Sites': allSitesData, 'EaseTec': easeTecData, 'IndusTech': indusTechData}

		# Write to sheet
		writer = pd.ExcelWriter(self.filename, engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated

		for sheetName in sheets.keys():
			sheets[sheetName].to_excel(writer, sheet_name = sheetName, index = False)

		writer.save()
