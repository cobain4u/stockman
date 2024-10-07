
class Item:
	def __init__(self,name,price,numOnShlf,d):
		self.name=name
		self.price=float(price)
		self.numOnShelf=int(numOnShlf)
		self.d=d
	
	def getName(self):
		return self.name

####### input new item and set a departement for the item######
	def newItem(self):
		while True:
		#g=department()
			name=input('please enter an item''\n')
			self.name=name
			self.d=input("please enter a department"'\n')
			department=self.d
			itemDic={name:department}
		
			options=input('would you like to add another item? 1= yes 2 = no''\n')
			if(options=='1'):
				new_name=name
				new_dep=department
				itemDic.update({name:department,new_name:new_dep})
				print(itemDic)
			elif (options=='2'):
				break
			else:
				print('invalid option please hit 1 or 2')
					
				
	def makelist(self):
	 return this.getName()
	
	
		
      
	
	