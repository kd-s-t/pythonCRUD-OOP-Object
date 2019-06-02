import Controllers.Software as s

class Hardware(s.Software):

	def __init__(self):
		self.clearScreen()
		self.setTable()

	def createHardware(self):
		self.licenseNumber = self.generateLicense() # Software Method

		print('\033[1;33;40mPlease input hardware name?\033[0m')
		self.hardwareName = input()

		print('\033[1;33;40mPlease input available license?\033[0m')
		self.availableLicense = input()

		print('\033[1;33;40mPlease input a start date?\033[0m')
		self.startDate = input()

		print('\033[1;33;40mPlease input a expiration date?\033[0m')
		self.expirationDate = input()

		count = 1
		for row in self.getTable():
			count = count+1

		self.id = int(count)

		self.createSoftware(self.id, self.hardwareName)
		s.Software.__init__(self, self.availableLicense, self.startDate, self.expirationDate)

		self.clearScreen()
		print(self.getTable())
		self.displayUI()

	def displayUI(self):
		print('\033[1;33;40mWhat do you wanna do?\033[0m \033[1;32;40m 1. Create Hardware \033[0m or \033[1;32;40m2. Update Expiration Date \033[0m or \033[1;32;40m3. Update Available License \033[0m \033[1;31;40m4. Exit \033[0m')
		self.choice = int(input())

		if self.choice is 1:
			self.createHardware()
		if self.choice is 2:
			self.updateExpirationDate()
		if self.choice is 3:
			self.updateAvailableLicense()
		if self.choice is 4:
			self.clearScreen()
			print("\033[1;32;40mThank you! \033[0m")

		self.clearScreen()
		print(self.getTable())