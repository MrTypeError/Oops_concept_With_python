class Item:
    pay_rate=0.8 #This is the pay rate for the discout of 20%
    def __init__(self, name: str, price: float, quantity= 2): 
        #here we have specified the datatype for the valuses to be passed .
        # if you assign float thn it can take float as well as intiger as a argument.
        #Run validations to the recived arguments         
        assert price>=0,f"Entered Price {price} must be greater then zero and can't be less then zero"
        assert price>=0,f"Entered Quantity {quantity} must be greater then zero and can't be less then zero"

        #assign self objects
       
        self.name=name
        self.price=price
        self.quantity=quantity
        # print("Hello it's me a Constroctor ")

        # Actions to execute


        # def apply_discount(self):
        #     self.price=self.price*Item.pay_rate #this will take the pay_rate at the class level 
       
        def apply_discount(self):
            self.price=self.price*self.pay_rate # this will take the pay_rate at the instance level 

        def Calculate_Total_price(self): 

            return self.price*self.quantity

        
# item1=Item("Phone",5000,6)
# item1.Name="Phone"
# item1.price=10000
# item1.quantity=6
# print(item1.name,item1.price,item1.quantity)

# item2=Item("laptop",10000,6)
# item2.Name="laptop"
# item2.price=10000
# item2.quantity=6
# print(item2.name,item2.price,item2.quantity)

#item2.has_numpad=False # we alwasys don't need to initate the property in the constructor we can crate dynamicaly in the program as we need 

# print(item1.Calculate_Total_price())
# print(item2.Calculate_Total_price())

# print(Item.pay_rate) #Checks at the class level and returns the value of pay_rate.
# print(item1.pay_rate) #It first checks at the instannce/object level and not gets the vlues it goes to the class level and returns the pay_rate.
# print(item2.pay_rate) #It first checks at the instannce/object level and not gets the vlues it goes to the class level and returns the pay_rate.


# print(Item.__dict__) # All the attribute at the class level in a form of  dictonary  
# print(item1.__dict__) # All the attribute at the instance/object level in form of  a dictonary


