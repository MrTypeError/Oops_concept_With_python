from item import Item
class Phone(Item):
     def __init__(self, name, price, quantity= 2,brokenPhone=1): 
        super().__init__(                   # This will inherite all the basic characteristics of the parent class and 
            name,price,quantity            # we don't have to wirte agin and again    
        )


        # assert price>=0,f"Entered Price {price} must be greater then zero and can't be less then zero"
        # assert quantity>=0,f"Entered Quantity {quantity} must be greater then zero and can't be less then zero"
        assert brokenPhone>=0,f"Entered Broken Phone  {brokenPhone} must be greater then zero and can't be less then zero"
        self.brokenPhone=brokenPhone