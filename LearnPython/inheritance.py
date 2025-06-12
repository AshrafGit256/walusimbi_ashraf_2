# Father Mother Skilss

class Father:
    def skills(self):
        print('Coding, Fishing')


class Mother:
    def skills(self):
        print('Cooking, cleaning')


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)


c = Child()
c.skills()
