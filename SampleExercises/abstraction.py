from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing Shape
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Concrete class implementing Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage of the classes
rect = Rectangle("blue", 5, 10)
circle = Circle("red", 7)

print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")

print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
