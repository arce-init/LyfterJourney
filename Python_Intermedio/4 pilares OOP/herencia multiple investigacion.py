class DragRacingMixin:

    def launch(self):
        print(f"{self.name} launches off the line at {self.horsepower} HP!")

    def quarter_mile(self):
        print(f"{self.name} finishes the quarter mile in a new personal best!")

class DriftMixin:

    def initiate_drift(self):
        print(f"{self.name} kicks the rear end out and initiates the drift")

    def counter_steer(self):
        print(f"{self.name} counter-steers to hold the perfect angle")

class OffRoadMixin:

    def engage_4wd(self):
        print(f"{self.name} engages 4-wheel drive for rough terrain")

class DragCar(DragRacingMixin):

    def __init__(self, name, horsepower):
        self.name = name
        self.horsepower = horsepower


class DriftCar(DriftMixin):

    def __init__(self, name, horsepower):
        self.name = name
        self.horsepower = horsepower

class TunedCar(DragRacingMixin, DriftMixin):

    def __init__(self, name, horsepower):
        self.name = name
        self.horsepower = horsepower

class RallyCar(DriftMixin, OffRoadMixin):

    def __init__(self, name, horsepower):
        self.name = name
        self.horsepower = horsepower


evo = DragCar("Lancer Evolution", 1500)
evo.launch()
evo.quarter_mile()

rx7 = DriftCar("Mazda RX-7", 800)
rx7.initiate_drift()
rx7.counter_steer()

supra = TunedCar("Toyota Supra", 1000)
supra.launch()
supra.initiate_drift()

subaru = RallyCar("Subaru WRX STI", 700)
subaru.initiate_drift()
subaru.engage_4wd()