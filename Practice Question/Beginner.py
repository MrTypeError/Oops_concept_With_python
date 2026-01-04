class Animal :
    def property():
        print("Have Different Sounds")

class Dog(Animal) :
    def property(self):
        print("Have 4 legs and are cuite !!!")
        

calling_obj = Dog()
calling_obj.property()