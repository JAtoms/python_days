from car import Car

class Cole(Car):
    def newBreed(self):
        print("Seol")


class Kojo(Cole):
    def onPoint(self):
        print("Koje")

car_1 = Car("Honda", "Civic", 2024, "Black")

# print(car_1.color)
# print(car_1.wheeels)

kojo = Kojo
kojo.stop(None)

