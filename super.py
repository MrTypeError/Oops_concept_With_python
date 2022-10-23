
class Person:

	def __init__(self, name, id):
		self.name = name
		self.id = id
	def Display(self):
		print(self.name, self.id)
	

class Emp(Person):
	
	def __init__(self, name, id):
		self.name_ = name
		super().__init__(name, id)

	def Print(self):
		print("Emp class called")

Emp_details = Emp("Deb Kumar", 103)

print(Emp_details.name_, Emp_details.name)
