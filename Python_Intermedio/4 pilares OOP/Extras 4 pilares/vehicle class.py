class Vehicle:

    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})"

class Car(Vehicle):

    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - {self.doors} doors"

class Motorcycle(Vehicle):

    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Type: {self.type}"

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "All-Terrain")

print(vehicle1.get_info())
print(vehicle2.get_info())