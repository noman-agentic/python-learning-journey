class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")

    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def move(self):
        print("Car is driving on the road")


my_car = Car("Toyota", 180, "Petrol")
my_car.show_info()   # এটা কোথা থেকে এসেছে — Vehicle নাকি Car?
my_car.move()         # এটা কার version চলবে?
print(my_car.fuel_type)

