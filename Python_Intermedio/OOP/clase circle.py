class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.1416 * (self.radius ** 2)

my_circle = Circle(5)
print(round(my_circle.get_area(), 2))