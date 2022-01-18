## Animal is-a object (yes, sort of confusing) look at the e
class Animal(object):
	pass

# Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		# Dog has-a name
		self.name = name

# Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		# Cat has-a name
		self.name = name

# Person is-a object
class Person(object):

	def __init__(self, name):
		# Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

# Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		# Employee has-a salary
		self.salary = salary

# Fish is-a object
class Fish(object):
	pass

# Salmon is-a fish
class Salmon(Fish):
	pass

# Halibut is-a fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# Marry has-a pet called satan
mary.pet = satan

# Frank is-a employee
frank = Employee("Frank", 120000)

# Frank has-a pet named rover
frank.pet = rover

# Flipper is-a fish
flipper = Fish()

# Crouse is-a salmon
crouse = Salmon()

# Harry is-a halibut
harry = Halibut()