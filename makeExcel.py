import xlsxwriter

# Purpose of this file:
# For each website, create a sheet and export results in a tabular form to their respective sheets

class MakeWorkbook:
	filename = ""
	workbook = None
	headers = ["Name", "Price", "Link"]
	easeTec = None
	indusTech = None

	# Create a workbook with the name corresponding to the search joined with '_'
	def __init__(self, search, easeTec, indusTech):
		self.workbook = xlsxwriter.Workbook('_'.join(search) + ".xlsx")
		self.easeTec = easeTec
		self.indusTech = indusTech
		self.easeTecExcel()
		self.indusTechExcel()
		self.workbook.close()
	
	# Make an excel sheet for IndusTech in the same workbook
	def easeTecExcel(self):
		worksheetEaseTec = self.workbook.add_worksheet('EaseTec')

		# Write header
		for i, head in enumerate(self.headers):
			worksheetEaseTec.write(0, i, head)

		row = 1
		col = 0
		# Write each line
		for i in range(len(self.easeTec.name)):
			worksheetEaseTec.write(row, col, self.easeTec.name[i])
			worksheetEaseTec.write(row, col+1, self.easeTec.price[i])
			worksheetEaseTec.write(row, col+2, self.easeTec.link[i])

			row = row + 1

	# Make an excel sheet for IndusTech in the same workbook
	def indusTechExcel(self):
		worksheetIndusTech = self.workbook.add_worksheet('IndusTech')

		# Write header
		for i, head in enumerate(self.headers):
			worksheetIndusTech.write(0, i, head)

		row = 1
		col = 0
		# Write each line
		for i in range(len(self.indusTech.name)):
			worksheetIndusTech.write(row, col, self.indusTech.name[i])
			worksheetIndusTech.write(row, col+1, self.indusTech.price[i])
			worksheetIndusTech.write(row, col+2, self.indusTech.link[i])

			row = row + 1