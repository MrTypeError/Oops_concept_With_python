'''
This is the implimentation without using the Super keyword
So, this implimentation is not calling the Parent class constructor which is not correct
'''

class Parent:
    def __init__(self): #Parent Constructor
        print("Parent init")
    
class Child(Parent):
    def __init__(self): #Child Constructor
        print("Child init")

# First call
obj1 = Child()

'''
    So we will use the super keyword which will call the 
    parent constructor whenever the child class is called.
'''


class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")


obj1 = Child()