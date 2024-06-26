import math
class Circle:

    def __init__(self, radius, color):
        """
        Initialize a Circle class
        Arguments:
            radius (float) - radius of the circle which is the distance from the center of the circle
            color (String) - represents the color of the circle
        """
        self._radius = radius
        self._color = color

    @property
    def radius(self):
        """ returns the radius of the circle, represented as a float number."""
        return self._radius

    @property
    def color(self):
        return self._color

    @color.setter
    def setColor(self, newColor):
        self._color = newColor

    def diameter(self):
        return 2*self._radius

    def find_area(self):
        return math.pi * (self._radius **2)

    def perimeter(self):
        return 2*math.pi*self._radius

help(Circle)
#help(Circle.radius.__doc__)