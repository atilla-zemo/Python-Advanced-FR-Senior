# Verebrung über mehrere Ebenen
class Grandparent:
    height = 150
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50

    # Konstruktor einer Klasse
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

basim = Child()


