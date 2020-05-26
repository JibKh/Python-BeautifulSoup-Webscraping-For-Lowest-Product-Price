import pandas as pd

# Purpose of this file:
# 1) Create a sheet for each website containing product price, name and link
# 2) Create a fully compiled sheet in ascending order of price for comparison

class MakeWorkbook:
	filename = ""
	websites = None


	def __init__(self, search, websites):
		self.filename = '_'.join(search) + ".xlsx"
		self.websites = websites

		# Function to make the pandas dataframe and export to excel
		self.makeDataFrame()

	def makeDataFrame(self):
		dataFrames = [None]
		sheetNames = ['All Sites']

		# Convert to pandas dataframe
		for site in self.websites:
			siteData = pd.DataFrame({'Website': [site.website] * len(site.name), 'Name': site.name, 'Price': site.price, 'Link': site.link})
			siteData.sort_values(by = ['Price'], inplace = True)
			dataFrames.append(siteData)
			sheetNames.append(site.website)
		
		# Concat all data to a single table
		allSitesData = pd.concat(dataFrames)
		
		# Sort in ascending order of price
		allSitesData.sort_values(by = ['Price'], inplace = True)

		dataFrames[0] = allSitesData

		# Write to sheet
		writer = pd.ExcelWriter(self.filename, engine = 'xlsxwriter') # pylint: disable=abstract-class-instantiated

		for i in range(len(sheetNames)):
			dataFrames[i].to_excel(writer, sheet_name = sheetNames[i], index = False)

		writer.save()
