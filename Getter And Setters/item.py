import csv

class Item:
    All=[]
    pay_rate=0.8 #This is the pay rate for the discout of 20%
    def __init__(self, name, price, quantity= 2): 
        #here we have specified the datatype for the valuses to be passed .
        # if you assign float thn it can take float as well as intiger as a argument.
        #Run validations to the recived arguments      
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
   
        # assert price>=0, f"Entered Price {price} must be greater then zero and can't be less then zero"
        # assert quantity>=0, f"Entered Quantity {quantity} must be greater then zero and can't be less then zero"

        #assign self objects
       
        self.__name=name
        self.__price=price
        self.quantity=quantity
        # print("Hello it's me a Constroctor ")

        # Actions to execute
        # Encapsulation is performed here 
        @property
        def price(self):
            return self.__price
        def apply_discount(self):
            self.__price=self.__price*Item.pay_rate #this will take the pay_rate at the class level 
        def apply_incriment(self,incrimnet_value):
             self.__price=self.__price+self.__price*incrimnet_value
        def Calculate_Total_price(self): 

            return self.price*self.quantity

        Item.All.append(self)
        
        @classmethod
        def instance_from_CSV(cls):
            with open('Items.csv','r') as f:
                reader=csv.DictReader(f)
                items=list(reader)
            for item in items :
                Item(
                    name=item.get('Name'),
                    price=float(item.get('Price')),
                    quantity=int(item.get('Quantity')),
                    )

        def __repr__(self): #The __repr__() function returns a printable representation of the given object.
            return f"{self.__class__.__name__}({self.name},{self.price},{self.quantity})"
       
        @staticmethod
        def is_intiger(num):
            #this will check that number entered is a float or a point zero number 
            #example :- 5.0,10.0,20.0
            if isinstance(num,float):
               #Basically it will count all the point zero values 
                return num.is_integer()
            elif isinstance(num,int):
                return True
            else:
                return False 
        @property
        # Property Decorator = Read-Only Attribute
        def name(self):
            return self.__name # making private {__name}
        @name.setter            #This setter decorator helps you to
                                #give a new value to the read only property 
        def name(self, value):
            if len(value) > 10:
                raise Exception("The name is too long!")
            else:
                self.__name = value

       
       