from polimorfismo.Circle import Circle
from polimorfismo.Rectangle import Rectangle
from polimorfismo.Triangle import Triangle

radius = 10
circle = Circle(radius)
area = circle.get_area()
print("area del circulo " + str(area))


width = 20
height = 10
rectangle = Rectangle(width, height)
area = rectangle.get_area()
print("area del rectangulo " + str(area))

base = 10
height = 20
triangle = Triangle(base, height)
area = triangle.get_area()
print("area del triangulo " + str(area))

