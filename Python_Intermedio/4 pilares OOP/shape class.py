from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.1416 * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * 3.1416 * self.radius

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return self.side * 4

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 6)

shapes = [circle, square, rectangle]

for shape in shapes:
    print(f"Area: {shape.calculate_area()}, Perimeter: {shape.calculate_perimeter()}")