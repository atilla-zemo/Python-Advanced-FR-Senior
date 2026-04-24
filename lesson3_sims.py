import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Car(brands_of_car)

    def get_job(self):
        if self.car.drive():
            self.job = Job(work_list)
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()

        if manage == "fuel":
            print("I bought fuel!")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food!")
            self.money -= 50
            self.home.food += 50
        elif manage == "kebap":
            print("Banger!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day_title = f" Today's the {day}. of {self.name}'s life "
        print(f"{day_title:*^50}\n")

        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")

        home_indexes = "Home Indexes"
        print(f"{home_indexes:^50}\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")

        car_indexes = f"{self.car.brand} Car Indexes"
        print(f"{car_indexes:^50}\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

        if self.job is not None:
            job_indexes = "Job Indexes"
            print(f"{job_indexes:^50}\n")
            print(f"Job - {self.job.job}")
            print(f"Salary - {self.job.salary}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Broke...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            print("Settled in house")
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"I bought a car of {self.car.brand}")

        if self.job is None:
            self.get_job()
            if self.job is not None:
                print(f"I'm going to get a job as a(n) {self.job.job} with"
                      f" a salary of {self.job.salary}")

        self.days_indexes(day)

        dice = random.randint(1, 4)

        if self.satiety < 20:
            print("I'll go eat.")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess...\n"
                      "So I will clean the house.")
                self.clean_home()
            else:
                print("Let's chill.")
                self.chill()
        elif self.money < 0:
            print("Going to work.")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Let's go to work.")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for a Kebap :)")
            self.shopping("kebap")

        return True


class Car:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

work_list = {
    "IT-Developer": {"salary": 50, "gladness_less": 10},
    "Mercenary": {"salary": 100, "gladness_less": 3},
    "Stripper": {"salary": 150, "gladness_less": 30},
    "Furry": {"salary": 20, "gladness_less": 8}
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Audi": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

import time

atilla = Human("Atilla")

for day in range(1, 366):
    time.sleep(0.5)
    if not atilla.live(day):
        break
