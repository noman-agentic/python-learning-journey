class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"\"{self.title}\" by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book1 = Book("The Alchemist", "Paulo Coelho")
print(book1)

book2 = Book("The Alchemist", "Paulo Coelho")
print(repr(book2))


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")

    def move(self):
        print("Vehicle is moving")

    def __str__(self):
        return f"Brand='{self.brand}', Speed='{self.speed}'"


class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def move(self):
        print("Car is driving on the road")

my_car = Car("Toyota", 180, "Petrol")
print(my_car)