
	class Item:
	def __init__(self,name,price,quantity,d):
		self.name=name
		self.price=float(price)
		self.quantity=int(quantity)
		self.d=d
	
	def getName(self):
		return self.name
	def getQuantity(self):
		return self.quantity
####### input new item and set a departement for the item######
	def newItem(self):
		while True:
		#g=department()
			name=input('please enter an item''\n')
			self.name=name
			quantity=input("how many do you need?"'\n')
			self.quantity=quantity
			department=self.d
			
		
			options=input('would you like to add another item? 1= yes 2 = no''\n')
			if(options=='1'):
				new_name=name
				amount=quantity
				
			elif (options=='2'):
				print(name+":" 
+ " " + quantity)
				break
			else:
				print('invalid option please hit 1 or 2')
					
				
	def makelist(self):
	 return this.getName()
	
	
		
      
	
	
