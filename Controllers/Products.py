from prettytable import PrettyTable

class Products:

	def __init__(self):
		self.products = PrettyTable(['ID', 'Name', 'Type'])
		self.id   = ""
		self.name = ""
		self.type = ""

	def clearScreen(self):
		print('\033c')

	def init(self):
		print('What do you wanna do? 1. Add or 2. Update 3. Exit')
		choice = int(input())

		if choice is 1:
			self.add()
		if choice is 2:
			self.update()
		if choice is 3:
			self.clearScreen()
			print("Thank you!")
			return False
			
		self.clearScreen()
		self.init()

	def add(self):
		count = 1
		for row in self.products:
			count = count+1

		self.id = int(count)

		print('Enter a product name:')
		self.name = input()

		print('What type of product?')
		self.type = input()

		self.products.add_row([self.id, self.name, self.type])
		self.clearScreen()
		print("New Product has been added!")
		self.products.sortby = "ID"
		print(self.products)

		self.init()


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