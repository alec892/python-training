from polimorfismo.Shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pow(self.radius, 2) * math.pi
