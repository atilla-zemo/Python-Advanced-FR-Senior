# Kapselungen von Variablen
# Maschine, Zahnräder, Knöpfe
# Wir möchten die Zahnräder nach außen hin schützen
class HelloWorld:
    # Klassenattribute / Klassenvariable
    name = "Hello"
    _name = "_Hello"  # Eine Empfehlung es nicht außen zu verwenden
    __name = "__Hello" # Python versteckt diese Variablen für Außenstehende

    def __init__(self):
        # Objektattribute / Objektvariablen
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"

    def printer(self):
        print(self.name)
        print(self._name)
        print(self.__name)
        print(self.world)
        print(self._world)
        print(self.__world)

# Objekt der Klasse HelloWorld erstellt
hey = HelloWorld()
hey.printer()

class Hello(HelloWorld):
    def __init__(self):
        print(self.__hello)

hi = Hello()
