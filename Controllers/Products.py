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
		print('\033[1;33;40mWhat do you wanna do?\033[0m \033[1;32;40m 1. Add \033[0m or \033[1;32;40m2. Update \033[0m \033[1;31;40m3. Exit \033[0m')
		choice = int(input())

		if choice is 1:
			self.add()
		if choice is 2:
			self.update()
		if choice is 3:
			self.clearScreen()
			print("\033[1;32;40mThank you! \033[0m")
			

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
		print("\033[1;32;40mNew Product has been added! \033[0m")
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
			print("\033[0;37;41mSorry we couldn't find what your looking for. \033[0m")
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
		print("\033[1;32;40mProduct updated! \033[0m")
		self.products.sortby = "ID"
		print(self.products)

		self.init()