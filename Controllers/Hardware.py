import Products as products

class Hardware(products):
	licenseNumber = 0
	availableLicense = ""
	startDate = ""
	expirationDate = ""

	def update(self):
		print('Search by id:')
		looking_for_id = int(input())

		count = 0
		found = 'no'
		for row in self.products:
			row.border = False
			row.header = False

			self.id    = int(row.get_string(fields=["ID"]).strip())
			self.name  = row.get_string(fields=["Name"]).strip()
			self.type  = row.get_string(fields=["Type"]).strip()
			row_number = count
			if(self.id == looking_for_id):
				found = 'yes'
				break
		 
			count = count+1

		if(found == 'no'):
			self.clearScreen()
			print("Sorry we couldn't find what your looking for.")
			self.products.sortby = "ID"
			print(self.products)
			self.init()

		print('Edit name:')
		self.name = input()

		print('Edit type:')
		self.type = input()

		self.products.del_row(row_number)

		self.products.add_row([self.id, self.name, self.type])
		
		self.clearScreen()
		print("Product updated!")
		self.products.sortby = "ID"
		print(self.products)

		self.init()
