class Human:
    def __init__(self, name="Human"):
        self.name = name


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for human in args:
            self.passengers.append(human)

    def print_passengers_name(self):
        if self.passengers:
           print(f"Names of {self.brand} passengers:")
           for passenger in self.passengers:
               print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


olivia = Human("Olivia")
timofej = Human("Timofej")
david = Human("David")

mercedes = Car("Mercedes")

mercedes.add_passenger(olivia, timofej, david)

mercedes.print_passengers_name()


