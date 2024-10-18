
from inv import Item

 	 
item=Item("coco nut",3,3,'baking')#this creats an item
dic={}
while True:
	item.newItem()
	dic={item.getQuantity():item.getName()}
	break
	
	print(dic)
	
	
	
	
