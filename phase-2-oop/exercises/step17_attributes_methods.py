class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)

car1.display_info()


class BankAccount:
    def __init__(self, owner_name, balance = 0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount

noman_ac = BankAccount("Noman")

print(noman_ac.owner_name)
noman_ac.deposit(100)
print(noman_ac.check_balance())
noman_ac.withdraw(500)
noman_ac.withdraw(50)
print(noman_ac.check_balance())