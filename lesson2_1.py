# Class-attribute Vs. Object-attribute
class Student:
    # Class-attribute
    amount_of_student = 0

    # Object-attribute
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_student += 1

    def __str__(self):
        return f"I am a student. My height is {self.height}"

eyluel = Student(height=167)
print(eyluel.amount_of_student)

rafael = Student(175)
print(rafael.amount_of_student)

basim = Student(200)
print(basim.amount_of_student)

print(eyluel.amount_of_student)

# print object
print(basim)

