class Item:
    def Calculate_Total_price(self,x,y): #self is one of the general convention use by the all the dev all over the globe
                                         # and you can use yor own keyword at that place but to make it simple we will use self
        return x*y


#This is one of the object of the class Item:
item1=Item() #type(item) class concept will be shown here 
item1.Name='phone'# here we have created the instance from a defined class of string  type(str)
item1.price=5000  # here we have created the instance from a defined class of intiger  type(int)
item1.quantity=10 # here we have created the instance from a defined class of intiger  type(int)
# item1.Calculate_Total_price(item1.quentity,item1.price)
print(item1.Calculate_Total_price(item1.quantity,item1.price))


#Now we are making another object for the same class and show how it work.

item2=Item()
item2.Name="laptop"
item2.price=10000
item2.quantity=6 
print(item2.Calculate_Total_price(item2.quantity,item2.price))