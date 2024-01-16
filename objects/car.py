def stop():
    print("This car is stopping")


class Car:
    wheeels = None

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.wheeels = 4

    def drive(self):
        print("This " + self.make + " car is driving")
