class Person:

    def __init__(self, name):
        self.name = name
        self.age = 0


class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} got in the bus.")
        else:
            print("The bus is full!")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} got off the bus.")
        else:
            print(f"{person.name} is not in the bus.")


my_bus = Bus(2)

person_1 = Person("Alejandro")
person_2 = Person("Sofia")
person_3 = Person("Fabian")

my_bus.add_passenger(person_1)
my_bus.add_passenger(person_2)
my_bus.add_passenger(person_3)

my_bus.remove_passenger(person_1)
my_bus.add_passenger(person_3)