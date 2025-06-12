#Superclass
class Bird:
    def fly(self):
        print("Bird flies in the sky")

#Derived class
class Eagle(Bird):
    def fly(self):
        print("Eagle flies at high altitude")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies at low altitude")

#How we use polymorphism
def flight_test(bird):
    bird.fly()
    
#Create objects
eagle1 = Eagle()
sparrow1 = Sparrow()

flight_test(eagle1)
flight_test(sparrow1)