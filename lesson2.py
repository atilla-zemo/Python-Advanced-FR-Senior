class Student:
    def __init__(self):
        self.height = 160
        print("I am alive!")


first_student = Student()

makarius = Student()
print(makarius.height)

class Pupil:
    def __init__(self, height=160):
        self.height = height

lazar = Pupil(height=169)
ukwn_pupil = Pupil()

print(lazar.height)
print(ukwn_pupil.height)
