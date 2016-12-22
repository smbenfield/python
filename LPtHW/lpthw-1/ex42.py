#!/usr/bin/python

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a instance of the class Animal
class Dog(Animal):

	def __init__(self,name):
		## Dog has-a name that is name
		self.name = name

## Cat is-a instance of the class Animal
class Cat(Animal):

	def __init__(self,name):
		## Cat has-a name that is name
		self.name = name

## Class Person is-a object
class Person(object):

	def __init__(self,name):
		## Person has-a name that is name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a instance of the class Person
class Employee(Person):

	def __init__(self,name,salary):
		##  hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary that is salary
		self.salary = salary

## class Fish is-a object
class Fish(object):
	pass

## Salmon is-a instance of the class Fish
class Salmon(Fish):
	pass

## Halibut is-a instance of the class Fish
class Halibut(Fish):
	pass


## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet named Satan
mary.pet = satan

## Frank is-a Employee who makes 120000
frank = Employee("Frank", 120000)

## Frank has-a Pet named Rover
frank.pet = rover

## Flipper is-a instance of the class Fish
flipper = Fish()

## Crouse is-a instance of the class Salmon
crouse = Salmon()

## Harry is-a instance of the class Halibut
harry = Halibut()

