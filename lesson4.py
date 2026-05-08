# Das Schema der Vererbung
class Parent:
    pass

# Child erbt von Parent
class Child(Parent):
    pass

class Human:
    height = 170

class Student(Human):
    pass

class Worker(Human):
    pass

# Objekt der Klasse Student
rafael = Student()
print(rafael.height)

