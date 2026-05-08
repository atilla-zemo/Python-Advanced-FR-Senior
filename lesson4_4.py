# Mehrfachvererbung

class Computer:
    def __init__(self):
        super().__init__()  # Bereitet es für Mehrfachvererbung vor
        self.memory = 128

    def calculate(self):
        print("Calculating...")

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4K"

    def display(self):
        print("I display the image on the screen...")

# Smartphone erbt von Computer & Display
class Smartphone(Computer, Display):
    def print_info(self):
        print(self.memory)
        print(self.resolution)

iPhone = Smartphone()
iPhone.calculate()
iPhone.display()
iPhone.print_info()