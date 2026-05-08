# Das super()-Prinzip
# Aus der Kindklasse etwas von der Elternklasse verwenden
class Hello:
    # Konstruktor
    def __init__(self):
        print("Hello!")

class HelloWorld(Hello):
    def __init__(self):
        super().__init__()  # Verbindet Konstruktoren
        print("World!")

# Objekt der Klasse HelloWorld
hello_world = HelloWorld()

# Super() mit Attributen
class Class1:
    var = 20

    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)  # 20
        super().__init__()
        print(self.var)  # 10
        # Auf Attribute von der Elternklasse zugreifen
        print(super().var)


class2 = Class2()

class Grandparent:
    def about(self):
        print("I am a Grandparent")

    def about_myself(self):
        print("I like to smoke!")

class Parent(Grandparent):
    def about_myself(self):
        print("I am boring!")

class Child(Parent):
    def __init__(self):
        super().about()  # I am a Grandparent
        super().about_myself()  # I am boring!

timofej = Child()
