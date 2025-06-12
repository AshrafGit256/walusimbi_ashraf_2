class Vehicle:
    def sound(self):
        print('Vehicle makes a generic sound')

class Car(Vehicle):
    def sound(self):
        print('Car goes voom vooom voom!')

class Bicycle(Vehicle):
    def sound(self):
        print('Bicycle rings bell like tilili tilili!')

v = Vehicle()
v.sound()

c = Car()
c.sound()

b = Bicycle()
b.sound()
