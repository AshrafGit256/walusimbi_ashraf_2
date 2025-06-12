from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print('Car engine starts')
        
class Bike(Vehicle):
    def start(self):
        print('Bike engine starts')
        
car1 = Car()
bike1  = Bike()

car1.start()

# Exercise
# Submit your work on github for Method overriding, method overloading  and MRO
# MRO is Method resolution order I two real world example on the above.