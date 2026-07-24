class Rectangle:

    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("There is a negative value, values should be positive")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


try:
    height = float(input("Enter the height: "))
    width = float(input("Enter the width: "))

    rectangle = Rectangle(width, height)

    print(rectangle.get_area())
    print(rectangle.get_perimeter())
except ValueError as error:
    print(error)