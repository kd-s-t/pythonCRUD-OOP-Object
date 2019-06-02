import Controllers.Products as p
import random
from prettytable import PrettyTable

class Software(p.Products):
	
	def __init__(self, availableLicense, startDate, expirationDate):
		self.availableLicense = availableLicense
		self.startDate        = startDate
		self.expirationDate   = expirationDate

	def updateExpirationDate(self):
		print('Search by id:')
		looking_for_id = int(input())

		count = 0
		found = 'no'
		for row in self.software:
			row.border = False
			row.header = False
			self.id                = int(row.get_string(fields=["ID"]).strip())
			self.hardware_name     = row.get_string(fields=["Hardware Name"]).strip()
			self.license_number    = row.get_string(fields=["License number"]).strip()
			self.available_license = row.get_string(fields=["Available license"]).strip()
			self.start_date        = row.get_string(fields=["Start date"]).strip()
			self.expiration_date   = row.get_string(fields=["Expiration date"]).strip()
			row_number = count
			if(self.id == looking_for_id):
				found = 'yes'
				break
		 
			count = count+1

		if(found == 'no'):
			self.clearScreen()
			print("\033[0;37;41mSorry we couldn't find what your looking for. \033[0m")
			self.software.sortby = "ID"
			print(self.software)
			self.displayUI()

		print('Expiration license:')
		self.expiration_date = input()


		self.software.del_row(row_number)

		self.software.add_row([self.id, self.hardware_name, self.license_number, self.available_license, self.start_date, self.expiration_date])
		
		self.clearScreen()
		print("\033[1;32;40mSoftware updated! \033[0m")
		self.software.sortby = "ID"
		print(self.software)

		self.displayUI()

	def updateAvailableLicense(self):
		print('Search by id:')
		looking_for_id = int(input())

		count = 0
		found = 'no'
		for row in self.software:
			row.border = False
			row.header = False
			self.id                = int(row.get_string(fields=["ID"]).strip())
			self.hardware_name     = row.get_string(fields=["Hardware Name"]).strip()
			self.license_number    = row.get_string(fields=["License number"]).strip()
			self.available_license = row.get_string(fields=["Available license"]).strip()
			self.start_date        = row.get_string(fields=["Start date"]).strip()
			self.expiration_date   = row.get_string(fields=["Expiration date"]).strip()
			row_number = count
			if(self.id == looking_for_id):
				found = 'yes'
				break
		 
			count = count+1

		if(found == 'no'):
			self.clearScreen()
			print("\033[0;37;41mSorry we couldn't find what your looking for. \033[0m")
			self.software.sortby = "ID"
			print(self.software)
			self.displayUI()

		print('Available license:')
		self.available_license = input()


		self.software.del_row(row_number)

		self.software.add_row([self.id, self.hardware_name, self.license_number, self.available_license, self.start_date, self.expiration_date])
		
		self.clearScreen()
		print("\033[1;32;40mSoftware updated! \033[0m")
		self.software.sortby = "ID"
		print(self.software)

		self.displayUI()

	def generateLicense(self):
		self.licenseNumber = random.randrange(100,200)
		return self.licenseNumber

	def setTable(self):
		self.software = PrettyTable(['ID', 'Hardware Name', 'License number', 'Available license', 'Start date', 'Expiration date'])

	def createSoftware(self, id, hardwareName):
		self.software.add_row([id, hardwareName, self.licenseNumber, self.availableLicense, self.startDate, self.expirationDate])
	
	def getTable(self):
		return self.software