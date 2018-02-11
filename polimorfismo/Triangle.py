from polimorfismo.Shape import Shape


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2
