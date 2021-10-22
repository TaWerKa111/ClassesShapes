from math import pi, sqrt
from Classes2DShapes import Shape, Square, Circle, Triangle, Rectangle


class Cube(Shape):
    title = 'Куб'

    def __init__(self, length: float):
        self.length = length
        self.side = Square(self.length)

    def area(self) -> float:
        return self.side.area() * 6

    def radius_into_sphere(self) -> float:
        return self.length / 2

    def show_info(self) -> None:
        print(f'Площадь поверхности {self.title}а = {self.area()}\n'
              f'Радиус вписаной сферы в  {self.title} = {self.radius_into_sphere()}\n')


class Parallelepiped(Shape):
    title = 'Параллелепипед'

    def __init__(self, height: float, length: float, width: float):
        self.height = height
        self.length = length
        self.width = width

    def area(self) -> float:
        return 2 * (self.length * self.height + self.length * self.width + self.length * self.width)

    def diagonal(self) -> float:
        return sqrt(self.length ** 2 + self.height ** 2 + self.width ** 2)

    def show_info(self) -> None:
        print(f'Площадь поверхности {self.title}а = {self.area()}\n'
              f'Диагональ {self.title}а = {self.diagonal()}\n')


class Cylinder(Shape):
    title = 'Цилиндр'

    def __init__(self, height: float, radius: float):
        self.height = height
        self.circle = Circle(radius)

    def area(self) -> float:
        return self.circle.perimeter() * self.height + self.circle.area() * 2

    def area_foot(self) -> float:
        return self.circle.area()

    def show_info(self) -> None:
        print(f'Площадь поверхности {self.title}а = {self.area()}\n'
              f'Площадь основания {self.title}а = {self.area_foot()}\n')


class Sphere(Shape):
    title = 'Сфера'

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 4 * pi * self.radius ** 2

    def volume(self) -> float:
        return 4 / 3 * pi * self.radius ** 3

    def show_info(self) -> None:
        print(f'Площадь поверхности {self.title} = {self.area()}\n'
              f'Объем {self.title} = {self.volume()}\n')


class Tetrahedron(Shape):
    title = 'Тетраэдр'

    def __init__(self, side1: float):
        self.side = Triangle(side1, side1, side1)

    def area(self) -> float:
        """ Площадь поверхности тетраэдра """
        return self.side.area() * 4

    def height(self) -> float:
        return (self.side.side1 * sqrt(6)) / 3

    def show_info(self) -> None:
        print(f'Площадь поверхности {self.title}а = {self.area()}\n'
              f'Высота {self.title}а = {self.height()}\n')


class Cone(Shape):
    title = "Конус"

    def __init__(self, height: float, radius: float, forming: float):
        """ Инициализация значений
            height - высота конуса
            radius - радиус основания конуса
            forming - образующая конуса"""
        self.height = height
        self.radius = radius
        self.forming = forming

    def area(self) -> float:
        """ Площадь поверхности конуса """
        return pi * self.radius * self.forming + pi * self.radius ** 2

    def volume(self) -> float:
        return 1 / 3 * pi * self.radius ** 2 * self.height

    def show_info(self) -> None:
        print(f'Площадь поверхности {self.title}а = {self.area()}\n'
              f'Объем {self.title}а = {self.volume()}\n')

