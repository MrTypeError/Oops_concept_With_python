################################################################
                # Magic Methods OR Dunder Methods 
################################################################ 
            

class Item:
    pay_rate=0.8 #This is the pay rate for the discout of 20%
    All =[]
    def __init__(self, name, price,quantity= 2): 
        #here we have specified the datatype for the valuses to be passed .
        # if you assign float thn it can take float as well as intiger as a argument.
        #Run validations to the recived arguments         
        assert price>=0,f"Entered Price {price} must be greater then zero and can't be less then zero"
        assert price>=0,f"Entered Quantity {quantity} must be greater then zero and can't be less then zero"

        #assign self objects
       
        self.name=name
        self.price=price
        self.quantity=quantity
        print("Hello it's me a Constroctor ")

        # Actions to execute
        Item.All.append(self)
        
        def __repr__(self): #The __repr__() function returns a printable representation of the given object.
            return f"Item({self.name},{self.price},{self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.All) #This will show all the 5 instances 

for instance in Item.All: #this will give the names as output
    print(instance.name) 