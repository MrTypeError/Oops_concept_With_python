from item import Item
#from phone import Phone

#Item.instance_from_CSV()
print(Item.All)

item1=Item("New Item",1000)
item1.name="Another Name"

print(item1.name)   # When we want to bound the initialixed 
                    #value and dont want it to be changed in future {Read only} so we do {Encapsulation}